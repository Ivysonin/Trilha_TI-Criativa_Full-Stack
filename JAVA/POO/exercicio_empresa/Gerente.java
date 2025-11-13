public class Gerente extends Funcionario {
    private double bonus;

    public Gerente(String nome, double salarioBase) {
        super(nome, salarioBase);
    }

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }

    public double getBonus() {
        return bonus;
    }

    @Override
    public double calcularSalario() {
        return getSalarioBase() + bonus;
    }

    @Override
    public String inforFuncionario() {
        return "Gerente: " + getNome() +
                "\nSalário Base: " + getSalarioBase() +
                "\nBônus: " + getBonus() +
                "\nSalário Total: " + calcularSalario();
    }
}