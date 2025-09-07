import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        List<Integer> resultList = new ArrayList<>();
        
        for (String str : intStrs) {
            // 문자열 슬라이싱 및 정수 변환
            int num = Integer.parseInt(str.substring(s, s+l));
            
            // 조건 비교
            if (num > k) {
                
                resultList.add(num);
            }
        }
        
        // 리스트를 배열로 변환하여 반환
        int[] answer = new int[resultList.size()];
        for (int i = 0; i < resultList.size(); i++) {
            answer[i] = resultList.get(i);
        }
        
        return answer;
    }
}