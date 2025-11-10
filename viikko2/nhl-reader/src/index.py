from rich.console import Console
from rich.prompt import Prompt
from player import PlayerReader, PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    console = Console()
    while True:
        nationality = Prompt.ask("Nationality [bold magenta][USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS][/bold magenta]")
        if nationality == "":
            break

        players = stats.top_scorers_by_nationality(nationality)
        console.print(players)

if __name__ == "__main__":
    main()
