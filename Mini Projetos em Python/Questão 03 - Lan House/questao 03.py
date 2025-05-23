
print ("Bem-vindo à Smartlan de Alisson de Souza Rodrigues")

def escolha_servico():
  valor_servico = 0; # soma de todos os servicos adquiridos
  valor_extra = 0; # soma de todos os valores extras

  while True:
    print("\nEscolha o serviço desejado: ")
    print("DIG | Digitalização.")
    print("ICO | Impressão Colorida.")
    print("IBO | Impressão preto e branco.")
    print("FOT | Fotocópia.")
    servico = input(">>> ")
    
    if servico == "DIG":
      print("Você escolheu digitalização. O custo por página é R$01,10.")
      valor_servico += num_pagina(servico)
      if valor_servico != 0: # executa somente quando a função num_pagina(servico) retorna um valor diferente de zero (quando o número de páginas for diferente de zero ou menor que 20.001)
        valor_extra += servico_extra()

    elif servico == "ICO":
      print("Você escolheu impressão colorida. O custo por página é R$01,00.")
      valor_servico += num_pagina(servico)
      if valor_servico != 0:
        valor_extra += servico_extra()

    elif servico == "IBO":
      print("Você escolheu impressão preto e branco. O custo por página é R$00,40.")
      valor_servico += num_pagina(servico)
      if valor_servico != 0:
        valor_extra += servico_extra()

    elif servico == "FOT":
      print("Você escolheu fotocópia. O custo por página é R$00,20.")
      valor_servico += num_pagina(servico)
      if valor_servico != 0:
        valor_extra += servico_extra()

    else:
      print("Esolha uma opção válida.")
      continue

    # continuar adquirindo mais serviços
    continuar_comprando = input("Deseja realizar mais pedidos? (s/n) ")
    if continuar_comprando == "s":
      continue

    # valor total da conta
    print("O total foi de R${:.2f} (R${:.2f} de serviços e R${:.2f} de serviços adicionais).".format(valor_servico + valor_extra, valor_servico, valor_extra))
    break
def num_pagina(servico):
  while True:
    # serviço de digitalização
    if servico == "DIG":
      try:
        quantidade_paginas = int(input("Insira a quantidade de paginas: "))
        if quantidade_paginas < 20: # sem desconto
          print("Você escolheu {} páginas por R${:.2f}.".format(quantidade_paginas, 1.10 * quantidade_paginas))
          return 1.10 * quantidade_paginas
        elif quantidade_paginas < 200: # desconto de 15%
          print("Você escolheu {} páginas por R${:.2f} (desconto de 15%).".format(quantidade_paginas, 1.10 * quantidade_paginas * 0.85))
          return 1.10 * quantidade_paginas * 0.85
        elif quantidade_paginas < 2000: # desconto de 20%
          print("Você escolheu {} páginas por R${:.2f} (desconto de 20%).".format(quantidade_paginas, 1.10 * quantidade_paginas * 0.80))
          return 1.10 * quantidade_paginas * 0.80
        elif quantidade_paginas < 20000:  # desconto de 25%
          print("Você escolheu {} páginas por R${:.2f} (desconto de 25%).".format(quantidade_paginas, 1.10 * quantidade_paginas * 0.75))
          return 1.10 * quantidade_paginas * 0.75
        elif quantidade_paginas >= 20000:
          print("Não é aceito pedidos nessa quantidade de páginas.")
          return 0
      except:
        print("Insira um valor válido.")
        continue
    # serviço de impressão colorida
    elif servico == "ICO":
      try:
        quantidade_paginas = int(input("Insira a quantidade de paginas: "))
        if quantidade_paginas < 20: # sem desconto
          print("Você escolheu {} páginas por R${:.2f}.".format(quantidade_paginas, 1 * quantidade_paginas))
          return 1 * quantidade_paginas
        elif quantidade_paginas < 200: # desconto de 15%
          print("Você escolheu {} páginas por R${:.2f} (desconto de 15%).".format(quantidade_paginas, 1 * quantidade_paginas * 0.85))
          return 1 * quantidade_paginas * 0.85
        elif quantidade_paginas < 2000: # desconto de 20%
          print("Você escolheu {} páginas por R${:.2f} (desconto de 20%).".format(quantidade_paginas, 1 * quantidade_paginas * 0.80))
          return 1  * quantidade_paginas * 0.80
        elif quantidade_paginas < 20000:  # desconto de 25%
          print("Você escolheu {} páginas por R${:.2f} (desconto de 25%).".format(quantidade_paginas, 1 * quantidade_paginas * 0.75))
          return 1  * quantidade_paginas * 0.75
        elif quantidade_paginas >= 20000:
          print("Não é aceito pedidos nessa quantidade de páginas.")
          return 0
      except:
        print("Insira um valor válido.")
        continue

    # serviço de impressão preto e branco
    elif servico == "IBO":
      try:
        quantidade_paginas = int(input("Insira a quantidade de paginas: "))
        if quantidade_paginas < 20: # sem desconto
          print("Você escolheu {} páginas por R${:.2f}.".format(quantidade_paginas, 0.40 * quantidade_paginas))
          return 0.40 * quantidade_paginas
        elif quantidade_paginas < 200: # desconto de 15%
          print("Você escolheu {} páginas por R${:.2f} (desconto de 15%).".format(quantidade_paginas, 0.40 * quantidade_paginas * 0.85))
          return 0.40 * quantidade_paginas * 0.85
        elif quantidade_paginas < 2000: # desconto de 20%
          print("Você escolheu {} páginas por R${:.2f} (desconto de 20%).".format(quantidade_paginas, 0.40 * quantidade_paginas * 0.80))
          return 0.40 * quantidade_paginas * 0.80
        elif quantidade_paginas < 20000:  # desconto de 25%
          print("Você escolheu {} páginas por R${:.2f} (desconto de 25%).".format(quantidade_paginas, 0.40 * quantidade_paginas * 0.75))
          return 0.40 * quantidade_paginas * 0.75
        elif quantidade_paginas >= 20000:
          print("Não é aceito pedidos nessa quantidade de páginas.")
          return 0
      except:
        print("Insira um valor válido.")
        continue

    # serviço de fotocópia
    elif servico == "FOT":
      try:
        quantidade_paginas = int(input("Insira a quantidade de paginas: "))
        if quantidade_paginas < 20:  # sem desconto
          print("Você escolheu {} páginas por R${:.2f}.".format(quantidade_paginas, 0.20 * quantidade_paginas))
          return 0.20 * quantidade_paginas
        elif quantidade_paginas < 200:  # desconto de 15%
          print("Você escolheu {} páginas por R${:.2f} (desconto de 15%).".format(quantidade_paginas, 0.20 * quantidade_paginas * 0.85))
          return 0.20 * quantidade_paginas * 0.85
        elif quantidade_paginas < 2000:  # desconto de 20%
          print("Você escolheu {} páginas por R${:.2f} (desconto de 20%).".format(quantidade_paginas, 0.20 * quantidade_paginas * 0.80))
          return 0.20 * quantidade_paginas * 0.80
        elif quantidade_paginas < 20000:  # desconto de 25%
          print("Você escolheu {} páginas por R${:.2f} (desconto de 25%).".format(quantidade_paginas, 0.20 * quantidade_paginas * 0.75))
          return 0.20 * quantidade_paginas * 0.75
        elif quantidade_paginas >= 20000:
          print("Não é aceito pedidos nessa quantidade de páginas.")
          return 0
      except:
        print("Insira um valor válido.")
        continue

    break


def servico_extra():
  while True:
    print("Deseja realizar um pedido adicional?")
    print("1 | Encadernação simples por R$15,00.")
    print("2 | Encadernação de capa dura por R$40,00.")
    print("0 | Não desejo mais nada.")
    escolha = input(">>> ")

    # encadernação simples
    if escolha == "1":
      return 15
    # encadernação de capa dura
    elif escolha == "2":
      return 40
    # não desejar mais nada
    elif escolha == "0":
      return 0
    else:
      print("Escolha uma opção válida.")
      continue

    break


escolha_servico()