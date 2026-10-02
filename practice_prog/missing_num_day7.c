#include <stdio.h>
#include <stdint.h>
#include <limits.h>
#include <stdbool.h>

void print_arr(int *arr, int n) {
        int i = 0;
        for(i = 0; i < n;i++) {
                printf("%d ",arr[i]);
        }
        printf("\n");
}

int max_val_arr(int *arr, int n) {
	int max = INT_MIN, i = 0;
	for (i = 0; i < n;i++) {
		if (arr[i] > max) {
			max = arr[i];
		}
	}
	return max;
}

int missing_elt(int *arr, int n, int max_val) {
	int i = 0, j = 0, found = 0;
	for(i = 0; i < max_val;i++) {
		found = 1;
		for(j = 0; j < n; j++) {
			if (arr[j] == i) {
				found = 0;
			}
		}
		if (found) {
			break;
		}
	}
	return i;
}

void main() {
	int n, *arr, i, max_val = 0;
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
	max_val = max_val_arr(arr, n);
	int mis_elt = 0;
	mis_elt = missing_elt(arr, n, max_val);
	printf("the mis elt %d\n",mis_elt);
	free(arr);
}

