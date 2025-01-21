# 객체지향이 없다면?
# 비디오 게임 소프트웨어 만들기

musk = {
    "name": "Musk",
    "XP": 1000,
    "team": "Team X",
}


def create_player_for_team(name, xp, team):
    pass


def create_playeer(name, xp, team):
    return {
        "name": name,
        "XP": xp,
        "team": team,
    }


def introduce_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hello! My name is {name} and I play for {team}")


introduce_player(musk)

musk = create_playeer("musk", 2000, "Team Y")
lynn = create_playeer("Lynn", 1500, "Team Blue")

teams = {"TeamX": [musk], "Team Blue": [lynn]}
print(musk)
