#include <string>
#include <stack>

class Solution {
public:
    std::string decodeString(std::string s) {
        std::stack<int> counts;
        std::stack<std::string> strings;
        std::string currentString = "";
        int k = 0;
        
        for (char c : s) {
            if (isdigit(c)) {
                k = k * 10 + (c - '0');
            } else if (c == '[') {
                counts.push(k);
                strings.push(currentString);
                k = 0;
                currentString = "";
            } else if (c == ']') {
                std::string temp = currentString;
                currentString = strings.top();
                strings.pop();
                int currentK = counts.top();
                counts.pop();
                while (currentK-- > 0) {
                    currentString += temp;
                }
            } else {
                currentString += c;
            }
        }
        
        return currentString;
    }
};