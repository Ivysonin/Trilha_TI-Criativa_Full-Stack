public class Vendedor extends Funcionario{
    private double comissao;

    public Vendedor(String nome, double salarioBase) {
        super(nome, salarioBase);
    }

    public void setComissao(double comissao) {
        this.comissao = comissao;
    }

    public double getComissao() {
        return comissao;
    }

    @Override
    public double calcularSalario() {
        return getSalarioBase() + comissao;
    }

    @Override
    public String inforFuncionario() {
        return "Vendedor: " + getNome() +
                "\nSalário Base: " + getSalarioBase() +
                "\nComissão: " + getComissao() +
                "\nSalário Total: " + calcularSalario();
    }
}