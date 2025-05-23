package empresa;

import java.util.ArrayList;

public class Cofrinho {
	
	// cria um ArrayList para armazenar as moedas
	private ArrayList<Moeda> listaMoedas = new ArrayList();
	
	// adiciona uma moeda ao ArrayLst listaMoedas
	public void adicionar(Moeda m) {
		this.listaMoedas.add(m);
	}
	
	// remove de listaMoedas a primeira ocorrência da moeda especificada
	public void remover(Moeda m) {
		this.listaMoedas.remove(m);
	}
	
	// lista todas as moedas no ArrayList listaMoedas
	public void listagemMoedas() {
		//verifiva se o cofre está vazio
		if(this.listaMoedas.isEmpty()) {
			System.out.println("O cofrinho está vazio.");
			return;
		}
		
		// mostra o tipo e o valor de cada moeda
		for(Moeda m : this.listaMoedas) {
			m.info();
		}
	}
	
	// converte todas as moedas no cofrinho para real e retorna esse valor
	public double totalConvertido() {
		if(this.listaMoedas.isEmpty()) {
			return 0;
		}
		
		double valorConvertido = 0;
		
		for(Moeda m : this.listaMoedas) {
			valorConvertido += m.converter(); // soma o valor convertido para real da moeda analisada a cada iteração do laço ao valorConvertido
		}
		
		return valorConvertido;
	}
}
