##C°-F°-°K converter
def convert(temp,unit):
    if temp.isnumeric():
        temp = float(temp)
 
        if unit.lower().strip(' ') == "k":
         
            temp -= 273.15
            print(f'\nThe Temperature is {temp}C°')
            
        
        elif unit.lower().strip(' ') == "f":
    
            temp = (temp - 32) * 5/9
            print(f'\nThe Temperature is {ftemp}C°')
            
        
    else:
        print ('\nWrong input, try again')

t = input('\nWich is the room temp?: ') 
u = input('\nWich is the temp unit (K or F)?: ')

convert(t,u)
            
