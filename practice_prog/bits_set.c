#include<stdio.h>
#include<stdint.h>
#include<stdbool.h>

bool is_power_2(int num) {

	if ((num > 0) && ((num & (num-1)) == 0)) {
		return 1;
	}
	return 0;
}

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
	bitset(5);
	bitset(10);
	bitset(100);
#if 0
	printf("%s\n",is_power_2(16) ? "YES" : "NO");
	printf("%s\n",is_power_2(10) ? "YES" : "NO");
	printf("%s\n",is_power_2(32) ? "YES" : "NO");
#endif
}
