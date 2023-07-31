from lib.multiclass_todo import *

"""
Given a todo task
We can see the task and complete properties set correctly
"""
def test_task_properties_set_correctly():
    todo1 = Todo('Do the laundry')
    assert todo1.task == 'Do the laundry'
    assert todo1.complete == False