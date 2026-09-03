class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int x = 0; 
        int y = 0;

        for (int i = 0; i < nums.length; i++){
            if (nums[i] == 0) {
                x = Math.max(x,y);
                y = 0; 
            } else{
                y++;
            }
        }
        return Math.max(x,y);
    }

}