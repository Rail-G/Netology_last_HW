

def calculate_salary():
    salar = int(input('Введите желаемую зарплату: '))
    kids = int(input('Введите количество детей: '))
    tax1 = salar * 0.13
    tax2 = salar * 0.30
    tax3 = salar * 0.1
    if kids == 1:
        tax4 = salar * 0.25
    elif kids == 2:
        tax4 = salar * 0.33
    elif kids > 2:
        tax4 = salar * 0.5
    else: 
        tax4 = 0
    res_salar = salar - tax1 - tax2 - tax3 - tax4 
    if res_salar < 0:
        return 'Ваша зарплата: {:.2f}, НДФЛ: {:.2f}, Страховые взносы: {}, Штраф за опоздание {}, Алименты: {:.2f}. Не порядок, вы нам еще и должны >:D'.format(res_salar, tax1, tax2, tax3, tax4)
    return 'Ваша зарплата: {:.2f}, НДФЛ: {:.2f}, Страховые взносы: {}, Штраф за опоздание {}, Алименты: {:.2f}'.format(res_salar, tax1, tax2, tax3, tax4)

if __name__ == '__main__':
    print(calculate_salary())