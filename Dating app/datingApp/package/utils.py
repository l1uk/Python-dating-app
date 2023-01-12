class Utils(object):
    @staticmethod
    def integerInput(min, max):
        choice = -1
        while(choice < min or choice > max):
            try:
                choice = int(input("Your choice: "))
            except ValueError:
                print("Invalid input")
            if choice < min or choice > max:
                print("Choice out of range")
        return choice