class TodoList:
    def __init__(self):
        self.list = []
        self.complete_list = []

    def add(self, todo):
        # todo = todo.task
        self.list.append(todo)
        
    
    def incomplete(self):
        return self.list

    def complete(self):


        for todo in self.list:
            if todo.complete == True:
                self.complete_list.append(todo.task)
            
        return self.complete_list
            

        # Returns:
        #   A list of Todo instances representing the todos that are complete
    

    def give_up(self):
        
        for todo in self.list:
            todo.complete = True
