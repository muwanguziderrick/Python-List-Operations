def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    
    :param price: Original price of the item (float or int)
    :param discount_percent: Discount percentage (float or int)
    :return: Final price after applying the discount, or original price if discount < 20%
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(original_price, discount)
    print(f"Final price: {final_price}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")