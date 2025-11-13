public class Main {
    public static void main(String[] args) {

        var gerente = new Gerente("Ivyson", 1000);
        gerente.setBonus(300); // Adicionando o bônus do gerente
        System.out.println(gerente.inforFuncionario()); // Exibindo informações

        System.out.println("\n");

        var vendedor = new Vendedor("Pedro", 500);
        vendedor.setComissao(200);
        System.out.println(vendedor.inforFuncionario()); // Exibindo informações
    }
}