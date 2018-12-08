print('Привет! Мы рады тебя видеть в нашей столовой "Голодный студент"!')
print('Ознакомься с нашим ассортиментом еды и введи желаемое блюдо для заказа. '
      'К сожалению, не все блюда доступны именно сегодня.')
print('Меню\n гречка\n тефтели \n компот \n суп \n котлеты\n'
      ' омлет \n каша \n борщ\n булочка\n '
      'бутерброд \n хлеб\n какао\n чай \n сок ')
order = input('Введи свой заказ(через пробел): ')
order = order.split()

with open('menu.txt') as f_in:
    menu = f_in.readlines()
i = 0
while i < len(menu):
    menu[i] = menu[i].rstrip('\n')
    i += 1

for i in range(len(order)):
    if order[i] in menu:
        with open('price.txt') as p_in:
            price = p_in.readlines()
        p = 0
        while p < len(price):
            price[p] = price[p].rstrip('\n')
            p += 1

        cost = 0
        for i in range(len(order)):
            for p in range(len(price)):
                if order[i] in price[p]:
                    a = price[p]
                    cost += int(a[a.find('-')+2:])
    else:
        print('Сегодня в нашем меню отсутствует', order[i])
        del order[i]
        break
print('Вы заказали:', ' '.join(order))
print('Сумма заказа:', cost, 'рублей')