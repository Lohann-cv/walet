import sqlite3
# Voir le lexic pour plus d'explication, ici on est sur plusieur fonction donc chaqune ouvret puis ferme la database


# Initialise la base de données
def init_db():
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT,
            type TEXT CHECK(type IN ('income', 'outcome')),
            date TEXT DEFAULT CURRENT_DATE
        )
    ''')
    conn.commit()
    conn.close()


# Insère une transaction dans la db
def insert_transaction(amount, category, type):
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (amount, category, type)
        VALUES (?, ?, ?)
    ''', (amount, category, type))
    conn.commit()
    conn.close()


# Récupère les transaction de la db
def get_all_transactions():
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    transactions = cursor.fetchall()
    conn.close()
    return transactions


# Récupère les incomes de la db
def get_incomes():
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    cursor.execute('SELECT amount FROM transactions WHERE type = "income"')
    incomes = cursor.fetchall()
    conn.close()
    return [income[0] for income in incomes]


# Récupère les outcomes et leur category de la db
def get_outcomes():
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    cursor.execute(
        'SELECT amount, category FROM transactions WHERE type = "outcome"')
    outcomes = cursor.fetchall()
    conn.close()
    return outcomes
