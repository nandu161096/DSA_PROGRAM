#include<stdio.h>
#include<stdint.h>
#include<stdbool.h>

bool is_power_2(int num) {

	if ((num > 0) && ((num & (num-1)) == 0)) {
		return 1;
	}
	return 0;
}

void main() {
	printf("%s\n",is_power_2(16) ? "YES" : "NO");
	printf("%s\n",is_power_2(10) ? "YES" : "NO");
	printf("%s\n",is_power_2(32) ? "YES" : "NO");
}
