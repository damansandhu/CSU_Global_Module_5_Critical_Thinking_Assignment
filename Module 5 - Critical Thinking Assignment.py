# Part 1: Average Rainfall Calculation

# Initialize total rainfall and total months
total_rainfall = 0
total_months = 0

# Ask the user for the number of years
years = int(input("Enter the number of years: "))

# Outer loop for each year
for year in range(1, years + 1):
    print(f"Year {year}:")
    
    # Inner loop for each month
    for month in range(1, 13):
        monthly_rainfall = float(input(f"  Enter the inches of rainfall for month {month}: "))
        total_rainfall += monthly_rainfall
        total_months += 1

# Calculate the average rainfall
average_rainfall = total_rainfall / total_months

# Output the results
print(f"\nNumber of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall}")
print(f"Average rainfall per month: {average_rainfall:.2f}")


# Part 2: CSU Global Bookstore Points Calculation

# Ask the user for the number of books purchased
books_purchased = int(input("Enter the number of books purchased this month: "))

# Determine points based on the number of books purchased
if books_purchased == 0:
    points = 0
elif books_purchased == 2:
    points = 5
elif books_purchased == 4:
    points = 15
elif books_purchased == 6:
    points = 30
elif books_purchased >= 8:
    points = 60
else:
    points = 0

# Output the results
print(f"Points awarded: {points}")
