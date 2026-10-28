#include <stdio.h>
#include <stdint.h>

#define SIZE 100


struct node {
	int key;
	struct node *next;
};

struct node *table[SIZE];

int hash(int key) {
	return abs(key)%SIZE; 
}

int search(int key) {
	int idx = hash(key);
	struct node *curr = table[idx];

	while(curr) {
		if (curr->key == key) {
			return 1;
		}
		curr = curr->next;
	}
	return 0;
}

void insert(int key) {
	if (search(key)) {
		return;
	}
	int idx = hash(key);
	struct node *newnode = (struct node*)malloc(sizeof(struct node));
	newnode->key = key;
	newnode->next = table[idx];
	table[idx] = newnode;
}

void remove_key(int key) {
        int idx = hash(key);
        struct node *curr = table[idx], *prev = NULL;

	while(curr) {
		if (curr->key == key) {
			if(prev == NULL) {
				table[idx] = curr->next;
			} else {
				prev->next = curr->next;
			}
			free(curr);
			return;
		}
		prev = curr;
		curr = curr->next;
	}
}

void main() {
	int arr1[] = {1,2,2,1,3};
	int arr2[] = {2,2,3};
	int i = 0;

	for(i = 0; i < sizeof(arr1)/sizeof(arr1[0]);i++) {
		insert(arr1[i]);
	}

	for(i = 0; i < sizeof(arr2)/sizeof(arr2[0]);i++) {
		if (search(arr2[i])) {
			printf("%d ",arr2[i]);
			remove_key(arr2[i]);
		}
	}

}

