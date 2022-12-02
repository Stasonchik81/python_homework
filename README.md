# python_homework
Для сдачи домашних заданий по курсу GB - разработчик

[Homework1](#Homework1) | [Homework2](#Homework2) | [Homework3](#Homework3)

<div id="Homework1"></div>

## Homework1

***
1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет

2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ⋀ - and ⋁ - or ¬ - not

3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3

4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21

<div id="Homework2"></div>

## Homework2

***
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

0,56 -> 11

2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

Пример:

Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
n = 3
[-3, -2, -1, 0, 1, 2, 3]
--> 0 2 3
-3 * -1 * 0 = 0
Вывод: 0

5. Реализуйте алгоритм перемешивания списка.

<div id="Homework3"></div>

## Homework3

***
1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

Пример:

[2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 10.01] => 0.19

4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10

5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]