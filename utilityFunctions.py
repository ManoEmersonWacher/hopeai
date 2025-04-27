class utilityFunctions():
        def Subfields():
            print("Sub-fields in AI are:")
            print("Machine Learning")
            print("Neural Networks")
            print("Vision")
            print("Robotics")
            print("Speech Processing")
            print("Natural Language Processing")

        def OddEven():
            numb = int(input("Enter a number:"))
            if((numb % 2) == 0):
                print(numb,"is Even number")
            else:
                print(numb,"is Odd number")

        def Eligible():
            gender = input("Enter your Gender:")
            age = int(input("Enter your Age:"))
            if(gender == 'Male'):
                if(age >=21 ):
                    print("ELIGIBLE")
                else:
                    print("NOT ELIGIBLE")
            elif(gender == 'Female'):
                if(age >=18 ):
                    print("ELIGIBLE")
                else:
                    print("NOT ELIGIBLE")

        def percentage():
            Subject1= int(input("Enter the mark of Subject1"))
            Subject2= int(input("Enter the mark of Subject1"))
            Subject3= int(input("Enter the mark of Subject1"))
            Subject4= int(input("Enter the mark of Subject1"))
            Subject5= int(input("Enter the mark of Subject1"))
            Total = Subject1+Subject2+Subject3+Subject4+Subject5
            Percentage = (Total/500)*100
            print("Subject1=",Subject1)
            print("Subject2=",Subject2)
            print("Subject3=",Subject3)
            print("Subject4=",Subject4)
            print("Subject5=",Subject5)
            print("Total : ",Total)
            print("Percentage : ",Percentage)

        def triangle():
            Height = int(input("Enter the Height:"))
            Breadth = int(input("Enter the Breadth:"))
            Area_triangle = (Height*Breadth)/2
            print("Area formula: (Height*Breadth)/2")
            print("Area of Triangle:",Area_triangle)
            Height1 = int(input("Enter the Height1:"))
            Height2 = int(input("Enter the Height2:"))
            Breadth = int(input("Enter the Breadth:"))
            Perimeter_triangle = Height1+Height2+Breadth
            print("Perimeter formula: Height1+Height2+Breadth")
            print("Perimeter of Triangle:",Perimeter_triangle)