# Summary:
# Yeh program contacts add, view, search, update, delete karta hai. Data file mein save hota hai.
import json
def load():
    try: return json.load(open('contacts.json'))
    except: return []
def save(lst):
    json.dump(lst, open('contacts.json','w'))
def add():
    c = {'name':input('Name: '),'phone':input('Phone: '),'email':input('Email: ')}
    d = load(); d.append(c); save(d); print('Contact added!\n')
def view():
    d = load()
    if not d: print('No contacts.\n')
    else:
        for i, c in enumerate(d, 1): print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")
def search():
    q = input('Name/Phone: '); d = load(); f = 0
    for c in d:
        if c['name']==q or c['phone']==q: print(f"Found: {c}"); f = 1
    if not f: print('Not found.\n')
def update():
    q = input('Phone: '); d = load()
    for c in d:
        if c['phone']==q:
            c['name']=input('New Name: '); c['email']=input('New Email: ')
            save(d); print('Updated!\n'); return
    print('Not found.\n')
def delete():
    q = input('Phone: '); d = load()
    try: n = [i for i,c in enumerate(d) if c['phone']==q][0]
    except: print('Not found.\n'); return
    del d[n]; save(d); print('Deleted!\n')
while True:
    print('===== Contact Book =====\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit')
    c = input('Enter your choice: ')
    if c=='1': add()
    elif c=='2': view()
    elif c=='3': search()
    elif c=='4': update()
    elif c=='5': delete()
    elif c=='6': print('Exiting...'); break
    else: print('Invalid!\n')
