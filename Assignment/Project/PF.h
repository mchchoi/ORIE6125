#ifndef PF_H
#define PF_H
#include "PFInputs.h"
#include <Eigen/Dense>

// boost headers
#include <boost/random.hpp>
#include <boost/math/distributions.hpp> // import all distributions
#include <boost/random/normal_distribution.hpp>
#include <boost/random/mersenne_twister.hpp>

using namespace Eigen;

class PF
{
   public:
      VectorXd particles; // particle X
      VectorXd weights; // weights
      PF(const PFInputs &input); // constructor
      void run(); // run Particle Filter
      void propagate(VectorXd &particles, VectorXd &weights, int t);
      VectorXd resample(const VectorXd &particles, const VectorXd &weights); // resampling step

   private:
      int N;    // number of particles
      int T;	// number of time steps
      int resample_interval; // resample interval, an integer from [1,T]
      int seed;
      double g_std; // standard deviation of g
      double f_std; // standard deviation of f
      VectorXd y;  // size T+1  observations/data from external model (e.g. Kalman filter/time series)
      boost::mt19937 rng; // random number generator
};
#endif
