import unittest
from testDjikstraProlog import findShortestPath
from trainDatabase import *

MRT_B, MRT_BC = mrt_blue_line.split(','), mrt_blue_line_cost
MRT_P, MRT_PC = mrt_purple_line.split(','), mrt_purple_line_cost
BTS_SU, BTS_SUC = bts_sukhumvit_line.split(','), bts_sukhumvit_line_cost
BTS_SI, BTS_SIC = bts_silom_line.split(','), bts_silom_line_cost
AL, AL_C = air_link_line.split(','), air_link_line_cost

class TestFindShortestPath(unittest.TestCase):
    def setUp(self):
        print("set up test find shortest path")
        self.BMA = [(MRT_B, MRT_BC),
                    (MRT_P, MRT_PC),
                    (BTS_SU, BTS_SUC),
                    (BTS_SI, BTS_SIC),
                    (AL, AL_C)]

    # one to next one (2 adjacency)
    def test_adjacency_station(self):
        print("Start test: adjacency station")
        for lst, cost_BMA in self.BMA:
            # print("DOING: " + lst[0])
            for index in range(len(lst) - 1):
                from_input, to_input = lst[index], lst[index + 1]
                # print(from_input, to_input),
                path_lst, cost = findShortestPath(from_input, to_input)
                # print(path_lst)
                self.assertEqual(len(path_lst), 2)
                self.assertEqual(cost, cost_BMA)
        print("Success test")

    # first one to end station
    def test_first_to_end_station(self):
        print("Start test: first to end")
        for lst, cost_BMA in self.BMA:
            first_station = lst[0]
            count = 1
            cost_total = 0
            for index in range(1, len(lst)):
                count += 1
                cost_total += cost_BMA
                path_lst, cost = findShortestPath(first_station, lst[index])
                self.assertLessEqual(cost, cost_total)
        print("success test")

    # Test Cross Station
    def test_cross_station(self):
        print("start test: cross station")
        FROM_STATION = 0
        TO_STATION = 1
        COST = 2
        N_STATION = 3
        test_cases = [["phaya_thai", "sala_daeng", 6, 19],
                      ["ari", "makkasan", 7, 29],
                      ["phra_ram_9", "hua_mak", 5, 17],
                      ["saphan_kwai", "bang_sue", 5, 13],
                      ["chong_nonsi", "si_lom", 3, 8],
                      ["nana", "sukhumvit", 3, 7],
                      ["bang_sue", "wong_sawang", 5, 6]]  # MRT and Purple
        for test_case in test_cases:
            path_lst, cost = findShortestPath(test_case[FROM_STATION], test_case[TO_STATION])
            self.assertEqual(len(path_lst), test_case[COST])
            self.assertEqual(cost, test_case[N_STATION])
        print("success test")

    # Random From to
    def test_random_station(self):
        print("start test: random station")
        import random
        MBA = MRT_B + MRT_P + BTS_SU + BTS_SI + AL
        for i in range(10):
            FROM, TO = random.sample(MBA, 2)
            path_lst, cost = findShortestPath(FROM, TO)
            self.assertGreater(len(path_lst), 0)
            self.assertGreater(cost, 0)
        print("success test")

    def test_no_path(self):
        self.assertEqual(findShortestPath("siam", "aaa"), False)

if __name__ == '__main__':
    unittest.main()
