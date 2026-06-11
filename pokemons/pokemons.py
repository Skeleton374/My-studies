import pandas as pd

df = pd.read_csv('pokemon.csv')

valid = False

while valid == False:
    print('''Введите характеристику из предложенных, которую хотите узнать.
легкие покемоны — покемоны с весом меньше 10 кг
огненные покемоны — покемоны с типом равным "Fire"
легендарные покемоны — легендарные покемоны с весом больше 100 кг
водяные покемоны — водяные покемоны с ростом меньше 1 метра
покемоны без багов — покемоны, у которых НЕ первый тип "Bug"''')

    entered_data = input('Поиск по характеристике: ')

    light_pokemon = df[df['Weight'] <= 10]
    fire_pokemon = df[df['Type1'] == 'Fire']
    legendary_heavy = df[(df['Legendary'] == 1) & (df['Weight'] >= 100)]
    water_short = df[(df['Type1'] == 'Water') & (df['Height'] <= 1)]
    not_bug = df[df['Type1'] != 'Bug']
    
    if entered_data == 'легкие покемоны':
        print(light_pokemon.to_string())
        valid = True
    elif entered_data == 'огненные покемоны':
        print(fire_pokemon.to_string())
        valid = True
    elif entered_data == 'легендарные покемоны':
        print(legendary_heavy.to_string())
        valid = True
    elif entered_data == 'водяные покемоны':
        print(water_short.to_string())
        valid = True
    elif entered_data == 'покемоны без багов':
        print(not_bug.to_string())
        valid = True
    else:
        print('Некорректные данные. Выберите из предложенного списка.')

    
# отфильтрованные_данные = df[df['Название_столбца'] >= число]