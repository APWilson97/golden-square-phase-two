from lib.todo import Todo

"""Given a task
Sets task property and complete property to false"""

def test_initialize_todo_task_false():
    todo1 = Todo('Do the laundry')
    assert todo1.task == 'Do the laundry'
    assert todo1.complete == False

def test_mark_complete_one_task():
    todo1 = Todo('Do the laundry')
    todo1.mark_complete()
    assert todo1.complete == True