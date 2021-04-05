#include <stdio.h>
#define N 10
int main()
{
	int arr[N] = {84, 190, 86, 244, 216, 220, 255, 227, 231, 235};
	int sum = 0;
	for (int i = 0; i < N; i++)
	{
		if (!((arr[i] & 68) ^ 68))
		{
			sum += arr[i];
		}
	}
	printf("Sum: %d\n", sum);
	return 0;
}
