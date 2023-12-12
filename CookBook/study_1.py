def c_k(cb):
    with open(cb, encoding=('utf-8')) as ck:
        cook_book = {}
        for menu in ck.read().split('\n\n'):
            name, len_, *ingredients = menu.split('\n')
            list_ = []
            for ingredient in ingredients:
                ingredient_name = ingredient.split(' | ')
                list_.append({'ingredient_name': ingredient_name[0], 'quantity': int(ingredient_name[1]), 'measure': ingredient_name[2]})
            cook_book[name] = list_
    return cook_book

# print(c_k('recipes.txt'))  # Для проверки

def get_shop_list_by_dishes(dishes, person_count):
    menu = {}
    for dishe in dishes:
        if dishe in c_k('recipes.txt').keys():
            for i in c_k('recipes.txt')[dishe]:
                if i['ingredient_name'] not in menu:
                    menu[i['ingredient_name']] = {'measure': i['measure'], 'quantity': i['quantity'] * person_count}
                else: # Учет повторяющегося ингредиента
                    for k in menu.values():
                        k['quantity'] += i['quantity'] * person_count   
        else:
            menu['Отсутствует/не существует'] = f'Такого блюда {dishe} нету'
    return menu

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)) # Есть в рецепте

print(get_shop_list_by_dishes(['Воробей', 'Омлет'], 2)) # Воробья нету в рецепте :(

