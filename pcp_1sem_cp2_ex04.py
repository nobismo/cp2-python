nome = input("digite seu nome: ")
salario_base = float(input("digite seu salário base: "))
bonus = input("você recebeu bônus? (y ou n): ")
cargo = int(input("digite seu cargo (1, 2, 3 ou 4): "))
horas_extras = int(input("digite quantas horas extras você trabalhou: ")) #valor da hora extra é 1.5% do salário inicial por hora
faltas = int(input("digite quantas faltas você teve: ")) #desconto de 2% do salário inicia por falta
print()

bonus = 0

if cargo == 1:
  print("seu cargo é: gerente. seu bônus é de R$1000")
  bonus = 1000
elif cargo == 2:
  print("seu cargo é: analista. seu bônus é de R$500")
  bonus = 500
elif cargo == 3:
  print("seu cargo é: assistente. seu bônus é de R$300")
  bonus = 300
elif cargo == 4:
  print("seu cargo é: estagiário. seu bônus é de R$100")
  bonus = 100
else:
  print("cargo inválido")

salario_com_bonus = salario_base + bonus
print()

valor_hora_extra = (salario_base * 0.015) * horas_extras
total_acrescimo = valor_hora_extra + bonus

def calcular_salario_com_acrescimos (salario_com_bonus, valor_hora_extra):
  salario_com_acrescimos = salario_com_bonus + valor_hora_extra
  print(f"seu salário base pós acrescimos de bônus e horas extras é: R${salario_com_acrescimos}")
  print(f"o total de acrescimo ao seu salário é: R${total_acrescimo}")
  print()
  return salario_com_acrescimos
salario_com_acrescimos = calcular_salario_com_acrescimos(salario_com_bonus, valor_hora_extra)

valor_falta = (salario_base * 0.02) * faltas
def calcular_salario_com_descontos (salario_com_acrescimos, valor_falta):
  salario_com_descontos = salario_base - valor_falta
  print(f"seu salário base pós descontos de faltas é: R${salario_com_descontos}")
  print(f"o total de desconto ao seu salário é: R${valor_falta}")
  print()
  return salario_com_descontos
salario_com_descontos = calcular_salario_com_descontos(salario_com_acrescimos, valor_falta)

def calcular_salario_liq (salario_com_acrescimos, valor_falta):
  salario_liq = salario_com_acrescimos - valor_falta
  print(f"seu salário líquido é: R${salario_liq}")
  return salario_liq
salario_liq = calcular_salario_liq(salario_com_acrescimos, valor_falta)
