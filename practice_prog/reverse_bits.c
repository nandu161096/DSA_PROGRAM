#include<stdio.h>
#include<stdint.h>
#include<stdbool.h>

void reverse_bits(int num) {
	int i = 0, rev_num = 0;
	for(i = 0;i<8;i++) {
		if (((num >> i) & 1) == 1) {
			rev_num = rev_num | (1 << (7-i));
		}
	}
	printf("num %d rev_num %d\n",num,rev_num);
}

void main() {
	reverse_bits(8);
	reverse_bits(10);
}
