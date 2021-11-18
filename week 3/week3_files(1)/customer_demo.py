from customer import Customer

customers = []
with open('customers.txt', 'r') as file:
    for line in file:
        # splits each line of file by whitespace
        info = line.split()
        first_name = info[0]
        last_name = info[1]
        orders = []
        # add each order to a list
        for i in range(2,len(info)):
            orders.append(info[i])
            # create customer object and add to list of customers
            customers.append(Customer(first_name, last_name, orders))

# call add_order method on the first customer object in list
customers[0].add_order('44567')
print(customers[0].get_orders())
