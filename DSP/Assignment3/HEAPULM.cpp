/*

Approach Used : 
Step 1 : First insert all element in priority queue.
Step 2 : Pop out element from priority queue and insert it in binary search tree.
Step 4 : Repeat Step 2 until priority queue becomes empty.
Step 5 : Now print inorder traversal of BST.It is the output to be printed.
 
*/
//----------------------------------------------------------------------------------
/*
Sample Input

7 a/7 b/6 c/5 d/4 e/3 f/2 g/1
7 a/1 b/2 c/3 d/4 e/5 f/6 g/7
7 a/3 b/6 c/4 d/7 e/2 f/5 g/1
0

Sample Output

(a/7(b/6(c/5(d/4(e/3(f/2(g/1)))))))
(((((((a/1)b/2)c/3)d/4)e/5)f/6)g/7)
(((a/3)b/6(c/4))d/7((e/2)f/5(g/1)))

*/
//--------------------------------------------------------------------------------
#include <iostream>
#include <string>
#include <queue>
using namespace std;

struct Node {
  Node *lchild;
  pair<int , string> key;
  Node *rchild;
} *root = NULL;

void Insert(pair<int , string> data) {

  struct Node *temp = new Node();
  temp->key = data;
  temp->lchild = temp->rchild = NULL;

  if (root == NULL) {
    root = temp;
    return;
  }

  struct Node *ptr = root, *prev;

  while (ptr) {

    prev = ptr;

    if (data.second > ptr->key.second) {
      ptr = ptr->rchild;
    }

    else if (data.second < ptr->key.second) {
      ptr = ptr->lchild;

    }
    else
      return;
  }

  if (data.second > prev->key.second)prev->rchild = temp;
  else prev->lchild = temp;

  return;
}

void Inorder(struct Node *p) {

  if (p) {
    cout << "(";
    Inorder(p->lchild);
    cout << p->key.second << "/" << p->key.first;
    Inorder(p->rchild);
    cout << ")";
  }
}

int main() {

  int N;
  while (cin >> N) {
    if (N == 0) break;

    priority_queue<pair<int, string>> pq_max;
    string str ;

    for (int i = 0; i < N; i++) {
      cin >> str;
      int len = str.size();
      string temp = "";
      int j = 0 , num = 0;
      while (str[j] != '/') {
        temp += str[j];
        j++;
      }
      j++;
      while (j < len) {
        num = num * 10 + (str[j] - '0');
        j++;
      }

      pq_max.push(make_pair(num, temp));
    }
    while (!pq_max.empty()) {
      pair<int, string> ele =  pq_max.top();
      Insert(pq_max.top());
      pq_max.pop();
    }
    Inorder(root);
    root = NULL;
    cout << endl;
  }
}

