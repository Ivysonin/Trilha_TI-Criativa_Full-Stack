// String -> texto
let saudacao = 'Olá, mundo!';
console.log(saudacao);

// Number -> 1, 2.2
let idade = 18;
console.log("Essa é minha idade:", idade);

// Boolean -> verdadeiro ou falso
let logado = true;
console.log("Está logado:", logado);

// Null -> valor nuol (intencionalmente vazio)
let resposta = null;
console.log(resposta);

// Object -> conjunto de pares chave:valor
let pessoa = {
    nome:"Ivyson",
    idade:17,
    altura:1.71
}
console.log(pessoa)
console.log(`Nome: ${pessoa.nome}`)
console.log(`Idade: ${pessoa.idade}`)
console.log(`Altura: ${pessoa.altura}`)

// Array -> lista de valores (índices começam em 0)
let frutas = ["Banana", "Uva", "Laranja"]
console.log(frutas)
console.log(frutas[1])