#include<vector>
#include<iostream>
#include<string>
using namespace std;

struct TreeNode{    
    int val;
    TreeNode *left=nullptr;
    TreeNode *right=nullptr;
};

vector<int> InorderTraversal(TreeNode *root);

int main(){
    TreeNode root, n1, n2, n3, n4, n5;
    root.val = 0, root.left = &n1, root.right = &n2;
    n1.val = 1, n1.left = &n3, n1.right = &n4;
    n2.val = 2;
    n3.val = 3, n3.right = &n5;
    n4.val = 4, n5.val = 5;

    auto ans = InorderTraversal(&root);
    for(auto i:ans){
        cout << i << ' ';
    }
    //cout << InorderTraversal(&root) << endl;
}

vector<int> InorderTraversal(TreeNode *root){
    
    if(root==nullptr){
        vector<int> res;
        return res;
        }

    vector<int> left = InorderTraversal(root->left);

    left.insert(left.end(), root->val);

    vector<int> right = InorderTraversal(root->right);

    if(!right.empty())
        left.insert(left.end(), right.begin(), right.end());

    return left;
}