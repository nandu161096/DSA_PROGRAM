#include<stdio.h>
#include<stdint.h>
#include<ctype.h>

void main() {
	char s[] = "A man, a plan, a canal: Panama";
	char ch, s2[sizeof(s)];
	int i = 0, k = 0;
	for(i = 0; s[i] != '\0';i++) {
		if (isalpha((unsigned char)s[i])) {
			s2[k] = tolower((unsigned char)s[i]);
			k++;
		}
	}
	int left = 0;
	int right = k-1;
	uint8_t is_not_pal = 0;
	while(left < right) {
		if (s2[left] !=  s2[right]) {
			is_not_pal = 1;
			break;
		}
		left += 1;
		right -= 1;
	}
	if (is_not_pal) {
		printf("Str is not pal\n");
	} else {
		printf("Str is pal\n");
	}
}
