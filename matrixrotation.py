def rotate_90(matrix):
    matrix =  [list(row[::-1]) for row in zip(*matrix)]
    return matrix

def is_beautiful(matrix):
    if matrix[0][0] < matrix[0][1] and matrix[1][0] < matrix [1][1] and matrix [0][0] < matrix [1][0] and matrix[0][1]< matrix[1][1]:
        return True
    else:
        return False
    



t = int(input())
matrices = []
answer = []

for _ in range(t):
    matrix = []
    for _ in range(2):
        row = list(map(int, input().split()))
        matrix.append(row)
    matrices.append(matrix)

for matrix in matrices:
    temp = []
    for i in range(4):
        matrix = rotate_90(matrix)
        if is_beautiful(matrix):
            temp.append('yes')
    if 'yes' in temp:
        answer.append('yes')
    else:
        answer.append('no')

for ans in answer:
    print(ans)
