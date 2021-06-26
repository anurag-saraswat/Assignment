/*

Algorithm:

input:
array of weight of each item say, arr
observed change in total weight i.e. weight of stolen item.

1. Function checkBurg returns :
       -1 : if it found more than one combination of total number of missing item;
       -2 : if no answer is possible
      item: if found ans i.e total number of item stolen

2. Here Function checkBurg generate all possible combination of of items. By first picking from all items
one at a time, then picking two item at a time then three and so on. This is done by using bit manipulation.

3. After picking up set of items then check if there total weight is equal to the weight of stolen item.

4. If it is equal the we increase value of count to 1 and save number of item we get in this step.

5. If again find a set of item whose sum equates to sum(this can be checked by using value opf count)
then we check if number of item in set is equal to that of previous the no problem else return -1. That is
situation is ambigious.

6. If we did not get any solution then return -1


 For optimizing answer we ignore that input value whose value is greater than the total weight of item stolen.
this will lead to decrease in number of combination to be checked.


 */

/*

Input:
4
5 10
2 3 6 9 5
5 20
1 4 2 3 15
5 20
1 4 5 15 27
5 16
1 2 4 8 32

Output:
Case #1: 3
Case #2: 3
Case #3: AMBIGIOUS
Case #4: IMPOSSIBLE
 */



#include <iostream>
using namespace std;

typedef long long ll;

ll checkBurg(ll *input, int n, ll d) {

	ll itr = 1 << n;
	int count = 0;
	int ans = 0;
	for (ll i = 0; i < itr; i++) {
		ll weg = 0;
		ll item = 0;
		int j = 0;
		ll k = i;
		while (k) {
			if (k & 1) {
				weg = weg + input[j];
				item++;
			}
			k = k >> 1;
			j++;
		}

		if (weg == d) {
			if (count == 0) {
				count++;
				ans = item;
			}
			if (ans != item) return -1;

		}

	}
	if (count == 1) return ans;
	else return -2;
}



int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {

		int n;
		ll d;
		cin >> n >> d;
		ll input[n];
		int id = 0;
		for (int j = 0; j < n; j++) {
			ll inp;
			cin >> inp;
			if (inp <= d) {
				input[id] = inp;
				id++;
			}
		}
		ll ans = checkBurg(input, id, d);
		cout << "Case #" << i + 1 << ": ";
		if (ans == -1) cout << "AMBIGIOUS" << endl;
		else if (ans == -2) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
}

