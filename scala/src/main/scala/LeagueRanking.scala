import scala.io.Source
import scala.collection.mutable

object LeagueRanking {

  case class GameResult(team1: String, score1: Int, team2: String, score2: Int)

  def parseResult(resultLine: String): GameResult = {
      try {
          val parts = resultLine.split(",")
          // Split the first part to get team names and scores
          val team1Data = parts(0).trim.split(" ")
          val team2Data = parts(1).trim.split(" ")

          // Get team names by joining all but the last element
          val team1 = team1Data.init.mkString(" ")
          val score1 = team1Data.last.toInt
          val team2 = team2Data.init.mkString(" ")
          val score2 = team2Data.last.toInt

          GameResult(team1, score1, team2, score2)
      } catch {
          case e: Exception =>
              throw new IllegalArgumentException(s"Error parsing result: $resultLine", e)
      }
  }

  def updateStandings(standings: mutable.Map[String, Int], game: GameResult): Unit = {
    // Ensure both teams are initialized even if they score 0 points
    standings(game.team1) = standings.getOrElse(game.team1, 0)
    standings(game.team2) = standings.getOrElse(game.team2, 0)

    if (game.score1 > game.score2) {
      standings(game.team1) += 3
    } else if (game.score1 < game.score2) {
      standings(game.team2) += 3
    } else {
      standings(game.team1) += 1
      standings(game.team2) += 1
    }
  }

  def getSortedStandings(standings: mutable.Map[String, Int]): List[(String, Int)] = {
    standings.toList.sortBy { case (team, points) => (-points, team) }
  }

def formatStandings(sortedStandings: List[(String, Int)]): String = {
    var output = List[String]()
    var rank = 1
    var prevPoints: Option[Int] = None

    for ((team, points) <- sortedStandings) {
        if (!prevPoints.contains(points)) {
            rank = output.length + 1 // Update rank based on the current output length
        }
        prevPoints = Some(points)

        // Properly format the output string
        output = output :+ s"$rank. $team, $points pt${if (points != 1) "s" else ""}"
    }
    output.mkString("\n")
}


  def main(args: Array[String]): Unit = {
    val standings = mutable.Map[String, Int]()

    // Read input
    val inputLines = if (args.length > 0) {
      Source.fromFile(args(0)).getLines().toList
    } else {
      Source.stdin.getLines().toList
    }

    // Parse results and update standings
    inputLines.foreach { line =>
      val game = parseResult(line)
      updateStandings(standings, game)
    }

    // Generate sorted standings and print
    val sortedStandings = getSortedStandings(standings)
    val result = formatStandings(sortedStandings)
    println(result)
  }
}
