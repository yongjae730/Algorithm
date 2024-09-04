def hex(num):
    hex_to_bin = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    result = ''
    for i in num:
        result += hex_to_bin[i]

    return result
def password(ans):
    results = ''
    for j in range(len(ans)-1,-1,-1):
        if ans[j] == '1':
            results += ans[j::-1]
            break

    return results

def find_key(answer):
    pattern = {
        '001101': '0',
        '010011': '1',
        '111011': '2',
        '110001': '3',
        '100011': '4',
        '110111': '5',
        '001011': '6',
        '111101': '7',
        '011001': '8',
        '101111': '9',
    }
    result = ''
    for k in range(len(answer)-1,-1,-1):
        if answer[k][::-1] in pattern:
            result += pattern[answer[k][::-1]]+' '

    return result



num = input()

ans = hex(num)

answer = password(ans)

total_pass = []

for i in range(0,len(answer),6):
    if i+6 < len(answer):
        total_pass.append(answer[i:i+6])
    else:
        break

real_result = find_key(total_pass)

print(real_result)