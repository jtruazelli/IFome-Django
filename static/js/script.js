const botaoToggle = document.getElementById("btn-toggle");
const barraLateral = document.getElementById("sidebar");
const conteudo = document.querySelector(".conteudo-principal");

botaoToggle.addEventListener("click", function () {
    barraLateral.classList.toggle("recolhida");
    conteudo.classList.toggle("menu-recolhido");
});