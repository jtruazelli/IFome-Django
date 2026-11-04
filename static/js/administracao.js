// Alterna a exibição da tabela com todos os cardápios cadastrados (na tela de gestão ou importação)
function alternarSecao(idSecao, idTxtBtn, txtOcultar, txtExibir) {
    const secao = document.getElementById(idSecao);
    const txtBtn = document.getElementById(idTxtBtn);

    if (!secao || !txtBtn) return;

    if (secao.style.display === 'none' || secao.style.display === '') {
        secao.style.display = 'block';
        txtBtn.innerText = txtOcultar;
        secao.scrollIntoView({ behavior: 'smooth' });
    } else {
        secao.style.display = 'none';
        txtBtn.innerText = txtExibir;
    }
}

// Funções específicas para os botões de alternar
function alternarHistorico() {
    alternarSecao('secao-historico', 'txt-btn-hist', 'Ocultar Histórico', 'Ver Histórico Completo');
}

function alternarListaCompleta() {
    alternarSecao('secao-todos-cardapios', 'txt-btn-lista', 'Ocultar Lista Completa', 'Ver Todos os Cardápios Cadastrados');
}

// Preenche o formulário de importação/reutilização ao clicar em "Usar este modelo"
function preencherFormulario(manha, almoco, tarde) {
    const campoManha = document.getElementById('imp_manha');
    const campoAlmoco = document.getElementById('imp_almoco');
    const campoTarde = document.getElementById('imp_tarde');

    if (campoManha) campoManha.value = manha;
    if (campoAlmoco) campoAlmoco.value = almoco;
    if (campoTarde) campoTarde.value = tarde;

    if (campoManha) {
        campoManha.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}