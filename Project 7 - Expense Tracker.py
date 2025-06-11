# Summary:
# Yeh program expenses add, view, total, date search, category summary karta hai. Data file mein save hota hai.
import json
def load():
    try: return json.load(open('expenses.json'))
    except: return []
def save(lst):
    json.dump(lst, open('expenses.json','w'))
def add():
    e = {'date':input('Date: '),'cat':input('Category: '),'amt':input('Amount: ')}
    if not e['amt'].isdigit(): print('Invalid amount!\n'); return
    e['amt']=int(e['amt']); d=load(); d.append(e); save(d); print('Expense added!\n')
def view():
    d=load()
    if not d: print('No expenses.\n')
    else:
        for i,e in enumerate(d,1): print(f"{i}. {e['date']} | {e['cat']} | {e['amt']}")
def total():
    d=load()
    print('Total:', sum(e['amt'] for e in d), '\n')
def search():
    q=input('Date: '); d=load(); f=0
    for e in d:
        if e['date']==q: print(f"{e['date']} | {e['cat']} | {e['amt']}"); f=1
    if not f: print('No expenses for this date.\n')
def summary():
    d=load(); s={}
    for e in d: s[e['cat']]=s.get(e['cat'],0)+e['amt']
    print('Category Summary:', s, '\n')
while True:
    print('===== Expense Tracker =====\n1. Add Expense\n2. View Expenses\n3. Total Expenses\n4. Search by Date\n5. Category Summary\n6. Exit')
    c=input('Enter your choice: ')
    if c=='1': add()
    elif c=='2': view()
    elif c=='3': total()
    elif c=='4': search()
    elif c=='5': summary()
    elif c=='6': print('Exiting...'); break
    else: print('Invalid!\n')
