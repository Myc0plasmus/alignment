import unittest
from src.aligner import globalAlignment

class AlignerTest(unittest.TestCase):
    @classmethod
    def setUpClass(self): 
        self.globalAligner = globalAlignment(seq1="ATG", seq2="ACGT")

    def test_getScoreComparison(self):
        print("Running test for getScoreOnPos")
        assert self.globalAligner.getScoreOnPos(0,0) == self.globalAligner.matchScore
        assert self.globalAligner.getScoreOnPos(1,1) == self.globalAligner.mismatchScore
        assert self.globalAligner.getScoreOnPos(2,2) == self.globalAligner.matchScore
        assert self.globalAligner.getScoreOnPos(1,3) == self.globalAligner.matchScore
        print("OK")

    def test_matrix_generation(self):
        print("Running test for populateMatrices")
        self.globalAligner.populateMatrices()


        expectedScoreMatrix = [[0, -2, -4, -6], [-2, 1, -1, -3], [-4, -1, 0, -2], [-6, -3, -2, 1], [-8, -5, -2, -1]]
        expectedDirectionMatrix = [[[0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [-1, -1], [0, -1], [0, -1]], [[0, 0], [-1, 0], [-1, -1], [-1, -1]], [[0, 0], [-1, 0], [-1, -1], [-1, -1]], [[0, 0], [-1, 0], [-1, -1], [-1, 0]]]

        assert self.globalAligner.scoreMatrix == expectedScoreMatrix
        assert self.globalAligner.directionMatrix == expectedDirectionMatrix

        self.globalAligner.clearMatrices()
        print("OK")


    def test_findPath(self):
        # print(self.globalAligner.seq1)
        # print(self.globalAligner.seq2)
        print("Running test for findPath")
        self.globalAligner.populateMatrices()
        # for i in self.globalAligner.scoreMatrix:
        #     print(i)
        # for i in self.globalAligner.directionMatrix:
        #     print(i)
        # print()
        expectedPath = [[-1, -1], [-1, -1], [-1, -1], [-1, 0]] 
        self.globalAligner.findPath()
        # print(self.globalAligner.path)
        assert self.globalAligner.path == expectedPath
        self.globalAligner.clearMatrices
        print("OK")

    def test_printPath(self):
        print("Running test for findPath")
        self.globalAligner.populateMatrices()
        print(self.globalAligner.seq1)
        print(self.globalAligner.seq2)
        for i in self.globalAligner.scoreMatrix:
            print(i)
        for i in self.globalAligner.directionMatrix:
            print(i)
        print()
        self.globalAligner.findPath()
        print(self.globalAligner.path)
        self.globalAligner.printPath()

        print("OK")
    
        


if __name__ == "__main__":
    unittest.main()
