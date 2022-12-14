Пример использования реализации:</br>

Эта кусочно линейная функция заданная двумя точками</br>
Точки с одинаковым х переписывают друг друга</br>
Входящие точки: x=0,y=100 и x=10,y=122</br>

```
F = PieceWise(0,100)(10,122) #.. и т.д
```

Добавим еще одну точку, к примеру, x=30, y=0

```
F = F(30, 0)
```

Вычислим значение от x = 5 </br>
Cложность этого алгоритма:</br> 
O(n) - в худшем случае</br>
O(1) - в лучшем, когда __y__ не нужно вычислять
```
y = F.y(5) # Результат: y = 111
```

Вывод таблицы

```
F.table()
```
Результат </br>

|      x1       |       x2        |     a     |     b     |   
|:-------------:|:---------------:|:---------:|:---------:|
|   (0, 100)    | (10, 122) | 2.200 | 100.000 |
|   (10, 122)    |    (30, 0)     |    -6.100    |    183.000    |