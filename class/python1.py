# 物件類別
# class my_first_class:
#     str = "hello"

#     def say(self):
#         print(self.str)
#         return
# obj1 =my_first_class()
# obj1.say()

# class thousand_dollar:
#     Value = 1000
#     Number = ""
#     Color = ""
#     # 初始建構子
#     def __init__(self, num = "AA00000001", color = "blue"):
#         self.Number = num
#         self.Color = color
    
#     def show_num(self):
#         print(self.Number +", color: " + self.Color)
#         return
# # 改變編號
# first_money=thousand_dollar("TS54070191")
# first_money.show_num()
# # 只用預設值
# second_money = thousand_dollar()
# second_money.show_num()
# # 改變編號及顏色
# third_money = thousand_dollar("TN59845627","red")
# third_money.show_num()
# # 改變顏色
# forth_money = thousand_dollar(color="green")
# forth_money.show_num()

class dollar:
    Value = 0
    Number = ""
    Color = ""

    def __init__(self, val = 0, num = "AA00000001", color = "blue"):
        self.Value = val
        self.Number = num
        self.Color = color

class thousandDollar(dollar):
    length = 0
    width = 0
    def __init__(self, val=0, num="AA00000001", color="blue", length = 0, width = 0):
        super().__init__(val, num, color)
        self.length = length
        self.width = width

    def show_num(self):
        print(str(self.Value) + ", " + self.Number + ", color: " + self.Color + ", length: "+ str(self.length) + ", width: " + str(self.width))
        return

first_money = thousandDollar(1000, "TN54070191")
first_money.show_num()