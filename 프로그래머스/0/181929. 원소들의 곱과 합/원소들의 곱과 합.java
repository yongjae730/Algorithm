class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int sum_num = 0;
        int times_num = 1;
        for (int i = 0; i<num_list.length; i++) {
            sum_num += num_list[i];
            times_num = times_num*num_list[i];
        }
        return answer = Math.pow(sum_num,2) > times_num ? 1 : 0;
    }
}