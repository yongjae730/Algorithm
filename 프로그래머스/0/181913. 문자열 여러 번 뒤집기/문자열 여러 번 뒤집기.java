class Solution {
    public String solution(String my_string, int[][] queries) {
        
        // 1. String을 StringBuilder로 변환
        StringBuilder sb = new StringBuilder(my_string);
        
        // 2. queries 배열을 순회
        for (int[] query:queries) {
            int s = query[0];
            int e = query[1];
            
            // 3. s부터 e까지의 부분 문자열을 추출
            // sb.substring(s. e + 1) 에서 e+1을 하는 이유 :
            // substring(beginIndex, endIndex) 메소드는 endIndex를 포함하지 않으므로
            String part = sb.substring(s, e+1);
            
            // 4. 추출한 부분 문자열을 뒤집기 위해 새로운 StringBuilder를 생성하고 reverse()호출
            StringBuilder reversedPart = new StringBuilder(part);
            reversedPart.reverse();
            
            // 5. 원래 StringBuilder의 s부터 e까지의 영역을 뒤집힌 문자열로  교체
            // replace(start, end, str) 메소드 역시 end를 포함하지 않음
            sb.replace(s,e+1,reversedPart.toString());
        }
        
        return sb.toString();
    }
}