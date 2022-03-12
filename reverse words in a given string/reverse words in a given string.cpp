
 class Solution
{
    public:
    //Function to reverse words in a given string.
    string reverseWords(string S) 
    { 
        // code here 
        vector<string> vect;
        string holder = "";
        string ans = "";
        for(int i = 0; i < S.size(); i++){
            if (S[i] == '.') {
                vect.push_back(holder);
                holder = "";
                continue;
            }
            else
            holder += S[i];
        }
        vect.push_back(holder);
        int len = vect.size() - 1;
        int j = 0;
        while (j != len) {
            ans += vect.back();
            vect.pop_back();
            ans += ".";
            j += 1;
        }
        ans += vect.back();
        return ans;
        
    } 
};
