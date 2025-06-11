# Summary:
# Yeh program tasks add, view, mark as done, delete karta hai. Data file mein save hota hai.

import json
def load():
    try: return json.load(open('tasks.json'))
    except: return []
def save(lst):
    json.dump(lst, open('tasks.json','w'))
def add():
    t = input('New Task: ')
    d = load(); d.append({'task': t, 'done': False}); save(d); print('Task added!\n')
def view():
    d = load()
    if not d: print('No tasks.\n')
    else:
        for i, t in enumerate(d, 1): print(f"{i}. {t['task']} | Done: {t['done']}")
def mark():
    d = load()
    try: n = int(input('Task# to mark done: '))-1
    except: print('Invalid!\n'); return
    if 0<=n<len(d): d[n]['done'] = True; save(d); print('Marked as done!\n')
    else: print('Invalid!\n')
def delete():
    d = load()
    try: n = int(input('Task# to delete: '))-1
    except: print('Invalid!\n'); return
    if 0<=n<len(d): del d[n]; save(d); print('Deleted!\n')
    else: print('Invalid!\n')
while True:
    print('===== To-Do List App =====\n1. Add Task\n2. View Tasks\n3. Mark as Done\n4. Delete Task\n5. Exit')
    c = input('Enter your choice: ')
    if c=='1': add()
    elif c=='2': view()
    elif c=='3': mark()
    elif c=='4': delete()
    elif c=='5': print('Exiting...'); break
    else: print('Invalid!\n')
