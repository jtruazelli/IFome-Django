
document.addEventListener("DOMContentLoaded", function () {
    const btnToggle = document.getElementById("btn-toggle");
    const sidebar = document.getElementById("sidebar");

    btnToggle.addEventListener("click", function () {
        sidebar.classList.toggle("recolhida");

        const recolhida = sidebar.classList.contains("recolhida");

        btnToggle.setAttribute(
            "aria-label",
            recolhida ? "Expandir menu" : "Recolher menu"
        );
    });
});
