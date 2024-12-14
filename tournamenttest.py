import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):
    all_results = None
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.usain = runner_and_tournament.Runner('Усейн', 10)
        self.andrey = runner_and_tournament.Runner('Андрей', 9)
        self.nik = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                res[k] = str(v)
            print(res)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_1(self):
            first_run = runner_and_tournament.Tournament(90, self.usain, self.nik)
            result = first_run.start()
            last_runner = list(result.values())
            self.assertTrue(last_runner[-1] == 'Ник')
            self.all_results[result.values()] = result

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_2(self):
            second_run = runner_and_tournament.Tournament(90, self.andrey, self.nik)
            result = second_run.start()
            last_runner = list(result.values())
            self.assertTrue(last_runner[-1] == 'Ник')
            self.all_results[result.values()] = result

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_3(self):
            third_run = runner_and_tournament.Tournament(90, self.andrey, self.usain, self.nik)
            result = third_run.start()
            last_runner = list(result.values())
            self.assertTrue(last_runner[-1] == 'Ник')
            self.all_results[result.values()] = result

if __name__ == '__main__':
    unittest.main()

