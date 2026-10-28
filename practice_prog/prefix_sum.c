#include <stdio.h>
#include <stdint.h>

void main() {
	int arr[] = {2,4,1,3,5}, i = 0;
	int prefix[5] = {0};
	prefix[0] = arr[0];
	for (i = 1; i < sizeof(arr)/sizeof(arr[0]);i++) {
		prefix[i] = prefix[i-1] + arr[i];
	}
	printf("Arr and pref sum\n");
	for(i = 0; i < sizeof(arr)/sizeof(arr[0]);i++) {
		printf("%d ",arr[i]);
	}
	printf("\n");
	for(i = 0; i < sizeof(arr)/sizeof(arr[0]);i++) {
                printf("%d ",prefix[i]);
        }
}
