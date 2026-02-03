"""Exercise 1 — Beginner
Create a Student class with:

attributes: name, course, marks (a list of numbers)
methods:
average() → returns the average mark
grade() → returns 'A' ≥70, 'B' 60–69, 'C' 50–59, 'D' <50
Hint: average = sum(marks) / len(marks); handle empty list.
"""


# Implementation for Exercise 1
class Student:
	"""Simple Student class storing marks and computing average/grade."""
	def __init__(self, name, course, marks=None):
		self.name = name
		self.course = course
		# store marks as a list; default empty list when not provided
		self.marks = marks or []

	def average(self):
		"""Return average of marks. If no marks, return 0.0."""
		if not self.marks:
			return 0.0
		return sum(self.marks) / len(self.marks)

	def grade(self):
		"""Return letter grade based on average as specified."""
		avg = self.average()
		if avg >= 70:
			return "A"
		if 60 <= avg < 70:
			return "B"
		if 50 <= avg < 60:
			return "C"
		return "D"


# Short demonstration for Exercise 1
if __name__ == "__main__":
	s1 = Student("Alice", "Math", [75, 80, 68])
	s2 = Student("Bob", "History", [])
	print("Student:", s1.name, "Average:", s1.average(), "Grade:", s1.grade())
	print("Student:", s2.name, "Average:", s2.average(), "Grade:", s2.grade())






"""Exercise 2 — Intermediate
Create Product and Store:

Product same as earlier (sku, name, category, price, quantity).
Store methods:
add_product(product)
sell(sku, qty) — reduce stock (raise if insufficient)
report() — prints each product: sku, name, qty, total_value
Add error handling for selling more than in stock.
Hint: use dictionary sku -> Product.
"""


class Product:
	"""Represents a product in inventory."""
	def __init__(self, sku, name, category, price, quantity=0):
		self.sku = sku
		self.name = name
		self.category = category
		self.price = float(price)
		self.quantity = int(quantity)

	def total_value(self):
		return self.price * self.quantity


class Store:
	"""Simple store managing Products using sku -> Product mapping."""
	def __init__(self):
		self.products = {}

	def add_product(self, product):
		"""Add a product; if sku exists, increase its quantity."""
		if product.sku in self.products:
			existing = self.products[product.sku]
			existing.quantity += product.quantity
		else:
			self.products[product.sku] = product

	def sell(self, sku, qty):
		"""Sell `qty` of product with `sku`. Raise ValueError on insufficient stock."""
		if sku not in self.products:
			raise KeyError(f"Product with sku {sku} not found")
		prod = self.products[sku]
		if qty > prod.quantity:
			raise ValueError(f"Insufficient stock for sku {sku}: requested {qty}, available {prod.quantity}")
		prod.quantity -= qty
		# Return revenue for this sale
		return qty * prod.price

	def report(self):
		"""Print a report listing sku, name, qty, and total value for each product."""
		for sku, p in self.products.items():
			print(f"{sku}: {p.name} — Qty: {p.quantity} — Total Value: {p.total_value():.2f}")


# Short demonstration for Exercise 2
if __name__ == "__main__":
	store = Store()
	p1 = Product("SKU1", "Notebook", "Stationery", 2.5, 100)
	p2 = Product("SKU2", "Pen", "Stationery", 1.0, 50)
	store.add_product(p1)
	store.add_product(p2)
	try:
		revenue = store.sell("SKU1", 10)
		print("Sold 10 Notebook, revenue:", revenue)
	except Exception as e:
		print("Sell error:", e)
	store.report()




"""Exercise 3 — Advanced
Build a small SalesReport class:

It should accept a list of Transaction objects.
Provide methods:
revenue_by_product() → returns a dict {sku: revenue}
top_n_products_by_revenue(n) → returns list of tuples [(sku, revenue), ...] sorted desc
Hint: accumulate in a dict like totals[sku] = totals.get(sku, 0) + t.revenue().
"""


class Transaction:
	"""Represent a single sale transaction."""
	def __init__(self, sku, quantity, unit_price):
		self.sku = sku
		self.quantity = int(quantity)
		self.unit_price = float(unit_price)

	def revenue(self):
		return self.quantity * self.unit_price


class SalesReport:
	"""Analyze a list of Transaction objects to produce revenue summaries."""
	def __init__(self, transactions=None):
		self.transactions = transactions or []

	def revenue_by_product(self):
		totals = {}
		for t in self.transactions:
			totals[t.sku] = totals.get(t.sku, 0.0) + t.revenue()
		return totals

	def top_n_products_by_revenue(self, n):
		totals = self.revenue_by_product()
		# sort items by revenue descending and return top n as list of tuples
		sorted_items = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)
		return sorted_items[:n]


# Short demonstration for Exercise 3
if __name__ == "__main__":
	txs = [
		Transaction("SKU1", 3, 2.5),
		Transaction("SKU2", 5, 1.0),
		Transaction("SKU1", 2, 2.5),
	]
	report = SalesReport(txs)
	print("Revenue by product:", report.revenue_by_product())
	print("Top product:", report.top_n_products_by_revenue(1))
