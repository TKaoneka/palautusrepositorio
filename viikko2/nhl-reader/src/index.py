import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN:")

    for player in players:
        print(f"{player.name} team {player.team} goals {player.goals} assists {player.assists}")
    
    players_sorted = sorted(players, key=lambda x: x.goals + x.assists, reverse=True)
    print("Players from FIN (sorted by G/A):")

    for player in players_sorted:
        print(f"{player.name:25} {player.team:15} {player.goals} + {player.assists} = {player.goals + player.assists}")
 
if __name__ == "__main__":
    main()
