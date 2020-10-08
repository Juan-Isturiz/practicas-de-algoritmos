def ah_wey():
    n = input('\nInsert the max range:\n')
    pp = []
    if n.isnumeric():
        for i in range(int(n) + 1):
            if i % 5 == 0:
                pp.append(i)
        print('\n')
        print(pp)
    else:
        print('\nInvalid input, try again.\n')
