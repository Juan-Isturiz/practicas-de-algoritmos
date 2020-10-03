def calc():
    opt = input('\nWhat do you wanna calculate:\n1 Area of a triangle\n2 Area of a circle\n3 Area of a square or rectangle\n\n')
    if opt.isnumeric():
        print("\nThe numbers must be integers")
        if int(opt.strip()) == 1:
            figure = "triangle"
            base = input("\nWhat's the base of the triangle?:\n")
            h = input("\nWhat's the height of the triangle?:\n")
            if base.isnumeric() and h.isnumeric():
                area = (int(base) * int(h)) / 2 
            else:
                print ("\nWrong input" + 2*"\n" + "Base and height must be integer numbers\n")
        if int(opt.strip()) == 2:
            figure = "circle"
            h = input("\nWhat's the radius of the circle?:\n")
            if h.isnumeric():
                area = (int(h))** 2 * 3.14        
            else:
                print ("\nWrong input" + 2*"\n" + "radius must be a integer\n")
        if int(opt.strip()) == 3:
            base = input("\nWhat's the base of the square or rectangle?:\n")
            h = input("\nWhat's the height of the square or rectangle?:\n")
            if base.isnumeric() and h.isnumeric():
                area = (int(base) * int(h))
                if int(base) ==int(h):
                    figure = 'square'
                else:
                     figure = 'rectangle'  
            else:
                print ("\nWrong input" + 2*"\n" + "Base and height must be integer numbers\n")
        
        print(f"\nThe area of the {figure} is {area}")


    else:
        print("\nInvalid option, try again")




calc()