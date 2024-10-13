from typing import List, Tuple, Dict
from collections import defaultdict

def parse_result(result_line: str) -> Tuple[str, int, str, int]:
    """Parse a game result string and return the teams and their scores."""
    try:
        parts = result_line.split(',')
        team1_data = parts[0].rsplit(' ', 1)
        team2_data = parts[1].rsplit(' ', 1)
        
        team1 = team1_data[0].strip()
        score1 = int(team1_data[1].strip())
        team2 = team2_data[0].strip()
        score2 = int(team2_data[1].strip())
        
        return team1, score1, team2, score2
    except (ValueError, IndexError) as e:
        raise ValueError(f"Error parsing result: {result_line}") from e

def update_standings(
    standings: defaultdict[str, int], 
    team1: str, score1: int, 
    team2: str, score2: int
) -> None:
    """Update the standings based on match results."""
    # Ensure both teams are added to standings, even if they don't win or score points.
    standings[team1] += 0
    standings[team2] += 0
    
    # Update standings based on game result.
    if score1 > score2:
        standings[team1] += 3
    elif score1 < score2:
        standings[team2] += 3
    else:
        standings[team1] += 1
        standings[team2] += 1

def get_sorted_standings(standings: Dict[str, int]) -> List[Tuple[str, int]]:
    """Return the standings sorted by points and team names."""
    return sorted(standings.items(), key=lambda x: (-x[1], x[0]))

def format_standings(sorted_standings: List[Tuple[str, int]]) -> str:
    """Format the standings for output."""
    output = []
    rank = 1
    prev_points = None
    for i, (team, points) in enumerate(sorted_standings):
        if points != prev_points:
            rank = i + 1
        prev_points = points
        output.append(f"{rank}. {team}, {points} pt{'s' if points != 1 else ''}")
    return "\n".join(output)

def main(input_lines: List[str]) -> None:
    """Main function to calculate and print league standings."""
    standings: defaultdict[str, int] = defaultdict(int)

    # Parse all results and update standings
    for line in input_lines:
        team1, score1, team2, score2 = parse_result(line)
        update_standings(standings, team1, score1, team2, score2)

    sorted_standings = get_sorted_standings(standings)
    result = format_standings(sorted_standings)
    print(result)

if __name__ == "__main__":
    import sys
    # Check if a filename is passed, else read from stdin
    input_lines = sys.stdin.read().splitlines() if len(sys.argv) == 1 else open(sys.argv[1]).read().splitlines()
    main(input_lines)
