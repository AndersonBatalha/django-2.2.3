import rows, json, os, django
from django.conf import settings
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "f12019.settings")
django.setup()

from app.models import Pais, Cidade, Evento, Circuito, Equipe, Titulo, Piloto, Pontuacao, Resultado

def str_to_date(data):
    dia, mes, ano = int(data[0:2]), int(data[3:5]), int(data[6:10])
    return datetime.date(year=ano, month=mes, day=dia)

def str_to_time(tempo):
    minuto, segundo, milissegundo = int(tempo[0]), int(tempo[2:4]), int(tempo[5:9])
    return datetime.time(hour=0, minute=minuto, second=segundo, microsecond=milissegundo)

if __name__ == '__main__':
    if 'db.sqlite3' not in os.listdir(settings.BASE_DIR):
        os.system("""
rm -rf db.sqlite3 &&
touch db.sqlite3 &&
python manage.py makemigrations
python manage.py migrate
        """)

    arquivo = open('db.json', mode='r').read()

    data = json.loads(arquivo)
    for (k, v) in data.items():
        print('\n', k)

        if type(v).__name__  == 'list':
            data = rows.import_from_dicts(v)
            for row in data:
                if k == 'calendario_temporada':

                    try:
                        pais = Pais.objects.get(pais=row.localizacao['pais'])
                    except Pais.DoesNotExist:
                        pais = Pais.objects.create(
                            pais=row.localizacao['pais']
                        )

                    try:
                        cidade = Cidade.objects.get(cidade=row.localizacao['cidade'])
                    except Cidade.DoesNotExist:
                        cidade = Cidade.objects.create(
                            cidade=row.localizacao['cidade'],
                            pais=pais,
                        )


                    try:
                        circuito = Circuito.objects.get(nome=row.nome_circuito)
                    except Circuito.DoesNotExist:
                        circuito = Circuito.objects.create(
                            nome=row.nome_circuito,
                            percurso = row.percurso,
                            numero_voltas = row.numero_voltas,
                            distancia_total = row.distancia_total,
                            primeira_corrida = row.primeira_corrida,
                            piloto_recorde_pista = row.recorde_pista['piloto_recorde'],
                            ano_recorde_pista = row.recorde_pista['ano_recorde'],
                            tempo_recorde_pista = str_to_time(row.recorde_pista['tempo_recorde']),

                            cidade=cidade
                        )

                    try:
                        evento = Evento.objects.get(nome_evento=row.nome_oficial_evento)
                    except Evento.DoesNotExist:
                        evento = Evento.objects.create(
                            nome_evento = row.nome_oficial_evento,
                            local = row.local,
                            data_inicio = str_to_date(row.data['data_inicio']),
                            data_termino = str_to_date(row.data['data_termino']),
                            url = row.url,
                            img_evento = row.img_file,
                            flag_icon = row.flag_icon,

                            circuito=circuito
                        )

                    print("{}\n{}\n{} ({})\n".format(
                        evento.nome_evento, circuito.nome, cidade.cidade, pais.pais)
                    )

                elif k == 'equipes':
                    try:
                        equipe = Equipe.objects.get(nome_equipe=row.equipe)
                    except Equipe.DoesNotExist:
                        equipe = Equipe.objects.create(
                            nome_equipe = row.equipe,
                            nome_oficial = row.nome_oficial,
                            numero_titulos = row.titulos_mundiais,
                            voltas_mais_rapidas = row.voltas_mais_rapidas,
                            pole_positions = row.pole_positions,
                            unidade_potencia = row.unidade_potencia,
                            chassi = row.chassis,
                            primeiro_campeonato = row.primeiro_campeonato,
                            posicao_melhor_resultado = row.melhor_resultado['posicao'],
                            nr_melhor_resultado = row.melhor_resultado['quantidade'],
                            url = row.url,
                            img = row.img_file,
                            logo = row.img_logo,
                            flag_icon = row.flag_icon,

                            cidade = Cidade.objects.get_or_create(
                                cidade=row.sede['cidade'],
                                pais=Pais.objects.get_or_create(pais=row.sede['pais'])[0],
                            )[0]
                        )
                    print(equipe.nome_equipe)
                else:
                    try:
                        piloto = Piloto.objects.get(nome=row.nome)
                    except Piloto.DoesNotExist:
                        piloto = Piloto.objects.create(
                            nome = row.nome,
                            numero = row.numero,
                            pontos_ganhos = row.pontos_ganhos,
                            data_nasc = str_to_date(row.data_nascimento),
                            corridas_disputadas = row.gps_disputados,
                            numero_podios = row.podios,
                            numero_titulos = row.titulos_mundiais['nr_titulos'],
                            pos_melhor_resultado = row.melhor_colocacao['posicao'],
                            nr_melhor_resultado = row.melhor_colocacao['quantidade'],
                            img = row.img_file,
                            flag_icon = row.flag_icon,

                            cidade = Cidade.objects.get_or_create(
                                cidade=row.naturalidade['cidade'],
                                pais=Pais.objects.get_or_create(pais=row.naturalidade['pais'])[0],
                            )[0],
                            equipe = Equipe.objects.get(nome_equipe=row.equipe)
                        )
                        if len(row.titulos_mundiais['titulos']) > 0:
                            for ano in row.titulos_mundiais['titulos']:
                                titulo = Titulo.objects.get_or_create(
                                    ano_titulo=ano
                                )[0]
                                piloto.titulos.add(titulo)
                            piloto.save()

                    print("%s (%s)" % (piloto.nome, piloto.equipe.nome_equipe))
        else:
            if k == 'pontuação':
                for (chave, valor) in v.items():
                    p = Pontuacao.objects.get_or_create(
                        posicao=int(chave),
                        pontuacao_corrida=valor
                    )[0]
                    print('%dº = %d pontos' %(p.posicao, p.pontuacao_corrida))
            else:
                for (chave, valor) in v.items():
                    print('\n', chave)
                    data = rows.import_from_dicts(valor)
                    for row in data:
                        r = Resultado.objects.get_or_create(
                            resultado = Pontuacao.objects.get(posicao=row.posicao),
                            piloto = Piloto.objects.get(nome=str(chave)),
                            evento = Evento.objects.get(local=row.grande_premio),
                            melhor_volta = 0
                        )[0]

                        try:
                            if row.melhor_volta == 1:
                                r.melhor_volta = row.melhor_volta
                                r.save()
                        except AttributeError:
                            pass

                        print("%s\n%dº = %d pontos" % (r.evento.local, r.resultado.posicao,
                                          r.resultado.pontuacao_corrida ) )
