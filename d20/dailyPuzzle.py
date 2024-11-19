from dxx.superDailyPuzzle import SuperDailyPuzzle

# advent of code 2023 day 20 as template
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        modules = {}
        for line in self.data.splitlines():
            start = line.split("->")[0].strip()
            if list(start)[0] == "%" or list(start)[0] == "&":
                type = list(start)[0] 
                start = start[1:]
            else:
                type = None
            ends = [x.strip() for x in line.split("->")[1].strip().split(",")]
            modules[start] = (type, ends)
        self.parsed = modules

    def part_one(self, **kwargs):
        print(self.parsed)
        self.part_one_result = 0

    def part_two(self, **kwargs):
        self.part_two_result = 0