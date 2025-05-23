print ("Bem-vindo ao Controle de Livros de Alisson de Souza Rodrigues")

lista_livro = []
id_global = 0

def tela_inicial():
    while True:
        print("=" * 100)
        print("-" * 44 + "TELA INICIAL" + "-" * 44)

        print("(1) Cadastrar Livro")
        print("(2) Consultar Livro")
        print("(3) Remover Livro")
        print("(4) Sair")

        escolha = input("Escolha a opção desejada: ")
        if escolha == "1":
            cadastrar_livro(id_global)
        elif escolha == "2":
        	consultar_livro()
        elif escolha == "3":
        	remover_livro()
        elif escolha == "4":
            break
        else:
            print("Escolha uma opção válida.")
            continue


def cadastrar_livro(id):
	print("=" * 100)
	print("-" * 42 + "CADASTRAR LIVRO" + "-" * 43)
	livro = {}
	livro["id"] = id
	livro["nome"] = input("Insira o nome do livro: ")
	livro["autor"] = input("Insira o autor do livro: ")
	livro["editora"] = input("Insira a editora do livro: ")
	lista_livro.append(livro.copy())
	
	global id_global # para o Python reconher a variável global id_global dentro desta função na instrução a seguir
	id_global += 1

def consultar_livro():
	while True:
		print("=" * 100)
		print("-" * 42 + "CONSULTAR LIVRO" + "-" * 43)
		
		print("(1) Consultar Todos")
		print("(2) Consultar por Id")
		print("(3) Consultar por Autor")
		print("(4) Retornar ao Menu")
		
		escolha = input("Escolha a opção desejada: ")
		
		# exibe todos os livros cadastrados
		if escolha == "1": 
			for i in lista_livro: # obtem um dicionário na lista list_livro a cada iteração
				for j, k in i.items(): # extrai o conjunto par-chave de cada dicionário
					print("{}: {}".format(j, k))
				print(" ")
				
		# pesquisa um livro por seu Id
		elif escolha == "2":
			id = input("Insira o Id do livro: ")
			dicionario_indice = " "
			# procura em lista_livro o índice do dicionario que corresponde ao id do livro passado e armazena esse índice em dicionario_indice se houver
			for i in lista_livro:
				for j, k in i.items():
					if j == "id" and str(k) == id:
						dicionario_indice = lista_livro.index(i)
			# exibe os dados do dicionario com o livro cadastrado conforme o indice indicado em dicionario_indice
			try:
				for j, k in lista_livro[dicionario_indice].items():
					print("{}: {}".format(j, k))
			# se o livro não for encontrado, dicionario_indice continuará igual a " " (string vazi), isso gerará um erro na linha anterior que é tratato pelo except a seguir
			except:
				print("Livro não encontrado.")
			
		# consulta os livros de um autor
		elif escolha == "3":
			autor = input("Insira o autor: ")
			livros_autor = [] # lista com todos os livros do autor
			
			# procura por todos os livros do autor especificado
			for i in lista_livro:
				for j, k in i.items():
					if j == "autor" and str(k) == autor:
						livros_autor.append(i)
			# lista todos os livros em livros_autor
			if livros_autor != []:
				for i in livros_autor:
					for j, k in i.items():
						print("{}: {}".format(j, k))
			else:
				print("Nenhum livro foi encontrado.")
				
		# retorna ao menu principal
		elif escolha == "4":
			break
		else:
			print("Escolha uma opção válida.")
			continue
		
		break

def remover_livro():
	print("Remover Livro")
	print("=" * 100)
	print("-" * 44 + "REMOVER LIVRO" + "-" * 43)

	id = input("Insira o id do livro: ")
	indice = " " # indice do livro a ser removido
	
	# pesquisa pelo indice do livro a ser deletado
	for i in lista_livro:
		for j, k in i.items():
			if j == "id" and str(k) == id:
				indice = lista_livro.index(i)
	try:
		del lista_livro[indice]
	except:
		print("Id inválido.")
	
tela_inicial()