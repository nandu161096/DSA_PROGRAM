#include<stdio.h>
#include<stdint.h>

void remove_dup(int *nums, int size) {
    int k = 1, i = 0;
    int start_elt = nums[0];
    for (i = 1; i <size; i++) {
        if (start_elt != nums[i]) {
		nums[k] = nums[i];
		k += 1;
		start_elt = nums[i];
	}
    }
    printf("k %d\n",k);
    for(i = 0; i < k;i++) {
	    printf("%d ",nums[i]); 
    }
    printf("\n");
}

void main() {
	int nums[] =  {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
	remove_dup(nums, sizeof(nums)/sizeof(nums[0]));
}

