import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'], player_dict['nationality'], player_dict['assists'], player_dict['goals'], player_dict['penalties'], player_dict['team'], player_dict['games']
        )
    
        players.append(player)

    players = sorted(players, key=lambda player: player.points, reverse=True)    

    print("Oliot:")

    for player in players:
        if player.nationality == "FIN":
            print(player)


if __name__ == "__main__":
    main()
