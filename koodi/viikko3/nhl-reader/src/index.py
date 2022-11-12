from player import Player
import requests

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()
    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        if player_dict["nationality"] == "FIN":
            players.append(player_dict)
    sort = sorted(players, key=lambda player: player['goals'] + player['assists'] , reverse=True)
    #print("Oliot:")
    print("Players from FIN:")
    for player in sort:
        print(f"{player['name']} {player['goals']} + {player['assists']} = {player['goals'] + player['assists']}")
        
if __name__ == "__main__":
    main()
