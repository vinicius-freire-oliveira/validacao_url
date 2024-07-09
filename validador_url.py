""" Verifica se a base da URL está de acordo com o padrão correto.

Exemplos de URLs válidas:
    unitconverter.com/temperature
    unitconverter.com.br/temperature
    www.unitconverter.com/temperature
    www.unitconverter.com.br/temperature
    http://www.unitconverter.com/temperature
    http://www.unitconverter.com.br/temperature
    https://www.unitconverter.com/temperature
    https://www.unitconverter.com.br/temperature

Exemplos de URL inválidas:
    https://unitconverter/temperature
    http://unitconverter.naoexiste/temperature
    ht:unitconverter.naoexiste/temperature """

# https://www.unitconverter.com.br/temperature

# Importando a biblioteca 're' para lidar com expressões regulares
import re

# Definindo a URL que será verificada
url = "unitconverter.com/temperature"

# Definindo o padrão de URL usando uma expressão regular
padrao_url = re.compile('(http(s)?://)?(www.)?unitconverter.com(.br)?/temperature')

# Tentando encontrar uma correspondência entre a URL e o padrão definido
match = padrao_url.match(url)

# Se não houver correspondência (match) entre a URL e o padrão, uma exceção será levantada
if not match:
    raise ValueError("A URL não é válida.")

# Caso contrário, a URL é considerada válida e essa mensagem será impressa na tela
print("A URL é válida")
