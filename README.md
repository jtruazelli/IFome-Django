# 🍽️ IFome

Sistema web para consulta e gerenciamento dos cardápios do refeitório do Instituto Federal de Rondônia (IFRO) — Campus Cacoal.

## Sobre o projeto

O **IFome** é um Projeto Integrador desenvolvido por estudantes do curso Técnico em Informática do IFRO — Campus Cacoal. O sistema pretende disponibilizar os cardápios do refeitório de maneira prática para estudantes e servidores, reduzindo a necessidade de impressão e de deslocamento até o refeitório apenas para consultar as refeições. Também busca facilitar a atualização dos cardápios e oferecer um espaço para avaliações e comentários.

## Funcionalidades previstas

- Consulta ao cardápio e aos pratos oferecidos.
- Visualização dos ingredientes, dos alergênicos e das informações nutricionais.
- Login, logout e controle de acesso administrativo.
- Avaliação das refeições por estrelas e comentários.
- Cadastro, edição e importação/reutilização de cardápios anteriores pela administração.
- Consulta administrativa a um resumo das avaliações.

> **Status:** projeto em desenvolvimento. As funcionalidades acima são planejadas e poderão ser ajustadas ao longo da implementação.

## Tecnologias

- Python
- Django
- HTML
- CSS
- JavaScript
- Bootstrap
- SQLite

## Equipe e divisão de responsabilidades

| Integrante | App Django | Responsabilidades |
|---|---|---|
| Fernanda Kanazawa Inomata | `cardapio` | Página principal; visualização do cardápio, pratos, ingredientes, alergênicos e tabela nutricional. |
| Letícia Danielly de Lavor Oliveira | `usuarios` | Login, logout, autenticação e permissões de administrador. |
| Julia Truazelli Rossi (líder) | `avaliacoes` | Avaliação por estrelas e comentários. |
| Isis Maciel Pinho | `administracao` | Desenvolvimento da área administrativa independente, com navegação e layout próprios; gerenciamento dos cardápios e painel de resumo das avaliações. |

## Apps Django: Models, Views e arquivos

A estrutura abaixo é o **planejamento inicial**. Os nomes das Views, os Models e os arquivos poderão ser ajustados conforme o desenvolvimento e a integração entre os apps.

### `cardapio` — Fernanda

**Finalidade:** disponibilizar a página principal e as informações sobre os cardápios e as refeições.

**Models previstos:** `Cardapio`, `Prato`, `Ingrediente`, `Alergenico` e `TabelaNutricional`, com seus relacionamentos.

**Views previstas:** página principal; consulta ao cardápio; detalhamento de pratos, ingredientes, alergênicos e informações nutricionais.

**Arquivos previstos:** `models.py`, `views.py`, `urls.py`, `admin.py` (se necessário) e `templates/cardapio/`.

### `usuarios` — Letícia

**Finalidade:** autenticar usuários e controlar o acesso às funcionalidades administrativas.

**Models previstos:** utilização do modelo de usuário do Django; personalizações somente se necessárias.

**Views previstas:** login, logout e controle de acesso conforme as permissões do usuário.

**Arquivos previstos:** `views.py`, `urls.py`, `forms.py` (se necessário) e `templates/usuarios/`.

### `avaliacoes` — Julia

**Finalidade:** receber avaliações das refeições e comentários.

**Models previstos:** `Avaliacao`.

**Views previstas:** registrar avaliação por estrelas e comentário; enviar mensagens para as cozinheiras.

**Arquivos previstos:** `models.py`, `views.py`, `urls.py`, `forms.py` e `templates/avaliacoes/`.

### `administracao` — Isis

**Finalidade:** desenvolver a **área administrativa do IFome**, separada visualmente da área pública do sistema. Essa área terá interface, layout e barra de navegação próprios, reunindo em um só lugar as funcionalidades exclusivas dos administradores (CAED e nutricionista).

**Funcionalidades previstas:**
- Página inicial/painel administrativo com acesso às ferramentas de gerenciamento.
- Navegação própria entre as páginas administrativas.
- Cadastro, edição e importação/reutilização de cardápios anteriores.
- Consulta a um resumo das avaliações e dos comentários sobre as refeições.
- Acesso restrito aos usuários com permissão administrativa, em integração com o app `usuarios`.

**Models previstos:** reutilizar os Models `Cardapio` e `Avaliacao` dos apps correspondentes, evitando duplicar dados.

**Views previstas:** painel administrativo; listagem e gerenciamento dos cardápios; formulários de cadastro, edição e importação/reutilização; painel de resumo das avaliações.

**Arquivos previstos:**
- `views.py`: Views das páginas administrativas e das ações de gerenciamento.
- `urls.py`: rotas exclusivas da área administrativa.
- `forms.py`: formulários de cadastro e edição de cardápios, conforme a integração com `cardapio`.
- `templates/adm/base_admin.html`: layout-base próprio, incluindo a barra de navegação administrativa.
- `templates/adm/`: páginas do painel, gerenciamento dos cardápios e resumo das avaliações.
- Arquivos CSS e JavaScript próprios da interface administrativa, conforme a organização de arquivos estáticos do projeto.

**Observação:** a área administrativa é uma interface própria do IFome, não apenas uma configuração do painel automático do Django (`admin.py`).

### Integração entre os apps

- `administracao` utilizará os dados de `cardapio` para cadastrar e atualizar os cardápios exibidos aos visitantes.
- `administracao` consultará os dados de `avaliacoes` para apresentar o resumo administrativo.
- `usuarios` será responsável pela autenticação e pelo controle de permissões de acesso às páginas administrativas.

## Organização do desenvolvimento no GitHub

Cada integrante desenvolverá suas funcionalidades em uma **branch individual**, evitando alterações diretas e simultâneas na branch principal. As mudanças serão registradas por commits e enviadas ao repositório por push; a integração será feita após revisão pela equipe.

| Integrante | Branch individual |
|---|---|
| Fernanda | Kanazawa |
| Letícia | Leticia |
| Julia | Truazelli |
| Isis | Maciel |

## Etapa atual

Organização do repositório, definição das responsabilidades por app e início da implementação colaborativa do sistema.
