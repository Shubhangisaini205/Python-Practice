from Chef import Chef
 #  inheriting the function of Chef Class here ny using class ChineseChef(Chef):
class ChineseChef(Chef):
    def make_FriedRice(self):
        print("The Chef makes fried Rice")

    def make_Burger(self): # this is overwriting the makeburger for simple chef
      print("The chef makes a non-veg Berger")