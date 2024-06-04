class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not any(t.name == task.name for t in self.tasks):
            self.tasks.append(task)

    def remove_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]

    def get_highest_priority_task(self):
        if not self.tasks:
            return None
        try:
            return max(self.tasks, key=lambda task: task.priority)
        except ValueError:
            return None

    def get_task_count(self):
        return len(self.tasks)
    
    def print_tasks(self):
        if not self.tasks:
            print("No tasks")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(f"- {task.name} (Priority: {task.priority})")