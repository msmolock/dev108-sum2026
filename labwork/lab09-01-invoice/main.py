#!/usr/bin/env python3
# Michael Smolock
# August 8, 2026
# Dev 108
# Exercise 9-1: Invoice program with shipping cost and locale currency formatting


import locale as lc

from decimal import Decimal
from decimal import ROUND_HALF_UP

# display a title
print("The Invoice program")
print()

choice = "y"
while choice == "y":
    
    # get the user entry
    order_total = Decimal(input("Enter order total: "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()               

    # determine the discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate the results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)                                
    subtotal = order_total - discount

    # Calculate shipping cost (8.5% of subtotal)
    shipping_percent = Decimal(".085")
    shipping_cost = subtotal * shipping_percent
    shipping_cost = shipping_cost.quantize(Decimal("1.00"), ROUND_HALF_UP)

    # Calculate sales tax (5% of subtotal)
    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)                                 
    invoice_total = subtotal + shipping_cost + sales_tax

    # Set locale for currency formatting 
    lc.setlocale(lc.LC_ALL, 'en_US.UTF-8 ')


    # Format order total and invoice total with $
    order_total = lc.currency(order_total, grouping=True)
    invoice_total = lc.currency(invoice_total, grouping=True)

    # display the formatted results
    print(f"Order total:        {order_total:>10}")
    print(f"Discount amount:    {discount:10,}")
    print(f"Subtotal:           {subtotal:10,}")
    print(f"Shipping Costs:     {shipping_cost:10,}")
    print(f"Sales tax:          {sales_tax:10,}")
    print(f"Invoice total:      {invoice_total:>10}")
    print()

    choice = input("Continue? (y/n): ")    
    print()
    
print("Bye!")