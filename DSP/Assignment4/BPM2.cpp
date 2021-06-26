/*
Approach Used :
1. For a given no. N, first we calculate the sum of first N natural numbers, that will stored as "total_sum".
2. Now to make two partitions of numbers from 1 to N, We will divide the "total_sum" by 2, and assigned as sum of numbers present in a pertition for each partitions, which consists of 02 possibilities :
    a. if the total_sum is even then the sum of elements of both the partitions is equal(i.e. total_sum is equally divided in both partitions) and thus the resulting minimum absolute difference of sum of elemetens of each partitions will be 0.
    b. if the total_sum is odd then the sum of elements of partition1 is one less than the sum of elements of partition2 and thus the resulting minimum absolute difference of sum of elements of each partitions will be 1.

3. Now, we'll just have to find the lexiographically smallest combination of numbers(form 1 to N) that sums to the sum of elements of partition1. This task is performed by "findSubsets()" function, which returns the smallest(lexiographically) combination.

4. Finally, "sequence_hash()" function will compute the hash for the above generated combination and print it.
*/
/*
Sample Input :
9
2 10 1000000000
3 10 1000000000
4 10 1000000000
5 10 1000000000
6 10 1000000000
7 10 1000000000
8 10 1000000000
9 10 1000000000
1000 1000000000 1000000
*/
/*
Sample Output :
Case 1: 1 1
Case 2: 0 12
Case 3: 0 14
Case 4: 1 124
Case 5: 1 1234
Case 6: 0 1247
Case 7: 0 12348
Case 8: 1 123457
Case 9: 0 1000
*/

#include<iostream>
#include<vector>
using namespace std;
typedef long long ull;
static int found;


// function to find the smallest combinations(lexiographically) which sums to a given Number
void findSubsets(ull *numbers, ull sum, vector<ull> &subset, vector<vector<ull>> &final_list, ull i, ull N){
  if(sum < 0){
    return;
  }
  if(sum == 0){
    final_list.push_back(subset);
    found = 1;
    return;
  }
  while(i<N && sum - numbers[i] >= 0){
      if(found == 0){
        subset.push_back(numbers[i]);
        findSubsets(numbers, sum - numbers[i], subset, final_list, i+1, N);
        i++;
        subset.pop_back();
      }else if(found == 1){
        return;
      }
  }

}


// Calculate the hash value of sequence
long long sequence_hash(vector<ull> &sequence, long long B, long long M){
  long long result = 0;
  for(ull i=0; i<sequence.size(); i++){
    result = (result * B + sequence[i]) % M;
  }
  return result;
}   


// Driver Code
int  main() {
  ull T;  
  cin >> T;
  for(ull t=1; t<=T; t++){
    ull N, B, M;
    cin >> N >> B >> M;
    ull total_sum = 0;
    int min_diff;
    

    ull numbers[N];
    for(ull i=1; i<=N; i++){
      numbers[i-1] = i;
      total_sum += i;
    }
    if((total_sum & 1) == 0){
      min_diff = 0;
    }else{
      min_diff = 1;
    }
    ull sum = total_sum >> 1;

    vector<ull> subset;
    vector<vector<ull>> final_list;

    found = 0;
    findSubsets(numbers, sum, subset, final_list, 0, N);
    
    cout << "Case " << t << ": "<< min_diff << " "<< sequence_hash(final_list[0], B, M) << endl;
  }  
  return 0;
}