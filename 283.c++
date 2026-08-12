class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        if (nums.empty()) return; // Fixed: void function must return void, not 0

        int i = 0; // Tracks position for the next non-zero element

        for (int j = 0; j < nums.size(); j++) {
            if (nums[j] != 0) {
                swap(nums[j], nums[i]);
                i++;
            } // Closes if block
        }     // Closes for loop
    }         // Closes moveZeroes function
};             // Closes Solution class