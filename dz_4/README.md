**Урок 4. Введение в многозадачность**  
*Задания 7 (три варианта)*  
� Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
� Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
� Массив должен быть заполнен случайными целыми числами от 1 до 100.
� При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
� В каждом решении нужно вывести время выполнения вычислений.  
1. Многопоточный вариант. Программа создает (n) потоков (по умолчанию 5) и находит сумму элементов массива из (k) 1_000_000 целых чисел в 
интервале от a до b.  
2. Мультипрцесорный вариант. Программа создает (n) пороцессов и находит сумму элементов массива из (k) 1_000_000 целых чисел в 
интервале от a до b.  
3. Асинхронный вариант. Программа создает (n) параллельных задач и находит сумму элементов массива из (k) 1_000_000 целых чисел в  
интервале от a до b.  
 
Реализация:  
https://github.com/SB44444/DZ_Flask/tree/master/dz_4