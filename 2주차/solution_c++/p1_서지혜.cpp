#include <iostream>
#include <stack>
#include <string>
 
using namespace std;
 
int main(){
    string input;
    stack<char> s;
    int result = 0;
    
    cin >> input;
    
    for(int i = 0; i < input.size(); i++) {
        if(input[i] == '(')
            s.push(input[i]);
        else {
            s.pop();
            if(input[i-1] == '(')
                result += s.size();
            else
                result += 1;  
        }
    }
    cout << result << endl;
    return 0;
}
