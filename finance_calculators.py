import math

#ask the user to choose which plan they want to go for 
print("investment - to calculate the amount of interest you'll earn on your investment \nbond - to calculate the amount you'll have to pay on a home loan")
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")



#making sure the lower or upper case doesnt make the algorithm bug prompt the user for the other variable that are needed to calculate the investment plan when chosen
if user_choice.lower() == "investment":
    deposit = int(input("Enter how much do you want to deposit: "))
    interest_rate = int(input("Enter without '%' the interest rate: "))
    year_plan = int(input("Enter how long in years you plan on investing: "))
    interest_plan = input("Please enter the type of interest you want, either 'simple' or 'compound': ")

    #second if elif statement for the two different types of investment calculate accordingly to the chosen plan 
    if interest_plan.lower() == "simple":
        total_interest_simple = deposit * (1 + ((interest_rate/100) * year_plan ))

        print(f" after {year_plan} years with an interest of {interest_rate}% and depositing £{deposit} the total will be: £", total_interest_simple)

    elif interest_plan.lower() == "compound":
        total_interest_compound = deposit * math.pow((1 + (interest_rate/100)), year_plan)

        print(f" after {year_plan} years with an interest of {interest_rate}% and depositing £{deposit} the total will be: £", total_interest_compound)



#prompt the user for the variables needed to calculate the bond when chosen 
elif user_choice.lower() == "bond":
    house_value = int(input("Please enter the current value of the house: "))
    interest_rate = int(input("Please enter the interest rate without the '%' symbol: "))
    month_plan = int(input("Please enter the amount of months you plan on to repay the bond: "))
    total_monthly_repayment = (((interest_rate/100)/12) * house_value) / (1 - (1 + ((interest_rate/100)/12)) ** (- month_plan))

    print(f"Wtih the house value being £ {house_value} and an interest rate of {interest_rate}% during {month_plan} months you will have to pay £", total_monthly_repayment, " each months.")


#make sure to print an error message when the user inputs something else that investment or bond 
else:
    print("Please enter a correct answer.")