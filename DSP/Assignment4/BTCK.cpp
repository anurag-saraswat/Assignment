/*
Algorithm/Approach

Write a recursive function backtrack, which perform backtracking.
Backtrack functionality is explained as comments below

Solution accepted on SPOJ
SPOJ submission 26847315

*/


#include <iostream>
using namespace std;
typedef unsigned long long ll;

bool backTrack(ll *input, int *output, ll k , ll curr_sum, int index) {
	//Return if index value exceeds 10 or sum exceeds from the given sum as input
	if (index > 10) return 0;

	// if index == 10 we found answer.
	// since we are checking for answer lexiographically therefore first found answer is lexiographically smaller.
	// We have to print that ans only so return from this step

	if (curr_sum > k) return 0;
	if (index == 10) {
		return 1;
	}

	for (int i = 0; i < 10; i++) {
		//Checking if i is not used before.
		bool flag = 1;
		for (int j = 0; j < index; j++) {
			if (i == output[j]) {
				flag = 0;
				break;
			}
		}
		// if i is used before then check for other values of i.
		if (!flag) continue;

		// if we reach here then we have value of i which is not used before now and this to output array
		// also update curr_sum by adding weight from input array

		output[index] = i;
		ll sum = curr_sum + i * input[index];
		//Recursively call backTrack
		if (backTrack(input, output, k , sum , index + 1)) {
			return 1;
		}

	}
	return 0;
}

int main() {
	int n ;
	ll input[10];
	ll k;
	cin >> n;
	for (int i = 0; i < n; i++) {

		for (int j = 0; j < 10; j++) {
			cin >> input[j];
		}
		cin >> k;
		int output[10];
		bool out = backTrack(input, output, k , 0, 0);

		if (out) {
			for (int j = 0; j < 10; j++) {
				cout << output[j] << " ";
			}
			cout << endl;
		}
		else cout << -1 << endl;
	}
}

