import runner as rr
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Запускаем тест")
    def test_walk(self):
        item_walk = rr.Runner('Ran1')
        for i in range(10):
            item_walk.walk()
        self.assertEqual(item_walk.distance, 50)

    @unittest.skipIf(is_frozen, "Запускаем тест")
    def test_run(self):
        item_run = rr.Runner('Ran2')
        for i in range(10):
            item_run.run()
        self.assertEqual(item_run.distance, 100)

    @unittest.skipIf(is_frozen, "Запускаем тест")
    def test_challenge(self):
        item1 = rr.Runner('Ran3')
        item2 = rr.Runner('Ran4')
        for i in range(10):
            item1.walk()
            item2.run()
        self.assertNotEqual(item1.distance, item2.distance)


if __name__ == '__main__':
    unittest.main()

