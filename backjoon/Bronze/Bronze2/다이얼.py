a = str(input())  
b = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

sum = 0 

for i in a:

    for j in b:
        if i in j:
            num = b.index(j) + 3
            sum += num

print(sum)

# a = str(input())  
# b = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']



# sum = 0 

# for i in a:

#     for j in b:
#         if a[i] in j:
#             num = b.index(j) + 3
#             sum += num

# print(sum)