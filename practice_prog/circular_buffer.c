#include<stdio.h>
#include<stdint.h>
#include<stdbool.h>

#define SIZE 5
struct circular_Queue {
	int arr[SIZE];
	int front;
	int rear;
};

void init(struct circular_Queue *q) {
	q->front = q->rear = -1;
	int i = 0;
	for(i = 0; i < SIZE;i++)  {
		q->arr[i] = 0;
	}
}

bool is_full(struct circular_Queue *q) {
	if ((q->rear + 1) % SIZE == q->front) {
		return 1;
	}
	return 0;
}

bool is_empty(struct circular_Queue *q) {	
	if (q->front == -1) {
		return 1;
	}
	return 0;
}

void enqueue(struct circular_Queue *q, int data) {
	if (is_full(q)) {
		printf("Queu is full\n");
		return;
	}

	if (is_empty(q)) {
		q->front = q->rear = 0;
	} else {
		q->rear = (q->rear + 1)%SIZE;
	}
	q->arr[q->rear] = data; 
}

void dequeue(struct circular_Queue *q) {

	if (is_empty(q)) {
		printf("Queue is empty\n");
		return;
	}
	int data = q->arr[q->front];

	if (q->front == q->rear) {
		q->front = q->rear = -1;
	} else {
		q->front = (q->front +1)%SIZE;
	}
	printf("Dequeue data %d\n",data);
}

void print(struct circular_Queue *q) {
	int i = q->front;

	while(1) {
		printf("data is %d\n",q->arr[i]);
		if (i == q->rear) {
			break;
		}
		i = (i + 1) % SIZE;
	}
}

void main() {

	struct circular_Queue q;
	init(&q);
	enqueue(&q, 1);
	enqueue(&q, 2);
	enqueue(&q, 3);
	enqueue(&q, 4);
	print(&q);
	dequeue(&q);
	print(&q);
}
