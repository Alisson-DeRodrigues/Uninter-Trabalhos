print("Bem-vindo à Loja de Alisson de Souza Rodrigues")

print("=" * 17 + " Cardápio " + "=" * 17)
print("===" + "| Tamanho |" + " Cupuaçu (CP) " + "| Açaí (AC) |" + "===")
print("===" + "|    P    |" + "   R$ 09,00   " + "| R$ 11,00  |" + "===")
print("===" + "|    M    |" + "   R$ 14,00   " + "| R$ 16,00  |" + "===")
print("===" + "|    G    |" + "   R$ 18,00   " + "| R$ 20,00  |" + "===")
print("=" * 44)


conta = 0; # valor final da compra
while True:
  # escolha do produto desejado
  sabor = input("\nEscolha o sabor desejado: ")
  if sabor == "CP":
    print("O sabor escolhido foi Cupuaçu.")
  elif sabor == "AC":
    print("O sabor escolhido foi Açaí.")
  else:
    print("Sabor Inválido. Tente novamente.")
    continue
  
  # escolha do tamanho do produto desejado
  tamanho = input("\nEscolha o tamanho desejado (P/M/G): ")
  if tamanho == "P" and sabor == "CP":
    print("Você escolheu um Cupuaçu Pequeno: R$09,00")
    conta += 9;
  elif tamanho == "P" and sabor == "AC":
    print("Você escolheu um Açaí Pequeno: R$11,00")
    conta += 11;
  elif tamanho == "M" and sabor == "CP":
    print("Você escolheu um Cupuaçu Médio: R$14,00")
    conta += 14;
  elif tamanho == "M" and sabor == "AC":
    print("Você escolheu um Açaí Médio: R$16,00")
    conta += 16;
  elif tamanho == "G" and sabor == "CP":
    print("Você escolheu um Cupuaçu Grande: R$18,00")
    conta += 18;
  elif tamanho == "G" and sabor == "AC":
    print("Você escolheu um Açaí Grande: R$20,00")
    conta += 20;
  else:
    print("Tamanho Inválido. Tente novamente")
    continue

  # comtinuar pedido e valor total da conta
  repetir = input("\nDeseja fazer outro pedido? (S/N)? ")
  if repetir == "S":
    continue
  else:
    print("O total a ser pago é: R${:.2f}".format(conta))
    break

