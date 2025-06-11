# Summary:
# Yeh program library books ka record add, display, search, issue, return karta hai. Saara data file mein save hota hai.

import json
def load():
    try: return json.load(open('books.json'))
    except: return []
def save(lst):
    json.dump(lst, open('books.json','w'))
def add():
    b = {'title':input('Title: '),'author':input('Author: '),'isbn':input('ISBN: '),'status':'available'}
    d = load(); d.append(b); save(d); print('Book added!\n')
def show():
    d=load()
    if d: [print(f"{i+1}. {b['title']} | Author: {b['author']} | ISBN: {b['isbn']} | Status: {b['status']}") for i,b in enumerate(d)]
    else: print('No books.\n')
def issue():
    d=load(); i=input('ISBN: ')
    for b in d:
        if b['isbn']==i and b['status']=='available': b['status']='issued'; save(d); print('Book issued!\n'); return
    print('Not found or already issued.\n')
def ret():
    d=load(); i=input('ISBN: ')
    for b in d:
        if b['isbn']==i and b['status']=='issued': b['status']='available'; save(d); print('Book returned!\n'); return
    print('Not found or not issued.\n')
def search():
    q=input('Title/ISBN: '); d=load(); f=0
    for b in d:
        if b['title']==q or b['isbn']==q: print(f"Found: {b}"); f=1
    if not f: print('Not found.\n')
while True:
    print('===== Library Book Tracker =====\n1. Add Book\n2. Display Books\n3. Issue Book\n4. Return Book\n5. Search Book\n6. Exit')
    c = input('Enter your choice: ')
    if c=='1': add()
    elif c=='2': show()
    elif c=='3': issue()
    elif c=='4': ret()
    elif c=='5': search()
    elif c=='6': print('Exiting...'); break
    else: print('Invalid!\n')
