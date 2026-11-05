units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    print("Eligible for full subsidy")
elif units <= 200:
    print("Eligible for partial subsidy")
else:
    print("Not eligible for subsidy")


income = float(input("Enter annual income: "))
units = int(input("Enter electricity units for eligibility check: "))

if income <= 250000:
    if units <= 200:
        print("Eligible (nested if)")
    else:
        print("Not eligible (nested if)")
else:
    print("Not eligible (nested if)")

if income <= 250000 and units <= 200:
    print("Eligible (Boolean condition)")
else:
    print("Not eligible (Boolean condition)")

category = int(input("Enter category (1, 2 or 3): "))
match category:
    case 1:
        print("Full subsidy")
    case 2:
        print("Partial subsidy")
    case 3:
        print("No subsidy")
    case _:
        print("Invalid category")
