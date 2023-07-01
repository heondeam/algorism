from sys import stdin as s
from collections import deque

s = open("input.txt", "rt")
""" 
문제

의찬이는 '아주 소프트웨어'의 본사 건물 관리자이다. 
평소처럼 따분한 일과를 보내던 어느 날, 아주 소프트웨어 본사의 엘리베이터가 고장이 났다. 
회사 사람들에게 엘리베이터를 수리하는 데 하루가 걸린다고 하자 사람들은 불평을 토하기 시작했다. 
의찬이는 어쩔 수 없이 관리실에서만 조작이 가능한 비상용 엘리베이터를 사용하기로 하였다.

비상용 엘리베이터는 최대 1명만 탑승할 수 있고 관리실에서만 조작이 가능하다. 
관리실에는 엘리베이터를 이동시킬 수 있는 버튼들이 있어 관리실에서 원하는 층에 해당하는 버튼을 누르면 엘리베이터를 해당 층으로 이동시킬 수 있다.

의찬이는 매일 관리실의 CCTV를 보면서 서면서 회사 사람들의 이동 패턴들을 지겹도록 봐왔기 때문에 
CCTV를 통해 엘리베이터 앞에 기다리고 있는 사람이 누구인지 보기만 해도 어느 층으로 가려고 하는지 알 수 있다. 
의찬이는 CCTV를 통해 기다리고 있는 사람이 누구인지 확인하고 최소한의 조작으로 엘리베이터를 이동시켜 각자 원하는 층에 내려주려고 한다.

각 층에 한 명씩의 사람들이 기다리고 있고, 
사람들을 모두 원하는 층에 내려주기 위해 버튼을 눌러야 하는 최소 횟수와 눌러야하는 버튼 순서를 출력한다. 
엘리베이터는 처음에 1층에 위치하고 있다.

첫째 줄에는 건물 층 수 N 이 주어진다. (2 ≤ N ≤ 100,000)
다음 줄에는 N개의 정수 A1, ..., AN이 주어지는데 Ai는 i층에서 기다리고 있는 사람이 가고자 하는 층이다. (1 ≤ Ai ≤ N, 1 ≤ i ≤ N)
이때, 현재 층으로 이동하고자 하는 경우는 없다.(Ai ≠ i)

첫째 줄에는 버튼을 눌러야 하는 최소 횟수를 출력한다.
다음 줄에는 버튼을 눌러야 하는 순서를 공백으로 구분하여 출력한다. 
가능한 방법이 여러가지라면 그 중 하나를 아무거나 출력한다.
"""

def DFS(v):

    stack = [v]
    visited[v] = 1

    while stack:
        nowVertex = stack.pop()

        for i in graph[nowVertex]:
            if visited[i] != 1:
                stack.append(i)
                visited[i] = 1



if __name__ == "__main__":
    n = int(s.readline().rstrip())
    pushes = [0] + list(map(int, s.readline().rstrip().split()))

    visited = [0] * (n + 1)

    graph = []

    for i in range(n + 1):
        graph.append([])

    for i in range(1, n + 1):
        graph[i].append(pushes[i])

    DFS(1)

    print(visited)
