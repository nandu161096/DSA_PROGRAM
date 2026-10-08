
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool is_palin(char *str, int n)
{
	int left = 0, right = n-1;
	while (left < right) {
		if (str[left] != str[right]) {
			return false;
		}
		left++;
		right--;
	}
	return true;
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
	printf("The string %s is %s",arr,is_palin(arr,n)?"Palin":"Not palin");
}

