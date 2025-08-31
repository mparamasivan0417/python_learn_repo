print(f'Available Items are breakfast: Idly, Vadai, Dosai, Pongal, Coffee')
menu = {'Idly': 10, 'Vadai': 10, 'Dosai': 20, 'Pongal': 30, 'coffee':15}
tot = 0
while True:
    ite = input('please enter your item:').strip()
    if ite == '':
        break
    if ite in menu:
        tot += menu[ite]
        print(f'you enetered {ite} and total is {tot}')
    else:
        print('Entered item is not available')