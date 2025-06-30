class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        boolean answer = true;
        
        boolean temp1 = true;
        boolean temp2 = true;
        
        if (x1==false && x2 == false) {
            temp1 = false;
        }
        
        if (x3 == false && x4 == false) {
            temp2 = false;
        }
        
        if (temp1 == true && temp2 == true) {
            answer = true;
        } else {
            answer = false;
        }
        
        
        
        
        return answer;
    }
}