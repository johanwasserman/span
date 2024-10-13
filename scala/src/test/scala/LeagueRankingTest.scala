import org.scalatest.funsuite.AnyFunSuite
import scala.collection.mutable

class LeagueRankingTest extends AnyFunSuite {

  test("parseResult should correctly parse a game result") {
    val result = LeagueRanking.parseResult("Lions 3, Snakes 1")
    assert(result.team1 == "Lions")
    assert(result.score1 == 3)
    assert(result.team2 == "Snakes")
    assert(result.score2 == 1)

    val drawResult = LeagueRanking.parseResult("Tarantulas 2, FC Awesome 2")
    assert(drawResult.team1 == "Tarantulas")
    assert(drawResult.score1 == 2)
    assert(drawResult.team2 == "FC Awesome")
    assert(drawResult.score2 == 2)
  }

  test("updateStandings should correctly update the standings for a win") {
    val standings = mutable.Map("Lions" -> 0, "Snakes" -> 0)
    LeagueRanking.updateStandings(standings, LeagueRanking.GameResult("Lions", 3, "Snakes", 1))
    assert(standings("Lions") == 3)
    assert(standings("Snakes") == 0)
  }

  test("updateStandings should correctly update the standings for a draw") {
    val standings = mutable.Map("Lions" -> 0, "Snakes" -> 0)
    LeagueRanking.updateStandings(standings, LeagueRanking.GameResult("Lions", 2, "Snakes", 2))
    assert(standings("Lions") == 1)
    assert(standings("Snakes") == 1)
  }

  test("getSortedStandings should sort standings by points and team name") {
    val standings = mutable.Map("Lions" -> 3, "Snakes" -> 1, "Tarantulas" -> 6, "Grouches" -> 0)
    val sortedStandings = LeagueRanking.getSortedStandings(standings)
    val expected = List(("Tarantulas", 6), ("Lions", 3), ("Snakes", 1), ("Grouches", 0))
    assert(sortedStandings == expected)
  }

  test("formatStandings should return the correct output string") {
    val standings = List(("Tarantulas", 6), ("Lions", 3), ("Snakes", 1), ("Grouches", 0))
    val output = LeagueRanking.formatStandings(standings)
    val expectedOutput = "1. Tarantulas, 6 pts\n2. Lions, 3 pts\n3. Snakes, 1 pt\n4. Grouches, 0 pts"
    assert(output == expectedOutput)
  }
}
