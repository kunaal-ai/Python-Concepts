stock_dic = {"apple": "159", "amazon": "1200"}


class Alpha:
    def __init__(self, c_name):
        self.c_name = c_name

    def get_price(self):
        for i, j in stock_dic.items():
            if i == self.c_name:
                return j


hol = {"apple": 17}
class Portfolio(Alpha):
    def __init__(self, c_name):
        super().__init__(c_name)

    def my_holdings(self):
        for i, j in hol.items():
            if i == self.c_name:
                return j

    def total_value(self):
        price = self.get_price()
        units = self.my_holdings()
        return int(price) * int(units)  # type: ignore


obj = Portfolio("apple")
print(obj.total_value())
