#include <stdio.h>
#include <stdint.h>

void main() {
	char str[50];
	scanf("%s",&str);
	int count[256] = {0}, i = 0, printed[256] = {0};
	for(i = 0; str[i] != '\0'; i++) {
		count[(unsigned char)str[i]]++;
	}
        for(i = 0; str[i] != '\0'; i++) {
               if ((count[(unsigned char)str[i]] >1) && (printed[(unsigned char)str[i]] == 0)) {
		       printf("%c ",str[i]);
		       printed[(unsigned char)str[i]] = 1;
	       }
        }
}
