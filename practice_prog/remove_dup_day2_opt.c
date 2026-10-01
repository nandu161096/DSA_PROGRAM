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

int *remove_duplicates(int *arr, int n, int *new_size) {
	int *rem = (int*)malloc(n*sizeof(int));
	int i = 0, k = 0;

	for(i=0;i<n;i++) {
		if (!is_present(rem, arr[i], k)) {
			rem[k] = arr[i];
			k++;
		}
	}
	*new_size = k;
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
	int *ptr, n, i = 0, *rem, new_size;
	printf("Enter the num of elts\n");
	scanf("%d",&n);
	ptr = (int*)malloc(n*sizeof(int));
	for(i = 0; i <n;i++) {
		scanf("%d",&ptr[i]);
	}
	print_arr(ptr,n);
	rem = remove_duplicates(ptr,n,&new_size);
	print_arr(rem,new_size);
	free(rem);
	free(ptr);
}

