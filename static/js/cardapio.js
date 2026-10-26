
console.log("Arquivo cardapio.js carregado!");

const sidebar = document.getElementById("sidebar");
const openSidebar = document.getElementById("openSidebar");
const closeSidebar = document.getElementById("closeSidebar");

if (sidebar && openSidebar && closeSidebar) {
    function abrirSidebar() {
        sidebar.classList.add("aberta");
        document.body.classList.remove("sidebar-fechada");

        openSidebar.setAttribute("aria-expanded", "true");
        openSidebar.setAttribute("aria-label", "Recolher menu");
    }

    function fecharSidebar() {
        sidebar.classList.remove("aberta");
        document.body.classList.add("sidebar-fechada");

        openSidebar.setAttribute("aria-expanded", "false");
        openSidebar.setAttribute("aria-label", "Abrir menu");
    }

    openSidebar.addEventListener("click", abrirSidebar);
    closeSidebar.addEventListener("click", fecharSidebar);

    // Inicia a página com a barra recolhida
    fecharSidebar();
}
