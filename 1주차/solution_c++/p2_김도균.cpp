#include <stdio.h>

int main(void)
{
	int i = 0;
	int cnt = 0;
	scanf("%d", &cnt);
	for (i = 0; i < cnt; i++)
	{
		int j = 0;
		int n;
		int x = 1;
		int y = 2;
		int z = 4;
		int ans = x + y + z;
		scanf("%d", &n);
		switch (n)
		{
		case 1:
			ans = 1;
			break;
		case 2:
			ans = 2;
			break;
		case 3:
			ans = 4;
			break;
		default:
			break;
		}
		if (n >= 4)
		{
			for (j = 4; j < n; j++)
			{
				int tmp = ans;
				ans = 2 * ans - x;
				x = y;
				y = z;
				z = tmp;
			}
		}
		printf("%d\n", ans);
	}

	return 0;
}
