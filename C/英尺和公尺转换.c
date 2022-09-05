#include <stdio.h>

int main()
{
	printf("请输入身高尺寸，如输入\'5 7\'表示5尺7寸\n");
	
	double foot;
	double inch;
	
	scanf("%lf %lf", &foot, &inch);
	
	printf("身高是%f米。\n",
	((foot+inch/12)*0.3048));
	
	return 0;
}
