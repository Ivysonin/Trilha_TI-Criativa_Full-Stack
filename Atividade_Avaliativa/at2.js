const buttons = document.querySelectorAll(".add-cart");

buttons.forEach(btn => {
  btn.addEventListener("click", () => {
    alert("Produto adicionado ao carrinho!");
  });
});