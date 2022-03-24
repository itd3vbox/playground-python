import unittest

class Test1(unittest.TestCase):

    def setUp(self):
        # init ...
        pass

    def tearDown(self):
        # end ...
        pass

    def test_a1(self):
        self.assertEqual(1, 1)

    def test_a2(self):
        has_winner = True
        is_game_end = False
        self.assertTrue(has_winner)

        self.assertFalse(is_game_end)

    

if __name__ == '__main__':
    unittest.main()