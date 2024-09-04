'''
주어진 리스트는 여러 개의 문자열로 구성되어 있다.
❖ 이 리스트에서 길이가 가장 긴 문자열을 반환하는 longest_string 함수를 완성하시오.
❖ 만약 길이가 같은 문자열이 여러 개 있다면, 리스트에서 먼저 찾은 문자열을 반환한다.
❖ 문자열은 길이가 0 인 것도 리스트에 존재할 수 있다.
❖ Python 내장 함수 len 사용시 감점
'''


############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장함수 len 함수를 사용하지 않습니다.
def longest_string(str_list):
    str_cnt={} # 딕셔너리에 키-밸류 형태로 길이 측정
    
    for i in str_list:
        cnt = 0     # 키값으로 할당할 cnt 변수 생성
        for j in i:
            cnt += 1 # 인덱스별 문자열을 순회하여 cnt+=1 을 해줌으로써 길이를 측정

        str_cnt[i] = cnt #밸류값에 cnt 할당
    
    max(str_cnt.values()) # 가장 높은 밸류 값 추출

    
    




   



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 

print(longest_string(["apple", "banana", "cherry", "date"]))  # "banana"
print(longest_string(["cat", "caterpillar", "dog", "elephant"]))  # "caterpillar"
print(longest_string(["a", "ab", "abc", "abcd"]))  # "abcd"
