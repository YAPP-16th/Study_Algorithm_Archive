def check_ripen_index(board, i, j) :
    try:
        if (board[i][j] != -1 and board[i][j] != 1) and (j != -1 and i != -1):
            board[i][j] = 1
        else :
            return False
        return True
    except:
        return False

def ripen(board, ripe_tomato_location_list, not_ripe_tomato) :
    location_tmp = []

    for ripe_tomato_location in ripe_tomato_location_list :
        i, j = ripe_tomato_location

        if check_ripen_index(board, i-1, j) :
            location_tmp.append([i - 1,j])
            not_ripe_tomato -= 1
        if check_ripen_index(board, i+1, j) :
            location_tmp.append([i + 1, j])
            not_ripe_tomato -= 1
        if check_ripen_index(board, i, j-1) :
            location_tmp.append([i, j - 1])
            not_ripe_tomato -= 1
        if check_ripen_index(board, i, j+1) :
            location_tmp.append([i, j + 1])
            not_ripe_tomato -= 1

    ripe_tomato_location_list.clear()
    ripe_tomato_location_list.extend(location_tmp)

    return not_ripe_tomato


M,N = list(map(int, input().split()))

board = []

for i in range(N) :
    line = list(map(int, input().split()))
    board.append(line)

not_ripe_tomato = 0
ripe_tomato = 0
empty = 0

ripe_tomato_location_list = []
for i in range(N) :
    for j in range(M) :
        if board[i][j] == 0 :
            not_ripe_tomato += 1
        elif board[i][j] == 1 :
            ripe_tomato += 1
            ripe_tomato_location_list.append([i,j])
        else :
            empty += 1

if ripe_tomato + empty == M*N :
    print(0)
else :
    answer = 0
    while True:
        prev_not_ripe_tomato = not_ripe_tomato
        not_ripe_tomato = ripen(board, ripe_tomato_location_list, not_ripe_tomato)

        if(prev_not_ripe_tomato == not_ripe_tomato):
            if not_ripe_tomato == 0 :
                print(answer)
            else :
                print(-1)
            break

        answer += 1