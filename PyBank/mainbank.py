import csv
import os

def average(numbers):
    return sum(numbers) / len(numbers)

total_months = 0
total_profit_losses = 0
profit_losses = []
dates = []

with open('budget_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
   
    next(csv_reader)
    
    for row in csv_reader:
        
        date = row[0]
        profit_loss = int(row[1])  
        
        total_months += 1
        total_profit_losses += profit_loss
        
        profit_losses.append(profit_loss)
        dates.append(date)

changes = [profit_losses[i + 1] - profit_losses[i] for i in range(len(profit_losses) - 1)]

average_change = average(changes)

greatest_increase = max(changes)
greatest_decrease = min(changes)

greatest_increase_date = dates[changes.index(greatest_increase) + 1]
greatest_decrease_date = dates[changes.index(greatest_decrease) + 1]

print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
