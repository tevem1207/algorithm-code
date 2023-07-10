def dfs(life, cost, saved):
    global answer

    answer = max(answer, saved)
    if cost >= life:
        return

    for i, town in enumerate(towns):
        next_cost = cost + town[0]
        if life >= next_cost:
            if visited[i] == "0":
                visited[i] = "1"
                tmp = "".join(visited)

                if tmp in visited_set:
                    visited[i] = "0"
                    continue

                visited_set.add(tmp)
                dfs(life-next_cost, next_cost, saved+town[1])
                visited[i] = "0"


answer = 0
n, k = map(int, input().split())
towns = sorted(zip(map(int, input().split()), map(int, input().split())))
visited = ["0"] * n
visited_set = set()
dfs(k, 0, 0)

print(answer)
