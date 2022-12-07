import unittest
import main


class TestMainSimple(unittest.TestCase):
    def setUp(self) -> None:
        self.start_configuration = """    [D]
[N] [C]
[Z] [M] [P]
"""
        self.moves = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

        self.number_of_stacks = 3
        return super().setUp()

    def test_loadStacks(self):
        stacks = main.loadStacks(self.start_configuration, self.number_of_stacks)
        self.assertEqual(stacks, [["Z", "N"], ["M", "C", "D"], ["P"]])

    def test_moveOne(self):
        stacks = main.loadStacks(self.start_configuration, self.number_of_stacks)
        main.moveOne(stacks, 1 - 1, 2 - 1)
        self.assertEqual(stacks, [["Z"], ["M", "C", "D", "N"], ["P"]])

    def test_moveN(self):
        stacks = main.loadStacks(self.start_configuration, self.number_of_stacks)
        main.moveN(stacks, 2, 1 - 1, 2 - 1)
        self.assertEqual(stacks, [[], ["M", "C", "D", "N", "Z"], ["P"]])

    def test_executeMoves(self):
        stacks = main.loadStacks(self.start_configuration, self.number_of_stacks)
        result = main.executeMoves(self.moves, stacks)
        self.assertEqual(stacks, [["C"], ["M"], ["P", "D", "N", "Z"]])
        self.assertEqual(result, "CMZ")

    def test_moveN9001(self):
        stacks = main.loadStacks(self.start_configuration, self.number_of_stacks)
        main.moveN9001(stacks, 2, 1 - 1, 2 - 1)
        self.assertEqual(stacks, [[], ["M", "C", "D", "Z", "N"], ["P"]])

    def test_executeMoves9001(self):
        stacks = main.loadStacks(self.start_configuration, self.number_of_stacks)
        result = main.executeMoves9001(self.moves, stacks)
        self.assertEqual(stacks, [["M"], ["C"], ["P", "Z", "N", "D"]])
        self.assertEqual(result, "MCD")


class TestMainReal(unittest.TestCase):
    def setUp(self) -> None:
        with open("day5/input", "r") as f:
            self.moves = f.read()

        with open("day5/start_configuration", "r") as f:
            self.start_configuration = f.read()

        self.number_of_stacks = 9
        return super().setUp()

    def test_part1(self):
        stacks = main.loadStacks(self.start_configuration, self.number_of_stacks)
        result = main.executeMoves(self.moves, stacks)
        self.assertEqual(result, "VPCDMSLWJ")

    def test_part2(self):
        stacks = main.loadStacks(self.start_configuration, self.number_of_stacks)
        result = main.executeMoves9001(self.moves, stacks)
        self.assertEqual(result, "TPWCGNCCG")


if __name__ == "__main__":
    unittest.main()
