#include <stdio.h>
#include <stdint.h>
#include <string.h>

void main() {
	char str1[7] = "lsten", str2[7] = "silent";
	if (strlen(str1) != strlen(str2)) {
		printf("not anagram\n");
		return;
	}
	int count[256] = {0}, i = 0;
	for(i = 0; str1[i]!= '\0'; i++) {
		count[(unsigned char)str1[i]]++;
		count[(unsigned char)str2[i]]--;
	}
	for(i = 0; i < 256;i++) {
		if (count[i] != 0) {
		 printf("not anagram\n");
                return;
		}
	}
	printf("Anagram");
}

