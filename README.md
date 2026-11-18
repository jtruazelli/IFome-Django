# 🍽️ IFome

Sistema web para consulta e gerenciamento dos cardápios do refeitório do Instituto Federal de Rondônia (IFRO) — Campus Cacoal.

## Sobre o projeto

O **IFome** é um Projeto Integrador desenvolvido por estudantes do curso Técnico em Informática do IFRO — Campus Cacoal. O sistema disponibiliza os cardápios do refeitório de maneira prática e pública para estudantes e servidores, reduzindo a necessidade de impressão e de deslocamento até o refeitório para consultar as refeições. Também oferece um painel administrativo completo para atualização diária dos cardápios e acompanhamento das avaliações e mensagens de carinho enviadas pela comunidade escolar.

## Funcionalidades implementadas

- **Área Pública (Estudantes e Servidores — sem necessidade de login):**
  - Consulta ao cardápio diário (Lanche da Manhã, Almoço e Lanche da Tarde).
  - Avaliação das refeições por nota (1 a 5 estrelas) com comentários e envio de mensagens de carinho à equipe da cozinha.
- **Área Administrativa (Acesso Autenticado e Autorizado por Perfis):**
  - Login, logout e controle de acesso baseado em **Groups** e **Permissions** do Django (`Nutricionista` vs. `Estagiario_CAED`).
  - Dashboard administrativo com indicadores de satisfação (média do dia e média geral), contagem de comentários e feed das últimas avaliações.
  - Cadastro, edição (completa e rápida *inline*), exclusão segura (via `POST` com modal de confirmação) e importação/clonagem de cardápios anteriores.
  - Resumo estatístico das avaliações com filtros por período e estrela, distribuição percentual das notas e moderação de comentários.
  - Tela personalizada de erro **403 (Acesso Restrito)** e desabilitação visual de ações para perfis somente leitura.

> **Status:** Sistema funcional com CRUDs completos, validações de integridade e controle granular de autorização (`Groups` e `Permissions`) implementados.

## Tecnologias

- Python 3
- Django
- HTML5 & CSS3 (com suporte a modo claro/escuro)
- JavaScript
- Bootstrap 5 & Bootstrap Icons
- SQLite

---

## Como executar o projeto localmente

### 1. Clonar o repositório e ativar o ambiente virtual

```bash
git clone [https://github.com/jtruazelli/IFome-Django.git](https://github.com/jtruazelli/IFome-Django.git)
cd IFome-Django
python -m venv .venv
```

* **Windows (PowerShell):**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
* **Linux / macOS:**
  ```bash
  source .venv/bin/activate
  ```

### 2. Instalar dependências e aplicar migrações

```bash
pip install -r requirements.txt
python manage.py migrate
```

### 3. Configurar perfis de acesso e usuários de teste (automático)

O projeto possui um comando de gerenciamento personalizado (`configurar_perfis`) que cria automaticamente os grupos de permissão (`Nutricionista` e `Estagiario_CAED`) e dois usuários prontos para teste:

```bash
python manage.py configurar_perfis
```

### 4. Iniciar o servidor

```bash
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/` para a área pública ou `http://127.0.0.1:8000/administracao/` para o painel administrativo.

---

## Controle de Acesso, Perfis (`Groups`) e Permissões

Como os estudantes consultam o cardápio e enviam avaliações publicamente sem login, o controle de autorização foi estruturado para diferenciar dois perfis dentro da área administrativa:

| Perfil (`Group`) | Permissões Atribuídas | Comportamento no Sistema | Credencial de Teste |
|---|---|---|---|
| **`Nutricionista`** | `view_cardapio`, `add_cardapio`, `change_cardapio`, `delete_cardapio`, `view_avaliacao`, `delete_avaliacao` | Acesso total para cadastrar, editar, importar e excluir cardápios, além de moderar/excluir avaliações. | **Usuário:** `nutri_teste`<br>**Senha:** `ifome123` |
| **`Estagiario_CAED`** | `view_cardapio`, `view_avaliacao` | Acesso somente leitura: visualiza métricas, cardápios e comentários, mas vê os botões de ação desabilitados (`.btn-sem-permissao`) e recebe **HTTP 403** se tentar acessar rotas de escrita diretamente. | **Usuário:** `estagiario_teste`<br>**Senha:** `ifome123` |

---

## Equipe e divisão de responsabilidades

| Integrante | App Django | Responsabilidades |
|---|---|---|
| Fernanda Kanazawa Inomata | `cardapio` | Página principal e exibição pública do cardápio do dia por turnos. |
| Letícia Danielly Oliveira de Lavor | `usuarios` | Login, logout, autenticação e controle de acesso. |
| Julia Truazelli Rossi (líder) | `avaliacoes` | Sistema de avaliações por estrelas, cadastro de opiniões e mensagens de carinho. |
| Isis Maciel Pinho | `administracao` | Painel administrativo completo, gerenciamento de cardápios (CRUD e importação), relatório estatístico e controle de permissões (`Groups`/`Permissions`). |

---

## Apps Django: Models, Views e Arquivos

### `cardapio` — Fernanda

**Finalidade:** Exibir o cardápio público do dia atual para estudantes e servidores.

**Models:**
- `Cardapio`: armazena a `data` (única) e os textos das refeições (`refeicao_manha`, `refeicao_almoco` e `refeicao_tarde`).

**Views:**
- `index`: busca o cardápio do dia atual (via `localdate()`), formata os itens de cada refeição por linha e renderiza a página principal (`index.html`).

**Arquivos:** `models.py`, `views.py`, `urls.py`, `templates/index.html`.

---

### `usuarios` — Letícia

**Finalidade:** Autenticar administradores e controlar o acesso às funcionalidades restritas do sistema.

**Models:** Utiliza o modelo padrão de autenticação do Django (`User`).

**Views:** Login, logout e integração com o sistema de autenticação (`@login_required`).

**Arquivos:** `views.py`, `urls.py`, `templates/usuarios/`.

---

### `avaliacoes` — Julia

**Finalidade:** Receber o feedback dos usuários sobre o cardápio e mensagens para a equipe do refeitório.

**Models:**
- `Avaliacao`: armazena o `tipo` (`'1'` - Cardápio do Dia ou `'2'` - Mensagem de Carinho), `nota` (1 a 5), `mensagem`, `nome_autor` e `data_criacao`.

**Views:**
- `pagina_avaliacoes`: lista as avaliações do cardápio e as mensagens de carinho publicadas.
- `cadastrar_avaliacao`: processa e valida a nota e o comentário enviado pelo usuário.
- `mensagem_carinho`: permite o envio direto de mensagens afetuosas à equipe da cozinha.

**Arquivos:** `models.py`, `views.py`, `urls.py`, `templates/avaliacoes/avaliacoes.html`, `templates/avaliacoes/cadastroAvaliacoes.html`, `templates/avaliacoes/mensagemCarinho.html`.

---

### `administracao` — Isis

**Finalidade:** Área administrativa do IFome, desenvolvida com layout, navegação lateral, suporte a tema claro/escuro próprios e controle de permissões por perfil.

**Funcionalidades:**
- Dashboard com indicadores gerais: média de satisfação do dia e geral, total de comentários e lista das últimas avaliações.
- Gerenciamento completo de cardápios (listagem com filtro por período, criação, edição completa, edição rápida *inline* e exclusão).
- Ferramenta de importação/clonagem rápida de cardápios recentes.
- Relatório e resumo estatístico de comentários (média geral, contagem total e distribuição por estrelas) com opção de moderação/exclusão.
- Proteção de rotas com `@login_required` e `@permission_required(..., raise_exception=True)`, além de comando customizado `configurar_perfis.py` para inicialização de grupos e usuários de teste.

**Views:**
- `dashboard`: visão geral com estatísticas e métricas de avaliações.
- `lista_cardapios`: listagem de cardápios com suporte a filtros por período e edição rápida do cardápio atual.
- `novo_cardapio` & `editar_cardapio`: criação e atualização de refeições diárias via formulário (`CardapioForm`).
- `excluir_cardapio`: remoção segura de cardápios via `POST`.
- `importar_cardapio`: interface de cópia/reutilização baseada nos últimos cardápios salvos.
- `resumo_comentarios` & `excluir_comentario`: visualização analítica das avaliações e exclusão de comentários inadequados.

**Arquivos:**
- `views.py`, `urls.py`, `forms.py`, `management/commands/configurar_perfis.py`.
- `templates/base_adm.html` e `templates/403.html` (na pasta global `templates/`).
- `administracao/templates/adm/`: `dashboard.html`, `cardapio.html`, `novo_cardapio.html`, `editar_cardapio.html`, `importar_cardapio.html`, `resumo_comentarios.html`.

---

### Mapeamento de Rotas (`urls.py`)

#### `administracao/urls.py` (`app_name = 'administracao'`)
- `/administracao/` (`dashboard`)
- `/administracao/cardapios/` (`cardapio`)
- `/administracao/cardapios/novo/` (`novo_cardapio`)
- `/administracao/cardapios/<id>/editar/` (`editar_cardapio`)
- `/administracao/cardapios/<id>/excluir/` (`excluir_cardapio`)
- `/administracao/importar/` (`importar_cardapio`)
- `/administracao/comentarios/` (`resumo_comentarios`)
- `/administracao/comentarios/<id>/excluir/` (`excluir_comentario`)

#### `cardapio/urls.py`
- `/` (`index`)

#### `avaliacoes/urls.py`
- `/avaliacoes/` (`pagina_avaliacoes`)
- `/avaliacoes/cadastrar/` (`cadastrar_avaliacao`)
- `/avaliacoes/mensagem-carinho/` (`mensagem_carinho`)

---

## Organização do desenvolvimento no GitHub

Cada integrante desenvolve suas funcionalidades em uma **branch individual**, enviando as alterações por commits/push para revisão antes do merge na branch principal.

| Integrante | Branch individual |
|---|---|
| Fernanda | `Kanazawa` |
| Letícia | `Leticia` |
| Julia | `Truazelli` |
| Isis | `Maciel` |

## Etapa atual

Autorização baseada em `Groups` e `Permissions` concluída (com comando automatizado `configurar_perfis`, proteção de rotas via `@permission_required`, desabilitação visual nos templates e tela personalizada `403.html`), preparando o sistema para os ajustes finais de produção e documentação da entrega final.