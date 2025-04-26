class multipleFunctions():
    def OddEven():
        numb = int(input("Enter a number:"))
        if((numb % 2) == 0):
            print(numb,"is Even number")
        else:
            print(numb,"is Odd number")

    def BMI():
        weight = float(input("Enter the BMI Index:"))
        if(weight < 18.5):
            print("Underweight")
        elif((weight >= 18.5) and (weight <= 24.9)):
            print("Normal range")
        elif((weight >= 25.0) and (weight <= 29.9)):
            print("Overweight")
        else:
            print("Very Overweight")