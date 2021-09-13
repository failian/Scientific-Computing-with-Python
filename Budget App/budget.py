class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        string = self.category.center(30, '*')
        tot_amount = 0
        for item in self.ledger:
            tot_amount += item['amount']
            string += '\n' + item['description'][0:23].ljust(23)
            string += format(item['amount'], '.2f').rjust(7)
        string += '\nTotal: ' + format(tot_amount, '.2f')
        return string

    def deposit(self, amount, description=''):
        self.ledger.append(
            {"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append(
                {"amount": amount * -1, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

    def transfer(self, amount, instance):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {instance.category}')
            instance.deposit(amount, f'Transfer from {self.category}')
            return True
        return False

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        return False


def create_spend_chart(categories):
    spent_list = []
    categories_list = []
    max_cat_len = 0

    for category in categories:
        max_cat_len = max(max_cat_len, len(category.category))
        categories_list.append(category.category)

        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += item["amount"] * -1
        spent_list.append(round(spent, 2))

    padded_cat_list = list(map(lambda x: x.ljust(max_cat_len), categories_list))
    total = sum(spent_list)
    percentage_list = []
    for amount in spent_list:
        percentage_list.append(int((((amount / total) * 10) // 1) * 10))
    print(percentage_list)

    string = 'Percentage spent by category\n'
    steps = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
    for step in steps:
        string += str(step).rjust(3) + '|'
        for percent in percentage_list:
            if percent >= step:
                string += " o "
            else:
                string += "   "
        string += " \n"

    string += "    " + "-" * ((3 * len(categories)) + 1) + "\n"

    for n in range(max_cat_len):
        string += '    '
        for cat in padded_cat_list:
            string += f' {cat[n]} '
        string += ' \n'
    return string.strip('\n')
