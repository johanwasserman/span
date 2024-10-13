import unittest
from typing import Tuple, List
from league_ranking import parse_result, update_standings, get_sorted_standings, format_standings

class TestLeagueRanking(unittest.TestCase):

    def test_parse_result(self) -> None:
        """Test the parse_result function for correct parsing of game results."""
        test_cases: List[Tuple[str, Tuple[str, int, str, int]]] = [
            ("Lions 3, Snakes 1", ("Lions", 3, "Snakes", 1)),
            ("Tarantulas 2, FC Awesome 2", ("Tarantulas", 2, "FC Awesome", 2))
        ]
        for input_line, expected in test_cases:
            with self.subTest(input_line=input_line):
                result = parse_result(input_line)
                self.assertEqual(result, expected, 
                                 f"Failed to parse result. Expected: {expected}, Got: {result}")

    def test_update_standings_win(self) -> None:
        """Test updating standings for a match where one team wins."""
        standings = {"Lions": 0, "Snakes": 0}
        update_standings(standings, "Lions", 3, "Snakes", 1)
        self.assertEqual(standings["Lions"], 3, "Lions should have 3 points after winning.")
        self.assertEqual(standings["Snakes"], 0, "Snakes should have 0 points after losing.")

    def test_update_standings_draw(self) -> None:
        """Test updating standings for a match where the game is a draw."""
        standings = {"Lions": 0, "Snakes": 0}
        update_standings(standings, "Lions", 2, "Snakes", 2)
        self.assertEqual(standings["Lions"], 1, "Lions should have 1 point after drawing.")
        self.assertEqual(standings["Snakes"], 1, "Snakes should have 1 point after drawing.")

    def test_sorted_standings(self) -> None:
        """Test sorting the standings by points and team names."""
        standings = {"Lions": 3, "Snakes": 1, "Tarantulas": 6, "Grouches": 0}
        sorted_standings = get_sorted_standings(standings)
        expected = [("Tarantulas", 6), ("Lions", 3), ("Snakes", 1), ("Grouches", 0)]
        self.assertEqual(sorted_standings, expected, 
                         f"Standings were not sorted correctly. Expected: {expected}, Got: {sorted_standings}")

    def test_format_standings(self) -> None:
        """Test formatting the sorted standings into the correct string format."""
        standings = [("Tarantulas", 6), ("Lions", 3), ("Snakes", 1), ("Grouches", 0)]
        output = format_standings(standings)
        expected_output = "1. Tarantulas, 6 pts\n2. Lions, 3 pts\n3. Snakes, 1 pt\n4. Grouches, 0 pts"
        self.assertEqual(output, expected_output, 
                         f"Formatted standings were incorrect. Expected: {expected_output}, Got: {output}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
