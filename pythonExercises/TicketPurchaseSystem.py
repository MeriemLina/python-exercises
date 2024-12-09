def ticket_checking(name):
    if name == 'VIP':
        print(f"enjoy the show for free!")
    else:
        calculate_price()

def calculate_price():
    nbr_tickets = int(input('how many tickets would you like to buy?'))
    price = nbr_tickets * 15.50
    print(f"the total cost is : {price}")
    print('enjoy the show!')

ticket_checking(input('enter your name'))
