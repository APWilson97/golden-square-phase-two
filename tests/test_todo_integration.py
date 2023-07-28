from lib.todo import *
from lib.todo_list import *

def test_add_three_tasks_then_show_incomplete():
    task_list = TodoList()
    todo1 = Todo('Do the laundry')
    todo2 = Todo('Wash the dishes')
    todo3 = Todo('Shop for food')
    task_list.add(todo1)
    task_list.add(todo2)
    task_list.add(todo3)
    assert task_list.incomplete() == [todo1, todo2, todo3]

def test_add_three_tasks_complete_two():
    task_list = TodoList()
    todo1 = Todo('Do the laundry')
    todo2 = Todo('Wash the dishes')
    todo3 = Todo('Shop for food')
    task_list.add(todo1)
    task_list.add(todo2)
    task_list.add(todo3)
    todo1.mark_complete()
    todo3.mark_complete()
    assert task_list.complete() == [todo1, todo3]
    assert task_list.incomplete() == [todo2]

"""Given 3 tasks added to the list
mark all tasks as complete and return all of them in a list"""

def test_add_three_tasks_give_up_all_show_them():
    task_list = TodoList()
    todo1 = Todo('Do the laundry')
    todo2 = Todo('Wash the dishes')
    todo3 = Todo('Shop for food')
    task_list.add(todo1)
    task_list.add(todo2)
    task_list.add(todo3)
    task_list.give_up()
    assert task_list.complete() == [todo1, todo2, todo3]
