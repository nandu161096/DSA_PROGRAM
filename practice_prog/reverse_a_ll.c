#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

struct node {
	int data;
	struct node *next;
};

void print(struct node *head) {
	struct node *temp = head;
	while (temp !=NULL) {
		printf("%d ",temp->data);
		temp = temp->next;
	}
	printf("\n");
}

struct node* reverse(struct node *head) {
	struct node *curr = head, *prev = NULL, *next = NULL;
	while(curr) {
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return prev;
}

void main() {
	struct node *head = NULL, *temp = NULL, *prev = NULL, *rev = NULL;
	int n, i = 0;
	printf("Enter the number of nodes\n");
	scanf("%d",&n);
	for(i = 0; i < n;i++) {
		temp = (struct node*)malloc(sizeof(struct node));
		temp->next = NULL;
		scanf("%d",&temp->data);
		if(head == NULL) {
			head = temp;
		} else {
			prev->next = temp;
		}
		prev = temp;
	}
	print(head);
	rev = reverse(head);
	print(rev);
}
