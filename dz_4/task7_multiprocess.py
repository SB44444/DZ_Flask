"""Задание №7 Мультипрцесорный вариант.
� Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
� Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
� Массив должен быть заполнен случайными целыми числами от 1 до 100.
� При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
� В каждом решении нужно вывести время выполнения вычислений."""
import multiprocessing
from random import randint
from time import time
"""Программа создает (n) пороцессов и находит сумму элементов массива из (k) 1_000_000 целых чисел в 
интервале от a до b."""

counter2 = multiprocessing.Value('i', 0)
my_list = []


def sum_list_counter(get_list: list[int], cnt: multiprocessing.Value):
    sum_list_nambers = 0
    for x in get_list:
        sum_list_nambers += x
    with cnt.get_lock():
        cnt.value += sum_list_nambers


def main():
    global counter2
    global my_list
    processes: list[multiprocessing.Process] = []
    for i in range(n):
        proc = multiprocessing.Process(target=sum_list_counter, args=(my_list, counter2))
        processes.append(proc)
        proc.start()
    for proc in processes:
        proc.join()
    return counter2

if __name__ == "__main__":
    start_time = time()
    a, b = 1, 100  # Интервал целых чисел
    n = 2  # количество процессов,
    k = 1_000_000  # количество чисел в массиве
    my_list = [randint(a, b) for _ in range(k)]
    total_counter = main()
    with total_counter.get_lock():
        counter2 = total_counter.value
    print(f"Сумма чисел в массиве: {counter2:_}")
    print(f'Время работы программы {time() - start_time} секунд.')
