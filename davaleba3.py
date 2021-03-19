

class Calculator:
    

    def addition(self):
        self.x = x
        self.y = y
        return x + y

    def subtraction(self):
        self.x = x
        self.y = y
        return x - y

    def multiplication(self):
        self.x = x
        self.y = y
        return x * y

    def dividing(self):
        self.x = x
        self.y = y

        if (y == 0):
            a = "ნულზე გაყოფა არ შეიძლება"  
        else:
            a = self.x / self.y

        return a


x = int(input("შეიყვანეთ რიცხვი:"))
y = int(input("შეიყვანეთ რიცხვი:"))

p1 = Calculator()

choice = 1
while choice != 0:
    print("აირჩიეთ მოქმედება!:")
    print("0. უკან")
    print("1. Mimateba")
    print("2. Gamokleba")
    print("3. Gamrvleba")
    print("4. Gakopa")
    choice = int(input("აირჩიეთ მოქმედება:"))
    if choice == 1:
        print(p1.addition())
    elif choice == 2:
        print(p1.subtraction())
    elif choice == 3:
        print(p1.multiplication())
    elif choice == 4:
        print(p1.dividing())
else:
  print("თქვენ დაბრუნდით უკან!")                  


   