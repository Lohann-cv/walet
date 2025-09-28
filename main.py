import database as db


def value_input():
    db.init_db()

    income = float(input("Veuiller saisir votre rentrer d'argent : "))
    db.insert_transaction(income, "Revenu", "income")

    outcomes = []
    categories = []
    while True:
        try:
            outcome = float(
                input("Veuiller rentrer votre dépense (ou 0 pour continuer) : "))
        except ValueError:
            print("Veuiller rentrer une valeur numérique positive !")
            continue
        if outcome == 0:
            break
        if outcome < 0:
            print("Veuiller rentrer une valeur positive !")
            continue
        category = input("Veuiller rentrer la catégorie de la dépense : ")
        db.insert_transaction(outcome, category, "outcome")
        outcomes.append(outcome)
        categories.append(category)
    return income, outcomes, categories


# calcule la balance total à l'aide des data déjà ajouter sur le income et outcome en les appelant
def total_balance():
    incomes = db.get_incomes()
    outcomes = db.get_outcomes()
    total_income = sum(incomes)
    total_outcome = sum([outcome[0] for outcome in outcomes])
    return total_income - total_outcome, total_outcome


def categories_of_outcomes():
    outcomes = db.get_outcomes()
    outcomes_categories = {}
    for amount, category in outcomes:
        if category in outcomes_categories:
            outcomes_categories[category] += amount
        else:
            outcomes_categories[category] = amount
    return outcomes_categories


# Exécution
income, outcomes, categories = value_input()
total_money, total_outcomes = total_balance()
outcomes_categories = categories_of_outcomes()

print(
    f"Vos dépenses totales sont de {total_outcomes}\nVotre solde est de {total_money}\nDépenses par catégorie :")
for category, value in outcomes_categories.items():
    print(f"{category}: {value} euros")
