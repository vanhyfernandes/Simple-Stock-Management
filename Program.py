class Stock:
    def __init__(self, name, initial_level): 
        self.name = name
        self.quantity_on_hand = initial_level 
    
    def print_summary (self):
        print("%s: %d" % (self.name, self.quantity_on_hand))

    def add_stock(self, quantityAdded):
        self.quantity_on_hand = self.quantity_on_hand + quantityAdded
    
    def remove_stock(self, quantityRemoved):
        if quantityRemoved > self.quantity_on_hand:
            print("FAILED - quantity on hand: %d" % self.quantity_on_hand)
        else:
            self.quantity_on_hand = self.quantity_on_hand - quantityRemoved

test1 = Stock("Test Stock", 100) 
test1.print_summary()
test2 = Stock("Another Item", 10) 
test2.print_summary()
line = 0

def total_summary():
    print("---- Summary ----")
    test1.print_summary()
    test2.print_summary()

def add_stock():
    line = 0

    print("1 - %s" % test1.name)
    print("2 - %s" % test2.name)

    while line != 1 and line != 2:
        line = input("Select an option: ") 
        num = int(line)
    
    total_summary()
    line = input("quantity to add: ") 
    qtd = int(line)

    if num == 1:
        test1.print_summary()
        test1.add_stock(qtd)
    
    if num == 2:
        test2.print_summary()
        test2.add_stock(qtd)
    
    total_summary()

    
def remove_stock():
    line = 0

    print("1 - %s" % test1.name)
    print("2 - %s" % test2.name)

    while line != 1 and line != 2:
        line = input("Select an option: ") 
        num = int(line)
    
    total_summary()
    line = input("quantity to remove: ") 
    qtd = int(line)
    if num == 1:
        test1.print_summary()
        test1.remove_stock(qtd)
    
    if num == 2:
        test2.print_summary()
        test2.remove_stock(qtd)

    total_summary()

while line != 1 and line != 2 and line != 3:
    print("1 - Add stock")
    print("2 - Remove stock")
    print("3 - Print Summary")
    line = input("Select an option: ") 
    num = int(line)
if num == 1:
    add_stock()
if num == 2:
    remove_stock()
if num == 3:
    total_summary()

