import sys

n = int(input())

arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

dic=dict()

for i in arr:#빈도수 구하기
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

mx=max(dic.values())#빈도수 중 최대값 구하기
mx_dic=[]#최빈값 숫자를 저장할 배열

for i in dic:#빈도수 딕셔너리에서
    if mx==dic[i]:#최빈값의 key저장
        mx_dic.append(i)

print(round(sum(arr)/n))
print(arr[len(arr)//2])
if len(mx_dic)>1:#최빈값이 여러개라면
    print(mx_dic[1])#두번째로 작은 값  3)최빈값
else:#하나라면
    print(mx_dic[0])#해당 값 출력  3)최빈값
print(max(arr)-min(arr))