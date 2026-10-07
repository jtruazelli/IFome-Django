const btnTheme = document.getElementById('btn-theme-toggle');
        const themeIcon = document.getElementById('theme-icon');

        // Carrega tema salvo
        if (localStorage.getItem('theme') === 'dark') {
            document.body.classList.add('dark-mode');
            if (themeIcon) themeIcon.textContent = '☀️';
        }

        if (btnTheme) {
            btnTheme.addEventListener('click', () => {
                document.body.classList.toggle('dark-mode');
                const isDark = document.body.classList.contains('dark-mode');
                localStorage.setItem('theme', isDark ? 'dark' : 'light');
                if (themeIcon) themeIcon.textContent = isDark ? '☀️' : '🌙';
            });
        }
