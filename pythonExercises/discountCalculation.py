def calculate_discount(amount, nbr_items, day):
    if nbr_items >= 5:
        if day == 'saturday' or 'sunday':
            discounted_price = amount - amount*0.25
        else :
            discounted_price = amount - amount*0.15
        return discounted_price

    elif nbr_items>0 :
        if day == 'saturday' or 'sunday':
            discounted_price = amount - amount*0.20
        else :
            discounted_price = amount - amount*0.1
        return discounted_price

price = float(input('enter the total amount'))
items = int(input('how many items do you have?'))
day = input('what day is it?')

new_price = calculate_discount(price, items, day.lower())
print(f"the price after discount is : {new_price}")
