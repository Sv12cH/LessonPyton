# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.

#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    result=0

    def __init__(self, size):
        self.size=size

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result+=self.consumption+other.consumption
        return Jacket(0)

    def __str__(self):
        res=Clothes.result
        Clothes.result=0
        return f"{res}"

class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.size / 6.5) + 0.5


class Jacket(Clothes):
    @property
    def consumption(self):
        return round((self.size *2 + 0.3)/100)


coat = Coat(42)
jacket = Jacket(170)

print(f"Общий расход ткани {coat+jacket}")

