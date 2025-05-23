package empresa;

public abstract class Moeda {
	
	protected double valor;
	
	// informa o nome e valor da moeda
	public abstract void info();
	
	// converte para real de acordo com a cotação da moeda 
	public abstract double converter();

	public Moeda(double valor) {
		super();
		this.valor = valor;
	}
	
	
	
	
}
