diretório_legenda = "How I Met Your Mother (2005) - S01E01 - Pilot (1080p AMZN WEB-DL x265 Silence).srt"
operacao = 'subtrair'  # Pode ser 'adicionar' ou 'subtrair'

import re, chardet
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

# Detectar a codificação do arquivo
def detectar_codificacao(arquivo):
    with open(arquivo, 'rb') as f:
        resultado = chardet.detect(f.read())
        return resultado['encoding']

# Ajustar os tempos
def ajustar_tempos(diretório_legenda, tempo_ajuste, operacao):
    # Detectar a codificação
    codificacao = detectar_codificacao(diretório_legenda)
    
    # Ler o arquivo de legendas com a codificação detectada
    with open(diretório_legenda, 'r', encoding=codificacao) as f:
        texto = f.readlines()

    novo_texto = []
    
    for linha in texto:
        if '-->' in linha:
            tempo_inicial, tempo_final = linha.split(' --> ')
            tempo_inicial_td = str_para_timedelta(tempo_inicial.strip())
            tempo_final_td = str_para_timedelta(tempo_final.strip())
            
            if operacao == 'adicionar':
                tempo_inicial_td += tempo_ajuste
                tempo_final_td += tempo_ajuste
            elif operacao == 'subtrair':
                tempo_inicial_td -= tempo_ajuste
                tempo_final_td -= tempo_ajuste

            if tempo_inicial_td.total_seconds() < 0:
                tempo_inicial_td = timedelta(seconds=0)
            if tempo_final_td.total_seconds() < 0:
                tempo_final_td = timedelta(seconds=0)

            novo_tempo_inicial = timedelta_para_str(tempo_inicial_td)
            novo_tempo_final = timedelta_para_str(tempo_final_td)
            
            nova_linha = f"{novo_tempo_inicial} --> {novo_tempo_final}\n"
            novo_texto.append(nova_linha)
        else:
            novo_texto.append(linha)

    with open("legenda_ajustada.srt", 'w', encoding='utf-8-sig') as f:
        f.writelines(novo_texto)

tempo_ajuste = timedelta(seconds=1)  # Para adicionar 180 segundos

# Chamar a função para ajustar os tempos
ajustar_tempos(diretório_legenda, tempo_ajuste, operacao)