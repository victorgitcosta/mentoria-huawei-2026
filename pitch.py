class task:
    _id = 0

    def __init__(self, name, dueDate):
        task._id += 1
        self.id = task._id
        self.name = name
        self.dueDate = dueDate
        self.isCompleted = False

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def dueDate(self):
        return self._dueDate
    
    @dueDate.setter
    def dueDate(self, dueDate):
        self._dueDate = dueDate

    @property
    def getid(self):
        return self.id

    def __str__(self):
        return f"A tarefa {self.id} chamada {self.name} tem o prazo de {self.dueDate}!"
    
    def completeTask(self):
        task.isCompleted = True

class taskManager:
    def __init__(self):
        self.nome = "NoNotion"
        self.tasks = []
    
    def addTask(self, task):
        self.tasks.append(task)
        print(f"{task.name}")

    def listarTarefas(self):
        for tarefa in self.tarefas:
            print(tarefa)

task1 = task("Pitch", "12/04/2026")
task2 = task("Pitch+1", "13/04/2026")
print(task1.getid)

print(task1)
print(task2)
taskManager = taskManager()

menu = True

while menu:
    comando = input(f"""==============================
    Gerenciador de Tarefas {taskManager.nome}
    ==============================
    1. Adicionar nova tarefa
    2. Ver todas as tarefas
    3. Concluir uma tarefa
    4. Sair do programa\n""")
    match comando:
        case "1" | 1:
            nome_tarefa = input(f"Coloque o nome da tarefa:" )
            prazo_tarefa = input(f"Coloque o prazo da tarefa: ")
            task = task(nome_tarefa, prazo_tarefa)
            taskManager.addTask()
        case "2" | 2:
            taskManager.listarTarefas
        case "3" | 3:
            index = input(f"Qual é o index da tarefa que concluíste?")
            task.completeTask()
        case "4" | 4:
            print(f"""==================================
Obrigado por usar nossa aplicação!
==================================""")
            menu = False