class Human:
  head = 1      #поля класса
  hands = 2
  legs = 2
  body = 1

  #методы класса

  #__init__   -   инициализация экземпляра класса    self - это ссылка на экземпляр
  def __init__(self, human_name):
    self.name = human_name


masha = Human('Маша')
adam = Human('Адам')
print(adam.name)
