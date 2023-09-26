from lib.todo_class_system import Todo
from lib.todo_list_class_system import TodoList

'''given todo tasks, they are added to a todo list '''
def test_tasks_are_added_to_list():
    todo_list = TodoList()
    task_1 = Todo('Fix the washing machine')
    task_2 = Todo('Clean the kitchen')
    todo_list.add(task_1)
    todo_list.add(task_2)
    actual = todo_list.incomplete() 
    expected = [task_1, task_2]
    assert actual == expected
