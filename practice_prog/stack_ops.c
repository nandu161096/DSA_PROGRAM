#include<stdio.h>

#define SIZE 100
int stack[SIZE];
int top = -1;

void push(int val) {
	if (top == SIZE-1) {
		printf("Stack over flow");
	}
	stack[++top] = val;
}

int pop() {
	if (top == -1) {
		printf("Stack is underflow");
	}
	return stack[top--];
}

int peek() {
	if (top == -1) {
                printf("Stack is underflow");
        }
	return stack[top];
}

void display() {
	int i = 0;
	for(i = 0; i <= top;i++) {
		printf("%d ",stack[i]);
	}
	printf("\n");
	for(i = top; i>=0 ; i--) {
		printf("%d ",stack[i]);
	}
	printf("\n");
}

void main() {
	push(10);
	push(1);
	push(30);
	display();
	pop();
	display();
}
