class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        # A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        print(amount)
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output

def create_spend_chart(categories):
    category_names = []
    spent = []
    spent_percentages = []

    for category in categories:
        total_spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total_spent -= item['amount']
        spent.append(round(total_spent, 2))
        category_names.append(category.name)

    for amount in spent:
        spent_percentages.append(round(amount / sum(spent), 2) * 100)

    graph = "Percentage spent by category\n"
    labels = range(100, -10, -10)

    for label in labels:
        graph += str(label).rjust(3) + "| "
        for percent in spent_percentages:
            if percent >= label:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"

    graph += "    " + "-" * (len(category_names) * 3 + 1) + "\n     "

    longest_name_length = max([len(name) for name in category_names])

    for i in range(longest_name_length):
        for name in category_names:
            if len(name) > i:
                graph += name[i] + "  "
            else:
                graph += "   "
        if i < longest_name_length - 1:
            graph += "\n     "

    return graph

