# Summary:
# Yeh program bank accounts create, deposit, withdraw, balance check, transaction history karta hai. Data file mein save hota hai.

import json
def load():
    try: return json.load(open('accounts.json'))
    except: return []
def save(lst):
    json.dump(lst, open('accounts.json','w'))
def create():
    a={'name':input('Name: '),'acc':input('Acc#: '),'bal':0,'history':[]}
    d=load(); d.append(a); save(d); print('Account created!\n')
def deposit():
    n=input('Acc#: '); d=load()
    try: amt=int(input('Amount: '))
    except: print('Invalid!\n'); return
    for a in d:
        if a['acc']==n: a['bal']+=amt; a['history'].append(f'Deposit:{amt}'); save(d); print('Deposited!\n'); return
    print('Account not found.\n')
def withdraw():
    n=input('Acc#: '); d=load()
    try: amt=int(input('Amount: '))
    except: print('Invalid!\n'); return
    for a in d:
        if a['acc']==n:
            if a['bal']>=amt: a['bal']-=amt; a['history'].append(f'Withdraw:{amt}'); save(d); print('Withdrawn!\n')
            else: print('Insufficient balance.\n')
            return
    print('Account not found.\n')
def balance():
    n=input('Acc#: '); d=load()
    for a in d:
        if a['acc']==n: print(f"Balance: {a['bal']}\n"); return
    print('Account not found.\n')
def history():
    n=input('Acc#: '); d=load()
    for a in d:
        if a['acc']==n: print('History:',*a['history']); return
    print('Account not found.\n')
while True:
    print('===== Bank Account System =====\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Transaction History\n6. Exit')
    c=input('Enter your choice: ')
    if c=='1': create()
    elif c=='2': deposit()
    elif c=='3': withdraw()
    elif c=='4': balance()
    elif c=='5': history()
    elif c=='6': print('Exiting...'); break
    else: print('Invalid!\n')
