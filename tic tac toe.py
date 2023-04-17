#  Проверка введёного значения
def f_check_input(v, size, field):
    v = v.lower()
    if v == 'stop':
        return 'stop'
    try:
        v = tuple(map(int, v.split(' ')))
        if 0 in v or len(v) != 2 or max(v) > size or field[v[0]][v[1]] != '-':
            position_valid = False
            print(f'Вы ввели неверные координаты: {v}')
            v = input(f'Уважаемый {user}, введите, адрес ячейки, \n'
                      f'или введите stop, если хотите остановить игру \n: ')
            return f_check_input(v, size, field)
    except:
        print(f'Вы ввели неверные координаты: {v}')
        v = input(f'Уважаемый {user}, введите, адрес ячейки, \n'
                  f'или введите stop, если хотите остановить игру \n: ')
        return f_check_input(v, size, field)
    return v


# Проверка победителя
def f_check_victory(array, field_size):
    for i in range(field_size):  # проверка Строк
        i += 1
        if '-' in array[i][1]:
            continue
        if all((array[i][1] == c or c == array[i][0]) for c in array[i]):  # генератор bool
            return array[i][1]  # Возваращает победителя

    for j in range(field_size):  # проверка Столбцов
        j += 1
        list = []
        if array[1][j] == '-':
            continue
        for i in range(field_size):
            i += 1
            list.append(array[1][j] == array[i][j])
        if all(list):
            print('Столбец!')
            return array[1][j]  # Возваращает победителя

    # Проверка диагоналей
    list_down = []
    list_up = []
    for i in range(field_size):  # Проверка диагоналей
        i += 1
        list_down.append(array[1][1] == array[i][i] and array[i][i] != '-')
        list_up.append(
            (array[1][(field_size)] == array[i][(field_size) - (i - 1)] and array[i][(field_size) - (i - 1)] != '-'))
    if (not '-' in list_down) and all(list_down):
        return array[1][1]  # Возваращает победителя
    if (not '-' in list_up) and all(list_up):
        return array[1][field_size]  # Возваращает победителя


# Граничные условия
size = 4
field_size = size - 1
field = [['-' for j in range(size)] for i in range(size)]
for i in range(size):
    field[i][0] = str(i)
    field[0][i] = str(i)
user = ''  # Gamer's name (X or 0)

# Не обновляется переменная {user} при вызове переменной txt_1!!! Почему?
# txt_1 = (f'Уважаемый {user}, введите, пожалуйста, \n'
#          f'адрес ячейки (номер строки и столбца через '
#          f'пробел),\nв которой Вы хотите поставить {user} \n: ')


# Game!1
for cell in range(field_size ** 2):
    # while '-' in field:
    # print(cell)
    position = None
    print(*field, sep='\n')
    if cell % 2 == 0:
        user = 'X'
    else:
        user = '0'
    incoming = input(f'Уважаемый {user}, введите, пожалуйста, \n'
                     f'адрес ячейки (номер строки и столбца через '
                     f'пробел),\nв которой Вы хотите поставить {user} \n: ')

    position = f_check_input(incoming, size, field)
    if position == 'stop':  # Проверка запроса на окончание игры
        print('Игра окончена!')
        break
    field[position[0]][position[1]] = user
    winner = f_check_victory(field, field_size)
    if winner:  # Проверка победителя
        print(*field, sep='\n')
        print(f'{winner}, вы победили!')
        print('Игра окончена!')
        break
    elif cell == field_size ** 2 - 1:
        print('Игра окончена! Победитель не выявлен!')
