#include <stdio.h>
#include <stdint.h>
#include <string.h>

int main() {
	char str[50];
	int count[256] = {0}, i = 0;
	scanf("%s",&str);
	for(i = 0; str[i] != '\0';i++) {
		count[(unsigned char)str[i]]++;
	}
	for(i = 0; str[i] != '\0';i++) {
		if (count[(unsigned char)str[i]] == 1) {
			printf("index is i %d\n",i);
			return i;
		}
	}
	return -1;
}
