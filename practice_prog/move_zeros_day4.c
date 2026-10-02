#include <stdio.h>
#include <stdint.h>

void print_arr(int *arr, int n) {
        int i = 0;
        for(i = 0; i < n;i++) {
                printf("%d ",arr[i]);
        }
        printf("\n");
}

void move_zeros(int *arr, int n) {
	int i = 0, pos = 0;
	for(i = 0 ; i < n;i++) {
		if (arr[i] != 0) {
			int temp = arr[pos];
			arr[pos] = arr[i];
			arr[i] = temp;
			pos += 1;
		}
	}
	print_arr(arr, n);
}

void main() {
	int n, *arr, i;
	printf("Enter the number of elets\n");
	scanf("%d",&n);
	arr = (int*)malloc(n*sizeof(int));
	if (arr == NULL) {
		printf("Alloc failed\n");
		return;
	}
	for(i = 0; i < n;i++) {
		scanf("%d",&arr[i]);
	}
	print_arr(arr,n);
	move_zeros(arr, n);
	print_arr(arr,n);
}

