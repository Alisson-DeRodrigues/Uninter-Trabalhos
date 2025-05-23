package empresa;

import java.util.Scanner;

public class Menu {
	
	private Scanner teclado;
	private Cofrinho cofrinho;
	
	public Menu() {
		teclado = new Scanner(System.in); // instancia um scanner
		cofrinho = new Cofrinho(); // instancia um cofrinho
	}
	
	public void menuPrincipal() {
		
		System.out.println("Menu Principal");
		System.out.println("[1] Adicionar moeda");
		System.out.println("[2] Remover moeda");
		System.out.println("[3] Listar moedas");
		System.out.println("[4] Calcular valor total convertido para real");
		System.out.println("[0] Encerrar");
		
		String opcaoEscolhida = teclado.next();
		
		switch(opcaoEscolhida) {
		case "0":
			System.out.println("Cofre fechado.");
			break;
		case "1":
			menuAdicionarMoeda();
			menuPrincipal();
			break;
		case "2":
			menuRemoverMoeda();
			menuPrincipal();
			break;
		case "3":
			menuListarMoedas();
			menuPrincipal();
			break;
		case "4":
			menuValorCofrinhoEmReal();
			menuPrincipal();
			break;
		default:
			System.out.println("Opção inválida.");
			System.out.println();
			menuPrincipal();
			break;
		}
	}
	
	public void menuAdicionarMoeda() {
		System.out.println("Escolha o tipo da moeda: ");
		System.out.println("[1] Real");
		System.out.println("[2] Dolar");
		System.out.println("[3] Euro");
		
		int moedaEscolhida = 0;
		double valorEscolhido = 0;
		
		try {
			moedaEscolhida = teclado.nextInt();
			
			System.out.print("Digite o valor: ");
			valorEscolhido = teclado.nextDouble();
		} catch (Exception e) {
			return;
		}
		
		// adiciona a moeda escolhida no cofrinho
		Moeda moeda = null;
		if(moedaEscolhida == 1) {
			moeda = new Real(valorEscolhido);
		}
		else if(moedaEscolhida == 2) {
			moeda = new Dolar(valorEscolhido);
		}
		else if(moedaEscolhida == 3) {
			moeda = new Euro(valorEscolhido);
		}
		else {
			System.out.println("Escolha uma moeda válida.");
			System.out.println();
			menuPrincipal();
		}
		
		cofrinho.adicionar(moeda);
		
		System.out.println("Moeda adicionada.");
		System.out.println();
	}
	
	public void menuRemoverMoeda() {
		System.out.println("Escolha o tipo da moeda: ");
		System.out.println("[1] Real");
		System.out.println("[2] Dolar");
		System.out.println("[3] Euro");
		
		int moedaEscolhida = 0;
		double valorEscolhido = 0;
		
		try {
			moedaEscolhida = teclado.nextInt();
			
			System.out.print("Digite o valor: ");
			valorEscolhido = teclado.nextDouble();
		} catch (Exception e) {
			return;
		}
		
		// remove a moeda escolhida no cofrinho
		Moeda moeda = null;
		if(moedaEscolhida == 1) {
			moeda = new Real(valorEscolhido);
		}
		else if(moedaEscolhida == 2) {
			moeda = new Dolar(valorEscolhido);
		}
		else if(moedaEscolhida == 3) {
			moeda = new Euro(valorEscolhido);
		}
		else {
			System.out.println("Escolha uma moeda válida.");
			System.out.println();
			menuPrincipal();
		}
		
		cofrinho.remover(moeda);
		System.out.println("Moeda removida.");
		System.out.println();
	}
	
	public void menuListarMoedas() {
		cofrinho.listagemMoedas(); 	// lista todas as moedas presentes no cofrinho
		System.out.println();
	}
	
	public void menuValorCofrinhoEmReal() {
		double totalCofreEmReal = cofrinho.totalConvertido(); // armazena o total de moedas convertido para real
		System.out.println("O total de moedas no cofrinho convertidos para real é: " + totalCofreEmReal);
		System.out.println();
	}
}
