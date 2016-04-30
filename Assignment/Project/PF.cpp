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

using namespace Eigen;
using namespace boost::math;
Class PF
{
   public:
      PF(int len );             // simple constructor
      PF(const PF &obj);  // copy constructor
      void run();

      ~PF();                     // destructor

   private:
      int N;    // number of particles
      int T;	// number of time steps
      VectorXd y;  // size T+1  observations/data from external model (e.g. Kalman filter/time series)
      double g_std; // standard deviation of g
      double f_std; // standard deviation of f
};

struct PFInputs {
   int N;	// number of particles
   int T;	// number of time steps

   VectorXd y;  // size T+1 observations/data from external model (e.g. Kalman filter/time series)
     
   double g_std; // standard deviation of g
   double f_std; // standard deviation of f
};


// Constructor
PF::PF(const PFInputs &input)
{
  N = input.N;
  T = input.T;
  y = input.y;
  g_std = input.g_std;
  f_std = input.f_std;
}

// Run particle filter
void PF::run()
{
  VectorXd particles(N); // particle X
  VectorXd weights(N); // weights

  normal f(0, f_std); // f = q
  normal g(0, g_std); // TODO: What is the mean of g?

  boost::mt19937 rng; // random number generator

  boost::normal_distribution<> f_rng(0, f_std); // sample from f = q
  
  for(int i = 0; i < N; i++) {
  	particles[i] = f_rng(rng); 
        weights[i] = pdf(g, y[0]);
  }


}

PF::PF(const PF &obj)
{
}

PF::~PF(void)
{
}

