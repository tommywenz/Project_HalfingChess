from character import *
from abc import ABC, abstractmethod

class Villain(Character):
    def __init__(self):
        super().__init__(Player.VILLAIN)

    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        if from_coord.x != to_coord.x or from_coord.y != to_coord.y:
            return False
        else:
            return super().is_valid_move(from_coord, to_coord, board)

    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        return super().is_valid_attack(from_coord, to_coord, board)

    def calculate_dice(self, attack=True, lst: list = [], *args, **kwargs) -> int:
        return super().calculate_dice(attack, lst, *args, **kwargs)

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        return super().deal_damage(target, damage, *args, **kwargs)


class Goblin(Villain):
    def __init__(self):
        super().__init__()
        self.health = 3
        self.temp_health = 3
        self.combat = [2, 2]


class Skeleton(Villain):
    def __init__(self):
        super().__init__()
        self.health = 2
        self.temp_health = 2
        self.combat = [2, 1]
        self.move = 2


class Necromancer(Villain):
    def __init__(self):
        super().__init__()
        self.combat = [1, 2]
        self.range = 3

    def raise_dead(target: Character):
        if not Player.VILLAIN:
            target = Player.VILLAIN

        target.health = target.health // 2

class Heroes(Character):
    def __init__(self):
        super().__init__(Player.HERO)

    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        return super().is_valid_move(from_coord, to_coord, board)

    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        return super().is_valid_attack(from_coord, to_coord, board)

    def calculate_dice(self, attack, lst=[], *args, **kwargs) -> int:
        return super().calculate_dice(attack, lst)

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        return super().deal_damage(target, damage, *args, **kwargs)


class Warrior(Heroes):
    def __init__(self):
        super().__init__()
        self.health = 7
        self.temp_health = 7
        self.combat = [2, 4]

    def calculate_dice(self, target: Character, attack=True, lst: list = [], gob: list = []):
        if not isinstance(target, Goblin):
            super().calculate_dice(attack, lst)
        else:
            if not gob:
                for i in gob:
                    i += 2
            else:
                gob = list([randint(1, 6), randint(1, 6)])


class Mage(Heroes):
    def __init__(self):
        super().__init__()
        self.combat = [2, 2]
        self.range = 3
        self.move = 2

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        super().deal_damage(target, damage, *args, **kwargs)
        damage += 1


class Paladin(Heroes):
    def __init__(self):
        super().__init__()
        self.__heal = bool
        self.health = 6
        self.temp_health = 6

    @property
    def heal(self):
        return self.__heal

    @heal.setter
    def heal(self, new_amnt):
        self.__heal = new_amnt


    # TODO- How to check if something is in range or not
    def revive(self, target: Character):
        if target
        target.temp_health -= self.health // 2
        pass












