# agent.md — System Prompt para Agentes de IA

> Repositório: **aulas etec**  
> Propósito: Plataforma de conteúdo educacional estático para disciplinas do curso técnico da ETEC.  
> Baseado estritamente na estrutura e padrões de código encontrados neste repositório. **Não invente tecnologias, frameworks ou padrões ausentes.**

---

## 1. Objetivo do Projeto

Portal de navegação e distribuição de aulas para 6 disciplinas do ensino técnico. Cada disciplina possui um menu (`index.html`) que indexa páginas de aula (`aula-XX.html`) com conteúdo teórico, exemplos de código interativos, exercícios e laboratórios práticos. O site é 100% estático, hospedado no GitHub Pages.

Disciplinas ativas:
- **Algoritmos** — Lógica, Portugol, Python, Java (30 aulas)
- **Banco de Dados I** — Modelagem relacional, SQL/PostgreSQL (33 aulas)
- **Banco de Dados II** — Placeholder (1 arquivo)
- **Desenvolvimento de Sistemas** — Programação Python (10 aulas)
- **Interface Web I** — HTML e CSS (10 aulas + projeto CRUD)
- **Interface Web II** — JavaScript full-stack, DOM, APIs, MVC (30 aulas)

---

## 2. Stack Tecnológico

| Camada | Tecnologia | Detalhe |
|--------|-----------|---------|
| **Linguagens** | HTML5, CSS3, JavaScript (ES6+) | Todo o conteúdo é browser-side |
| **Linguagens de ensino** | Python 3, Java, SQL (PostgreSQL), Arduino C/C++ | Embutidas nas aulas como exemplos |
| **CSS Framework** | Tailwind CSS v3 (via CDN) | Usado nas páginas de aula (`<script src="https://cdn.tailwindcss.com">`) |
| **Ícones** | Font Awesome 6 (via CDN) | Usado em Banco de Dados I e Interface Web I/Aula 15 |
| **Fontes** | Google Fonts: Inter, Fira Code, Oswald | CDN |
| **Banco de Dados** | Neon.tech (PostgreSQL cloud) | Única integração real: `Interface Web I/Aula 15/script_db.js` |
| **Hospedagem** | GitHub Pages | Deploy automático via GitHub Actions |
| **Editor** | VS Code + Live Server (portas 5500/5501) | Configurado em `.vscode/settings.json` |
| **Formatter** | Prettier (esbenp.prettier-vscode) | Configurado apenas em `Algoritmos/.vscode/` |
| **Controle de versão** | Git | `.gitignore` ignora apenas `Interface Web I/Docker Desktop Installer.exe` |

**O que NÃO existe neste projeto:**
- `package.json`, `node_modules`, npm, yarn
- `requirements.txt`, pip, virtualenv
- Docker, docker-compose
- `.env` ou variáveis de ambiente
- Webpack, Vite, ou qualquer bundler
- React, Vue, Angular, ou qualquer framework SPA
- TypeScript
- Testes automatizados
- Linters configurados (apenas Prettier em Algoritmos)

---

## 3. Arquitetura e Estrutura de Diretórios

```
raiz/
├── index.html                  ← Hub central: 6 cards linkando para cada disciplina
├── arduino.ino                 ← Código Arduino (Bluetooth + controle de motores)
├── agent.md                    ← Este arquivo
├── .gitignore
├── .gitmodules                 ← Vazio (sem submódulos)
├── .vscode/
│   └── settings.json           ← Live Server porta 5500, root "/"
├── workflows/
│   └── static.yml              ← GitHub Actions: deploy automático no push para main
│
├── Algoritmos/
│   ├── index.html              ← Menu: grid de 30 cards gerados via JS
│   ├── aula-01.html ... aula-30.html
│   ├── aula-05.html, aula-06.html  ← Podem usar numeração não sequencial
│   ├── gabarito-aulas-01-04.html
│   ├── README.md
│   ├── Exercicios/
│   │   └── aula_11.py          ← Exercício Python standalone
│   └── .vscode/
│       └── settings.json       ← Prettier + formatOnSave
│
├── Banco de dados I/
│   ├── index.html              ← Menu: 33 cards com etapa (Fundamentação/DDL/DML/DQL)
│   ├── aula-01.html ... aula-33.html
│   ├── aula-13-1.html          ← Aula complementar
│   ├── aula-27.1.html          ← Aula complementar
│   ├── aula-27-exemplo-agregados.sql  ← Script SQL standalone
│   ├── prova_01.html
│   └── Aulas.txt               ← Ementa completa do curso (39 aulas planejadas)
│
├── Banco de dados II/
│   └── index.html              ← Placeholder: 4 módulos "Em organização"
│
├── Desenvolvimento de Sistemas/
│   ├── index.html              ← Menu: 8 cards
│   ├── aula-01.html ... aula-10.html  ← Nem todas as aulas existem (ex: 05, 08 ausentes)
│   └── gabarito-aulas-01-07.html
│
├── Interface Web I/
│   ├── index.html              ← Menu: 10 cards
│   ├── aula-01.html ... aula-14.html
│   ├── atividade.html
│   ├── gabarito-aulas-01-06.html
│   └── Aula 15/                ← Projeto CRUD completo
│       ├── index.html
│       ├── style.css
│       ├── script.js           ← ES6 module, importa de script_db.js
│       ├── script_db.js        ← Conexão real Neon.tech PostgreSQL
│       ├── enunciado-tema-B.html
│       ├── modelo_prova.pdf
│       └── aula15.zip
│
├── Interface Web II/
│   ├── index.html              ← Menu: 30 cards
│   ├── aula-01.html ... aula-33.html
│   ├── aulas_extras.txt
│   └── Exercicios/
│       ├── script.js
│       ├── aula-07.html
│       └── aula12/
│           ├── index.html
│           ├── script.js
│           ├── script_paulo.js
│           └── style.css
│
└── Modelo/
    ├── aula1.html              ← Template base: tema claro, funções JS
    └── aula10.html             ← Template base: manipulação de DOM
```

**Regra de navegação**: Toda página de aula tem um link `← Voltar ao menu` que aponta para `index.html` da disciplina ou `../index.html` (raiz). O atributo `href` em arquivos de exercício em subpastas usa caminhos relativos.

---

## 4. Padrões de Código (Guidelines)

### 4.1 Estrutura de arquivos HTML

Todo arquivo `.html` neste repositório segue este esqueleto:

```html
<!DOCTYPE html>
<html lang="pt-BR">  <!-- ou lang="pt-pt" -->
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>...</title>
    <!-- CSS vai aqui: <style> ou <link> ou <script src="tailwind CDN"> -->
</head>
<body>
    <!-- Conteúdo -->
    <!-- JavaScript vai aqui: <script> no final do body -->
</body>
</html>
```

### 4.2 Dois estilos visuais coexistem — RESPEITE o contexto

**Estilo A — Index/Menu de disciplina (dark theme):**
- CSS custom properties no `:root` com `--tone` como cor de destaque
- Background escuro com grid pattern via `body::before`
- Fonte: `Consolas, "Courier New", monospace`
- Cards gerados dinamicamente via JavaScript a partir de array `aulas[]`
- Estrutura: `criarCard(aula)` → `document.createElement('a')` → `.aula-card`
- Cores de `--tone` por disciplina:
  - Algoritmos: `#ff8a5b` (laranja)
  - Banco de Dados I: `#22c55e` (verde)
  - Desenvolvimento de Sistemas: `#8ce99a` (verde claro)
  - Interface Web I: `#ffd166` (amarelo)
  - Interface Web II: `#c792ea` (roxo)

**Estilo B — Página de aula (light theme):**
- Tailwind CSS via CDN (`<script src="https://cdn.tailwindcss.com">`) como framework-base
- Background claro (`bg-slate-50`), texto escuro (`text-slate-900`)
- Header com gradiente escuro (`gradient-bg`)
- Fontes: Inter para corpo, Fira Code para código (via Google Fonts CDN)
- Alternativamente (Modelo/ e algumas aulas): CSS 100% inline sem Tailwind, tema claro com `--primary: #4f46e5`

### 4.3 Componente "Code Window" (bloco de código)

Padrão universal em todas as aulas para exibir código:

```html
<div class="code-window no-select" id="code-block">
    <div class="terminal-header">
        <div class="dot bg-[#ff5f56]"></div>
        <div class="dot bg-[#ffbd2e]"></div>
        <div class="dot bg-[#27c93f]"></div>
        <span class="text-slate-400 text-xs ml-4 font-mono">NOME_DO_ARQUIVO.EXT</span>
    </div>
    <div class="p-8">
        <pre><code>...</code></pre>
    </div>
</div>
```

Acompanhado de:
- CSS: `user-select: none`, `-webkit-user-select: none`, `cursor: not-allowed`
- JS: bloqueio de `copy`, `dragstart`, `contextmenu`, `keydown` (Ctrl+C/V/A)
- Overlay visual: texto "CÓDIGO BLOQUEADO - DIGITE PARA APRENDER"

### 4.4 Destaque de sintaxe (syntax highlighting)

Custom CSS classes para colorir código, **sem bibliotecas** (Prism.js, highlight.js NÃO são usados):

| Linguagem | Classes CSS |
|-----------|------------|
| Portugol | `.pt-keyword`, `.pt-variable`, `.pt-function`, `.pt-operator`, `.pt-number`, `.pt-string`, `.pt-comment` |
| Python | `.py-keyword`, `.py-string`, `.py-comment`, `.py-function`, `.py-number`, `.python-keyword`, `.python-string`, `.python-comment`, `.python-function`, `.python-number` |
| SQL | `.sql-keyword`, `.sql-type`, `.sql-comment`, `.sql-string`, `.sql-number` |
| JavaScript | `.js-keyword`, `.js-string`, `.js-comment`, `.js-function`, `.js-number` |
| HTML/CSS | `.tag`, `.attr`, `.string`, `.comment`, `.keyword`, `.function`, `.css-selector`, `.style-tag` |
| Genérico | `.keyword { color: #c586c0; }`, `.string { color: #ce9178; }`, `.comment { color: #6a9955; font-style: italic; }`, `.function { color: #dcdcaa; }` |

### 4.5 Nomenclatura

- Arquivos de aula: `aula-XX.html` (XX com zero à esquerda, ex: `aula-01.html`)
- Arquivos complementares: `aula-XX.Y.html` (ex: `aula-27.1.html`, `aula-13-1.html`)
- Subpastas de exercícios: `Exercicios/` ou `Aula XX/`
- CSS classes: kebab-case (`aula-card`, `btn-back`, `code-window`, `terminal-header`)
- IDs JavaScript: camelCase (`gridContainer`, `codeBlock`, `customMessage`)
- Funções JavaScript: camelCase (`criarCard`, `validarSQL`, `ativarLoja`)
- Variáveis CSS: kebab-case com prefixo `--` (`--tone`, `--bg`, `--muted`)
- Constantes globais: UPPER_SNAKE_CASE (`DATABASE_URL`, `NEON_API_TOKEN`)

### 4.6 JavaScript

- **Vanilla JS apenas.** Sem jQuery, sem frameworks.
- Código no final do `<body>`, dentro de tag `<script>` (sem `defer`/`async` no atributo)
- ES6 modules (`import`/`export`) usados apenas em `Interface Web I/Aula 15/` (arquivo `script.js` importa de `script_db.js`)
- `const` e `let`; evitar `var`
- Template literals para gerar HTML dinâmico
- Arrow functions são aceitas mas `function` declarations também são comuns
- `fetch()` para chamadas HTTP (Neon.tech)
- Tratamento de erros com `try/catch` e retorno de `null` ou `[]` em caso de falha

### 4.7 Tratamento de erros

- Em JavaScript: try/catch com console.error + fallback (retornar `null`, `[]`, ou `false`)
- Em Python (aulas/exercícios): validação de entrada com `if` + `print()` de erro + re-pedir input
- Em SQL: scripts com comentários explicativos sobre o que pode dar errado
- Erros NUNCA são exibidos ao usuário final em produção; console.error é usado para debug

### 4.8 Regras de ouro

- **Nunca adicione comentários** em código de produção a menos que o usuário peça explicitamente
- **Não use bibliotecas de terceiros** que não estejam já referenciadas nos arquivos existentes
- **Mantenha arquivos autocontidos** — cada HTML deve poder ser aberto diretamente no navegador (dependências apenas de CDN)
- **Respeite o estilo visual existente** — se a disciplina usa Tailwind, use Tailwind; se usa CSS custom properties, mantenha o padrão
- **Copy protection por padrão** — novos blocos de código em páginas de aula devem incluir `user-select: none` e bloqueio de eventos de cópia
- **Idioma**: Todo conteúdo visível é em português (pt-BR). Comentários em código também podem ser em português.

---

## 5. Regras de Deploy / Ambiente

### 5.1 Comandos essenciais

Não há comandos de build, instalação ou runtime. O projeto é servido estaticamente.

**Desenvolvimento local:**
```
# Abrir a raiz com VS Code + Live Server (porta 5500)
# Para Algoritmos, porta 5501 (configurado em Algoritmos/.vscode/settings.json)
```

**Deploy:**
- Push para branch `main` dispara GitHub Actions (`workflows/static.yml`)
- O workflow faz upload de todo o repositório como artefato e publica no GitHub Pages
- Nenhum passo manual de build é necessário

### 5.2 Variáveis de ambiente e credenciais

**Neon.tech PostgreSQL** (produção, hardcoded em `Interface Web I/Aula 15/script_db.js`):
```javascript
const DATABASE_URL = "postgresql://neondb_owner:...@ep-nameless-thunder-...neon.tech/ETEC_A_2026?sslmode=require";
const NEON_API_TOKEN = "https://ep-nameless-thunder-...apirest...neon.tech/ETEC_A_2026/rest/v1";
```
Essas credenciais estão expostas no código-fonte. Para novas aulas que precisem de banco, siga o mesmo padrão de `script_db.js`:
- `DATABASE_URL` para conexão PostgreSQL nativa
- Endpoint HTTP do Neon para queries via `fetch()`
- Queries parametrizadas com `$1, $2, ...` para evitar SQL injection

### 5.3 Portas do Live Server

| Disciplina | Porta |
|-----------|-------|
| Raiz e demais disciplinas | 5500 |
| Algoritmos | 5501 |

### 5.4 Como criar uma nova aula

1. Copie o template apropriado de `Modelo/` (aula1.html para aulas com interação JS, aula10.html para manipulação de DOM)
2. Renomeie para `aula-XX.html` dentro da disciplina correta
3. Adapte o conteúdo mantendo o estilo visual da disciplina (verificar se usa Tailwind CDN ou CSS inline)
4. Adicione a entrada correspondente no array `aulas[]` do `index.html` da disciplina
5. Inclua o link `← Voltar ao menu` apontando para o `index.html` correto

### 5.5 Estrutura do array `aulas[]` nos index.html

```javascript
const aulas = [
    {
        arquivo: 'aula-01.html',
        titulo: 'Aula 01',
        tema: 'Nome do Tema',      // exibido no chip
        icone: 'ABC',               // exibido grande no card
        resumo: 'Descrição curta.', // texto do card
        etapa: 'Fundamentação'      // (opcional) usado como data-label
    },
    // ...
];
```

A função `criarCard(aula)` gera um elemento `<a class="aula-card">` com `data-label` e o insere no `#gridContainer`.
