"""Задание №7 Асинхронный вариант.
� Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
� Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
� Массив должен быть заполнен случайными целыми числами от 1 до 100.
� При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
� В каждом решении нужно вывести время выполнения вычислений."""

import asyncio
from random import randint
from time import time

"""Программа создает (n) параллельных задач и находит сумму элементов массива из (k) 1_000_000 целых чисел в 
интервале от a до b."""
counter3 = 0  # Глобальная перемренная
my_list = []


async def sum_list_counter(get_list: list[int]):
    sum_list_nambers = 0
    global counter3
    for x in get_list:
        sum_list_nambers += x
    counter3 += sum_list_nambers


async def main():
    global my_list
    tasks = [asyncio.create_task(sum_list_counter(my_list)) for _ in range(n)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time()
    a, b = 1, 100  # Интервал целых чисел
    n = 5  # количество асинхронных задач,
    k = 1_000_000  # количество чисел в массиве
    my_list = [randint(a, b) for _ in range(k)]
    asyncio.run(main())
    print(f"Сумма чисел в массиве: {counter3:_}")
    print(f'Время работы программы {time() - start_time} секунд.')
