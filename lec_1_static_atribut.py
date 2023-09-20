class Ball :
    # создание статического атрибута
    color = 'red'
    radius = 5

    # статический метод обращение только через имя класса
    def info() :
        print('просто хороший класс')

ball = Ball()
#ВЫЗОВ СТАТИЧЕСКИХ АТРИБУТОВ
'''
print(ball.color)
print(Ball.radius)
'''

print(Ball.radius)
print(Ball.info())

# изменение статических атрибутов экземпляра
ball.color = 'white'
print(ball.color)
print(Ball.color)

Ball.color = 'white'
new_ball = Ball()
print(Ball.color)
print(new_ball.color)