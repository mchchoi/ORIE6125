#include <boost/lexical_cast.hpp>
#include <iostream>

int main()
{
  using boost::lexical_cast;
  int a= lexical_cast<int>("123456");
  double b = lexical_cast<double>("123.456");
  std::cout << a << std::endl;
  std::cout << b << std::endl;
  return 0;
}
