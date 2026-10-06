const btnToggle = document.getElementById("btn-toggle");
const cabecalho = document.getElementById("cabecalho");
const conteudo = document.querySelector(".conteudo-principal");

botaoToggle.addEventListener("click", function () {
    barraLateral.classList.toggle("recolhida");
    conteudo.classList.toggle("menu-recolhido");
});