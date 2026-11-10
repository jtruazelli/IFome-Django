# 🍽️ IFome

Sistema web para consulta e gerenciamento dos cardápios do refeitório do Instituto Federal de Rondônia (IFRO) — Campus Cacoal.

## Sobre o projeto

O **IFome** é um Projeto Integrador desenvolvido por estudantes do curso Técnico em Informática do IFRO — Campus Cacoal. O sistema disponibiliza os cardápios do refeitório de maneira prática para estudantes e servidores, reduzindo a necessidade de impressão e de deslocamento até o refeitório para consultar as refeições. Também facilita a atualização diária dos cardápios e oferece um espaço para avaliações e mensagens de carinho da comunidade escolar.

## Funcionalidades implementadas e previstas

- 
Consulta ao cardápio diário (Manhã, Almoço e Tarde).
- 
Visualização da tabela de refeições e horários.
- 
Login, logout e controle de acesso restrito à administração.
- 
Avaliação das refeições por nota (estrelas) e envio de comentários ou mensagens de carinho.
- 
Painel administrativo exclusivo com dashboard estatístico.
- 
Cadastro, edição, exclusão e importação/reutilização de cardápios anteriores.
- 
Consulta administrativa ao resumo das avaliações com distribuição por estrelas e exclusão de comentários.

> **Status:** Projeto em desenvolvimento avançado com rotas, views, modelos de dados e interface administrativa totalmente integrados.

## Tecnologias

- 
Python
- 
Django
- 
HTML5
- 
CSS3 (com suporte a modo claro/escuro)
- 
JavaScript
- 
Bootstrap 5 & Bootstrap Icons
- 
SQLite

## Equipe e divisão de responsabilidades

| Integrante | App Django | Responsabilidades |
|---|---|---|
| Fernanda Kanazawa Inomata | `cardapio` | Página principal; exibição do cardápio do dia por turnos e tabela geral. |
| Letícia Danielly de Lavor Oliveira | `usuarios` | Login, logout, autenticação e controle de permissões de usuário. |
| Julia Truazelli Rossi (líder) | `avaliacoes` | Sistema de avaliações por estrelas, cadastro de opiniões e mensagens de carinho. |
| Isis Maciel Pinho | `administracao` | Painel administrativo completo, gerenciamento de cardápios (CRUD e importação) e relatório estatístico de avaliações. |

## Apps Django: Models, Views e Arquivos

### `cardapio` — Fernanda

**Finalidade:** Exibir o cardápio público do dia atual e a tabela geral para estudantes e servidores.

**Models:**
- `Cardapio`: armazena a `data` (única) e os textos das refeições (`refeicao_manha`, `refeicao_almoco` e `refeicao_tarde`).

**Views:**
- `index`: busca o cardápio do dia atual (via `localdate()`), formata os itens de cada refeição por linha e renderiza a página principal (`index.html`).
- `tabela`: exibe a tabela informativa do refeitório (`tabela.html`).

**Arquivos:** `models.py`, `views.py`, `urls.py`, `templates/index.html`, `templates/tabela.html`.

---

### `usuarios` — Letícia

**Finalidade:** Autenticar administradores e controlar o acesso às funcionalidades restritas do sistema.

**Models:** Utiliza o modelo padrão de autenticação do Django (`User`).

**Views:** Login, logout e controle de permissões de acesso às rotas protegidas (`@login_required`).

**Arquivos:** `views.py`, `urls.py`, `forms.py` (se necessário), `templates/usuarios/`.

---

### `avaliacoes` — Julia

**Finalidade:** Receber o feedback dos usuários sobre o cardápio e mensagens para a equipe do refeitório.

**Models:**
- `Avaliacao`: armazena o `tipo` ('1' - Cardápio do Dia ou '2' - Mensagem de Carinho), `nota` (1 a 5), `mensagem`, `nome_autor` e `data_criacao`.

**Views:**
- `pagina_avaliacoes`: lista as avaliações do cardápio e as mensagens de carinho publicadas.
- `cadastrar_avaliacao`: processa e valida a nota e o comentário enviado pelo usuário.
- `mensagem_carinho`: permite o envio direto de mensagens afetuosas à equipe da cozinha.

**Arquivos:** `models.py`, `views.py`, `urls.py`, `templates/avaliacoes/avaliacoes.html`, `templates/avaliacoes/cadastroAvaliacoes.html`, `templates/avaliacoes/mensagemCarinho.html`.

---

### `administracao` — Isis

**Finalidade:** Área administrativa do IFome, desenvolvida com layout, navegação lateral e suporte a tema claro/escuro próprios, isolada visualmente da área pública.

**Funcionalidades:**
- Dashboard com indicadores gerais: média de satisfação, total de comentários e lista das últimas avaliações.
- Gerenciamento completo de cardápios (listagem, criação, edição e exclusão).
- Ferramenta de importação/reutilização rápida de cardápios recentes.
- Relatório e resumo estatístico de comentários (média geral, contagem total e distribuição por estrelas) com opção de exclusão.
- Proteção de rotas com decorador `@login_required`.

**Views:**
- `dashboard`: visão geral com estatísticas e métricas de avaliações.
- `lista_cardapios`: listagem de cardápios com suporte a filtros por período e refeição.
- `novo_cardapio` & `editar_cardapio`: criação e atualização de refeições diárias via formulário (`CardapioForm`).
- `excluir_cardapio`: remoção de cardápios do sistema.
- `importar_cardapio`: interface de cópia/reutilização baseada nos últimos cardápios salvos.
- `resumo_comentarios` & `excluir_comentario`: visualização analítica das avaliações e exclusão de comentários inadequados.

**Arquivos:**
- `views.py`, `urls.py`, `forms.py`.
- `templates/base_adm.html`: layout-base do painel com menu lateral dinâmico, topbar e script de tema.
- `templates/adm/`: `dashboard.html`, `cardapio.html`, `novo_cardapio.html`, `editar_cardapio.html`, `importar_cardapio.html`, `resumo_comentarios.html`.

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
- `/tabela/` (`tabela`)

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

Integração entre os apps finalizada (painel administrativo alimentado por `cardapio` e `avaliacoes`), telas ajustadas com layout responsivo e validações de regras de negócio em fase de testes finais.