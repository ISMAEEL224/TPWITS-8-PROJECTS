# Summary:
# Yeh program products add, view, search, update, delete karta hai. Data file mein save hota hai.
import json
def load():
    try: return json.load(open('inventory.json'))
    except: return []
def save(lst):
    json.dump(lst, open('inventory.json','w'))
def add():
    p = {'name':input('Name: '),'id':input('ID: '),'qty':input('Qty: ')}
    if not p['qty'].isdigit(): print('Invalid qty!\n'); return
    p['qty']=int(p['qty']); d=load(); d.append(p); save(d); print('Product added!\n')
def view():
    d=load()
    if not d: print('No products.\n')
    else:
        for i,p in enumerate(d,1): print(f"{i}. {p['name']} | {p['id']} | {p['qty']}")
def update():
    q = input('ID: '); d = load()
    for p in d:
        if p['id']==q:
            newq = input('New Qty: ')
            if not newq.isdigit(): print('Invalid!\n'); return
            p['qty']=int(newq); save(d); print('Updated!\n'); return
    print('Not found.\n')
def delete():
    q = input('ID: '); d = load()
    try: n = [i for i,p in enumerate(d) if p['id']==q][0]
    except: print('Not found.\n'); return
    del d[n]; save(d); print('Deleted!\n')
def search():
    q = input('Name/ID: '); d = load(); f = 0
    for p in d:
        if p['name']==q or p['id']==q: print(f"Found: {p}"); f = 1
    if not f: print('Not found.\n')
while True:
    print('===== Inventory Management =====\n1. Add Product\n2. View Inventory\n3. Update Quantity\n4. Delete Product\n5. Search Product\n6. Exit')
    c = input('Enter your choice: ')
    if c=='1': add()
    elif c=='2': view()
    elif c=='3': update()
    elif c=='4': delete()
    elif c=='5': search()
    elif c=='6': print('Exiting...'); break
    else: print('Invalid!\n')
