#  This program is designed to allow a company to assist their users with basic financial calculations based on our investments and loan repayments
#  using both simple and compound interest rates. The program will assist users in gaining a better understanding of their financial goals.

import math 


user_choice = input("""Welcome to our financial calculator program. \nPlease choose either 'investment' or 'bond' from the menu below to proceed
                    \n 1. Investment \t - to calculate the amount of interest you'll earn on interest. \n 2. Bond \t - to calculate the amount you'll have to pay on a home loan.\n""")

print("You have selected {}.".format(user_choice))
user_choice = user_choice.lower() #  Changing the users choice into lower case so the user will be able to type the input in caps or not and the code will still work

if user_choice == "investment": #The user has chosen investment calculations
    
    deposit = float(input("Please enter in the amount you wish to deposit ")) #  using a float for currency values & interest values. Capturing all required data.
    interest_invest_display = input("Please enter in the interest rate you will receive - please enter the number only ")
    interest_invest = float(interest_invest_display)/100 #  converting interest rate to a percentage for storage and mathematical purposes.
    period_invest = float(input("Please enter in the number of years you will invest with us for. "))
    interest = input("Will you be using Compound or Simple interest? ")
    interest = interest.lower() #  ensuring the code will continue even if the user has used caps or not.
    print("Thank you for filling everything in, just a moment. \n ")

    if interest == "simple": #  Calculating an investment using simple interest
        
        return_invest = (deposit*(1.0+interest_invest*period_invest)) #  Simple interest formulae
        return_invest = round(return_invest , 2 ) #  Rounding for currency purposes.
        print("Using simple interest, an investment amount of R{} for {} years at an interest rate of {}% will yield a return of R{}"
             .format(deposit, period_invest, interest_invest_display, return_invest)) #  carrying over the print line for ease of reading

    
    elif interest == "compound": #Calculating investment using compound interest
        
        return_invest = (deposit*math.pow((1+interest_invest),period_invest)) #  Compound interest formulae
        return_invest = round(return_invest , 2) #  Rounding for currency purposes.
        print("Using Compound interest, an investment of R{} for {} years at an interest rate of {}% will yield a return of R{}"
              .format(deposit, period_invest, interest_invest_display, return_invest)) #  Carrying over the print line for ease of reading

    else:
        print("You did not enter simple or compound for the interest rate type")

elif user_choice == "bond": #The user has chosen bond calculations
    
    present_value = float(input("Please enter in the value of the bond "))
    interest_bond_display = input("Please enter in the interest rate of the bond - numbers only ")
    interest_bond = float(interest_bond_display) /12 / 100 #Dividing annual interest rate by 12 for monthly rate. Dividing by 100 to store as a percent
    period_bond = float(input("Please enter in the number of months the bond will be repaid "))

    print(interest_bond)
    
    bond_payment = (interest_bond*present_value) / (1 - (1 + interest_bond)**(-period_bond)) #Calculating bond payments
    bond_payment = round(bond_payment, 2) #Rounding off to two decimal places
    
    print("With a bond value of R{} , an interest rate of {}% and a repayment term of {} months, your monthly bond repayment will be R{}"
          .format(present_value , interest_bond_display , period_bond , bond_payment))

else:
    print("You did not type 'Investment' or 'Bond'")
                
