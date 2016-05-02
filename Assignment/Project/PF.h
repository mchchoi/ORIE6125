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
      /* A public field indicating the position of the particles */
      VectorXd particles;

      /* A public field indicating the weights of the particles */
      VectorXd weights;

      /* Constructor of the class from PFInputs */
      PF(const PFInputs &input);

      /* Run the Particle Filter with desired parameters from PFInputs */
      void run();

      /* Draw a random sample for each particle at time t and update particles and weights */
      void propagate(VectorXd &particles, VectorXd &weights, int t); 

      /* Perform the resampling step in PF and return the new position of the particles */
      VectorXd resample(const VectorXd &particles, const VectorXd &weights); 

   /* Inputs to PF, which are initialized by PFInputs */
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
