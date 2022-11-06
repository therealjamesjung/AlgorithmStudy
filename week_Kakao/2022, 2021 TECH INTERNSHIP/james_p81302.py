

def dfs(place, row, col, depth, start_r, start_c):
    if row == start_r and col == start_c and depth > 0:
        return True
    if row > 4 or col > 4 or row < 0 or col < 0 or depth == 3 or place[row][col] == 'X':
        return True
    if place[row][col] == 'P' and depth > 0:
        return False
    return dfs(place, row + 1, col, depth + 1, start_r, start_c) and \
        dfs(place, row, col + 1, depth + 1, start_r, start_c) and \
        dfs(place, row - 1, col, depth + 1, start_r, start_c) and \
        dfs(place, row, col - 1, depth + 1, start_r, start_c)


def solution(places):
    answer = []

    for place in places:
        flag = 1
        for i, row in enumerate(place):
            for j, col in enumerate(row):
                if col == 'P':
                    if not dfs(place, i, j, 0, i, j):
                        answer.append(0)
                        flag = 0
                        break
            if not flag:
                break
        if flag:
            answer.append(1)

    return answer


print(solution(places))
