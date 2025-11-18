public class Validacao {

    public String validar(String email) {
        if (email != null && email.contains("@") && email.contains(".")) {
            return "E-mail validado com sucesso!";
        } else {
            return "Esse e-mail não é válido!";
        }
    }

    public String validar(long cpf) {
        String c = String.valueOf(cpf);

        if (c.matches("\\d{11}")) {
            return "CPF validado com sucesso!";
        } else {
            return "Esse CPF não é válido";
        }
    }

    public String validar(String senha, int tamanhoMinimo) {
        if (senha != null && senha.length() >= tamanhoMinimo) {
            return "Senha validada com sucesso!";
        } else {
            return "Essa senha não é válida!";
        }

    }
}