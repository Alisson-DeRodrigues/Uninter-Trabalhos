package empresa;

public class Euro extends Moeda {
	
	double cotacaoEuro = 5.56; // armazena a cotação do Euro
	
	public Euro(double valor) {
		super(valor);
	}

	@Override
	public void info() {
		System.out.println("Euro: " + valor);
	}

	@Override
	public double converter() {
		return this.valor*cotacaoEuro;
	}
	
	// altera o comportamento de equals da classe mãe Object para que o método filho remove() delete a primeira ocorrência, no cofrinho instanciado, do objeto passado como parâmetro da classe Moeda
	// internamente no método remove(), força o equals a utilizar como comparador a classe e o valor das moedas no lugar do seus endereços de memória correspondentes
	@Override
	public boolean equals(Object o) {
			
		// compara primeiro a classe dos dois objetos Moeda
		if (this.getClass() != o.getClass()) {
			return false;
		}
			
		// compara o valor de cada moeda caso as classes sejam iguais
		Euro objetoDeEuro = (Euro) o;// força a conversão do objeto "o" da classe Object para Euro, pois Object não possui o atributo valor
		if(this.valor != objetoDeEuro.valor) {
			return false;
		}
		return true;
	}
	
}
