def hex(hex_num):
    hex_dict = {
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
        'F': '1111',
    }
    result =''
    for i in range(len(hex_num)):
        result += hex_dict[hex_num[i]]

    return result

def bin(arr):

    for k in range(len(arr)):
        cnt = 0
        cal = arr[k]
        bin_cal = cal[::-1]
        result = 0
        for q in range(len(bin_cal)):
            result += int(bin_cal[q])*(2**cnt)
            cnt += 1



        print(result,end = ' ')


hex_num = input()
arr = []

ans = hex(hex_num)

for j in range(0,len(ans),7):
    if j+7 < len(ans):
        arr.append(ans[j:j+7])
    else:
        arr.append(ans[j:])
bin(arr)