def calculate_discount(price, dicount_percent):
    #Apply discountv only if it's 20% or more
    if discount_percent >= 20:
        discount_amount = (dicount_percent / 100) * price
        final_price = price - discount_amount
        return round(final_price, 2) # rounds to 2 decimal places
    else:
        return round(price, 2)
#prompt for input
price = float(input("Enter the original price:")) 
discount_percent = float(input("Enter the dicount percentage:"))
#calling the function
final_price = calculate_discount(price, discount_percent)
#print result
if discount_percent >= 20:
    print(f"The final price after {discount_percent}% discount is: {final_price}")
else:
    print(f"No discount applied. The price remains: {final_price}")