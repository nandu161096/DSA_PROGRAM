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
	int arr[] = {2, 2, 1};
	int result = 0, i = 0;
	for (i = 0; i < sizeof(arr)/sizeof(arr[0]) ;i++) {
		result = result ^ arr[i];
	}
	printf("result %d\n",result);
#if 0
	printf("%s\n",is_power_2(16) ? "YES" : "NO");
	printf("%s\n",is_power_2(10) ? "YES" : "NO");
	printf("%s\n",is_power_2(32) ? "YES" : "NO");
#endif
}
