import math
import random


def switch_player(name1,name2):
    while True:
        yield name1
        yield name2

print('приглашаем сыграть в игру "конфеты"')
print('нажмите 1 если хотите играть с человеком ')
print('нажмите 2 если будете играть с роботом новичком')
print('нажмите 3 если будете играть с роботом опытным')
print('нажмите 4 если будете играть с роботом мастером')

player_spice = input('ваш выбор: ')
print('на столе 221 конфета, за один раз по очереди можно взять от 1 до 28 конфет')
print('играют двое, побеждает тот, кто забрал последнюю партию конфет.')
if player_spice == '1':
    name1 = input('игрок номер один, введите имя: ')
    name2 = input('игрок номер два, введите имя: ')
    now_player = switch_player(name1, name2)
    candle_amount = 221
    while candle_amount > 0:
        turn_player = next(now_player)
        candle_take = int(input(f'{turn_player} возьмите от 0 до 28 конфет: '))
        if 0 < candle_take < 29:
            candle_amount = candle_amount - candle_take
            if candle_amount <= 0: break
        else:
            print('вы ввели неправильное число, ход переходит к другому игроку')
        print(f'осталось {candle_amount} конфет')
    print(f'победил {turn_player}')
if player_spice == '2':
    name1 = input('человек, введите имя: ')
    now_player = switch_player(name1, 'бот')
    candle_amount = 221
    while candle_amount > 0:
        turn_player = next(now_player)
        if turn_player == name1:
            candle_take = int(input(f'{turn_player} возьмите от 0 до 28 конфет: '))
            if 0 < candle_take < 29:
                candle_amount = candle_amount - candle_take
            else:
                print('вы ввели неправильное число, ход переходит к другому игроку')
        if turn_player == 'бот':
            if candle_amount < 29:
                candle_take = random.randint(0, candle_amount)
                candle_amount = candle_amount - candle_take
                print(f'бот взял {candle_take} конфет, осталось {candle_amount}')
            else:
                candle_take = random.randint(0, 29)
                candle_amount = candle_amount - candle_take
                print(f'бот взял {candle_take} конфет, осталось {candle_amount}')
    print(f'победил {turn_player}')
if player_spice == '3':
    name1 = input('человек, введите имя: ')
    now_player = switch_player(name1, 'бот')
    candle_amount = 221
    while candle_amount > 0:
        turn_player = next(now_player)
        if turn_player == name1:
            candle_take = int(input(f'{turn_player} возьмите от 0 до 28 конфет: '))
            if 0 < candle_take < 29:
                candle_amount = candle_amount - candle_take
            else:
                print('вы ввели неправильное число, ход переходит к другому игроку')
        if turn_player == 'бот':
            if candle_amount < 29:
                candle_take = candle_amount
                candle_amount = candle_amount - candle_take
                print(f'бот взял {candle_take} конфет, вы проиграли')
                break
            if 30 < candle_amount < 57:
                candle_take = candle_amount - 29
                candle_amount = candle_amount - candle_take
                print(f'бот взял {candle_take} конфет, осталось {candle_amount}')
            else:
                candle_take = random.randint(0,29)
                candle_amount = candle_amount - candle_take
                print(f'бот взял {candle_take} конфет, осталось {candle_amount}')
    print(f'победил {turn_player}')
if player_spice == '4':
    name1 = input('человек, введите имя: ')
    now_player = switch_player(name1, 'бот')
    candle_amount = 221
    count = 0
    while candle_amount > 0:
        turn_player = next(now_player)
        if turn_player == name1:
            candle_take_man = int(input(f'{turn_player} возьмите от 0 до 28 конфет: '))
            if 0 < candle_take_man < 29:
                candle_amount = candle_amount - candle_take_man
            else:
                print('вы ввели неправильное число, ход переходит к другому игроку')
        if turn_player == 'бот':
            if candle_amount < 29:
                candle_take = candle_amount
                candle_amount = candle_amount - candle_take
                print(f'бот взял {candle_take} конфет, вы проиграли')
                break
            elif 30 <= candle_amount <= 57:
                candle_take = candle_amount - 29
                candle_amount = candle_amount - candle_take
                print(f'бот взял {candle_take} конфет, осталось {candle_amount}')
            elif candle_amount > 57 and count == 1 and candle_take_man < 18:
                candle_take = 18 - candle_take_man
                candle_amount = candle_amount - candle_take
                print(f'бот взял {candle_take} конфет, осталось {candle_amount}')
            elif candle_amount > 57 and count == 1 and candle_take_man > 18:
                candle_take = 47 - candle_take_man
                candle_amount = candle_amount - candle_take
                print(f'бот взял {candle_take} конфет, осталось {candle_amount}')
            elif candle_amount > 57 and count > 1:
                candle_take = 29 - candle_take_man
                candle_amount = candle_amount - candle_take
                print(f'бот взял {candle_take} конфет, осталось {candle_amount}')
            else:
                candle_take = random.randint(0, 29)
                candle_amount = candle_amount - candle_take
                print(f'бот взял {candle_take} конфет, осталось {candle_amount}')
        count += 1
    print(f'победил {turn_player}')
    print(count)





