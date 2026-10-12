'''
Algorithm:
1. Receive product details, quantity, package size, price, discount rate, and tax rate from the user.
2. Calculate the total amount, discount, amount after discount, tax, and final payable amount.
3. Use floor division (//) to calculate the number of complete packages and modulo (%) to calculate the remaining individual items.
4. Format monetary values to two decimal places and display the sales invoice.

Example Input:
Product Name: Chocolate
Product Quantity: 23
Product Quantity In Package: 7
Product Price: 10
Discount Rate: 10
Tax Rate: 9

Example Output:
***************Sales Invoice***************
>>>>>>> Product Name:                Chocolate
>>>>>>> Product Quantity:            23
>>>>>>> Product Quantity In Package: 7
>>>>>>> Product Price:               10.00
*******************************************
          You purchased 3 pack and 2 items
                TotalAmount:         230.00
*******************************************
>>>>>>> Discount Rate:               10%
>>>>>>> Discount Amount:             23.00
*******************************************
          Amount after discount:     207.00
*******************************************
>>>>>>> Tax Rate:                    9%
>>>>>>> Tax Amount:                  18.63
*******************************************
>>>>>>> Amount payable after tax:  225.63
*******************************************
'''

#(Start) Receiving input from the user and assigning values ​​to variables 
ProductName = input("Product Name: ").strip().title()
ProductQuantity = int(input("Product Quantity: "))
ProductQuantityInPackage = int(input("Product Quantity In Package: "))
ProductPrice = float(input("Product Price: "))
DiscountRate = int(input("Discount Rate: "))
TaxRate = int(input("Tax Rate: "))
#(End) Receiving input from the user and assigning values ​​to variables

#(Start)Preliminary calculations
TotalAmount = ProductQuantity * ProductPrice
DiscountAmount = (TotalAmount * DiscountRate) / 100
AmountAfterDiscount = TotalAmount - DiscountAmount
TaxAmount = (AmountAfterDiscount * TaxRate) / 100 
AmountAfterTax = AmountAfterDiscount + TaxAmount
NumberOfCompletePackages = ProductQuantity // ProductQuantityInPackage
QuantityInPackage = ProductQuantity % ProductQuantityInPackage 
#(End)Preliminary calculations

#(Start)Preparing the output
FinalOutput = f'''
***************Sales Invoice***************
>>>>>>> Product Name:                {ProductName}
>>>>>>> Product Quantity:            {ProductQuantity}
>>>>>>> Product Quantity In Package: {ProductQuantityInPackage}
>>>>>>> Product Price:               {ProductPrice:.2f}
*******************************************
          You purchased {NumberOfCompletePackages} pack and {QuantityInPackage} items
            Total Amount:         {TotalAmount:.2f}
*******************************************
>>>>>>> Discount Rate:               {DiscountRate}%
>>>>>>> Discount Amount:             {DiscountAmount:.2f}
*******************************************
          Amount after discount:     {AmountAfterDiscount:.2f}
*******************************************
>>>>>>> Tax Rate:                    {TaxRate}%
>>>>>>> Tax Amount:                  {TaxAmount:.2f}
*******************************************
          Amount payable after tax:  {AmountAfterTax:.2f}
*******************************************
'''
#(End)Preparing the output

#(Start)Show output
print(FinalOutput)
#(End)Show output