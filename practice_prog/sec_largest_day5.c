#include <stdio.h>
#include <stdint.h>
#include <limits.h>

void print_arr(int *arr, int n) {
        int i = 0;
        for(i = 0; i < n;i++) {
                printf("%d ",arr[i]);
        }
        printf("\n");
}

int sec_largest(int *arr, int n) {
	int i = 0, pos = 0, largest = INT_MIN, second = INT_MIN;
	for(i = 0 ; i < n;i++) {
		if (arr[i] > largest) {
			second = largest;
			largest = arr[i];
		} else if ((arr[i] < largest) && (arr[i] > second)) {
			second = arr[i];
		}
	}
	return second;
}

void main() {
	int n, *arr, i, val = 0;
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
	val = sec_largest(arr, n);
	printf("sec largest val is %d\n",val);
	free(arr);
}

