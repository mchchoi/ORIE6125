#include <iostream>
#include <math.h>
using namespace std;

int main()
{
  double x = 2;

  while (x+1 != x)
	x = x * 2;
  
  while (x == x - 1)
	x--;

  if (x == (long long int)x)
	cout << x << endl;

  return 0; 
}
