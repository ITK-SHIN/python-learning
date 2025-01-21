class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"Hello! I'm {self.name} and I play for {self.team}")


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def show_player(self):
        for player in self.players:
            player.introduce()

    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

    def remove_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)
                return

    def total_XP(self):
        total = 0
        for player in self.players:
            total += player.xp

        print(f"{self.team_name}은 {total} 포인트가 있어요")
        return total


team_x = Team("Team X")

team_x.add_player("nico")

team_blue = Team("Blue Team")
team_blue.add_player("Lynn")
team_blue.add_player("AAA")
team_blue.add_player("BBB")
team_blue.add_player("CCC")


team_blue.show_player()
team_blue.total_XP()

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

team_x.show_player()
team_x.total_XP()
