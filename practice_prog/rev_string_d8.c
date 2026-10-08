
#include <stdio.h>
#include <stdlib.h>

void reverse_str(char *str, int n) {
	int left = 0, right = n-1;
	while (left < right) {
		char ch = str[left];
		str[left] = str[right];
		str[right] = ch;
		left++;
		right--;
	}
}

void main() {
	char *arr;
	int n, i = 0;
	printf("Enter the length of string\n");
	scanf("%d",&n);
	arr = (char*)malloc((n+1)*sizeof(char));
	for(i = 0; i < n;i++) {
		scanf(" %c",&arr[i]);
	}
	arr[i] = '\0';
	printf(" the string is %s\n",arr);
	reverse_str(arr,n);
	printf("Rev string is %s\n",arr);
}

