# Summary:
# Yeh calculator user se expression leta hai, result show karta hai, history file mein save karta hai.
import json
def load():
    try: return json.load(open('history.json'))
    except: return []
def save(lst):
    json.dump(lst, open('history.json','w'))
def calc():
    expr = input('Enter expression: ')
    try:
        res = eval(expr)
        print(f"Result: {res}\n")
        h = load(); h.append(f"{expr} = {res}"); save(h)
    except:
        print('Invalid expression!\n')
def show():
    h = load()
    if not h: print('No history.\n')
    else:
        for i, r in enumerate(h, 1): print(f"{i}. {r}")
while True:
    print('===== Basic Calculator =====\n1. Calculate\n2. Show History\n3. Exit')
    c = input('Enter your choice: ')
    if c=='1': calc()
    elif c=='2': show()
    elif c=='3': print('Exiting...'); break
    else: print('Invalid!\n')
