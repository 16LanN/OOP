class Device:
    def __init__(self, name=None, price=1, stock=0, warrantly_period=0):
        self.name = name
        self.price = price
        self.stock = stock
        self.warrantly_period = warrantly_period

    def display_info(self):
        return f"""Name: {self.name}
Price: {self.price}
Stock: {self.stock}
Warrantly Period: {self.warrantly_period}
____________________________________________________"""
    
    def __str__(self):
        return f"""Name: {self.name}
Price: {self.price}
Stock: {self.stock}
Warrantly Period: {self.warrantly_period}"""

    def apply_discount(self, discount_percentage):
        self.price = int(self.price - (self.price/100*discount_percentage))

    def is_available(self, amount):
        if amount <= self.stock:
            return True
        else:
            return False
        
    def reduce_stock(self, amount):
        self.stock -= amount


class Smartphone(Device):
    def __init__(self, screen_size, battery_life, name, price, stock):
        super().__init__(name=name, price=price, stock=stock)
        self.screen_size = screen_size
        self.battery_life = battery_life
        

    def __str__(self):
        return f"""Screen Size: {self.screen_size}
Battery Life: {self.battery_life}"""

    def make_call(self):
        return f"You're simulating a call"

    def install_app(self):
        return f"You're simulating a downloading of an app" 
    

class Laptop(Device):
    def __init__(self, ram_size, processor_speed, name, price, stock):
        super().__init__(name=name, price=price, stock=stock)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def __str__(self):
        return f"""Ram Size: {self.ram_size}
Processor Speed: {self.processor_speed}"""
    
    def run_program(self):
        return f"You're simulating a running programm"
    
    def use_keyboard(self):
        return f"You're simulating using a keyboard"
    

class Tablet(Device):
    def __init__(self, screen_resolution, weight, name, price, stock):
        super().__init__(name=name, price=price, stock=stock)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def __str__(self):
        return f"""Screen Resolution: {self.screen_resolution}
Weight: {self.weight}"""
    
    def browse_internet(self):
        return f"You're simulating a browser internet"
    
    def use_touchscreen(self):
        return f"You're simulating a touchscreen"
    

class Cart:
    def __init__(self):
        self.items = {}
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            if device.name in self.items:
                self.items[device.name] += amount
            else:
                self.items[device.name] = amount
            self.total_price += device.price * amount
            device.reduce_stock(amount)
        else:
            return f"Not enough stock for {device.name}"
    
    def remove_device(self, device, amount):
        if device.name in self.items:
            if self.items[device.name] >= amount:
                self.items[device.name] -= amount
                self.total_price -= device.price * amount
                device.reduce_stock(-amount)
            else:
                return f"Cannot remove {amount} of {device.name} - only {self.items[device.name]} in cart"
        else:
            return f"{device.name} is not in the cart"
    
    def get_total_price(self):
        return f"Total Price: ${self.total_price}"
    
    def print_items(self):
        return self.items
    
    def checkout(self):
        for i in self.items:
            print(f"Item: {i}, Quantity: {self.items[i]}")
        self.items = {}
        self.total_price = 0


Smartphone1 = Smartphone("6.5 inches", "24 hours", "iPhone 14", 500, 3)
Smartphone2 = Smartphone("5.8 inches", "18 hours", "Samsung Galaxy S21", 400, 4)
Laptop1 = Laptop("16GB", "3.2GHz", "MacBook Pro", 1200, 2)
Laptop2 = Laptop("8GB", "2.5GHz", "Dell XPS 13", 800, 5)
Tablet1 = Tablet("1920x1080", "500g", "iPad Pro", 300, 4)
Tablet2 = Tablet("2560x1440", "600g", "Samsung Galaxy Tab", 400, 3)

s = [Smartphone1, Smartphone2, Laptop1, Laptop2, Tablet1, Tablet2]
Cart1 = Cart()
while True:
    print("1. Show Devices")
    print("2. Show Cart")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        for i in s:
            print(i.display_info())
        while True:
            device_choice = input("Enter the name of the device you want to add to the cart (or 'back' to return to the main menu): ")
            if device_choice.lower() == "back":
                break
            else:
                found_device = None
                for device in s:
                    if device.name.lower() == device_choice.lower():
                        found_device = device
                        break
                if found_device:
                    amount = int(input(f"Enter the quantity of {found_device.name} you want to add to the cart: "))
                    Cart1.add_device(found_device, amount)
                else:
                    print("Device not found. Please try again.")
    elif choice == "2":
        print("__________________________________________________")
        print(Cart1.get_total_price())
        print(Cart1.print_items())
        print("__________________________________________________")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")