revenue = float(input("Enter the revenue, please:"))
costs = float(input("Enter the costs, please: "))
result = revenue - costs

if result > 0:
    print(f"Good. You company has earned {revenue - costs} dollar!")
elif result == 0:
    print(f"Your company didn't make any money!")
else:
    print(f"Oh, no. Ypu company is out for buisness by {abs(revenue - costs)}")

employess = int(input('Enter the number of employees:'))
print(f"Per employee, your company earned {result // employess}")

