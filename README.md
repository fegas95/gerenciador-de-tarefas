# 📝 Gerenciador de Tarefas (CLI)

Aplicação de linha de comando para gerenciar tarefas do dia a dia, com persistência de dados em banco SQLite.

## 🚀 Funcionalidades

- Adicionar novas tarefas
- Listar todas as tarefas com status e data de criação
- Marcar tarefas como concluídas
- Deletar tarefas

## 🛠️ Tecnologias

- Python 3.10+
- SQLite3 (banco de dados embutido)

## ▶️ Como executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/gerenciador-de-tarefas.git
cd gerenciador-de-tarefas

# Execute o programa
python main.py
```

## 💻 Exemplo de uso

```
╔══════════════════════════╗
║    GERENCIADOR DE TAREFAS  ║
╠══════════════════════════╣
║  1. Listar tarefas         ║
║  2. Adicionar tarefa       ║
║  3. Concluir tarefa        ║
║  4. Deletar tarefa         ║
║  0. Sair                   ║
╚══════════════════════════╝

  ID   STATUS     CRIADA EM            TAREFA
  ────────────────────────────────────────────────────────────
  1    ✅ Feita   2024-06-01 09:00     Estudar Python
  2    ⏳ Pendente 2024-06-01 10:30    Fazer projeto da faculdade
```

## 📁 Estrutura do projeto

```
task-manager/
├── main.py        # Interface de usuário (CLI)
├── database.py    # Funções de acesso ao banco de dados
└── README.md
```
