#include<stdio.h>
#include<stdint.h>
#include<stdbool.h>

void main() {
	int n = 12, i = 0;
	for(i = 0; i < 32;i++) {
		if ((n >> i) & 1) {
			printf("%d bit is set \n",i);
			break;
		}
	}
}
