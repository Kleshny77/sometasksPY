warehouse_lenth = int(input('длина склада = '))
warehouse_high = int(input('высота склада = '))
warehouse_width = int(input('ширина склада = '))
box_lenth = int(input('длина коробки с ноутбуком = '))
box_high = int(input('высота коробки с ноутбуком = '))
box_width = int(input('ширина коробки с ноутбуком = '))
count_lenth = warehouse_lenth // box_lenth
count_high = warehouse_high // box_high
count_width = warehouse_width // box_width
count_box = count_width * count_high * count_lenth
print(f'максимальное количество коробок в складе = {count_box}')