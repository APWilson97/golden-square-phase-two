from lib.multiclass_todo_list import *

"""
Given a todo list
When we add 2 tasks
We can see all tasks and they are initially incomplete
"""
def test_see_all_initial_incomplete_tasks():
    task_list = TodoList()
    todo1 = Todo('Do the laundry')
    todo2 = Todo('Cook dinner for tonight')
    task_list.add(todo1)
    task_list.add(todo2)
    assert task_list.incomplete() == [todo1, todo2]

"""
Given a todo list
When we add 3 tasks and mark 2 as complete
We can see all the tasks that are complete and are not complete
"""
def test_mark_two_complete_tasks():
    task_list = TodoList()
    todo1 = Todo('Do the laundry')
    todo2 = Todo('Cook dinner for tonight')
    todo3 = Todo('Go walk the dog')
    task_list.add(todo1)
    task_list.add(todo2)
    task_list.add(todo3)
    todo1.mark_complete()
    todo3.mark_complete()
    assert task_list.complete() == [todo1, todo3]
    assert task_list.incomplete() == [todo2]

"""
Given a todo list
When we add 3 tasks and give up
We should see all tasks marked as complete
"""
def test_give_up_three_tasks():
    task_list = TodoList()
    todo1 = Todo('Do the laundry')
    todo2 = Todo('Cook dinner for tonight')
    todo3 = Todo('Go walk the dog')
    task_list.add(todo1)
    task_list.add(todo2)
    task_list.add(todo3)
    task_list.give_up()
    assert task_list.complete() == [todo1, todo2, todo3]
    assert task_list.incomplete() == []