FILE_NAME = "active_customers_by_month.csv"

# Here's a re-usable method for showing a set of customer names, sorted alphabetically
def show_customer_list(heading: str, customers: set):
    print(heading)
    print("-" * 40)
    for customer in sorted(customers):
        print(customer)
    print()
