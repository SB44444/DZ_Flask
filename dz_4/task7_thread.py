"""Задание №7 Многопоточный вариант.
� Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
� Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
� Массив должен быть заполнен случайными целыми числами от 1 до 100.
� При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
� В каждом решении нужно вывести время выполнения вычислений."""

from random import randint
import threading
from time import time
"""Программа создает (n) потоков (по умолчанию 5) и находит сумму элементов массива из (k) 1_000_000 целых чисел в 
интервале от a до b."""
counter = 0  # Глобальная перемренная


def sum_list_counter(get_list: list[int]):
    sum_list_nambers = 0
    global counter
    for x in get_list:
        sum_list_nambers += x
    counter += sum_list_nambers


def increment_threads_worker(n: int = 5):
    threads = []
    for i in range(n):
        t = threading.Thread(target=sum_list_counter, args=[my_list])
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Сумма чисел в массиве: {counter:_}")

start_time = time()

if __name__ == "__main__":
    a, b = 1, 100
    n, k = 3, 1_000_000
    my_list = [randint(a, b) for _ in range(k)]
    increment_threads_worker()
    print(f'Время работы программы {time() - start_time} секунд.')



