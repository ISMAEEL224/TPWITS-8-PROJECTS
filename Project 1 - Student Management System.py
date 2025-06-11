# Summary:
# Yeh program students ka record add, display, search, update, delete karta hai. Saara data file mein save hota hai.

import json
def load():
    try: return json.load(open('students.json'))
    except: return []
def save(lst):
    json.dump(lst, open('students.json','w'))
def add():
    s = {'name':input('Name: '),'roll':input('Roll: '),'class':input('Class: '),'marks':input('Marks: ')}
    if not s['marks'].isdigit(): print('Invalid marks!\n'); return
    s['marks']=int(s['marks']); d=load(); d.append(s); save(d); print('Student added!\n')
def show():
    d=load()
    if not d: print('No records.\n')
    else:
        for i,s in enumerate(d,1): print(f"{i}. {s['name']} | {s['roll']} | {s['class']} | {s['marks']}")
def search():
    r=input('Roll: '); d=load(); f=0
    for s in d:
        if s['roll']==r: print(f"Found: {s}"); f=1
    if not f: print('Not found.\n')
def update():
    r=input('Roll: '); d=load()
    for s in d:
        if s['roll']==r:
            s['name']=input('New Name: '); s['class']=input('New Class: ')
            m=input('New Marks: ')
            if not m.isdigit(): print('Invalid!\n'); return
            s['marks']=int(m); save(d); print('Updated!\n'); return
    print('Not found.\n')
def delete():
    r=input('Roll: '); d=load()
    try: n=[i for i,s in enumerate(d) if s['roll']==r][0]
    except: print('Not found.\n'); return
    del d[n]; save(d); print('Deleted!\n')
while True:
    print('===== Student Management System =====\n1. Add Student\n2. Display All Students\n3. Search Student by Roll Number\n4. Update Student\n5. Delete Student\n6. Exit')
    c = input('Enter your choice: ')
    if c=='1': add()
    elif c=='2': show()
    elif c=='3': search()
    elif c=='4': update()
    elif c=='5': delete()
    elif c=='6': print('Exiting...'); break
    else: print('Invalid!\n')
