#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

bool is_present(int *ptr, int val, int n) {
	int i = 0;
	for(i = 0; i < n;i++) {
		if (ptr[i] == val) {
			return true;
		}
	}
	return false;
}

int *remove_duplicates(int *arr, int n) {
	int *rem = (int*)malloc(n*sizeof(int));
	int *hash = (int*)malloc(n*sizeof(int));
	int i = 0, k = 0;

	for(i=0;i<n;i++) {
		if (!is_present(hash, arr[i], n)) {
			hash[k] = arr[i];
			rem[k] = arr[i];
			k++;
		}
	}

	return rem;
}

void print_arr(int *arr, int n) {
        int i = 0;
        for(i = 0; i < n;i++) {
                printf("%d ",arr[i]);
        }
        printf("\n");
}

void main() {
	int *ptr, n, i = 0, *rem;
	printf("Enter the num of elts\n");
	scanf("%d",&n);
	ptr = (int*)malloc(n*sizeof(int));
	for(i = 0; i <n;i++) {
		scanf("%d",&ptr[i]);
	}
	print_arr(ptr,n);
	rem = remove_duplicates(ptr,n);
	print_arr(rem,n);
}

