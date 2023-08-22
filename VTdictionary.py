# Create a dictionary to represent a contact in our contact book
contact = {
    'name': 'Alice',
    'phone': '123-456-7890',
    'email': 'alice@example.com',
    'city': 'San Francisco'
}

# Let's print out some information about our contact
print("Name: " + contact['name'])
print("Phone: " + contact['phone'])
print("Email: " + contact['email'])
print("City: " + contact['city'])

# Now, Alice has moved to New York. We need to update this information in our contact book
contact['city'] = 'New York'

print("\nUpdated Contact Info:")
print("Name: " + contact['name'])
print("Phone: " + contact['phone'])
print("Email: " + contact['email'])
print("City: " + contact['city'])

# Let's add a new key-value pair to our contact
contact['website'] = 'alice.com'  
print("\nUpdated Contact Info:")
print("Name: " + contact['name'])
print("Phone: " + contact['phone'])
print("Email: " + contact['email'])
print("City: " + contact['city'])

#Loop through the dictionary  
  
contact = {'name': 'Alice', 'phone': '123-456-7890', 'email': 'alice@example.com', 'city': 'San Francisco'}

for key in contact:
    print("Key:", key)
    print("Value:", contact[key])

for value in contact.values():
    print("Value:", value)

for key, value in contact.items():
    print("Key:", key)
    print("Value:", value)
  

# Loop through the dictionary and print out the key-value pairs
for key, value in contact.items():
    print(key, ":", value)
  

# Creating a dictionary
customer = {'name': 'John Doe', 'age': 30}
print("Initial Dictionary:")
print(customer)

# Accessing a value in a dictionary
print("\nAccessing Value:")
print("Customer's name is: " + customer['name'])

# Adding a key-value pair
customer['address'] = '123 Maple St'
print("\nAdding Key-Value Pair:")
print(customer)

# Updating a value
customer['age'] = 31
print("\nUpdating Value:")
print(customer)

# Removing a key-value pair
del customer['address']
print("\nRemoving Key-Value Pair:")
print(customer)

# Looping over keys
print("\nLooping Over Keys:")
for key in customer:
    print(key)

# Looping over values
print("\nLooping Over Values:")
for value in customer.values():
    print(value)

# Looping over items
print("\nLooping Over Items:")
for key, value in customer.items():
    print(key, value)

# A list of customer dictionaries
customers = [
    {'name': 'John Doe', 'age': 30, 'address': '123 Maple St'},
    {'name': 'Jane Smith', 'age': 25, 'address': '456 Oak St'},
    {'name': 'Bob Johnson', 'age': 35, 'address': '789 Pine St'},
]

# Putting It All Together
print("\nProcessing Multiple Customers:")
for customer in customers:
    # Print their name and age
    print(f"\nName: {customer['name']}, Age: {customer['age']}")

    # Update their age
    customer['age'] += 1

    # Add a new key-value pair for purchase history
    customer['purchases'] = ['Apples', 'Oranges', 'Bananas']

    # Remove the address key-value pair
    del customer['address']

    # Print the updated customer
    print(customer)


