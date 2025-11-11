class Task:

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True


    
class TaskList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task: Task):
        self.tasks.append(task)
    
    def remove_task(self, task: Task):
        self.tasks.remove(task)
    
    def get_all_tasks(self):
        return self.tasks
    
    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]
    
    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]
    
if __name__ == '__main__':
    task1 = Task('Comprar leite', 'Ir ao supermercado e comprar leite')
    task2 = Task('Estudar Python', 'Ler capítulos do livro de Python')
    task3 = Task('Fazer exercícios', 'Resolver os exercícios do curso de Python')
    
    task_list = TaskList()
    task_list.add_task(task1)
    task_list.add_task(task2)
    task_list.add_task(task3)
    
    task1.mark_completed()
    
    print('Todas as tarefas:')
    for task in task_list.get_all_tasks():
        status = 'Concluída' if task.completed else 'Pendente'
        print(f'- {task.title}: {status}')
    
    print('\nTarefas concluídas:')
    for task in task_list.get_completed_tasks():
        print(f'- {task.title}')
    
    print('\nTarefas pendentes:')
    for task in task_list.get_pending_tasks():
        print(f'- {task.title}')