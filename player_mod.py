class player:
    playerName = None
    playerType = None
    numberOfDeaths = 0
    numberOfKills = 0

    def __init__(self, playerName, playerType):
        self.playerName = playerName
        self.playerType = playerType
        self.numberOfDeaths = 0
        self.numberOfKills = 0

    def playerDeath(self):
        self.numberOfDeaths += 1


