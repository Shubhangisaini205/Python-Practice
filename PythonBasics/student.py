class Student:

    def __init__(self,name,age,marks,isPresent):
        self.name=name
        self.age= age
        self.marks = marks
        self.isPresent = isPresent

    def on_honor_roll(self):
        if self.marks >= 600:
            return True
        else:
            return False