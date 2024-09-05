import sys

sys.stdin = open('input.txt', 'w')

T = int(input())
for tc in range(1, T + 1):
    # N 세로 M 가로 K 배양시간
    N, M, K = map(int, input().split())
