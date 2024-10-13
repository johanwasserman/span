# SPAN League Ranking Solution

This repository contains a solution for calculating and displaying league standings based on match results. The implementation is provided in both Python and Scala, showcasing the development of the algorithm (Python) and its productionisation (Scala).

## Table of Contents

- [Overview](#overview)
- [Python Implementation](#python-implementation)
  - [Algorithm Development](#algorithm-development)
- [Scala Implementation](#scala-implementation)
  - [Productionising the Solution](#productionizing-the-solution)

## Overview

The League Ranking Solution processes match results and computes the standings of teams in a league format. The solution takes inputs in a specific format and generates output reflecting each team's points based on wins, losses, and draws.

## Python Implementation

### Algorithm Development

The Python implementation focuses on developing the algorithm to parse match results, update standings, and format the output. 

#### Features:

- **Parsing Results**: Efficiently extracts team names and scores from input strings.
- **Updating Standings**: Maintains a dictionary to track points for each team.
- **Sorting Standings**: Produces a sorted list of teams based on their points.
- **Formatting Output**: Generates a readable string format for displaying standings.

#### Key Components:

- **`parse_result(result_line)`**: Extracts the teams and their scores from the input. It validates input and isolates parsing logic, making it easy to test and maintain.
- **`update_standings(standings, team1, score1, team2, score2)`**: Updates the standings (team points) based on match outcomes (win, loss, draw). It focuses purely on business logic (rules), which is clean and easy to extend.
- **`get_sorted_standings(standings)`**: Returns the standings, sorted by points and team names. This function separates the sorting logic from the rest of the system, making it flexible for changes (if sorting rules change).
- **`format_standings(sorted_standings)`**: Formats the final sorted standings for display. This focuses purely on presentation (output format).

#### Notes:

- Using strongly typed Python with type annotations improves code readability and maintainability by making expected input and output types explicit, which helps developers understand the code more easily. It allows for early error detection through static type checking, catching potential bugs before runtime. This leads to safer refactoring and better integration with IDEs, enhancing overall productivity in a data engineering project.
- Using defaultdict instead of a regular dict simplifies the process of managing default values, particularly for counting or accumulation tasks like tracking the scores of teams.
- The core data structure (`defaultdict(int)`) allows efficient team points lookups and updates.
- The sorting algorithm used (`sorted()`) is optimised for large datasets, handling the entire list of teams in O(n log n) time.
- For this problem, the data structure needed is straightforward—just team names mapped to their scores. A `dict` is more efficient and direct for this purpose.  

### Running the Tests
```bash
python -m unittest ../test_league_ranking.py
```

**_Output_**

```bash
test_format_standings (__main__.TestLeagueRanking.test_format_standings)
Test formatting the sorted standings into the correct string format. ... ok
test_parse_result (__main__.TestLeagueRanking.test_parse_result)
Test the parse_result function for correct parsing of game results. ... ok
test_sorted_standings (__main__.TestLeagueRanking.test_sorted_standings)
Test sorting the standings by points and team names. ... ok
test_update_standings_draw (__main__.TestLeagueRanking.test_update_standings_draw)
Test updating standings for a match where the game is a draw. ... ok
test_update_standings_win (__main__.TestLeagueRanking.test_update_standings_win)
Test updating standings for a match where one team wins. ... ok
```

### Running

- Ensure Python is installed
- From the root, change directory to the python folder

```bash
cd python
```

#### Running the Code

- Run the script with the input file:

```bash
python league_ranking.py ../input_file.txt
```

**_Output_**

```bash
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
```

## Scala Implementation

### Productionising the Solution

The Scala implementation refines the algorithm for production use, incorporating best practices for performance and maintainability.

#### Key Enhancements:

- **Type Safety**: Utilises Scala's strong type system to define data structures.
- **Error Handling**: Includes comprehensive error handling for parsing and input validation.
- **Unit Testing**: Implements tests using ScalaTest to ensure the reliability of the solution. To run the tests, use the command:

### Running

- Ensure Scala, SBT and Java are installed.
- From the root, change directory to the scala folder

```bash
cd scala
```

#### Running the Tests

```bash
sbt test
```

**_Output_**

```bash
[info] LeagueRankingTest:
[info] - parseResult should correctly parse a game result
[info] - updateStandings should correctly update the standings for a win
[info] - updateStandings should correctly update the standings for a draw
[info] - getSortedStandings should sort standings by points and team name
[info] - formatStandings should return the correct output string
[info] Run completed in 796 milliseconds.
[info] Total number of tests run: 5
[info] Suites: completed 1, aborted 0
[info] Tests: succeeded 5, failed 0, canceled 0, ignored 0, pending 0
[info] All tests passed.
[success] Total time: 3 s, completed Oct 11, 2024, 20:38:27
```

#### Running the Code

Compile the Scala code:

```bash
scalac src/main/scala/LeagueRanking.scala
```

Run the compiled code:

```bash
scala LeagueRanking ../input_file.txt
```

**_Output_**

```bash
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
```
