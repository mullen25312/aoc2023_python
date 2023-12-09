from dxx.superDailyPuzzle import SuperDailyPuzzle

import numpy as np

def extrapolate(sequence):
    tmp = sequence
    res = tmp[-1]

    while any(tmp != 0):
        tmp = np.diff(tmp)
        res += tmp[-1]

    return res

# advent of code 2023 day 9 as template
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        self.parsed = []
        for line in self.data.splitlines():
            self.parsed.append(np.array([int(x.strip()) for x in line.split(" ")]))

    def part_one(self, **kwargs):
        self.part_one_result = sum([extrapolate(sequence) for sequence in self.parsed])

    def part_two(self, **kwargs):
        self.part_two_result = sum([extrapolate(sequence[::-1]) for sequence in self.parsed])