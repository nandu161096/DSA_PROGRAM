#include <stdio.h>
#include <stdint.h>
#include <string.h>

void reverse(char *ptr, int left, int right) {
	char temp_ch;
	while(left < right) {
		temp_ch = ptr[right];
		ptr[right] = ptr[left];
		ptr[left] = temp_ch;
		left++;
		right--;
	}
}

void main() {
	char str[] = "I love    embedded    systems";
	printf("Before rev %s\n",str);
	reverse(str,0,strlen(str) -1);
	int i = 0, start_index = 0;
	for(i = 0;str[i] != '\0';i++) {
		if (str[i] == ' ') {
			if (start_index < i) {
				reverse(str, start_index, i-1);
			}
			start_index = i + 1;
		}
	}
	reverse(str, start_index, strlen(str) - 1);
	printf("After rev words %s\n",str);
}
