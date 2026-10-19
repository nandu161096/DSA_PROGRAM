#include <stdio.h>
#include <stdint.h>
#include <string.h>

void main() {
	char str[7] = "aaabbc", comp_str[7] = {0};
	int count = 1, i = 0, k = 0;
	int n = strlen(str);
	printf("length is %d\n",n);
	for(i = 1; i < n;i++) {
		if (str[i] == str[i-1]) {
			count++;
		} else {
			comp_str[k] = str[i-1];
			k++;
			comp_str[k] = count + '0';
			count = 1;
			k++;
		}
	}
	comp_str[k++] = str[n-1];
	comp_str[k++] = count + '0';
	printf("comp string is %s\n",comp_str);

}
