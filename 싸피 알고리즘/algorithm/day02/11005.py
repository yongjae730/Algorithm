numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def power(N, B):
    if N < B:
        return numbers[N]  # 'Z'
    return power(N // B, B) + numbers[N % B]

N, B = map(int, input().split())


print(power(N,B))
