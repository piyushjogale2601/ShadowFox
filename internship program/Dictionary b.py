your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

your_total_expenses = sum(your_expenses.values())
partner_total_expenses = sum(partner_expenses.values())

print("Your Total Expenses:", your_total_expenses)
print("Partner's Total Expenses:", partner_total_expenses)

if your_total_expenses > partner_total_expenses:
    print("You spent more money overall.")
elif partner_total_expenses > your_total_expenses:
    print("Your partner spent more money overall.")
else:
    print("You both spent the same amount of money.")

max_difference = 0
category_with_max_difference = ""

for category in your_expenses:
    difference = (your_expenses[category] - partner_expenses[category])
    if difference > max_difference:
        max_difference = difference
        category_with_max_difference = category

print("Category with the maximum difference in spending:", category_with_max_difference)
print("Difference:", max_difference)