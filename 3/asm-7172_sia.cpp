// g++ -Wall -masm=intel asm-7172_sia.cpp -o with_asm -static && ./with_asm
#include <iostream>
#include <stdlib.h> 
#include <time.h>       

using namespace std;


extern "C" {
	int N = 10;
	int *arr1 = new int[N];
	int *arr2 = new int[N];
	int *arr3 = new int[N*2];
}

int main()
{
	srand (time(NULL)); 
	for (int i = 0; i < N; i++)
	{
		arr1[i] = rand() % 100;
		cout << "arr1[" << i << "] = " << arr1[i] << "\n";
		arr2[i] = rand() % 100;
                cout << "arr2[" << i << "] = " << arr2[i] << "\n";
	}

	__asm(R"(
		.intel_syntax noprefix

		mov ecx, N
		mov esi, arr1
		mov edx, arr2
		mov edi, arr3
		fill:
			mov eax, [esi]
			mov [edi], eax
			add edi, 4
			add esi, 4
			
			mov eax, [edx]
			mov [edi], eax
			add edi, 4			
			add edx, 4
			loop fill
	)");
	
	cout << "arr3:\n";	
	for (int i = 0; i < N * 2; i++)
	{
		cout << arr3[i] << "\n";		
	} 
	delete[] arr1;
	delete[] arr2;
	delete[] arr3;	
	return 0;
}

