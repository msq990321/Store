#include <stdio.h>

int main()
{
	printf("��������߳ߴ磬������\'5 7\'��ʾ5��7��\n");
	
	double foot;
	double inch;
	
	scanf("%lf %lf", &foot, &inch);
	
	printf("�����%f�ס�\n",
	((foot+inch/12)*0.3048));
	
	return 0;
}
