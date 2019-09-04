# 그래프 경로
# 실패한 코드

def find(S, G):
    global graph
    for i in range(len(graph), 0, -1):
        if graph[i][-1] == G:
            for j in range(i-1):
                if graph[j][-1] == graph[i][0]:
                    if graph[j][0] == S:
                        return 1
                    else:
                        nG = graph[j][0]
                        find(S, nG)
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = list(map(int, input().split()))

    graph = []
    for e in range(E):
        path = list(map(int, input().split()))
        graph.append(path)
    print(graph)

    S, G = list(map(int, input().split()))

    if find(S, G) == 1:
        print(1)
    else:
        print(0)