customers = {}

with open("input.txt") as file:
	for line in file:
		customer, product, count = input().split()
		count = int(count)

		if customer not in customers.keys():
			customers[customer] = {product: count}
		else:
			products_dict = customers[customer]

			if product not in products_dict:
				products_dict[product] = count
			else:
				products_dict[product] += count


customers_keys = sorted(list(customers.keys()))

for customer in customers_keys:
	print(f"{customer}:")
	customer_products = customers[customer]
	customer_products_keys = sorted(list(customer_products.keys()))

	for product in customer_products_keys:
		print(f"{product} {customer_products[product]}")