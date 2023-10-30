#include "iostream"
#include "cmath"

using namespace std;

int get(int a, int b, int mode) {
	if (mode == 0) {
		return min(a, b);
	} else {
		return max(a, b);
	}
}

int getSeq(int arr[], int maxSize, int left, int right, int mode, int res) {

	left += (maxSize / 2);
	right += (maxSize / 2);

	while (left < right) {
		if (left % 2 == 1) {
			res = get(res, arr[left], mode);
			left += 1;
		}

		if (right % 2 == 1) {
			right -= 1;
			res = get(res, arr[right], mode);
		}
		left /= 2;
		right /= 2;
	}

	return res;
}

int main() {

	int N, M;

	cin >> N >> M;

	int maxSize = pow(2, ceil(log2(1.0 * N)));
	maxSize = N;

	cout << maxSize << "\n";

	int minArr[maxSize];
	int maxArr[maxSize];

	for (int i = 0; i < maxSize; i++) {
		minArr[i] = 0;
		maxArr[i] = 0;
	}

	int num;

	for (int i = 0; i < N; i++) {
		cin >> num;
		minArr[maxSize / 2 + i] = num;
		maxArr[maxSize / 2 + i] = num;
	}

	for (int i = maxSize / 2 - 1; i > 0; i--) {
		minArr[i] = minArr[i*2] < minArr[i*2+1] ? minArr[i*2] : minArr[i*2+1];
		maxArr[i] = maxArr[i*2] > maxArr[i*2+1] ? maxArr[i*2] : maxArr[i*2+1];
	}

	cout << getSeq(maxArr, N, 7, 10, 1, -1) << "\n";

	while (M-- > 0) {
		int left, right;
		cin >> left >> right;
		cout << left << " " << right << "\n";
		int minimum = getSeq(minArr, N, left, right+1, 0, 100000);
		int maximum = getSeq(maxArr, N, left, right+1, 1, -1);
		cout << minimum << " " << maximum << "\n";
		if (minimum == maximum) {
			cout << "NOT FOUND\n";
		} else {
			cout << maximum << "\n";
		}
	}

}