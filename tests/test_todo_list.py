from lib.todo_list import TodoList

"""Test where todo list is initially an empty list
"""

def test_initialize_todo_list_empty():
    task_list = TodoList()
    assert task_list.todo_list == []

def test_add_two_tasks():
    task_list = TodoList()
    task_list.add('Do the laundry')
    assert task_list.todo_list == ['Do the laundry']