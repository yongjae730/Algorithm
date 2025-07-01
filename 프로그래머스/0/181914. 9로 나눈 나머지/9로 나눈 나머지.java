class Solution {
    public int solution(String number) {
        int answer = 0;
        int numbers = 0;
        for (int i =0 ; i< number.length(); i++) {
            numbers += number.charAt(i) -'0';
        }
        answer = numbers%9;
        
        return answer;
    }
}