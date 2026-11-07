tasks = [
    ("study python", True),
    ("buy milk", False),
    ("push code", True),
]

# 値によって分岐：ifが前
def list_comp(tasks):
  li = [f"DONE: {task[0].upper()}" if task[1] == True
        else f"TODO: {task[0]}"
        for task in tasks 
        ]
  return li

# 条件によってフィルタ：ifが後
def filt_list(tasks):
  li = [f"DONE: {task[0].upper()}" for task in tasks if task[1] == True]
  return li

'''
先：何を作るか
後：どこで出すか、どんな条件を適用するか
'''

print(list_comp(tasks))
print(filt_list(tasks))