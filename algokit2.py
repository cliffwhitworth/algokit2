# Return transpose, rows, and columns of a matrix
class Matrix:
    def __init__(self, m):
        if [row for row in m if len(row) != len(m[0])]:
            raise ValueError("Rows need to be of equal length")
            
        self.matrix = [[int(i) for i in row.split()] for row in m.split('\n')]
        
    def __iter__(self):
        yield from self.matrix
        
    def show(self):
        return self.matrix
        
    def transpose(self):
        return [[row[i] for row in self.matrix] for i in range(len(self.matrix[0]))]
        
    def row(self, index):
        return self.matrix[index-1]
    
    def col(self, index):
        return self.transpose()[index-1]
    
    def saddle_points(self):
        points = []
        for i, row in enumerate(self.matrix):
            for j, col in enumerate(zip(*self.matrix)):          
                if max(row) == min(col):
                    points.append({'row': i+1, 'column': j+1})

        return points
    
matrix = Matrix('1 2 3\n4 5 6\n7 8 9\n8 7 6')
print(matrix.show())
print(matrix.transpose())
print(matrix.row(4))
print(matrix.col(3))
print(matrix.saddle_points())