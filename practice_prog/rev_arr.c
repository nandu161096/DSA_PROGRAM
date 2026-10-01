
#include <stdio.h>


void print_arr(int *arr, int n) {
	int i = 0;
	for(i = 0; i < n;i++) {
		printf("%d ",arr[i]);
	}
	printf("\n");
}

void reverse_arr(int *arr, int n) {
	int left = 0, right = n-1;
	while (left < right) {
		int temp = arr[right];
		arr[right] = arr[left];
		arr[left] = temp;
		left++;
		right--;
	}
}

void main() {
	int *arr, n, i = 0;
	printf("Enter the num of elts\n");
	scanf("%d",&n);
	for(i = 0; i < n;i++) {
		scanf("%d",&arr[i]);
	}
	print_arr(arr,n);
	reverse_arr(arr,n);
	print_arr(arr,n);
}

