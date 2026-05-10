# Smart Expense Tracker

A simple command-line application to track your monthly expenses and stay within your budget.

## Features

- Set a monthly budget
- Add expenses by category
- View expense summary
- Automatic alerts when budget is exceeded or 80% used

## Requirements

- Python 3.x

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. Enter your monthly budget when prompted.

3. Choose options:
   - 1: Add an expense (enter category and amount)
   - 2: View summary of expenses
   - 3: Exit the application

## Example

```
--- Welcome to Smart Expense Tracker ---
Enter your monthly budget: 1000

Remaining: 1000.00
1. Add Expense  2. Summary  3. Exit: 1
Category: Food
Amount: 200

Remaining: 800.00
1. Add Expense  2. Summary  3. Exit: 2

--- Summary ---
Food: 200.0
Total: 200.0
```

## Troubleshooting

- Ensure you have Python installed and run the script with `python main.py`.
- Input validation is basic; enter valid numbers for budget and amounts.
