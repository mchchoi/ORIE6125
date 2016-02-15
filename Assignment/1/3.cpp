#include <iostream>
#include <cmath>
using namespace std;

int main(){
  double x;   
  cin >> x ;
  if ( fpclassify(x) == FP_SUBNORMAL ){
     cout << "true";
  }
  else{ 
     cout << "false";
  }
}
