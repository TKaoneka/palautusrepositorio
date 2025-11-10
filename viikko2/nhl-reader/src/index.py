from player import Player, PlayerStats, PlayerReader
from rich.console import Console
from rich.prompt import Prompt

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    console = Console()
    season = Prompt.ask("Season [bold magenta][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26][/bold magenta] [bold cyan](2024-25)[/bold cyan]")
    nationality = Prompt.ask("Nationality [bold magenta][USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS][/bold magenta]")
    players = stats.top_scorers_by_nationality(nationality)
    console.print(players)

if __name__ == "__main__":
    main()
