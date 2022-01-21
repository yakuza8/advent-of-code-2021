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
    def lanternfish_fast(fish: List[int], days: int):
        from collections import defaultdict

        first_birth_mapping = defaultdict(int)
        total_fish_count = len(fish)

        # Prepare initial configuration
        for initial_fish in fish:
            first_birth_mapping[initial_fish] += 1

        # Iterate on each day
        for day in range(1, days + 1):
            current_fish = first_birth_mapping[day]

            last_day = day + 1
            while last_day < days + 1:
                first_birth_mapping[last_day + 8] += current_fish
                total_fish_count += current_fish
                last_day += 7
        return total_fish_count

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
        return Solution.lanternfish(fish=fish, days=days)


class Tests(unittest.TestCase):
    @staticmethod
    def _read_input(fish_list):
        return [int(_) for _ in fish_list.split(',')]

    def test_sample_input(self):
        fish_list = self._read_input('3,4,3,1,2')

        self.assertEqual(26, Solution.lanternfish_fast(fish=fish_list, days=18))
        self.assertEqual(5934, Solution.lanternfish_fast(fish=fish_list, days=80))
        self.assertEqual(
            26984457539, Solution.lanternfish_fast(fish=fish_list, days=256)
        )

        # self.assertEqual(26, Solution.lanternfish(fish=fish_list, days=18))
        # self.assertEqual(5934, Solution.lanternfish(fish=fish_list, days=80))
        # self.assertEqual(26984457539, Solution.lanternfish(fish=fish_list, days=256))

    def test_real_problem(self):
        fish_list = self._read_input(
            '3,5,2,5,4,3,2,2,3,5,2,3,2,2,2,2,3,5,3,5,5,2,2,3,4,2,3,5,5,3,3,5,2,4,5,4,3,5,3,2,5,4,'
            '1,1,1,5,1,4,1,4,3,5,2,3,2,2,2,5,2,1,2,2,2,2,3,4,5,2,5,4,1,3,1,5,5,5,3,5,3,1,5,4,2,5,'
            '3,3,5,5,5,3,2,2,1,1,3,2,1,2,2,4,3,4,1,3,4,1,2,2,4,1,3,1,4,3,3,1,2,3,1,3,4,1,1,2,5,1,'
            '2,1,2,4,1,3,2,1,1,2,4,3,5,1,3,2,1,3,2,3,4,5,5,4,1,3,4,1,2,3,5,2,3,5,2,1,1,5,5,4,4,4,'
            '5,3,3,2,5,4,4,1,5,1,5,5,5,2,2,1,2,4,5,1,2,1,4,5,4,2,4,3,2,5,2,2,1,4,3,5,4,2,1,1,5,1,'
            '4,5,1,2,5,5,1,4,1,1,4,5,2,5,3,1,4,5,2,1,3,1,3,3,5,5,1,4,1,3,2,2,3,5,4,3,2,5,1,1,1,2,'
            '2,5,3,4,2,1,3,2,5,3,2,2,3,5,2,1,4,5,4,4,5,5,3,3,5,4,5,5,4,3,5,3,5,3,1,3,2,2,1,4,4,5,'
            '2,2,4,2,1,4'
        )
        print(Solution.lanternfish_fast(fish=fish_list, days=80))
        print(Solution.lanternfish_fast(fish=fish_list, days=256))

        # print(Solution.lanternfish(fish=fish_list, days=80))
        # print(Solution.lanternfish(fish=fish_list, days=256))
