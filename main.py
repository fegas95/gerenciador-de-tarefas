from database import create_table, add_task, list_tasks, complete_task, delete_task


def show_menu():
    print("\n╔══════════════════════════╗")
    print("║    GERENCIADOR DE TAREFAS  ║")
    print("╠══════════════════════════╣")
    print("║  1. Listar tarefas         ║")
    print("║  2. Adicionar tarefa       ║")
    print("║  3. Concluir tarefa        ║")
    print("║  4. Deletar tarefa         ║")
    print("║  0. Sair                   ║")
    print("╚══════════════════════════╝")


def print_tasks(tasks):
    if not tasks:
        print("\n  Nenhuma tarefa encontrada.")
        return

    print(f"\n  {'ID':<4} {'STATUS':<10} {'CRIADA EM':<20} {'TAREFA'}")
    print("  " + "-" * 60)
    for task_id, title, done, created_at in tasks:
        status = "✅ Feita" if done else "⏳ Pendente"
        print(f"  {task_id:<4} {status:<10} {created_at:<20} {title}")


def main():
    create_table()
    print("\nBem-vindo ao Gerenciador de Tarefas!")

    while True:
        show_menu()
        choice = input("\nEscolha uma opção: ").strip()

        if choice == "1":
            tasks = list_tasks()
            print_tasks(tasks)

        elif choice == "2":
            title = input("Nome da tarefa: ").strip()
            if title:
                add_task(title)
                print(f"  ✅ Tarefa '{title}' adicionada!")
            else:
                print("  ⚠️  O nome não pode ser vazio.")

        elif choice == "3":
            task_id = input("ID da tarefa para concluir: ").strip()
            if task_id.isdigit():
                if complete_task(int(task_id)):
                    print(f"  ✅ Tarefa {task_id} concluída!")
                else:
                    print("  ⚠️  Tarefa não encontrada ou já concluída.")
            else:
                print("  ⚠️  Digite um ID válido.")

        elif choice == "4":
            task_id = input("ID da tarefa para deletar: ").strip()
            if task_id.isdigit():
                if delete_task(int(task_id)):
                    print(f"  🗑️  Tarefa {task_id} deletada.")
                else:
                    print("  ⚠️  Tarefa não encontrada.")
            else:
                print("  ⚠️  Digite um ID válido.")

        elif choice == "0":
            print("\nAté logo! 👋\n")
            break

        else:
            print("  ⚠️  Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
