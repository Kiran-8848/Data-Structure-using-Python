class Solution {
public:
    bool isPalindrome(int x) {
       int reversedhalf = 0;

       if ( x<0 || (x !=0 && x%10 == 0)){
        return false;
       }
        while ( x > reversedhalf){
           reversedhalf = ( reversedhalf *10) + (x%10);
           x /=10;
        }
        return x == reversedhalf || x == reversedhalf /10;
    }
};