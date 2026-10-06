console.log("Ficheiro base.js carregado com sucesso!");

openSidebar.onclick = () => (sidebar.classList.add('aberta'), document.body.classList.remove('sidebar-fechada'));
closeSidebar.onclick = () => (sidebar.classList.remove('aberta'), document.body.classList.add('sidebar-fechada'));