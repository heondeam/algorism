from sys import stdin as s

s = open("input.txt", "rt")

""" 
문제

bryan은 PPAP를 좋아한다. 
bryan은 어떻게 하면 사람들에게 PPAP를 전파할 수 있을까 고민하던 중 PPAP 문자열이라는 것을 고안하게 되었다.
PPAP 문자열은 문자열 P에서 시작하여, 
문자열 내의 P를 PPAP로 바꾸는 과정을 반복하여 만들 수 있는 문자열로 정의된다. 
정확하게는 다음과 같이 정의된다.
P는 PPAP 문자열이다.
PPAP 문자열에서 P 하나를 PPAP로 바꾼 문자열은 PPAP 문자열이다.
예를 들어 PPAP는 PPAP 문자열이다. 
또한, PPAP의 두 번째 P를 PPAP로 바꾼 PPPAPAP 역시 PPAP 문자열이다.
문자열이 주어졌을 때, 이 문자열이 PPAP 문자열인지 아닌지를 알려주는 프로그램을 작성하여라.

첫 번째 줄에 문자열이 주어진다. 문자열은 대문자 알파벳 P와 A로만 이루어져 있으며, 문자열의 길이는 1 이상 1,000,000 이하이다.
첫 번째 줄에 주어진 문자열이 PPAP 문자열이면 PPAP를, 아닌 경우 NP를 출력한다.
"""
# 스택? O(n)에 풀자
sentence = s.readline().rstrip()
org_str = ["P", "P", "A", "P"]
stack = []

# PPAP = P 
for i in range(len(sentence)):
    stack.append(sentence[i])

    if len(stack) >= 4 and stack[-4:] == org_str:
        for i in range(4):
            stack.pop()
        stack.append("P")

if stack == ["P"]:
    print("PPAP")
else:
    print("NP")
