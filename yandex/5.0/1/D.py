if __name__ == "__main__":
    matrix = []

    for i in range(8):
        matrix.append(list(input()))

    for i in range(8):
        for j in range(8):
            if matrix[i][j] == 'B':

                ii = i - 1
                jj = j - 1

                while ii >= 0 and jj >= 0 and (matrix[ii][jj] != 'R' and matrix[ii][jj] != 'B'):
                    matrix[ii][jj] = 'k'

                    ii -= 1
                    jj -= 1

                ii = i + 1
                jj = j + 1

                while ii < 8 and jj < 8 and (matrix[ii][jj] != 'R' and matrix[ii][jj] != 'B'):
                    matrix[ii][jj] = 'k'

                    ii += 1
                    jj += 1

                ii = i + 1
                jj = j - 1

                while ii < 8 and jj >= 0 and (matrix[ii][jj] != 'R' and matrix[ii][jj] != 'B'):
                    matrix[ii][jj] = 'k'

                    ii += 1
                    jj -= 1

                ii = i - 1
                jj = j + 1

                while ii >= 0 and jj < 8 and (matrix[ii][jj] != 'R' and matrix[ii][jj] != 'B'):
                    matrix[ii][jj] = 'k'

                    ii -= 1
                    jj += 1

            elif matrix[i][j] == 'R':
                ii = i + 1
                jj = j + 1

                while ii < 8 and matrix[ii][j] != 'B' and matrix[ii][j] != 'R':
                    matrix[ii][j] = 'k'
                    ii += 1

                while jj < 8 and matrix[i][jj] != 'B' and matrix[i][jj] != 'R':
                    matrix[i][jj] = 'k'
                    jj += 1

                ii = i - 1
                jj = j - 1

                while ii >= 0 and matrix[ii][j] != 'B' and matrix[ii][j] != 'R':
                    matrix[ii][j] = 'k'
                    ii -= 1

                while jj >= 0 and matrix[i][jj] != 'B' and matrix[i][jj] != 'R':
                    matrix[i][jj] = 'k'
                    jj -= 1

    c = 0

    for i in range(8):
        for j in range(8):
            if matrix[i][j] == '*':
                c += 1
    print(c)