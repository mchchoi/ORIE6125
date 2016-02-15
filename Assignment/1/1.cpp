#include <iostream>
#include <limits>
using namespace std;

int main()
{
  int z = 2;
  int conv = (int)(double)z;
  int old = z;

  while (z == conv && z > 0)
  {
    old = z;
    z = 2*z;
    conv = (int)(double)z;
  }
  
  z = old;
  conv = (int)(double)z;
  while (z == conv && z > 0)
  {
    old = z;;
    z++;
    conv = (int)(double)z;
  }

  cout << "The value old is " << old << endl;
  cout << "Largest int is " << numeric_limits<int>::max() << endl;
  cout << "The value old is " << old << endl;
  cout << "The value z is " << z << endl;
  cout << "The value conv is " << conv << endl;
 

  if ( old+1 != (int)(double)(old+1) )
  {
  	cout << "The value old is " << old << endl;
  	cout << "The value z is " << z << endl;
  	cout << "The value conv is " << conv << endl;
  }
  return 0; 
}
