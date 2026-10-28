#include <stdio.h>
#include <stdint.h>

void main() {
	//int temperatures[] = {73, 74, 75, 71, 69, 72, 76, 73};
	int temperatures[] = {30, 40, 35, 50, 45};
	int n = sizeof(temperatures)/sizeof(temperatures[0]);
	int stack[n], i = 0, top = -1;
	int answer[n];
	for(i = 0; i < n;i++) {
		answer[i] = 0;
	}

	for(i = 0; i < n;i++) {
		while ((top>=0) && (temperatures[i] > temperatures[stack[top]])) {
			int prev_index = stack[top--];
			answer[prev_index] = i - prev_index; 
		}
		stack[++top] = i;
	}
	for(i = 0; i < n;i++) {
		printf("i %d answ %d\n",i,answer[i]);
	}
}
