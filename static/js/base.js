document.addEventListener('DOMContentLoaded', () => {
    const btnTheme = document.getElementById('btn-theme-toggle');
    const themeIcon = document.getElementById('theme-icon');

    // Mudar o ícone do botão de tema
    function updateIcon(isDark) {
        if (!themeIcon) return;
        if (isDark) {
            themeIcon.classList.remove('bi-moon-stars');
            themeIcon.classList.add('bi-sun');
        } else {
            themeIcon.classList.remove('bi-sun');
            themeIcon.classList.add('bi-moon-stars');
        }
    }

    // Carregar tema salvo no localStorage
    const isDarkMode = localStorage.getItem('theme') === 'dark';
    if (isDarkMode) {
        document.body.classList.add('dark-mode');
        updateIcon(true);
    }

    // Evento de clique para o botão de tema (Compartilhado para Aluno e Adm)
    if (btnTheme) {
        btnTheme.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');
            const isDark = document.body.classList.contains('dark-mode');

            localStorage.setItem('theme', isDark ? 'dark' : 'light');
            updateIcon(isDark);
        });
    }

    // Lógica para Abrir e Fechar a Sidebar da Administração
    const openSidebarBtn = document.getElementById('openSidebar');
    const closeSidebarBtn = document.getElementById('closeSidebar');
    const sidebar = document.getElementById('sidebar');

    if (openSidebarBtn && sidebar) {
        openSidebarBtn.addEventListener('click', () => {
            document.body.classList.remove('sidebar-fechada');
            sidebar.classList.add('aberta');
        });
    }

    if (closeSidebarBtn && sidebar) {
        closeSidebarBtn.addEventListener('click', () => {
            document.body.classList.add('sidebar-fechada');
            sidebar.classList.remove('aberta');
        });
    }
});