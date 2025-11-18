public class Carregador {

    public void carregar() {
        System.out.println("Carregando dispositivo...");
    }

    public void carregar(String tipo) {
        if (tipo.equalsIgnoreCase("iphone")) {
            System.out.println("Carregando iPhone com entrada Lightning.");
        } else if (tipo.equalsIgnoreCase("android")) {
            System.out.println("Carregando Android com USB-C.");
        } else {
            System.out.println("Tipo de dispositivo desconhecido.");
        }
    }

    public void carregar(int voltagem, String tipo) {
        System.out.println("Carregando " + tipo + " na voltagem " + voltagem + "V.");
    }
}