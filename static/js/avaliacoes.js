document.addEventListener('DOMContentLoaded', function () {
    var stars = document.querySelectorAll('.star-icon');
    var inputNota = document.getElementById('nota-input');

    stars.forEach(function (star, index) {
        star.addEventListener('click', function () {
            var avaliacao = star.getAttribute('data-avaliacao');

            if (inputNota) {
                inputNota.value = avaliacao;
            }

            stars.forEach(function (s) {
                s.classList.remove('ativo');
            });

            for (var i = 0; i <= index; i++) {
                stars[i].classList.add('ativo');
            }
        });
    });

    var btnVoltar = document.getElementById('btn-voltar');

    if (btnVoltar) {
        btnVoltar.addEventListener('click', function (e) {
            e.preventDefault();
            // Retorna para a página anterior sem salvar nada
            window.history.back();
        });
    }

    var btnPublicar = document.getElementById('btn-publicar');
    var formAvaliacao = document.getElementById('form-avaliacao');

    if (btnPublicar && formAvaliacao) {
        btnPublicar.addEventListener('click', function () {
            formAvaliacao.submit();
        });
    }

});