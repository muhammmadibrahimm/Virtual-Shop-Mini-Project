general_shop = [{'item': 'flour','price': 120, 'inventory':200},
                    {'item': 'rice','price': 200, 'inventory':210},
                    {'item': 'sugar','price': 140, 'inventory':120},
                    {'item': 'lentils','price': 80, 'inventory':300},
                    {'item': 'ghee','price': 200, 'inventory':250},
                    {'item': 'eggs','price': 280, 'inventory':1000},
                    {'item': 'salt','price': 20, 'inventory':220},
                    {'item': 'oil','price': 440, 'inventory':25}]

def virtual_shop():
    cart = {}
    while True:
        item_name = input("What do you want? or press 'q' to exit")
        if item_name == "q":
            break
        else:
            for a in general_shop:
                if a['item']== item_name:
                    print(f"The Price of {item_name} is {a['price']}")
                    quantity = float(input("How much do you want?"))
                    if a['inventory'] >= quantity:
                        cart[item_name] = a['price'] * quantity
                        a['inventory']-= quantity
                    else:
                        print(f"{item_name} is not much enough in inventory")
    generate_bill(cart)

def generate_bill(cart):
    net = total(cart)
    tax = tax_apply(net)
    disc = discount(net)
    for item, price in cart.items():
        print(f"""
        {item} : {price}
        """)
        print(f"""
        Total Amount: {net}
        Applied Discount: {disc}
        Tax Apply: {tax}
        Amount Payable: {net + tax - disc}
        """)

def discount(total_amount):
    if total_amount >= 10000:
        disc = total_amount*.5
    elif total_amount >= 5000:
        disc = total_amount*.2
    elif total_amount >= 1000:
        disc = total_amount*.1
    else:
        disc = total_amount*0
    return disc    

def tax_apply(total_amount):
    if total_amount >= 10000:
        tax = total_amount*.5
    elif total_amount >= 5000:
        tax = total_amount*.3
    elif total_amount >= 1000:
        tax = total_amount*.2
    else:
        tax = total_amount*0
    return tax

def total(cart):
    total_amount = sum(cart.values())
    return total_amount

virtual_shop()
