import sys

def main():
    print("--- Welcome to Smart Expense Tracker ---")
    try:
        budget = float(input("Enter your monthly budget: "))
    except:
        print("Invalid input.")
        return

    spent = 0
    expenses = {}

    while True:
        print(f"\nRemaining: {budget - spent:.2f}")
        choice = input("1. Add Expense  2. Summary  3. Exit: ")

        if choice == '1':
            cat = input("Category: ")
            amt = float(input("Amount: "))
            spent += amt
            expenses[cat] = expenses.get(cat, 0) + amt
            
            # THE SMART LOGIC
            if spent > budget:
                print("!!! ALERT: BUDGET EXCEEDED !!!")
            elif spent > (budget * 0.8):
                print("--- Warning: 80% used ---")

        elif choice == '2':
            print("\n--- Summary ---")
            for c, a in expenses.items():
                print(f"{c}: {a}")
            print(f"Total: {spent}")

        elif choice == '3':
            sys.exit()

if __name__ == "__main__":
    main()
