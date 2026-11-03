document.addEventListener('DOMContentLoaded', function () {

    // Botão Voltar
    const btnVoltar = document.getElementById('btn-voltar');

    if (btnVoltar) {
        btnVoltar.addEventListener('click', function (e) {
            e.preventDefault();
            window.history.back();
        });
    }

    // Formulário de avaliação
    const formAvaliacao = document.getElementById('form-avaliacao');

    if (formAvaliacao) {
        formAvaliacao.addEventListener('submit', function (e) {

            const notaSelecionada = formAvaliacao.querySelector(
                'input[name="nota"]:checked'
            );

            const mensagem = formAvaliacao.querySelector(
                'textarea[name="mensagem"]'
            );

            if (!notaSelecionada) {
                e.preventDefault();
                alert('Por favor, selecione uma nota de 1 a 5 estrelas.');
                return;
            }

            if (!mensagem || !mensagem.value.trim()) {
                e.preventDefault();
                alert('Por favor, escreva um comentário.');
            }

        });
    }

});