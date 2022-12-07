import unittest
import main


class TestMainSimple(unittest.TestCase):
    def setUp(self) -> None:
        self.buffers = {'bvwbjplbgvbhsrlpgdmjqwftvncz': 5,
                        'nppdvjthqldpwncqszvftbrmjlhg': 6,
                        'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg': 10,
                        'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw': 11}

        return super().setUp()

    def test_computePart1(self):
        for buffer, result in self.buffers.items():
            self.assertEqual(main.computePart1(buffer), result)

class TestMainReal(unittest.TestCase):
    def setUp(self) -> None:
        with open("input", "r") as f:
            self.buffer = f.readline().strip()

        return super().setUp()

    def test_part1(self):
        result = main.computePart1(self.buffer)
        self.assertEqual(result, 1109)

    def test_part1(self):
        result = main.computePart1(self.buffer, 14)
        self.assertEqual(result, 3965)

if __name__ == "__main__":
    unittest.main()
