class RussiaError(Exception):
    def __str__(self):
        return f"With such money people can not live in abundance!"
def check_money(amount_of_money, limit_value):
        if amount_of_money> limit_value:
            return "anough money"
        else:
            raise RussiaError(amount_of_money)
money=0
check_money(money, 5000)




