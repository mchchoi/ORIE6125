#include <Eigen/Dense>

// boost headers
#include <boost/random.hpp>
#include <boost/bind.hpp>
#include <boost/function.hpp>
#include <boost/math/distributions.hpp> // import all distributions
#include <boost/random/uniform_int_distribution.hpp>
#include <boost/random/normal_distribution.hpp>
#include <boost/random/mersenne_twister.hpp>

#include <iostream>

Class PF
{
   public:
      PF(int len );             // simple constructor
      PF(const PF &obj);  // copy constructor
      ~PF();                     // destructor

   private:
      int N;    // number of particles
      int T;	// number of time steps

};

// Member functions definitions including constructor
PF::PF(int len)
{
    cout << "Normal constructor allocating ptr" << endl;
    // allocate memory for the pointer;
    ptr = new int;
    *ptr = len;
}

PF::PF(const PF &obj)
{
}

PF::~PF(void)
{
}

