import unittest
import runnertest
import tournamenttest


runnerAT = unittest.TestSuite()
runnerAT.addTest(unittest.TestLoader().loadTestsFromTestCase(runnertest.RunnerTest))
runnerAT.addTest(unittest.TestLoader().loadTestsFromTestCase(tournamenttest.TournamentTest))

runner = unittest.TextTestRunner(verbosity = 2)
runner.run(runnerAT)
