diretório_legenda = "Crips And Bloods Made In America Full Crime Documentary Free Movies By Cineverse [Portuguese] [translated] [DownloadYoutubeSubtitles.com].srt"
operacao = 'subtrair'  # Pode ser 'adicionar' ou 'subtrair'

import re
from datetime import timedelta

# Função para converter o tempo no formato "HH:MM:SS,SSS" para um objeto timedelta
def str_para_timedelta(time_str):
    h, m, s = time_str.split(':')
    s, ms = s.split(',')
    return timedelta(hours=int(h), minutes=int(m), seconds=int(s), milliseconds=int(ms))

# Função para converter timedelta de volta para o formato "HH:MM:SS,SSS"
def timedelta_para_str(td):
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    milliseconds = int(td.microseconds / 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

# Função para ajustar os tempos no arquivo .srt
def ajustar_tempos(diretório_legenda, tempo_ajuste, operacao):
    # Ler o arquivo de legendas .srt
    with open(diretório_legenda, 'r', encoding='utf-8-sig') as f:
        texto = f.readlines()

    novo_texto = []
    
    for linha in texto:
        # Procurar marcadores de tempo no formato "00:01:38,164 --> 00:01:40,300"
        if '-->' in linha:
            # Dividir os tempos de início e fim
            tempo_inicial, tempo_final = linha.split(' --> ')

            # Converter os tempos para timedelta
            tempo_inicial_td = str_para_timedelta(tempo_inicial.strip())
            tempo_final_td = str_para_timedelta(tempo_final.strip())
            
            # Ajustar o tempo de acordo com a operação
            if operacao == 'adicionar':
                tempo_inicial_td += tempo_ajuste
                tempo_final_td += tempo_ajuste
            elif operacao == 'subtrair':
                tempo_inicial_td -= tempo_ajuste
                tempo_final_td -= tempo_ajuste


            # Verificar se o tempo de ajuste resultou em valores negativos e corrigir
            if tempo_inicial_td.total_seconds() < 0:
                tempo_inicial_td = timedelta(seconds=0)
            if tempo_final_td.total_seconds() < 0:
                tempo_final_td = timedelta(seconds=0)

            # Converter de volta para o formato "HH:MM:SS,SSS"
            novo_tempo_inicial = timedelta_para_str(tempo_inicial_td)
            novo_tempo_final = timedelta_para_str(tempo_final_td)
            
            # Substituir a linha de tempo original
            nova_linha = f"{novo_tempo_inicial} --> {novo_tempo_final}\n"
            novo_texto.append(nova_linha)
        else:
            # Se não for um marcador de tempo, apenas adicionar a linha sem alterações
            novo_texto.append(linha)

    # Salvar o conteúdo ajustado em um novo arquivo
    with open("legenda_ajustada.srt", 'w', encoding='utf-8-sig') as f:
        f.writelines(novo_texto)

tempo_ajuste = timedelta(seconds=3)  # Para adicionar 180 segundos

# Chamar a função para ajustar os tempos
ajustar_tempos(diretório_legenda, tempo_ajuste, operacao)
