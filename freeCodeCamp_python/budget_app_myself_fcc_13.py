'''
A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
When the budget object is printed it should display:

A title line of 30 characters where the name of the category is centered in a line of * characters.
A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
A line displaying the category total.
Here is an example usage:
'''
# food = Category("Food")
# food.deposit(1000, "deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# print(food)

'''
And here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96

Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

Percentage spent by category

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
'''

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0.00

    def __str__(self):
        new_line = '\n'
        centered_name = self.name.center(30, '*')
        initial_deposit_string = 'initial deposit'.ljust(23)
        initial_deposit_dictionary = self.ledger[0]
        total_balance = initial_deposit = initial_deposit_dictionary["amount"]
        result_for_print = centered_name + new_line + initial_deposit_string + str(initial_deposit).rjust(7) + new_line

        for line in self.ledger:
            if len(line["description"]) > 23:
                result_for_print += line["description"][:23]
            else:
                result_for_print += line["description"].ljust(23)
            
            result_for_print += str(line["amount"]).rjust(7) + new_line
            total_balance -= line["amount"]

        result_for_print += "Total: " + str(round(total_balance,2))
        return result_for_print
        
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        total_balance = (self.ledger[0])["amount"]
        for line in self.ledger:
            total_balance += line["amount"]

        return total_balance
        
    def transfer(self, amount, destination_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination_category.name}")
            destination_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True


def create_spend_chart(categories):
    final_result = 'Percentage spent by category'
    new_line = '\n'
    percents = []
    for category in categories:
        category_instance = Category(category)
        total_balance = (category_instance.ledger[0])["amount"]
        total_withdrawals = 0
        for line in category_instance:
            if line["amount"] < 0:
                total_withdrawals -= line["amount"]
        percents.append((total_withdrawals/total_balance)//10)
    
    for index_multipler in range(11):
        percent_number = 100 - index_multipler*10
        final_result += f'{percent_number}|'.rjust(4) + ' '
        
        for index in range(len(categories)):
            if percents[index] <= percent_number/10:
                final_result += "o  "
            else:
                final_result += "   "
        
    final_result += new_line + '    '
        
    for _ in range(3*len(categories) + 2):
        final_result += '-'

    final_result += new_line

    longest_category_name = len(max(categories, key=len))
    for index in range(longest_category_name):
        for category in categories:
            final_result += '     '
            if index < len(category): 
                final_result += category[index] + '  ' + new_line
            else:
                final_result += '   ' + new_line

food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)