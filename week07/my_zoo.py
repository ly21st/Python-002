# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    category = ['食草', '食肉', '食杂']
    somatotype = ['小', '中等', '大', '巨大']
    nature = ['温顺', '中性', '凶猛']
    ferocious_somatotype = ['中等', '大', '巨大']

    def __init__(self, category, somatotype, nature, cry=''):
        Animal.check_args(category, somatotype, nature)
        self.category = category
        self.somatotype = somatotype
        self.nature = nature
        self.fierce = False
        self.cry = cry

    @classmethod
    def check_args(cls, category, somatotype, nature):
        if category not in cls.category:
            raise ValueError("category must be in ('食草', '食肉', '食杂')")
        if somatotype not in cls.somatotype:
            raise ValueError("somatotype must be in ('小', '中等', '大', '巨大')")
        if nature not in cls.nature:
            raise ValueError("nature must be in ('温顺', '中性', '凶猛')")

    def is_ferocious_animal(self, category, somatotype, nature):
        return somatotype in self.ferocious_somatotype and category == '食肉' and nature == '凶猛'

    @abstractmethod
    def set_fierce(self, category, somatotype, nature):
        pass


class Cat(Animal):
    def __init__(self, name, category, somatotype, nature, cry=''):
        super().__init__(category, somatotype, nature, cry)
        self.name = name
        self.set_fierce(category, somatotype, nature)
        self.is_pet = not self.fierce

    def set_fierce(self, category, somatotype, nature):
        if self.is_ferocious_animal(category, somatotype, nature):
            self.fierce = True
        else:
            self.fierce = False


class Dog(Animal):
    def __init__(self, name, category, somatotype, nature, cry=''):
        super().__init__(category, somatotype, nature, cry)
        self.name = name
        self.set_fierce(category, somatotype, nature)
        self.is_pet = not self.fierce

    def set_fierce(self, category, somatotype, nature):
        if self.is_ferocious_animal(category, somatotype, nature):
            self.fierce = True
        else:
            self.fierce = False


class Zoo(object):
    def __init__(self, name):
        self.name = name

    def add_animal(self, animal):
        class_name = type(animal).__name__
        if class_name in self.__dict__:
            raise ValueError(f'"{class_name}" is already exist')
        self.__dict__[class_name] = True


if __name__ == '__main__':
    #animal = Animal()
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print('have_cat', have_cat)
