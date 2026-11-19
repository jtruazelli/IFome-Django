document.addEventListener('DOMContentLoaded', () => {
    const starContainer = document.getElementById('rating-stars');

    // Se o elemento não existir na página atual (ex: na lista de avaliações), encerra o script sem erros
    if (!starContainer) return;

    const stars = starContainer.querySelectorAll('.star-btn');
    const inputNota = document.getElementById('input-nota');
    const form = document.getElementById('form-avaliacao');

    stars.forEach(star => {
        star.addEventListener('click', () => {
            const val = star.getAttribute('data-value');
            inputNota.value = val;

            // Limpa seleções anteriores
            stars.forEach(s => s.classList.remove('selected'));

            // Marca a estrela clicada (o CSS 'flex-direction: row-reverse' junto com '~' cuidará das anteriores)
            star.classList.add('selected');
        });
    });

    // Validação antes do envio do formulário
    if (form) {
        form.addEventListener('submit', (e) => {
            if (!inputNota.value || inputNota.value === "0") {
                e.preventDefault();
                alert('Por favor, selecione uma nota de 1 a 5 estrelas.');
            }
        });
    }
});