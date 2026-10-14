document.addEventListener('DOMContentLoaded', function () {

    // BOTÃO VOLTAR
    var btnVoltar = document.getElementById('btn-voltar');

    if (btnVoltar) {
        btnVoltar.addEventListener('click', function (e) {
            e.preventDefault();
            window.history.back();
        });
    }

    // BOTÃO PUBLICAR
    var btnPublicar = document.getElementById('btn-publicar');
    var formAvaliacao = document.getElementById('form-avaliacao');

    if (btnPublicar && formAvaliacao) {
        btnPublicar.addEventListener('click', function () {
            formAvaliacao.submit();
        });
    }

});