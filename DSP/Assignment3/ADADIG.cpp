
/*

Approach Used:

Step 1. Factorize N. If it has a prime factors  > 9, then there's no solution.
Step 2. Otherwise, it will be a number of the form 2a * 3b * 5c * 7d.
Any number with digital product N will have c digits 5 and d digits 7,
but the other digits are combinations of primes 2 and 3.
Find all possible combination of these arrangement whose multiplication is equal to input.
For getting sum equal to input add one's to the combination. Store Repeation of digits in array for each combination.
Step 3. Select one combination. and find out all possible arrangement of this combination.
Step 4. Sum up all arrangement of each combination. This is our required answer.

e.g for input 8

prime factor of 8 {2*2*2}

combination 1 : {2,2,2,1,1}  sum = mul = 8 arrangements possible =  5!/(3!*2!) = 10
combination 2 : {2,4,1,1}    sum = mul = 8 arrangement possible = 4!/(2!) = 12
combination 3 : {8}          sum = mul = 8 arrangement possible = 1

Total = 10+12+1 = 23{Expected Output}

*/

/*
Sample Input:

4
8
12
13
15

Sample Output:

23
240
0
72

*/

#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ll;

// factorial function
ll factorial(ll num) {
	ll fact = 1;
	for (ll i = 1; i <= num; i++) {
		fact = (fact * i);
	}
	return fact ;
}

// calculate possible combinations
ll combination(ll *arr1, ll length) {
	ll ans = 0;
	ll n = 0;

	for (ll i = 0; i < length; i++) {
		n = n + arr1[i];
	}

	ans = factorial(n);

	for (ll i = 0; i < length; i++) {
		ans = ans / factorial(arr1[i]) ;
	}
	return ans;
}

// return all possible combinations for digital multiplication
void find_subvectors(vector<ll>& ar, ll mul, vector<vector<ll> >& res, vector<ll>& r, ll rem, ll i)
{
	// If remainder becomes greater than zero -- return
	if (rem != 0)
		return;

	// if multiplication becomes 1 and remainder becomes 0 -- add the subvector into vector of subvectors
	if (rem == 0 && mul == 1)
	{
		res.push_back(r);
		return;
	}
	ll div;
	// Recur for all remaining elements until we find a subvector.
	while (i < ar.size() && mul > 1)
	{
		r.push_back(ar[i]);
		div = mul / ar[i];
		rem = mul % ar[i];

		// recur for next numbers
		find_subvectors(ar, div, res, r, rem, i);
		i++;

		// remove number from subvector (backtracking)
		r.pop_back();
	}
}

// Returns all combinations of numbers that have given digital multiplications.
vector<vector<ll> > find_combinations(vector<ll>& ar, ll mul)
{
	vector<ll> r;
	vector<vector<ll> > res;
	ll rem = 0;
	find_subvectors(ar, mul, res, r, rem, 0);
	return res;
}

// Driver code
int main()
{
	vector<ll> ar;
	ar.push_back(2);
	ar.push_back(3);
	ar.push_back(4);
	ar.push_back(5);
	ar.push_back(6);
	ar.push_back(7);
	ar.push_back(8);
	ar.push_back(9);
	ll n = ar.size();

	int inp;
	cin >> inp;
	for (int itr = 0; itr < inp; itr++) {
		int mul ;
		cin >> mul;

		vector<vector<ll> > res = find_combinations(ar, mul);

		// If result is empty, then
		if (res.size() == 0)
		{
			//If number contain prime factor greater than 7 then no solution exists.
			cout << 0 << endl;
			continue;
		}
		ll count = 0;
		// generate all combinations stored in res vector.
		for (ll i = 0; i < res.size(); i++)
		{

			if (res[i].size() > 0)
			{
				ll arr[10] = {0};
				for (ll j = 0; j < res[i].size(); j++) {
					arr[res[i][j]] = arr[res[i][j]] + 1;
				}


				ll sum = 0;

				for (ll pq = 0 ; pq < 10; pq++) {
					sum = sum + pq * arr[pq];
				}

				arr[1] = mul - sum;
				count = count + combination(arr, 10);
			}
		}
		cout << count << endl;



	}

	return 0;
}