import random

class Matrix(object):
    """docstring for Matrix."""
    def __init__(self, numRows, numCols, isRandom):
        # super(Matrix, self).__init__()
        self.numRows = numRows
        self.numCols = numCols
        self.values = []
        values = self.values
        for rows in range(0, numRows):
            colValues = []
            for cols in range(0, numCols):
                r = 0.00
                if(isRandom):
                    r = random.randint(1, 100)/100.0
                colValues.append(r)
            values.append(colValues)
        print(values)

    def printToConsole(self):
        numRows = self.numRows
        numCols = self.numCols
        values = self.values
        for i in range(0, numRows):
            for j in range(0, numCols):
                print(str(values[i][j]), end='\t')
            print("\n")

    def setValue(self, r, c, v):
        self.values[r][c] = v

    def getValue(self, r, c):
        self.values[r][c]

    def getRows(self):
        return self.numRows

    def getCols(self):
        return self.numCols
