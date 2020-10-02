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

#t = input('\nWich is the room temp?: ') 
#u = input('\nWich is the temp unit (K or F)?: ')
#convert(t,u)
import datetime
a = datetime.date.today().year
def sofa(name, lastna, age):
    nn = []
    ll = []
    for letter in name:
        nn.append(letter)
    for letter in lastna:
        ll.append(letter)
    lena = len(nn)
    lela = len(ll)
    print(f'your name is {lena} characters long')
    print(f'your name is {lela} characters long') 
    year = a - int(age)
    year2 = a - int(age)  - 1    
    print (f'You were born in {year} or {year2}')


#name = input('What is your name?: ')
#lastname = input('What is your lastname?: ')
#age = input('How old are you?: ')
#
#sofa (name, lastname, age)