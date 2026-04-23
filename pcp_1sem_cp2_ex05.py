  Nome_do_cliente = input("Digite seu nome completo: ")
  Idade = float(input("Digite sua idade: "))
  Renda_mensal = float(input("Digite sua renda mensal fixa: "))
  Valor_emprestimo = float(input("Digite o valor desejado para o seu emprestimo: "))
  Num_Parcelas = float(input("Digite em quantas parcelas seu emprestimo sera dividido com minimo 3 e limite de 24: "))

  def pode_aprovar(idade, renda, valor):
    if idade < 18:
      return False, "Emprestimo negado: Idade inferior a 18 anos."
    if valor > 20 * renda:
      return False, "Emprestimo negado: Valor excede os limites (mais de 20x a renda mensal)."
    return True, "Emprestimo aprovado."


  def definir_taxa(parcelas):
    if parcelas <= 6:
      return 0.05
    elif 7 <= parcelas <= 12:
        return 0.08
    elif 13 <= parcelas <= 24:
        return 0.10


  aprovado, mensagem_status = pode_aprovar(Idade, Renda_mensal, Valor_emprestimo)
  print(f"\nStatus da solicitação: {mensagem_status}")


  if aprovado:
      taxa_juros = definir_taxa(Num_Parcelas)
      print(f"Taxa de juros aplicada: {taxa_juros*100:.2f}%")

      financiamento = 0.01

      if Num_Parcelas > 0:
          if taxa_juros == 0:
              financiamento = Valor_emprestimo / Num_Parcelas
          else:
              term = (1 + taxa_juros)**Num_Parcelas
              if (term - 1) != 0:
                  financiamento = Valor_emprestimo * taxa_juros * term / (term - 1)
              else:
                  print("Erro de cálculo: Divisão por zero no termo da fórmula.")
                  financiamento = float('nan')
      else:
          print("Número de parcelas deve ser maior que zero.")
          financiamento = 0.0

      print(f"O financiamento mensal é: {financiamento:.2f}")
      print(f"O valor total a ser pago é: {Num_Parcelas * financiamento:.2f}")
