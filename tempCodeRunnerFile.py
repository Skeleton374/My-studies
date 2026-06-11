valid = False

while valid == False:
    
    entered_data = input('Поиск по характеристике: ')
    
    if entered_data == 'light_pokemon':
        print(light_pokemon)
        valid = True
    elif entered_data == 'fire_pokemon':
        print(fire_pokemon)
        valid = True
    elif entered_data == 'legendary_heavy':
        print(legendary_heavy)
        valid = True
    elif entered_data == 'water_short':
        print(water_short)
        valid = True
    elif entered_data == 'not_bug':
        print(not_bug)
        valid = True
    else:
        print('Некорректные данные. Выберите из предложенного списка.')