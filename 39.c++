class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> currentCombination;
        
        backtrack(candidates, target, 0, currentCombination, result);
        
        return result;
    }
    
private:
    void backtrack(const vector<int>& candidates, int remainingTarget, int startIndex, vector<int>& currentCombination, vector<vector<int>>& result) {
        if (remainingTarget == 0) {
            result.push_back(currentCombination);
            return;
        }
        
        if (remainingTarget < 0) {
            return;
        }
        
        for (int i = startIndex; i < candidates.size(); ++i) {
            currentCombination.push_back(candidates[i]);
            backtrack(candidates, remainingTarget - candidates[i], i, currentCombination, result);
            currentCombination.pop_back();
        }
    }
};