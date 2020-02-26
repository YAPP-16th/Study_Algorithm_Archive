def check_next_index(board, i, j, current_value) :
    try:
        if (board[i][j] != 0) and (j != -1 and i != -1):
            if board[i][j] == 1 or current_value + 1 < board[i][j]:
                board[i][j] = current_value + 1
                return True
            else :
                return False
        else :
            return False
    except IndexError:
        return False

N,M = list(map(int, input().split()))

board = []

for i in range(N) :
    line = list(map(int, list(input())))
    board.append(line)

locations = [[0,0]]
while True :
    i,j = locations.pop(0)

    if check_next_index(board, i - 1, j, board[i][j]):
        if [i - 1,j] not in locations :
            locations.append([i - 1,j])
    if check_next_index(board, i + 1, j, board[i][j]):
        if [i + 1,j] not in locations :
            locations.append([i + 1,j])
    if check_next_index(board, i, j - 1, board[i][j]):
        if [i,j - 1] not in locations :
            locations.append([i,j - 1])
    if check_next_index(board, i, j + 1, board[i][j]):
        if [i,j + 1] not in locations :
            locations.append([i,j + 1])

    if i == N-1 and j == M-1 :
        print(board[i][j])
        break
