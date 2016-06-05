######################
#######BudgetPy#######
##Author: Laurens N.##
######################

##Variables
balance = 0
currency = "€"
x = 1

##Commands
while x == 1:
    inp = input("")
    if inp == "help":
        print ("""\
Usage: [COMMAND] [OPTIONS] [VALUES]
                balance -- Shows the Budget Balance.
            setcurrency -- Asks for the Currency that should be usend in BudgetPy.
         income [VALUE] -- Adds the given Amount of Money to the Budget.
          outgo [VALUE] -- Removes the given Amount of Money from the Budget.
          """)
    elif inp == "balance":
        print ("The current Balance is: ", + balance)
    elif inp == "setcurrency":
        print("Current supported Currencies are: € and $")
        currencyinp = input("Enter your new Currency: ")
            if currencyinp == "€":
                currency = "€"
                print ("Currency has been set to € !")
            elif currencyinp == "$":
                currency = "$"
                print ("Currency has been set to $ !")
        
