# Name: Hasani Killiebrew
# Prog Purpose: This program finds Price for one ticket: $10.99
#   Sales tax rate: 5.5%

import datetime

##############  define global variables ############
# define tax rate and prices
SALES_TAX_RATE = .055
PR_S_PIZZA = 9.99
PR_M_PIZZA = 12.99
PR_L_PIZZA = 14.99
PR_XL_PIZZA = 17.99

# define global variables
num_pizzas = 0
subtotal = 0
sales_tax = 0
total = 0

##############  define program functions ################
def main():
    another_pizza = True
    while another_pizza:
     get_user_data()
     perform_calculations()
     display_results()
     yesno = input("\nWould you like to order another pizza? (Y/N):  ")
    if yesno. upper() != "Y":
        another_pizza = False

def get_user_data():
    global num_pizzas, pizza_size
    num_pizzas = int(input("Number of Pizzas: "))
    pizza_size = int(input("What size (5=S, 6=M, 7=L, 8=XL):  "))

    

        
def perform_calculations():
    global subtotal, sales_tax, pizza_size, num_pizzas, PR_S_PIZZA, PR_M_PIZZA, PR_L_PIZZA, PR_XL_PIZZA, total
    subtotal = num_pizzas * pizza_size
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax


if input == 5:
        subtotal = num_pizzas * PR_S_PIZZA

if input == 6:
        subtotal = num_pizzas * PR_M_PIZZA

if input == 7:
        subtotal = num_pizzas * PR_L_PIZZA

if input == 8:
        subtotal = num_pizzas * PR_XL_PIZZA

    
        

def display_results():
    print('------------------------------')
    print('**** PIZZA HOUSE  ****')
    print('Your neighborhood pizza house')
    print('------------------------------')
    print('Number of Pizzas: ' + format(num_pizzas))
    print('Subtotal      $ ' + format(subtotal,'8,.1f'))
    print('Sales Tax    $ ' + format(sales_tax,'8,.2f'))
    print('Total        $ ' + format(total,'8,.2f'))
    print('-------------------------------')
    print('Thank you, come again!')
    print(str(datetime.datetime.now()))

##########  call on main program to excute ###########
main()
