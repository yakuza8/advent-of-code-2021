import unittest
from dataclasses import dataclass
from typing import List


@dataclass
class LanternFish:
    # Constants
    NEW_BORN_BIRTH_TIMEOUT = 8
    BIRTH_PERIOD = 7

    # Internal counter
    next_birth: int

    def can_give_birth(self):
        return self.next_birth <= 0

    def give_birth(self, fish_list: List['LanternFish']):
        self.next_birth = self.BIRTH_PERIOD
        fish_list.append(LanternFish(next_birth=self.NEW_BORN_BIRTH_TIMEOUT))

    def live(self):
        self.next_birth -= 1


class Solution:
    @staticmethod
    def lanternfish(fish: List[int], days: int):
        fish_list = [LanternFish(next_birth=period) for period in fish]
        for day in range(days):
            new_born_fish = []
            for fish in fish_list:
                if fish.can_give_birth():
                    fish.give_birth(fish_list=new_born_fish)
                fish.live()
            fish_list.extend(new_born_fish)
        return len(fish_list)

    @staticmethod
    def lanternfish_part_two(fish: List[int], days: int):
        ...


class Tests(unittest.TestCase):
    @staticmethod
    def _read_input(fish_list):
        return [int(_) for _ in fish_list.split(',')]

    def test_sample_input(self):
        fish_list = self._read_input('3,4,3,1,2')
        self.assertEqual(26, Solution.lanternfish(fish=fish_list, days=18))
        self.assertEqual(5934, Solution.lanternfish(fish=fish_list, days=80))

    def test_real_problem(self):
        fish_list = self._read_input(
            '3,5,2,5,4,3,2,2,3,5,2,3,2,2,2,2,3,5,3,5,5,2,2,3,4,2,3,5,5,3,3,5,2,4,5,4,3,5,3,2,5,4,'
            '1,1,1,5,1,4,1,4,3,5,2,3,2,2,2,5,2,1,2,2,2,2,3,4,5,2,5,4,1,3,1,5,5,5,3,5,3,1,5,4,2,5,'
            '3,3,5,5,5,3,2,2,1,1,3,2,1,2,2,4,3,4,1,3,4,1,2,2,4,1,3,1,4,3,3,1,2,3,1,3,4,1,1,2,5,1,'
            '2,1,2,4,1,3,2,1,1,2,4,3,5,1,3,2,1,3,2,3,4,5,5,4,1,3,4,1,2,3,5,2,3,5,2,1,1,5,5,4,4,4,'
            '5,3,3,2,5,4,4,1,5,1,5,5,5,2,2,1,2,4,5,1,2,1,4,5,4,2,4,3,2,5,2,2,1,4,3,5,4,2,1,1,5,1,'
            '4,5,1,2,5,5,1,4,1,1,4,5,2,5,3,1,4,5,2,1,3,1,3,3,5,5,1,4,1,3,2,2,3,5,4,3,2,5,1,1,1,2,'
            '2,5,3,4,2,1,3,2,5,3,2,2,3,5,2,1,4,5,4,4,5,5,3,3,5,4,5,5,4,3,5,3,5,3,1,3,2,2,1,4,4,5,'
            '2,2,4,2,1,4')
        print(Solution.lanternfish(fish=fish_list, days=80))