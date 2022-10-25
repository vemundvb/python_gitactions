class Two:
    def __init__(self, number):
        self.number = number

    def number_is_two(self):
        if (self.number == 2):
            return True
        else:
            return False

    def return_number(self):
        print("here: " + self.number)
        return self.number
    


