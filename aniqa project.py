class Product:
    def init(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        self.stock_quantity -= quantity


# List of products (fruits and grocery items)
products = [
    Product(1, "Apple", "Fruit", 0.5, 100),
    Product(2, "Banana", "Fruit", 0.3, 150),
    Product(3, "Orange", "Fruit", 0.7, 80),
    Product(4, "Tomato", "Vegetable", 0.4, 50),
    Product(5, "Carrot", "Vegetable", 0.6, 60),
    Product(6, "Onion", "Vegetable", 0.8, 40)
]

# Simulating users and admins
users = {
    'admin': 'adminpass',
    'user': 'userpass'
}

# Ask for login
def login():
    print("Enter username: ", end="")
    username = input().strip()
    print("Enter password: ", end="")
    password = input().strip()
    
    if username in users and users[username] == password:
        print(f"Welcome, {username.capitalize()}!")
        return username
    else:
        print("Invalid login. Try again.")
        return None


# Function to display products (hide stock from users)
def display_products(is_admin=False):
    print("\nAvailable products:")
    for product in products:
        print(f"{product.name} - ${product.price}")
        if is_admin:
            print(f"  Stock: {product.stock_quantity}")
        print("")

# Function to handle user's cart and purchase
def user_cart():
    cart = {}
    while True:
        print("Enter product name to add to your cart, or type 'done' to complete your selection:")
        product_name = input().strip()
        
        if product_name.lower() == 'done':
            break
        
        product = next((p for p in products if p.name.lower() == product_name.lower()), None)
        if product:
            if product_name in cart:
                cart[product_name]['quantity'] += 1  # Every item added counts as 1 quantity
            else:
                cart[product_name] = {'price': product.price, 'quantity': 1}
            product.update_stock(1)  # Decrease stock by 1 for each item added
            print(f"{product_name} added to your cart.")
        else:
            print("Product not found. Please try again.")
    
    return cart

# Function to calculate the total bill (without tax)
def calculate_bill(cart):
    total = 0
    for product_name, details in cart.items():
        total += details['price'] * details['quantity']
    
    return total


# Main logic for managing login and cart
def main():
    username = None
    while not username:
        username = login()

    is_admin = username == 'admin'
    
    display_products(is_admin)  # Admin sees the stock levels, users do not

    if not is_admin:
        cart = user_cart()
        if cart:
            print("\nYour Cart Summary:")
            total = calculate_bill(cart)
            for product_name, details in cart.items():
                print(f"{product_name} - ${details['price']} x {details['quantity']} = ${details['price'] * details['quantity']}")
            print(f"\nSubtotal: ${total}")
        else:
            print("You didn't add any products to your cart.")
    else:
        print("\nAdmin Dashboard")
        display_products(True)  # Admin sees full product details (stock level)
        
        # Admin could add/edit/remove products here (left for further development)

if name == "main":
    main()