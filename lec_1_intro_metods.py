# встроенные методы для атрибутов
class Ball:
 
    # Создаем статические атрибуты класса
    color = 'red'
    radius = 5
 
ball = Ball()
 
# Вызов встроенных атрибутов выводит все встроенные атрибуты объекта
print(dir(ball))
print()
print(dir(Ball))
print(ball.__init__())
print(Ball.__init__)
print(help(Ball.__init__))
 
# Изменение пользовательских атрибутов экземпляра
ball.color = 'white'
print(ball.color)
print(Ball.color)