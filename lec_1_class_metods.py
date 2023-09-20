# метод __init__

class Ball:
 
    def __init__(self, mass):
        ''' Инициализатор (конструктор) — это
            специальный метод, который вызывается по
            умолчанию когда вы создаете экземпляр класса.
        '''
        print('Я вызвался')
 
        self.mass = mass
        self.image = 'hexagone'
        self.x = 0
        self.y = 0

# Методы, реализующие поведение экземпляров
# self – подразумеваемый экземпляр
    def drop(self):
        print('Я подбросился')
        self.x = 2
 
    def kick(self):
        print('Я пнулся')
        self.x += 1
 
    def fail(self):
        self.mass = self.mass - 0.1
 
# Вызов полей

ball = Ball(0.5)
print(ball.image)
print(ball.mass)
ball.image = 'lines'
print(ball.image)

print(ball.x)
ball.drop()
ball.kick()
print(ball.x)