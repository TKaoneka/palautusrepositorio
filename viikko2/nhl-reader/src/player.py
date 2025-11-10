import requests
from rich.table import Table

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url, timeout=10).json()

    def get_players(self):
        players = []
        for player_dict in self.response:
            players.append(Player(player_dict))
        return players

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nation):
        nation_players = list(sorted(filter(lambda x: x.nationality == nation, self.players), key=lambda x: x.goals + x.assists, reverse=True))
        table = Table(title=f"Season 2024-25 from {nation}")
        table.add_column("Released", style="cyan")
        table.add_column("teams", style="magenta")
        table.add_column("goals", style="green")
        table.add_column("assists", style="green")
        table.add_column("points", style="green")

        for player in nation_players:
            table.add_row(player.name, player.team, f"{player.goals}", f"{player.assists}", f"{player.goals + player.assists}")

        return table

class Player:
    def __init__(self, dictionary):
        self.name = dictionary['name']
        self.nationality = dictionary['nationality']
        self.assists = dictionary['assists']
        self.goals = dictionary['goals']
        self.team = dictionary['team']
        self.games = dictionary['games']

    def __str__(self):
        return f"{self.name:25} {self.team:15} {self.goals} + {self.assists} = {self.goals + self.assists}"
