import requests

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()

    def get_players(self):
        players = []
        for player_dict in self.response:
            players.append(Player(player_dict))
        return players

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nation):
        return list(sorted(filter(lambda x: x.nationality == nation, self.players), key=lambda x: x.goals + x.assists, reverse=True))

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
    
    def __str__(self):
        return f"{self.name:25} {self.team:15} {self.goals} + {self.assists} = {self.goals + self.assists}"
