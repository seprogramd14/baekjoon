#include <stdio.h>

int main(void) {
	int num;
	scanf("%d", &num);
	for (int i = 1; i <= num; i++) {
		for (int j = num; j > i; j--) printf(" ");
		printf("*");
		for (int j = 2; j < i*2-1; j++) printf(" ");
		if (i != 1) printf("*\n");
		else printf("\n");
	}
	return 0;
}