#include <stack>
#include <string>
#include <stdio.h>
#include <iostream>
using namespace std; 

int ans;

void fragment(stack<char> stack, string str) {
	for (size_t i = 0; i < str.size(); i++) {
		if (str.at(i) == '(') {
			stack.push('(');
		}
		else {
			if (str.at(i - 1) == '(') {
				stack.pop();
				ans += stack.size();
			}
			else {
				stack.pop();
				ans += 1;
			}
		}
	}
}

int main(void) {
	string str;
	cin >> str;
	stack<char> stack;
	fragment(stack, str);
	printf("%d\n", ans);
	return 0;
}
