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

struct hashtbl {
	int key_val;
	int cnt;
};

struct hashtbl hash1[100];

void freq_of_elt(int *arr, int n) {
	bool found = false;
	int i,j, size = 0;

	for(i = 0 ; i < n;i++) {
		found = false;
		for(j = 0; j < size; j++) {
			if (hash1[j].key_val == arr[i]) {
				hash1[j].cnt += 1;
				found = true;
				break;
			}
		}
		if (!found) {
			hash1[j].key_val = arr[i];
			hash1[j].cnt = 1;
			size += 1;
		}
	}
	for(i = 0; i <size;i++) {
		printf("Key elet %d cnt %d\n",hash1[i].key_val, hash1[i].cnt);
	}
}

void main() {
	int n, *arr, i, *freq;
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
	freq_of_elt(arr, n);

	free(arr);
}

