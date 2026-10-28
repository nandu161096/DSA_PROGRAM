#include<stdio.h>
#include<stdint.h>
#include<stdbool.h>

int bitset(int num) {
	int cnt = 0, i = 0;

	for(i = 0; i < 4*sizeof(int);i++) {
		if (((num >> i) & 1) == 1) {
			cnt++;
		}
	}
	printf("bit set %d\n",cnt);
}

void main() {
#if 0
	bitset(5);
	bitset(10);
	bitset(100);
#endif
	int a = 8;
	a = a | (1<<1);
	printf("After set a %d\n",a);
	a = a & ~(1<<1);
        printf("After clear a %d\n",a);
	a = a ^ (1<<1);
        printf("After toggle a %d\n",a);
	if (a & (1<<3)) {
		printf("3rd bit is set\n");
	} else {
		printf("3rd bit is not set\n");
	}
	int value = 0xAB;
	int bit_2_to_5 = (value >> 2) & ((1 << (5-2+1)) - 1);
	// (value >> start) & ((1 << (end -start +1)) -1)
	printf("bit_2_to_5 0x%x\n",bit_2_to_5);
	uint32_t val = 0xC3;
	uint32_t field_val = 0x5, start =2 , end = 5;
	uint32_t mask = ((1U << (end-start)) - 1) << start;
	val = val & ~(mask);
	val = val | ((field_val << start) & mask);
	printf("val 0x%x\n",val);

#if 0
	printf("%s\n",is_power_2(16) ? "YES" : "NO");
	printf("%s\n",is_power_2(10) ? "YES" : "NO");
	printf("%s\n",is_power_2(32) ? "YES" : "NO");
#endif
}
