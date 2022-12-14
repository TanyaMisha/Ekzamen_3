# #1  Задача1
#
# def card_number(card):
#   return '*' * (len(card)-4) + card[-4:]
#
# #2 Задача2
#
# def palindromeCheck(word):
#     if word[::-1] == word:
#         return print('Это палиндромом')
#     else:
#         return print('Это не палиндромом')





#3 Задача3

# class Tomato:
#     states = {0: 'ничего', 1: 'цветок', 2: 'незрелый', 3: 'зрелый'}
#
#     def __init__(self, index):
#         self._index = index
#         self._state = 0
#
#     def grow(self):
#         self._change_state()
#
#     def is_ripe(self):
#         if self._state == 3:
#             return True
#         return False
#
#     def _change_state(self):
#         if self._state < 3:
#             self._state += 1
#         self._print_state()
#
#     def _print_state(self):
#         print(f'Помидор {self._index} это {Tomato.states[self._state]}')
#
#
# class TomatoBush:
#
#     def __init__(self, num):
#         self.tomatoes = [Tomato(index) for index in range(0, num)]
#
#     def grow_all(self):
#         for tomato in self.tomatoes:
#             tomato.grow()
#
#     def all_are_ripe(self):
#         return all([tomato.is_ripe() for tomato in self.tomatoes])
#
#     def give_away_all(self):
#         self.tomatoes = []
#
#
# class Gardener:
#
#     def __init__(self, name, plant):
#         self.name = name
#         self._plant = plant
#
#     def work(self):
#         print('Работает')
#         self._plant.grow_all()
#         print('Закончил')
#
#     def harvest(self):
#         print('Собирает урожай')
#         if self._plant.all_are_ripe():
#             self._plant.give_away_all()
#             print('Урожай собран')
#         else:
#             print('Урожай не созрел')
#
#     @staticmethod
#     def knowledge_base():
#         print('Справка по садоводству')
#
#
# if __name__ == '__main__':
#     Gardener.knowledge_base()
#     great_tomato_bush = TomatoBush(4)
#     gardener = Gardener('Никита', great_tomato_bush)
#     gardener.work()
#     gardener.work()
#     gardener.harvest()
#     gardener.work()
#     gardener.harvest()


