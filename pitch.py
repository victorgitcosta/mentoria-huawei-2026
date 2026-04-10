import sys
import time

#Função para printar lentamente os títulos, imitando uma interface animada

def print_animado(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

#Classe task com id auto-incremental, nome e prazo

class Task:
    _id = 0

    def __init__(self, name, due_date):
        Task._id += 1
        self.id = Task._id
        self._name = name
        self._due_date = due_date
        self._completed = False

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("O nome não pode ser vazio.")
        self._name = value

    @property
    def due_date(self):
        return self._due_date
    
    @due_date.setter
    def due_date(self, value):
        self._due_date = value

    @property
    def completed(self):
        return self._completed
    
    @completed.setter
    def completed(self, value):
        if not isinstance(value, bool):
            raise ValueError("Completed deve ser True ou False")
        self._completed = value

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "O Concluída" if self.completed else "X Pendente"
        return f"[{self.id}] {self.name} | Prazo: {self.due_date} | {status}"

#Classe gerenciador de tasks para agregar as tasks

class TaskGerenciador:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, due_date):
        task = Task(name, due_date)
        self.tasks.append(task)
        print(f"Tarefa '{name}' adicionada!")

    def list_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa cadastrada.")
            return

        for task in self.tasks:
            print(task)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.complete()
                print(f"Tarefa {task_id} concluída!")
                return
        print("Tarefa não encontrada.")

gerenciador = TaskGerenciador()

menu = True

while menu:
    greetings = r"""
_____ _____ _____ _____ _____ _____ _____
 _____                     _       _
|   __|___ ___ ___ ___ ___|_|___ _| |___ ___
|  |  | -_|  _| -_|   |  _| | .'| . | . |  _|
|_____|___|_| |___|_|_|___|_|__,|___|___|_|
     _        _____             ___
   _| |___   |_   _|___ ___ ___|  _|___ ___
  | . | -_|    | | | .'|  _| -_|  _| .'|_ -|
  |___|___|    |_| |__,|_| |___|_| |__,|___|
     _____        _____     _   _
    |   | |___   |   | |___| |_|_|___ ___
    | | | | . |  | | | | . |  _| | . |   |
    |_|___|___|  |_|___|___|_| |_|___|_|_|
 _____ _____ _____ _____ _____ _____ _____"""
    print_animado(greetings, 0.003)
    comando = input("""
1. Adicionar nova tarefa
2. Ver todas as tarefas
3. Concluir uma tarefa
4. Sair do programa
Escolha: """)

    match comando:
        case "1" | 1:
            nome = input("Nome da tarefa: ")
            prazo = input("Prazo: ")
            gerenciador.add_task(nome, prazo)

        case "2" | 2:
            gerenciador.list_tasks()

        case "3" | 3:
            try:
                task_id = int(input("ID da tarefa a concluir: "))
                gerenciador.complete_task(task_id)
                gerenciador.list_tasks()
                parabenizacao = """
_____ _____ _____ _____ _____ _____ _____
                                      __ 
 _____             _                 |  |
|  _  |___ ___ ___| |_ ___ ___ ___   |  |
|   __| .'|  _| .'| . | -_|   |_ -|  |__|
|__|  |__,|_| |__,|___|___|_|_|___|  |__|
_____ _____ _____ _____ _____ _____ _____"""
                print_animado(parabenizacao, 0.008)
            except ValueError:
                print("Por favor, insira um número válido.")
        case "4" | 4:
            agradecimento = r"""
_____ _____ _____ _____ _____ _____ _____
                                    __
 _____ _       _           _       |  |
|     | |_ ___|_|___ ___ _| |___   |  |
|  |  | . |  _| | . | .'| . | . |  |__|
|_____|___|_| |_|_  |__,|___|___|  |__|
                |___|
_____ _____ _____ _____ _____ _____ _____"""
            print_animado(agradecimento, 0.008)
            menu = False
        case _:
            print("Opção inválida.")