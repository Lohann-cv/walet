import pandas as pd
import matplotlib.pyplot as plt


def value_input():
    income = float(input("Veuiller saisir votre rentrer d'argent : "))
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
        outcomes.append(outcome)
        categories.append(category)

    return income, outcomes, categories


income, outcomes, categories = value_input()


def total_balance(income, outcomes):
    total_outcomes = sum(outcomes)
    total_money = income - total_outcomes
    return total_money, total_outcomes


def categories_of_outcomes(outcomes, categories):
    outcomes_categories = {}
    for i in range(len(outcomes)):
        category = categories[i]
        if category in outcomes_categories:
            outcomes_categories[category] += outcomes[i]
        else:
            outcomes_categories[category] = outcomes[i]
    return outcomes_categories


total_money, total_outcomes = total_balance(income, outcomes)
outcomes_categories = categories_of_outcomes(outcomes, categories)

print(
    f"Vos dépenses totales sont de {total_outcomes}\nVotre solde est de {total_money}\nDépenses par catégorie :")
for category, value in outcomes_categories.items():
    print(f"{category}: {value} euros")


def outcomes_visualization(outcomes_categories):
    categories = list(outcomes_categories.keys())
    values = list(outcomes_categories.values())

    plt.bar(categories, values)
    plt.xlabel("Catégories")
    plt.ylabel("Montant (euros)")
    plt.title("Dépenses par catégorie")
    plt.show()


outcomes_visualization(outcomes_categories)
