class TodoList:
    def __init__(self):
        self.list = []
        self.complete_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.list.append(todo)
        
    
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return self.list

    def complete(self):


        for todo in self.list:
            if todo.complete == True:
                self.complete_list.append(todo.task)
            
        return self.complete_list
            

        # Returns:
        #   A list of Todo instances representing the todos that are complete
    

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self.list:
            todo.complete = True

