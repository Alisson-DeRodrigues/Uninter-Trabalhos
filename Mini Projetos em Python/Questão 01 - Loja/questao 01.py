print("Bem-Vindo à Loja de Alisson de Souza Rodrigues (RU 4381452)")

valor_produto = float(input("Insira o valor unitário do produto: "))
quantidade_produto = int(input("Insira a quantidade do produto: "))

valor_total = valor_produto * quantidade_produto
total_desconto = 0

if valor_total < 2500:
  # desconto de 0%
  print("O valor total da compra foi {:.2f}".format(valor_total))
elif valor_total < 6000:
  # desconto de 4% (0.96)
  total_desconto = valor_total * 0.96
  print("O valor total da compra sem desconto foi: {:.2f}".format(valor_total))
  print("O valor total da compra com desconto foi: {:.2f} (desconto de 4%)".format(total_desconto))
elif valor_total < 10000:
  # desconto de 7% (0.93)
  total_desconto = valor_total * 0.93
  print("O valor total da compra sem desconto foi: {:.2f}".format(valor_total))
  print("O valor total da compra com desconto foi: {:.2f} (desconto de 7%)".format(total_desconto))
else:
  # desconto de 11% (0.89)
  total_desconto = valor_total * 0.89
  print("O valor total da compra sem desconto foi: {:.2f}".format(valor_total))
  print("O valor total da compra com desconto foi: {:.2f} (desconto de 11%)".format(total_desconto))