class Game:
    def __init__(self,id):
        self.p1move=False
        self.p2move=False
        self.ready=False
        self.id=id
        self.moves=[None,None]
        self.wins=[0,0]
        self.egalite=0

    def get_player_move(self,p):
        return self.moves[p]

    def play(self,player,move):
        self.moves[player]=move
        if player==0:
            self.p1move=True
        else:
            self.p2move=True

    def connected(self):
        return self.ready

    def bothMove(self):
        return self.p2move and self.p1move

    def winner(self):

        p1= self.moves[0]
        p2= self.moves[1]

        winner=-1
        if p1=="R" and p2=="S":
            winner=0
        elif p1=="S" and p2=="R":
            winner=1
        elif p1=="P" and p2=="R":
            winner=0
        elif p1=="R" and p2=="P":
            winner=1
        elif p1=="S" and p2=="P":
            winner=0
        elif p1 == "P" and p2 == "S":
            winner = 1
        return winner

    def resetMove(self):
        self.p1move=False
        self.p2move=False