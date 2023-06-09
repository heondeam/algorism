from sys import stdin as s

s = open("input.txt", "rt")
""" 
문제

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 
가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
"""



if __name__ == "__main__":
    n = int(s.readline().rstrip())
    A = list(map(int, s.readline().rstrip().split()))

    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(1, n+1):

        maxValue = 0

        # 이전 수부터 첫번째 수까지 반복문
        for j in range(i-1, 0, -1):
            
            # 현재 수보다 작은 이전 수 중에서 가장 긴 길이를 count
            if A[j-1] < A[i-1] and dp[j] > maxValue:
                maxValue = dp[j]

            dp[i] = maxValue + 1

    print(max(dp))


""" 

모든 증가하는 부분 수열을 구한다?
그 중 가장 길이가 긴 것의 길이를 출력한다. - 완전탐색

동적 프로그래밍

각 숫자가 내가 만들고자 하는 증가수열의 마지막 항이라고 생각해보자.
1) 10이 내가 만들고자 하는 증가수열의 마지막 항이다.
10
2) 20이 내가 만들고자 하는 증가수열의 마지막 항이다.
10
10, 20
3) 10이 내가 만들고자 하는 증가수열의 마지막 항이다.
10
4) 30이 내가 만들고자 하는 증가수열의 마지막 항이다.
10, 30
10, 20, 30
20, 30
5) 20이 내가 만들고자 하는 증가수열의 마지막 항이다.
10
10, 20
6) 50이 내가 만들고자 하는 증가수열의 마지막 항이다.
10, 50
20, 50
30, 50
10, 20, 30, 50
20, 30, 50
30, 50


dp 테이블을 만든다 (A[i]로 끝나는 가장 긴 부분수열의 길이)

0 1 2 3 4 5 6
0 1 2 1 3 2 4


dp = [0] * (n + 1)

for i in range(1, n+1):

    max = 0

    for j in range(i-1, 0, -1):
        
        if A[j] < A[i] and dp[j] > max:
            max = dp[j]
        
        dp[i] = max + 1
        if dp[i] > res:
            res = dp[i]
"""