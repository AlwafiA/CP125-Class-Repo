def calc_discount(qty):
    if qty > 10 :
        discount = 0.15
    elif qty > 50:
        discount = 0.25
    else:
        discount = 0
    return discount , qty

def stock_available(qty, stock):

    if qty < stock:
        return True , stock
    else:
        return False , stock
    # return qty < stock
def total_price(price, qty, stock, discount):
    if stock_available(qty,stock) == True:
        total = price * qty * discount 
    else:
        total = 0
    return total

def display(price, total, stock, qty):
    print("Price :", price)
    print("Quantity :", qty)
    print("stock :", stock)
    print("Total :", total)

availabel = calc_discount(45)
stcok = stock_available(45,80)

