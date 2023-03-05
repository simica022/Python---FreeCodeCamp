class Category:

    def __repr__(self):
        return "Category()"
    def __str__(self):
        s = self.category.center(30, "*") + "\n"
        for _, (key, val) in enumerate(self.transactions.items()):
            # temp = "{0.ljust(23)[:23]}, {1:.2f}.rjust(7)".format(key, val)
            val = "{0:.2f}".format(val)
            temp = f"{key.ljust(23)[:23]}{str(val).rjust(7)}"
            s += temp + "\n"
        return s

    """Tracks budget persoanl budget spending"""
    def __init__(self, category):
        self.category = category
        self.transactions = dict()

    def deposit(self, amonut, name):
        """Tracks money added"""
        if name not in self.transactions:
            self.transactions[name] = 0
        self.transactions[name] = self.transactions[name] + amonut 

    def withdraw(self, amount, name ="No category"):
        """Tracks spending"""
        if name not in self.transactions:
            self.transactions[name] = 0
        self.transactions[name] = self.transactions[name] + amount * (-1)
    
    def get_balance(self):
        """Returns diff between total deposit and costs"""
        return sum(self.transactions.values())
    
    def transfer(self, amount, cls_name):
        '''Transfers money between classes'''
        if f"Transfer to {cls_name.category}" not in self.transactions:
            self.transactions[f"Transfer to {cls_name.category}"] = 0
        self.transactions[f"Transfer to {cls_name.category}"] = self.transactions[f"Transfer to {cls_name.category}"] + amount * (-1)
        cls_name.deposit(amount, f"Transfer from {self.category}")



def create_spend_chart(categories):

    spend = []
    for cat in categories:
        temp = 0
        for val in cat.transactions.values():
            if val < 0:
                temp += abs(val)
        spend.append(temp)

    total = sum(spend)
    percentage = [i/total * 100 for i in spend]

    s = "Percentage spent by category"
    for i in range(100, -1, -10):
        s += "\n" + str(i).rjust(3) + "|"
        for j in percentage:
            if j > i:
                s += " o "
            else:
                s += "   "
    # Spaces
        s += " "
    s += "\n    ----------"

    cat_length = []
    for category in categories:
        cat_length.append(len(category.category))
    max_length = max(cat_length)

    for i in range(max_length):
        s += "\n    "
        for j in range(len(categories)):
            if i < cat_length[j]:
                s += " " + categories[j].category[i] + " "
            else:
                s += "   "
    # Spaces
    s += " "

    return s
