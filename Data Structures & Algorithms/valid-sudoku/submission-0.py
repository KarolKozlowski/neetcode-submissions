import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        output = True

        rows =    [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                element = board[r][c]

                if element == '.':
                    continue

                if element in rows[r]:
                    output = False
                else:
                    rows[r].add(element)

                if element in columns[c]:
                    output = False
                else:
                    columns[c].add(element)

                square_row = math.floor(r/3)
                square_column = math.floor(c/3)
                square = square_row * 3 + square_column

                if element in squares[square]:
                    output = False
                else:
                    squares[square].add(element)



        return output
        