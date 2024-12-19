# Ajuste de Tempos em Arquivos de Legendas (.SRT)

Este projeto contém um script Python para ajustar os tempos de legendas no formato `.srt`, permitindo a adição ou subtração de um intervalo de tempo específico. O script é útil para sincronizar legendas com vídeos ou corrigir o tempo de exibição das legendas.

## Funcionalidades

- **Ajustar os tempos das legendas**: O script lê um arquivo de legendas `.srt` e ajusta os tempos de exibição das legendas com base em um intervalo de tempo fornecido.
- **Adicionar ou subtrair tempo**: Você pode adicionar ou subtrair um intervalo de tempo (em segundos, minutos, horas, etc.) de todas as entradas de tempo das legendas.
- **Prevenir tempos negativos**: O script garante que os tempos não sejam negativos, ajustando para 00:00:00,000 quando necessário.

## Como Funciona

O script trabalha com arquivos de legendas `.srt`, que seguem o formato:

```
1
00:01:38,164 --> 00:01:40,300
Legenda 1

2
00:02:42,145 --> 00:02:44,890
Legenda 2
```

O código realiza os seguintes passos:
1. Lê o arquivo `.srt` fornecido.
2. Para cada linha contendo os tempos de exibição das legendas (no formato `00:01:38,164 --> 00:01:40,300`), o script converte os tempos para o formato `timedelta`, aplica o ajuste de tempo (adicionar ou subtrair) e, em seguida, reescreve o arquivo com os novos tempos.
3. O arquivo ajustado é salvo com o nome `legenda_ajustada.srt`.

## Pré-requisitos

Certifique-se de ter o Python 3.x instalado. Além disso, o código usa a biblioteca `re` (expressões regulares) e `datetime`, que são bibliotecas padrão do Python e não necessitam de instalação adicional.

## Instalação

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/seu_usuario/ajuste-legendas.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd ajuste-legendas
   ```

## Como Usar

1. **Crie ou obtenha um arquivo de legendas .srt** (por exemplo, `Crips And Bloods Documentary.srt`).
   
2. **Edite o código**:
   - Altere o valor da variável `diretório_legenda` para o nome do seu arquivo de legenda.
   - Defina a operação: 'adicionar' para adicionar tempo ou 'subtrair' para subtrair tempo. 
   - Ajuste o tempo desejado em `tempo_ajuste`. Exemplo: `tempo_ajuste = timedelta(seconds=3)` para adicionar ou subtrair 3 segundos de todos os tempos.

3. **Execute o script**:
   - No terminal, execute o script:
     ```bash
     python python-subtitle-shift.py
     ```

4. **Verifique o arquivo de saída**:
   - Após a execução, o arquivo ajustado será salvo como `legenda_ajustada.srt` no mesmo diretório.

## Exemplo de Uso

Suponha que você tenha o seguinte arquivo de legenda (`exemplo.srt`):

```
1
00:01:38,164 --> 00:01:40,300
Legenda 1

2
00:02:42,145 --> 00:02:44,890
Legenda 2
```

Se você definir:

```python
tempo_ajuste = timedelta(seconds=3)  # Adicionar 3 segundos
operacao = 'adicionar'
```

O arquivo de saída será:

```
1
00:01:41,164 --> 00:01:43,300
Legenda 1

2
00:02:45,145 --> 00:02:47,890
Legenda 2
```

Se a operação for `subtrair`, o tempo será ajustado para 3 segundos a menos.
