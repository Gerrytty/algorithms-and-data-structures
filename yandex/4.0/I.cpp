#include "iostream"
#include "stack"

using namespace std;

int main() {

	char seq[100010];
	char* ptr = seq;

	stack<char> s;

	cin >> seq;

	bool ok = true;

	while (*ptr != '\0' && ok) {

		char symbol = *ptr;
		if (symbol == '(' || symbol == '{' || symbol == '[') {
			s.push(symbol);
		} else {
			if (s.size() < 1) {
				ok = false;
			} else {
				char lastSymbol = s.top();
				s.pop();
				if (symbol == ')' && lastSymbol != '(') {
					ok = false;
				} else if (symbol == '}' && lastSymbol != '{') {
					ok = false;
				} else if (symbol == ']' && lastSymbol != '[') {
					ok = false;
				}
			}
		}

		ptr++;
	}

	if (!ok || s.size() > 0) {
		cout << "no\n";
	} else {
		cout << "yes\n";
	}

}