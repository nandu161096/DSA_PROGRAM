#include <stdio.h>
#include <limits.h>

void main()
{
	int *ptr, n, i = 0, min_val = INT_MAX, max_val = INT_MIN;
	printf("Enter the number of elts\n");
	scanf("%d",&n);
	ptr = (int*)malloc(sizeof(n*sizeof(int)));
	if (ptr == NULL) {
		return 0;
	}
	for (i = 0; i <n;i++) {
		scanf("%d",&ptr[i]);
	}
	printf("Dummping the elt\n");
	for (i = 0; i <n;i++) {
                printf("%d ",ptr[i]);
        }
	min_val = max_val = arr[0];

	for(i = 0; i < n;i++) {
		if (ptr[i] < min_val) {
			min_val = ptr[i];
		} else if (ptr[i] > max_val) {
			max_val = ptr[i];
		}
	}
	printf("\n");
	printf("min val %d max val %d",min_val,max_val);
}
