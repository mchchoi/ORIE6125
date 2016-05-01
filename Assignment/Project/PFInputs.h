#ifndef PFINPUTS_H
#define PFINPUTS_H
#include <Eigen/Dense>

using namespace Eigen;

struct PFInputs {
   int N;	// number of particles
   int T;	// number of time steps
   int resample_interval; // resample interval, an integer from [1,T]
   int seed;    // seed of rng 
   double g_std; // standard deviation of g
   double f_std; // standard deviation of f
   VectorXd y;  // size T+1 observations/data from external model (e.g. Kalman filter/time series)
};

#endif
