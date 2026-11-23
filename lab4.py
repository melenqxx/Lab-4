from itertools import combinations  # нужна чтобы перебирать все наборы предметов

ITEMS = {  # словарь предметов,  назваание размер очки
    'r': ('Винтовка', 3, 25),
    'p': ('Пистолет', 2, 15),
    'a': ('Боекомплект', 2, 15),
    'm': ('Аптечка', 2, 20),
    'i': ('Ингалятор', 1, 5),
    'k': ('Нож', 1, 15),
    'x': ('Топор', 3, 20),
    't': ('Оберег', 1, 25),
    'f': ('Фляжка', 1, 15),
    'd': ('Антидот', 1, 10),
    's': ('Еда', 2, 20),
    'c': ('Арбалет', 2, 20),
}
TOTAL = sum(v[2] for v in ITEMS.values())  # сумма очков всех предметов

ROWS, COLS = 3, 3  
START = 10  
MUST = 'i'  # обязательный ингалятор 


def score(chosen):  # итоговые очки для набора
    taken = sum(ITEMS[k][2] for k in chosen)  # очки взятых предметов
    return START + taken - (TOTAL - taken)  # старт плюс взятые минус оставленные


def find_all(cap):  
    result = [] # спикок в который буду складывать все подходящие наборы
    for n in range(1, len(ITEMS) + 1):  # размер набора
        for combo in combinations(ITEMS, n):  # все наборы такого размера
            size = sum(ITEMS[k][1] for k in combo)  # сколько ячеек занимают
            if MUST in combo and size <= cap and score(combo) > 0:  # подходит ли набор
                result.append(combo) # ??
    return result


def show(chosen):  # рис инвентарь
    cells = []  # список клеток по порядку
    for k in chosen:
        cells += [k] * ITEMS[k][1]  # строка что бы занять нужное колво ячеек
    cells += [' '] * (ROWS * COLS - len(cells))  # пустые клетки в конце
    for i in range(0, len(cells), COLS):  # режем на строки по COLS штук
        print(','.join(f'[{c}]' for c in cells[i:i + COLS]))
    print('Итоговые очки выживания:', score(chosen))


all_sets = find_all(ROWS * COLS)  # все хорошие наборы для 3 на 3
best = max(all_sets, key=score)  # набор с максимальными очками
print('Лучший набор:', ', '.join(ITEMS[k][0] for k in best))
show(best)

print('\nДоп, 7 ячеек:')
if find_all(7):  # есть ли хоть один хороший набор
    print('Решение есть')
else:
    print('Решения нет, ни один набор не дает положительный счет')

print('\nВсе комбинации с положительным счетом:', len(all_sets))
for c in sorted(all_sets, key=score, reverse=True):  # сначала самые сильные
    print(''.join(c), 'очки =', score(c))
