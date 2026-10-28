#include <stdio.h>
#include <stdint.h>


void main() {
	int nums[] = {4, 5, 2, 10};
	int n = sizeof(nums)/sizeof(nums[0]), i = 0;
	int result[n], top = -1, stack[n];
	for(i = 0; i < n;i++) {
		result[i] = -1;
	}

	for(i = 0; i < n; i++) {
		while((top>=0) && (nums[i] > nums[stack[top]])) {
			int idx = stack[top--];
			result[idx] = nums[i];
		}
		stack[++top] = i;
	}

	for(i = 0;i < n;i++) {
		printf("i %d res %d\n",i,result[i]);
	}
}

