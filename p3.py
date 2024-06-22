# 프로젝트 문제 3번
input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
N = 4

forest = []

def problem3(input):
    bear_size = 2
    honeycomb_count = 0
    time = 0
    bear_x, bear_y = 0, 0
    # 입력 힌트

    # forest 리스트를 input 리스트로 초기화
    forest = [row[:] for row in input]
    
    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0
    print("곰의 초기 위치 x : {0}, y : {1}".format(bear_x, bear_y))

    #여기에서부터 코드를 작성하세요.

    while True:
        # 현재 위치에서 먹을 수 있는 벌집을 찾습니다.
        reachable_hives = bfs(forest, bear_x, bear_y, bear_size)
        
        if not reachable_hives:
            # 더 이상 먹을 벌집이 없으면 종료합니다.
            break
        
        # 가장 가까운 벌집을 먹으러 갑니다.
        dist, hive_x, hive_y = reachable_hives[0]
        time += dist
        honeycomb_count += 1
        forest[hive_x][hive_y] = 0  # 벌집을 먹고 빈칸으로 만듭니다.
        bear_x, bear_y = hive_x, hive_y

        # 곰의 크기를 증가시킵니다.
        if honeycomb_count == bear_size:
            bear_size += 1
            honeycomb_count = 0

    return time

from collections import deque

def bfs(forest, start_x, start_y, bear_size):
    N = len(forest)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start_x, start_y, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[start_x][start_y] = True
    reachable_hives = []

    while queue:
        x, y, dist = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if forest[nx][ny] <= bear_size:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
                    if 0 < forest[nx][ny] < bear_size:
                        reachable_hives.append((dist + 1, nx, ny))

    reachable_hives.sort()  # 거리순, 가장 위, 가장 왼쪽 순으로 정렬
    return reachable_hives

    result = 0
    return result

result = problem3(input)

assert result == 14
print("정답입니다.")