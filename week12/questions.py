"""Q1: Given this list of temperatures in Celsius:
celsius_temps = [0, 20, 37, 100, -10, 15]
Write a list comprehension to convert them to Fahrenheit using the formula: F = (C × 9/5) + 32
"""
# Answer Q1:
celsius_temps = [0, 20, 37, 100, -10, 15]
fahrenheit_temps = [(c * 9/5) + 32 for c in celsius_temps]
print("Q1 - Celsius to Fahrenheit:", fahrenheit_temps)

"""Q2: You have a list of customer ages:
ages = [25, 42, 17, 30, 65, 19, 21, 55, 16]
Create a list comprehension that keeps only ages 18 and older.
"""
# Answer Q2:
ages = [25, 42, 17, 30, 65, 19, 21, 55, 16]
adults = [age for age in ages if age >= 18]
print("Q2 - Adults (18+):", adults)

"""Q3: You're analyzing sales data:
sales = [1250, 890, 2100, 540, 3100, 980]
Create a list comprehension that returns "High" for sales > 1500, "Medium" for sales between 500-1500, and "Low" for sales < 500.
"""
# Answer Q3:
sales = [1250, 890, 2100, 540, 3100, 980]
sales_categories = ["High" if s > 1500 else "Medium" if s >= 500 else "Low" for s in sales]
print("Q3 - Sales categories:", sales_categories)
"""Q4: Given this list of strings:
products = ["laptop", "mouse", "keyboard", "monitor", "printer"]
Create a list comprehension that returns each product name capitalized and with " - In Stock" appended.
"""
# Answer Q4:
products = ["laptop", "mouse", "keyboard", "monitor", "printer"]
products_stock = [p.capitalize() + " - In Stock" for p in products]
print("Q4 - Products in stock:", products_stock)
"""Q5: You have a list with mixed data types:
data = [10, "20", 30.5, "invalid", 40, "50.5", "error"]
Write a list comprehension that converts only the numeric strings to floats, leaving non-numeric strings as they are.
"""
# Answer Q5:
def try_float(x):
    try:
        return float(x)
    except (ValueError, TypeError):
        return x

data = [10, "20", 30.5, "invalid", 40, "50.5", "error"]
converted_data = [try_float(x) for x in data]
print("Q5 - Converted data:", converted_data)
"""Part 2: Dictionary Comprehension Questions
Q6: You have two lists:
products = ["laptop", "mouse", "keyboard", "monitor"]
prices = [999.99, 29.99, 79.99, 299.99]
Create a dictionary comprehension that pairs each product with its price.
"""
# Answer Q6:
products = ["laptop", "mouse", "keyboard", "monitor"]
prices = [999.99, 29.99, 79.99, 299.99]
product_prices = {product: price for product, price in zip(products, prices)}
print("Q6 - Product prices:", product_prices)
"""Q7: Using the dictionary from Q6, create a new dictionary with 15% discount applied only to items priced above $100."""
# Answer Q7:
discounted_prices = {product: price * 0.85 if price > 100 else price for product, price in product_prices.items()}
print("Q7 - Discounted prices:", discounted_prices)

"""Q8: From the sales_data list in your example:
Create a dictionary comprehension that shows for each product:

Key: product name
Value: tuple containing (price, units, revenue)
"""
# Answer Q8:
sales_data = [
    {"name": "Laptop", "price": 999.99, "units": 5, "revenue": 4999.95, "category": "Electronics"},
    {"name": "Mouse", "price": 29.99, "units": 20, "revenue": 599.80, "category": "Accessories"},
    {"name": "Keyboard", "price": 79.99, "units": 15, "revenue": 1199.85, "category": "Accessories"},
    {"name": "Monitor", "price": 299.99, "units": 8, "revenue": 2399.92, "category": "Electronics"}
]
sales_dict = {item["name"]: (item["price"], item["units"], item["revenue"]) for item in sales_data}
print("Q8 - Sales data dict:", sales_dict)
"""Q9: You have a dictionary of student names and their scores:
scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 81}
Create a new dictionary that shows letter grades:

A for scores ≥ 90
B for scores 80-89
C for scores 70-79
D for scores < 70
"""
# Answer Q9:
scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 81}
grades = {name: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" 
          for name, score in scores.items()}
print("Q9 - Grades:", grades)
"""Q10: Given this list of employee data dictionaries:

employees = [
    {"name": "John", "hours": 45, "rate": 25.50},
    {"name": "Sarah", "hours": 40, "rate": 32.00},
    {"name": "Mike", "hours": 50, "rate": 28.75}
]
Create a dictionary comprehension where:

Key: employee name
Value: total pay (hours × rate) with overtime pay (1.5× rate) for hours over 40
Part 3: Combined Comprehension Questions
"""
# Answer Q10:
employees = [
    {"name": "John", "hours": 45, "rate": 25.50},
    {"name": "Sarah", "hours": 40, "rate": 32.00},
    {"name": "Mike", "hours": 50, "rate": 28.75}
]
employee_pay = {
    emp["name"]: (40 * emp["rate"]) + ((emp["hours"] - 40) * emp["rate"] * 1.5) if emp["hours"] > 40 
    else emp["hours"] * emp["rate"]
    for emp in employees
}
print("Q10 - Employee pay with overtime:", employee_pay)
"""Q11: Using the sales_data list from your example, create a list comprehension that returns only the products with revenue greater than $300."""
# Answer Q11:
high_revenue_products = [item["name"] for item in sales_data if item["revenue"] > 300]
print("Q11 - High revenue products:", high_revenue_products)

"""Q12: Create a dictionary from the sales_data where:

Key: product name
Value: percentage of total revenue that product contributes"""
# Answer Q12:
total_revenue = sum(item["revenue"] for item in sales_data)
revenue_percentage = {item["name"]: (item["revenue"] / total_revenue) * 100 for item in sales_data}
print("Q12 - Revenue percentages:", revenue_percentage)

"""Q13: Given this data:

customers = [
    {"name": "Alice", "purchases": [50, 125, 75]},
    {"name": "Bob", "purchases": [200, 50]},
    {"name": "Charlie", "purchases": [300, 150, 100, 50]}
]
Create a dictionary comprehension where:

Key: customer name
Value: total amount spent"""
# Answer Q13:
customers = [
    {"name": "Alice", "purchases": [50, 125, 75]},
    {"name": "Bob", "purchases": [200, 50]},
    {"name": "Charlie", "purchases": [300, 150, 100, 50]}
]
customer_totals = {cust["name"]: sum(cust["purchases"]) for cust in customers}
print("Q13 - Customer totals:", customer_totals)

"""Q14: From the customers list in Q13, create a list comprehension that returns customer names who have spent more than $400 in total."""
# Answer Q14:
big_spenders = [cust["name"] for cust in customers if sum(cust["purchases"]) > 400]
print("Q14 - Customers who spent > $400:", big_spenders)

"""Q15: You're analyzing website traffic data:

daily_visitors = {
    "Monday": [1200, 1100, 1300, 1400],
    "Tuesday": [1000, 900, 1100, 1200],
    "Wednesday": [1500, 1400, 1600, 1700]
}
Create a dictionary comprehension that shows for each day:

Key: day name
Value: average visitors (sum/4)
Part 4: Challenge Questions"""
# Answer Q15:
daily_visitors = {
    "Monday": [1200, 1100, 1300, 1400],
    "Tuesday": [1000, 900, 1100, 1200],
    "Wednesday": [1500, 1400, 1600, 1700]
}
avg_visitors = {day: sum(visitors) / len(visitors) for day, visitors in daily_visitors.items()}
print("Q15 - Average daily visitors:", avg_visitors)

"""Q16: The company is running a promotion: "Buy 2, get 1 free" on all items.
Using your original sales_data, calculate the new revenue if this promotion was applied to all sales."""
# Answer Q16:
# With "Buy 2, get 1 free", customer pays for 2 and gets 3 items, so effective price is 2/3 of original
promotion_revenue = {item["name"]: item["revenue"] * (2/3) for item in sales_data}
total_promotion_revenue = sum(promotion_revenue.values())
print("Q16 - Promotion revenue by product:", promotion_revenue)
print("Q16 - Total promotion revenue:", total_promotion_revenue)

"""Q17: You need to create an inventory report that shows:

Products sorted by profitability (revenue per unit sold)
Mark each product as "Restock Needed" if units sold > 10"""
# Answer Q17:
profitability = {item["name"]: {"profit_per_unit": item["revenue"] / item["units"], 
                                 "restock": "Yes" if item["units"] > 10 else "No"}
                 for item in sales_data}
sorted_profitability = sorted(profitability.items(), key=lambda x: x[1]["profit_per_unit"], reverse=True)
print("Q17 - Products sorted by profitability:")
for product, data in sorted_profitability:
    print(f"  {product}: ${data['profit_per_unit']:.2f} per unit, Restock: {data['restock']}")

"""Q18: Create a comprehensive sales summary dictionary using only comprehensions that includes:

Total revenue for each product
Average price across all products
Total units sold
Most profitable product
List of products that need restocking (units > 10)
"""
# Answer Q18:
comprehensive_summary = {
    "revenue_by_product": {item["name"]: item["revenue"] for item in sales_data},
    "average_price": sum(item["price"] for item in sales_data) / len(sales_data),
    "total_units_sold": sum(item["units"] for item in sales_data),
    "most_profitable_product": max(sales_data, key=lambda x: x["revenue"])["name"],
    "restock_needed": [item["name"] for item in sales_data if item["units"] > 10]
}
print("Q18 - Comprehensive summary:", comprehensive_summary)

"""Q19: Write a single dictionary comprehension that transforms sales_data into:

{
    "Laptop": {
        "price": 999.99,
        "units": 5,
        "revenue": 4999.95,
        "category": "Electronics"
    },
    # ... and so on for other products
}
(Assume categories: Laptop="Electronics", Mouse="Accessories", Keyboard="Accessories", Monitor="Electronics")"""
# Answer Q19:
category_map = {"Laptop": "Electronics", "Mouse": "Accessories", "Keyboard": "Accessories", "Monitor": "Electronics"}
transformed_sales = {item["name"]: {
    "price": item["price"],
    "units": item["units"],
    "revenue": item["revenue"],
    "category": category_map.get(item["name"], item["category"])
} for item in sales_data}
print("Q19 - Transformed sales data:", transformed_sales)

"""Q20: Create a function that takes any sales data list and returns a complete analysis using comprehensions only. The function should return a dictionary with all the metrics you've calculated."""
# Answer Q20:
def analyze_sales(sales_data):
    """Complete sales analysis function using comprehensions."""
    return {
        "revenue_by_product": {item["name"]: item["revenue"] for item in sales_data},
        "total_revenue": sum(item["revenue"] for item in sales_data),
        "average_price": sum(item["price"] for item in sales_data) / len(sales_data) if sales_data else 0,
        "total_units": sum(item["units"] for item in sales_data),
        "price_by_product": {item["name"]: item["price"] for item in sales_data},
        "units_by_product": {item["name"]: item["units"] for item in sales_data},
        "revenue_percentage": {item["name"]: (item["revenue"] / sum(s["revenue"] for s in sales_data)) * 100 
                             for item in sales_data} if sales_data else {},
        "most_profitable": max(sales_data, key=lambda x: x["revenue"])["name"] if sales_data else None,
        "restock_needed": [item["name"] for item in sales_data if item["units"] > 10],
        "high_revenue_items": [item["name"] for item in sales_data if item["revenue"] > 1000]
    }

analysis = analyze_sales(sales_data)
print("Q20 - Complete sales analysis:")
for key, value in analysis.items():
    print(f"  {key}: {value}")