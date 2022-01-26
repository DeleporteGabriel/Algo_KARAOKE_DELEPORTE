class Player:
    def __init__(self, pseudo, nbChanson):
        self.__pseudo = pseudo
        self.__score = [0]*nbChanson
    def getPseudo(self):
        return self.__pseudo
    def getScore(self, numChanson):
        return self.__score[numChanson]
    def replaceScore(self, numChanson, nouveauScore):
        if nouveauScore > self.__score[numChanson]:
            self.__score[numChanson] = nouveauScore
    def moyenneScore(self):
        total = 0
        for i in range(5):
            total = total + self.__score[i]
        return total/5
    def totalScore(self):
        total = 0
        for i in range(5):
            total = total + self.__score[i]
        return total
    def meilleurScore(self):
        max = 0
        numBest = 0
        for i in range(5):
            if max < self.__score[i]:
                max = self.__score[i]
                numBest = i
        return numBest
    def meilleurScorePoints(self):
        max = 0
        for i in range(5):
            if max < self.__score[i]:
                max = self.__score[i]
        return max
    def pireScore(self):
        min = 100
        numPire = 0
        for i in range(5):
            if min > self.__score[i]:
                min = self.__score[i]
                numPire = i
        return numPire
    def afficheScore(self):
        print(self.__score)

class Karaoke:
    def __init__(self, nombreChanson, nomJoueur1):
        self.__nbChanson = nombreChanson
        self.__joueur = {0:Player(nomJoueur1, nombreChanson)}
    def getJoueur(self, numJoueur):
        return self.__joueur[numJoueur]
    def addPlayer(self, nomJoueur):
        self.__joueur[len(self.__joueur)] = Player(nomJoueur, self.__nbChanson)
    def removePlayer(self):
        if len(self.__joueur) > 1:
            self.__joueur.popitem()
    def meilleurScoreChanson(self, chanson):
        listScore = [0] * len(self.__joueur)
        for i in range(len(self.__joueur)):
            listScore[i] = self.__joueur[i].getScore(chanson)
        max = 0
        numBest = 0
        for i in range(len(listScore)):
            if max < listScore[i]:
                max = listScore[i]
                numBest = i
        return numBest
    def meilleurScoreTotal(self):
        listScoreTotal = [0] * len(self.__joueur)
        for i in range(len(self.__joueur)):
            listScoreTotal[i] = self.__joueur[i].totalScore()
        max = 0
        numBest = 0
        for i in range(len(listScoreTotal)):
            if max < listScoreTotal[i]:
                max = listScoreTotal[i]
                numBest = i
        return numBest
    def meilleurScoreTout(self):
        listScoreBest = [0] * len(self.__joueur)
        for i in range(len(self.__joueur)):
            listScoreBest[i] = self.__joueur[i].meilleurScorePoints()
        max = 0
        numBest = 0
        for i in range(len(listScoreBest)):
            if max < listScoreBest[i]:
                max = listScoreBest[i]
                numBest = i
        return numBest
    def meilleureMoyenne(self):
        listScoreBest = [0] * len(self.__joueur)
        for i in range(len(self.__joueur)):
            listScoreBest[i] = self.__joueur[i].moyenneScore()
        max = 0
        numBest = 0
        for i in range(len(listScoreBest)):
            if max < listScoreBest[i]:
                max = listScoreBest[i]
                numBest = i
        return numBest
    
Main = Karaoke(5, "Fusette")
Main.addPlayer("Jean")
Main.addPlayer("Billy")
Main.addPlayer("LePauvreMecQuiVaEtreSupprime")
Main.getJoueur(3).replaceScore(0, 200)
Main.removePlayer()

Main.getJoueur(0).replaceScore(1, 103)
Main.getJoueur(1).replaceScore(0, 156)
Main.getJoueur(2).replaceScore(0, 56)
Main.getJoueur(2).replaceScore(1, 78)
Main.getJoueur(2).replaceScore(2, 34)

print("Score joueur 0 :")
Main.getJoueur(0).afficheScore()
print("Score joueur 1 :")
Main.getJoueur(1).afficheScore()
print("Score joueur 2 :")
Main.getJoueur(2).afficheScore()

print("Meilleur score du joueur 2 :")
print(Main.getJoueur(2).meilleurScorePoints())

print("Joueur avec le meilleur score de la deuxième chanson :")
print(Main.meilleurScoreChanson(1))

print("Joueur avec le meilleur total de score :")
print(Main.meilleurScoreTotal())
print("Joueur avec le meilleur score toutes chansons confondu :")
print(Main.meilleurScoreTout())
print("Joueur avec la meilleure moyenne :")
print(Main.meilleureMoyenne())