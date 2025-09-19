import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

read_file = pd.read_csv('expense_data_large.csv')

class ExpenseTracker:
    def __init__(self,DataFrame=read_file):
        DataFrame.fillna(0,inplace=True)

    # Add a new expense
    def add_expense(self,Date,Amount,Category,Description):
        self.Date = Date
        self.Amount = Amount
        self.Category = Category
        self.Description = Description

        with open('expense_data_large.csv', 'a') as f:
            f.write(f"{self.Date},{self.Amount},{self.Category},{self.Description}\n")
        
    # View summary of expenses
    def get_summary(self):
        super().__init__()
        ttl_avg = np.mean(read_file['Amount'])
        total_exp = read_file['Amount'].sum()
        print(f"Average Expense: {ttl_avg}")
        print(f"Total Expense: {total_exp}")

    # Visualize expenses
    def visualize_expenses(self):
        super().__init__()
        print("1. Bar Chart")
        print("2. Line Graph")
        print("3. Pie Chart")
        print("4. Histogram")

        choice = int(input("Choose a visualization type (1-4): "))

        # Bar chart
        if choice == 1:
            plt.figure(figsize=(10,5))
            Category_data = read_file.groupby('Category')['Amount'].sum()
            Category_data.plot(kind='bar')
            plt.xlabel('Category')
            plt.ylabel('Total Amount')
            plt.title('Expenses by Category')
            plt.xticks(rotation=360)
            plt.show()

        # Line graph
        elif choice == 2:
            plt.figure(figsize=(10,5))
            Date_data = read_file.groupby('Date')['Amount'].sum()
            Date_data.plot(kind='line', marker='o')
            plt.xlabel('Date')
            plt.ylabel('Total Amount')
            plt.title('Expenses Over Time')
            plt.xticks(rotation=360)
            plt.show()

        # Pie chart
        elif choice == 3:
            plt.figure(figsize=(8,8))
            Category_data = read_file.groupby('Category')['Amount'].sum()
            Category_data.plot(kind='pie', autopct='%1.1f%%')
            plt.title('Expenses Distribution by Category')
            plt.ylabel('')
            plt.show()

        # Histogram
        elif choice == 4:
            plt.figure(figsize=(10,5))
            read_file['Amount'].plot(kind='hist', bins=10, edgecolor='black')
            plt.xlabel('Amount')
            plt.ylabel('Frequency')
            plt.title('Expense Amount Distribution')
            plt.show()

        else:
            print("Invalid choice!")

    # Generate report
    def generate_report(self):
        super().__init__()
        report = read_file.groupby('Category')['Amount'].sum().reset_index()
        print(report)
     
    # Filter expenses by date or category
    def filter_expenses(self,Category):
        super().__init__()
        filtered_data = read_file.query(Category)
        print(filtered_data)

Tracker = ExpenseTracker()

while True:
    print("\n-----Expense Tracker Menu-----")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Visualize Expenses")
    print("4. Generate Report")
    print("5. Filter Expenses by Date/Category")
    print("6. Exit\n")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        Date = input("Enter date (YYYY-MM-DD): ")
        Amount = float(input("Enter amount: "))
        Category = input("Enter category: ")
        Description = input("Enter description: ")

        Tracker.add_expense(Date, Amount, Category, Description)
        print("Expense added successfully!")

    elif choice == 2:
        Tracker.get_summary()

    elif choice == 3:
        Tracker.visualize_expenses()

    elif choice == 4:
        Tracker.generate_report()

    elif choice == 5: 
        Category = input("Enter filter condition (e.g., Category == 'Food' or Amount > 100): ")
        Tracker.filter_expenses(Category)

    elif choice == 6:
        print("Thanks for using the Expense Tracker! Goodbye!")
        break

    else:
        print("Invalid choice!")
