import numpy as np

class globalAlignment:
    def __init__(self, matchScore=1, mismatchScore=-1, gapPenaltyScore=-2, seq1 = None, seq2 = None):
        self.matchScore = matchScore 
        self.mismatchScore = mismatchScore
        self.gapPenaltyScore = gapPenaltyScore
        self.scoreMatrix = []
        self.directionMatrix = []
        self.seq1 = seq1
        self.seq2 = seq2
        self.populatedMatrices = False
        self.path = []


    def clearMatrices(self):
        self.scoreMatrix = []
        self.directionMatrix = []
        self.populatedMatrices = False

    def clearSequences(self):
        self.seq1 = ""
        self.seq2 = ""
    
    def getScoreOnPos(self,pos1, pos2, seq1 = None, seq2 = None):
        if seq1 is None:
            if self.seq1 is None:
                raise ValueError("Value of seq1 has not been explicitly provided in getScoreOnPos and class wide seq1 is None") 
            seq1 = self.seq1

        if seq2 is None:
            if self.seq2 is None:
                raise ValueError("Value of seq2 has not been explicitly provided in getScoreOnPos and class wide seq2 is None")           
            seq2 = self.seq2

        if seq1[pos1] == seq2[pos2]:
            return self.matchScore
        else:
            return self.mismatchScore

    def populateMatrices(self, seq1 = None, seq2 = None):
        if seq1 is None:
            if self.seq1 is None:
                raise ValueError("Value of seq1 has not been explicitly provided in populateMatrix and class wide seq1 is None") 
            seq1 = self.seq1

        if seq2 is None:
            if self.seq2 is None:
                raise ValueError("Value of seq2 has not been explicitly provided in populateMatrix and class wide seq2 is None")           
            seq2 = self.seq2

        matrixWidth = len(seq1) + 1
        matrixHeight = len(seq2) + 1

        # self.scoreMatrix = np.zeros([matrixHeight, matrixWidth])
        self.scoreMatrix = [[0 for i in range(matrixWidth)] for j in range(matrixHeight)] 
        self.directionMatrix = [[[] for i in range(matrixWidth)] for j in range(matrixHeight)] 

        for i in range(matrixWidth):
            self.scoreMatrix[0][i] = i * self.gapPenaltyScore
            self.directionMatrix[0][i] = [0,0]

        for i in range(matrixHeight):
            self.scoreMatrix[i][0] = i * self.gapPenaltyScore
            self.directionMatrix[i][0] = [0,0] 

        choiceTranslationDict = {0 : [-1,-1], 1 : [-1,0], 2 : [0,-1]}

        for i in range(1,matrixHeight):
            for j in range(1,matrixWidth):
                choiceList = [self.scoreMatrix[i-1][j-1]+self.getScoreOnPos(j-1,i-1),
                              self.scoreMatrix[i-1][j]+self.gapPenaltyScore,
                              self.scoreMatrix[i][j-1]+self.gapPenaltyScore
                              ]
                
                self.scoreMatrix[i][j] = max(choiceList)
                self.directionMatrix[i][j] = choiceTranslationDict[choiceList.index(max(choiceList))]
        self.populatedMatrices = True

    def findPath(self): 
        if not self.populatedMatrices :
            raise ValueError("Matrices have not been populated")
        path = []
        y = len(self.directionMatrix) - 1
        x = len(self.directionMatrix[0]) - 1
        currentDirections = self.directionMatrix[y][x]
        while currentDirections != [0,0] :
            path.insert(0,currentDirections)
            y += currentDirections[0]
            x += currentDirections[1]
            currentDirections = self.directionMatrix[y][x]
        self.path = path

    def printPath(self):
        if self.seq1 is None or self.seq2 is None:
            raise ValueError("Neither of sequence strings cannot be None")
        pos = [0,0]
        seq1str = ""
        seq2str = ""
        for step in self.path:
            pos = [p-s for p,s in zip(pos,step)]
            print(pos)
            match step:
                case [-1,-1]:
                    seq1str = seq1str + self.seq1[pos[1]-1] 
                    seq2str = seq2str + self.seq2[pos[0]-1] 
                case [-1,0]:
                    seq1str = seq1str + "_" 
                    seq2str = seq2str + self.seq2[pos[0]-1]
                case [0,-1]:
                    seq1str = seq1str + self.seq1[pos[1]-1] 
                    seq2str = seq2str + "_"
        print(" ".join(list(seq1str)))
        print(" ".join([ " " if i == "_" or j == "_" else ("|" if i == j else ".") for i,j in zip(seq1str,seq2str)]))
        print(" ".join(list(seq2str)))


                    



if(__name__ == "__main__"):
    aligner = globalAlignment(seq1 = "AAA", seq2 = "GGGG")
    aligner.populateMatrices()
    print(aligner.scoreMatrix)
