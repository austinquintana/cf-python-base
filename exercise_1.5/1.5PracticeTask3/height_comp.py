class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches 


    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches "
        return output 
    
    def __gt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches 
        return height_inches_A > height_inches_B
    
    def __ge__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A >= height_inches_B

    def __ne__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A != height_inches_B
    
person_A_height = Height(4, 6)
person_B_height = Height(4, 5)
print("person_A_height > person_B_height: ", person_A_height > person_B_height)

person_A_height = Height(4, 5)
person_B_height = Height(4, 5)
print("person_A_height >= person_B_height: ", person_A_height >= person_B_height)

person_A_height = Height(5, 9)
person_B_height = Height(5, 10)
print("person_A_height != person_B_height: ", person_A_height != person_B_height)

height_1 = Height(4, 10)
height_2 = Height(5, 6)
height_3 = Height(7, 1)
height_4 = Height(5, 5)
height_5 = Height(6, 7)
height_6 = Height(5, 6)

heights = [height_1, height_2, height_3, height_4, height_5, height_6]

heights = sorted(heights)
for height in heights:
    print(height)

    

    