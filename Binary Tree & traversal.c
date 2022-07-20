#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *left;
    struct node *right;
};

struct node *tree=NULL;
int count=1;

struct node* insert(struct node *root,int val){
    if(root==NULL){
        root= (struct node*)malloc(sizeof(struct node));
        root->data=val;
        root->left=root->right=NULL;
        count++;
    }
    else{
        if(count%2==0)
         root->left=insert(root->left,val);
        else
    }
}
