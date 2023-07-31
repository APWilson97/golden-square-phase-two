from lib.multiclass_todo import Todo

class TodoList:
    def __init__(self):
        self.todo_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todo_list.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_list = []
        for task in self.todo_list:
            if task.complete == False:
                incomplete_list.append(task)
        return incomplete_list

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_list = [task for task in self.todo_list if task.complete == True]
        return complete_list

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for task in self.todo_list:
            task.complete = True