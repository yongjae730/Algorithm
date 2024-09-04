#numbers = []

#for a in range(0, 9):
#    num = int(input())
#    numbers.append(i)
    
#print(max(numbers))
#print(numbers.index(max(numbers))+1)
# 위의답은 틀림
numbers = []
for i in range(0, 9):
    num = int(input())
    numbers.append(num)
    
print(max(numbers))
print(numbers.index(max(numbers))+1)