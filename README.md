# Tpwits-8-Projects
## **🔍 Overview**  
This document details 8 practical Python terminal projects designed to solve real-world problems using basic programming skills. Each project was developed independently, focusing on **practicality**, **usability**, and **file-based data persistence**.  

---

## **📁 Project 1: Student Management System**  
**Objective:** Digitally manage student records (name, roll number, class, marks).  

### **💡 Key Insights:**  
- Uses **JSON** for secure data storage.  
- **Roll number** acts as a unique identifier for search/update.  
- Real-time file handling mimics database operations.  

### **🔍 Sample Code:**  
```python
def search():
    r = input('Roll: ')
    for s in load():
        if s['roll'] == r:
            print('Found:', s)
```

---

## **📚 Project 2: Library Book Tracker**  
**Objective:** Track book statuses (issued/available) in libraries.  

### **💡 Key Insights:**  
- **ISBN** serves as the primary key.  
- Dynamic status updates (issue/return).  
- Live availability checks.  

### **🔍 Sample Code:**  
```python
def ret():
    for b in load():
        if b['isbn'] == input() and b['status'] == 'issued':
            b['status'] = 'available'
            save(load())
```

---

## **💼 Project 3: Simple Bank Account System**  
**Objective:** Simulate banking operations (deposit, withdraw, balance check).  

### **💡 Key Insights:**  
- **Transaction history** logged for each account.  
- Balance validation prevents overdrafts.  
- Account numbers uniquely identify users.  

### **🔍 Sample Code:**  
```python
def withdraw():
    acc = input('Account#: ')
    for a in load():
        if a['acc'] == acc and a['bal'] >= int(input('Amount: ')):
            a['bal'] -= amount
            a['history'].append(f'Withdraw: {amount}')
```

---

## **✅ Project 4: To-Do List App**  
**Objective:** Manage daily tasks with completion tracking.  

### **💡 Key Insights:**  
- Tasks marked as **done/pending**.  
- Simple **add/delete** functionality.  
- JSON stores task history.  

### **🔍 Sample Code:**  
```python
def mark_done():
    tasks = load()
    tasks[int(input('Task#'))-1]['done'] = True
    save(tasks)
```

---

## **📱 Project 5: Simple Contact Book**  
**Objective:** Store and manage contact details (name, phone, email).  

### **💡 Key Insights:**  
- **Phone numbers** as unique keys.  
- Search by name/phone.  
- Persistent storage via JSON.  

### **🔍 Sample Code:**  
```python
def search():
    query = input('Name/Phone: ')
    for c in load():
        if query in (c['name'], c['phone']):
            print('Found:', c)
```

---

## **🧮 Project 6: Basic Calculator with History**  
**Objective:** Perform calculations with a history log.  

### **💡 Key Insights:**  
- Supports **+, -, *, /**.  
- **eval()** for expression parsing.  
- History saved in JSON.  

### **🔍 Sample Code:**  
```python
def calculate():
    expr = input('Enter expression: ')
    result = eval(expr)
    save(load() + [f"{expr} = {result}"])
```

---

## **💰 Project 7: Expense Tracker**  
**Objective:** Track expenses by date/category.  

### **💡 Key Insights:**  
- **Category-wise summaries** (e.g., Food, Transport).  
- Total spending calculations.  
- Date-based search.  

### **🔍 Sample Code:**  
```python
def category_summary():
    summary = {}
    for e in load():
        summary[e['cat']] = summary.get(e['cat'], 0) + e['amt']
    print(summary)
```

---

## **📦 Project 8: Simple Inventory Management**  
**Objective:** Track product quantities and details.  

### **💡 Key Insights:**  
- **Product IDs** for unique identification.  
- Quantity updates/checks.  
- Search by name/ID.  

### **🔍 Sample Code:**  
```python
def update_qty():
    id = input('Product ID: ')
    for p in load():
        if p['id'] == id:
            p['qty'] = int(input('New Qty: '))
            save(load())
```

---

## **🎯 Final Thoughts**  
These projects were a **hands-on journey** into Python programming, covering:  
✔ **File Handling** (JSON).  
✔ **Input Validation**.  
✔ **Modular Design**.  
✔ **Real-World Problem Solving**.  
              Thanks

