class Matrix(object):
    def __init__(self, matrix_string):
        # divide each string my the newline character into a list
        # each item in the list is a string representing one row
        self.matrix_split = matrix_string.split('\n')

    def row(self, index):
        # select the row at index, and convert each element to an integer
        return [int(i) for i in self.matrix_split[index-1].split()]

    def column(self, index):
        # loop through each row, selecting the value at the index. which creates the column
        return [int(i.split()[index-1]) for i in self.matrix_split]
