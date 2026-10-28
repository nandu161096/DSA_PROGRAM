#include <stdio.h>
#include <stdint.h>
#if 0
int is_need_present(int need, int visited[]) {
	int i = 0, len = sizeof(visited)/sizeof(visited[0]);
	for(i = 0; i < len;i++) {
		if (visited[i] == need) {
			return 1;
		}
	}
	return 0;
}
#endif
#define SIZE 1000
int hash[SIZE] = {0};
void main() {
	int numbers[] = {2, 7, 11, 15};
	int visited[sizeof(numbers)];
	int target = 9, need = 0, i = 0, n;
	
	for(i = 0; i < SIZE; i++) {
		hash[i] = -1;
	}
	n = sizeof(numbers)/sizeof(numbers[0]);

	for(i = 0; i <n;i++) {
		need = target - numbers[i];
		if (need >= 0 && need <= SIZE && hash[need] != -1 ) {
			printf("Index are %d %d\n",i+1,hash[need]+1);
		}
		hash[numbers[i]] = i;
	}
}
