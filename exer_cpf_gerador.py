# Gerando CPFs válidos com random()

import random

# Poderíamos gerar até 100 cpfs válidos de uma vez englobando todo o 
# código e indentado em um for ( for _ in range(100): )

nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0,9))

print(nove_digitos)

multiplicador_regressivo_1 = 10

resultado_digito1 = 0

for digito in nove_digitos:
    resultado_digito1 += int(digito) * multiplicador_regressivo_1
    multiplicador_regressivo_1 -= 1

digito_1 = (resultado_digito1 * 10) % 11

digito_1 = digito_1 if digito_1 <= 9 else 0


# Calculado o segundo dos últimos dois dígitos
dez_digitos = nove_digitos + str(digito_1)
multiplicador_regressivo_2 = 11

resultado_digito2 = 0

for digito in dez_digitos:
    resultado_digito2 += int(digito) * multiplicador_regressivo_2
    multiplicador_regressivo_2 -= 1

digito_2 = (resultado_digito2 * 10) % 11

digito_2 = digito_2 if digito_2 <= 9 else 0


cpf_gerado_pelo_algoritmo = f'{nove_digitos}{digito_1}{digito_2}'

print(cpf_gerado_pelo_algoritmo)




