class StudyManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, duration):
        if not name:
            return "Erro: Nome da tarefa não pode ser vazio."
        if duration <= 0:
            return "Erro: Duração deve ser positiva."
        self.tasks.append({"name": name, "duration": duration})
        return f"Tarefa '{name}' adicionada!"

    def list_tasks(self):
        if not self.tasks:
            return "Nenhuma tarefa agendada."
        return "\n".join([f"- {t['name']}: {t['duration']}min" for t in self.tasks])

def main():
    manager = StudyManager()
    print("--- Organizador de Estudos ---")
    while True:
        print("\n1. Adicionar Tarefa\n2. Listar\n3. Sair")
        choice = input("Escolha: ")
        if choice == "1":
            name = input("Matéria: ")
            try:
                time = int(input("Minutos: "))
                print(manager.add_task(name, time))
            except ValueError:
                print("Erro: Digite um número válido.")
        elif choice == "2":
            print(manager.list_tasks())
        elif choice == "3":
            break

if __name__ == "__main__":
    main()
