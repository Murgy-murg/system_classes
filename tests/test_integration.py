from lib.todo_class_system import Todo
from lib.todo_list_class_system import TodoList

'''given todo tasks, they are added to a todo list '''
def test_tasks_are_added_to_list():
    todo_list = TodoList()
    task_1 = Todo('Fix the washing machine')
    task_2 = Todo('Clean the kitchen')
    todo_list.add(task_1)
    todo_list.add(task_2)
    # print(todo_list.list[0].task)
    # assert todo_list.incomplete() == ['Fix the washing machine','Clean the kitchen']
    assert todo_list.incomplete() == [task_1,task_2]

"""returns list of items where complete value is true"""

def test_returns_list_of_complete_true():
    todo_list = TodoList()
    task_1 = Todo('Fix the washing machine')
    task_2 = Todo('Clean the kitchen')
    todo_list.add(task_1)
    todo_list.add(task_2)
    task_1.mark_complete()
    assert todo_list.complete() == [task_1.task]


"""complete value for items is true"""

def test_complete_is_true():
    todo_list = TodoList()
    task_1 = Todo('Fix the washing machine')
    task_2 = Todo('Clean the kitchen')
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.give_up()
    result_1 = task_1.complete
    assert result_1 == True
    result_2 = task_2.complete
    assert result_2 == True