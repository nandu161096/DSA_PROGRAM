#include <stdio.h>
#include <stdint.h>

#define SIZE 100
struct node {
	int key;
	int cnt;
	struct node *next;
};

struct node *table[SIZE] = {NULL};

int hash(int key) {
	return abs(key)%SIZE;
}

void insert(int key) {
	int idx = hash(key);
	struct node *curr = table[idx];

	while(curr) {
		if (curr->key == key) {
			curr->cnt += 1;
			return;
		}
		curr = curr->next;
	}
	struct node *newnode = (struct node*)malloc(sizeof(struct node));
	newnode->key = key;
	newnode->cnt = 1;
	newnode->next = table[idx];
	table[idx] = newnode;
}

void main() {
	int arr[] =  {2, 3, 2, 5, 3, 2, 5};
	int n = sizeof(arr)/sizeof(arr[0]), i = 0;
	for(i = 0; i < n;i++) {
		insert(arr[i]);
	}
	for (i = 0; i < SIZE; i++) {
		struct node *curr = table[i];
		while (curr) {
			printf("data %d cnt %d\n",curr->key, curr->cnt);
			curr = curr->next;
		}
	}
}
