#include <iostream>
#include <vector>

#include <Eigen/Dense>

// boost headers
#include <boost/random.hpp>
#include <boost/bind.hpp>
#include <boost/function.hpp>
#include <boost/math/distributions.hpp> // import all distributions
#include <boost/random/uniform_int_distribution.hpp>
#include <boost/random/normal_distribution.hpp>
#include <boost/random/mersenne_twister.hpp>


using namespace Eigen;
//using namespace boost::math;
struct PFInputs {
   int N;	// number of particles
   int T;	// number of time steps
   int resample_interval; // resample interval, an integer from [1,T]
   int seed;    // seed of rng 

   VectorXd y;  // size T+1 observations/data from external model (e.g. Kalman filter/time series)
     
   double g_std; // standard deviation of g
   double f_std; // standard deviation of f
};


class PF
{
   public:
      PF(const PFInputs &input);             // simple constructor
      PF(const PF &obj);  // copy constructor
      void run(); // run Particle Filter
      VectorXd resample(const VectorXd &particles, const VectorXd &weights); // resampling step
      void propagate(VectorXd &particles, VectorXd &weights, int t);
      ~PF();                     // destructor

   private:
      int N;    // number of particles
      int T;	// number of time steps
      int resample_interval; // resample interval, an integer from [1,T]
      boost::mt19937 rng; // random number generator
      int seed;
      VectorXd y;  // size T+1  observations/data from external model (e.g. Kalman filter/time series)
      double g_std; // standard deviation of g
      double f_std; // standard deviation of f
};



// Constructor
PF::PF(const PFInputs &input) : rng(input.seed)
{
  N = input.N;
  T = input.T;
  resample_interval = input.resample_interval; // resample interval, an integer from [1,T]
  seed = input.seed;
  y = input.y;
  g_std = input.g_std;
  f_std = input.f_std;
}

// Run particle filter
void PF::run()
{
  VectorXd particles = VectorXd::Zero(N); // particle X
  VectorXd weights = VectorXd::Ones(N); // weights

  //normal f(0, f_std); // f = q
  //normal g(0, g_std); // TODO: What is the mean of g?

  //boost::normal_distribution<> f_rng(0, f_std); // sample from f = q
  
  // T = 0
  //for(int i = 0; i < N; i++) {
  //	particles[i] = f_rng(rng); 
  //      weights[i] = pdf(g, y[0]);
  //}

  for(int t = 0; t <= T; t++){
       if (t % resample_interval == 0 && t > 0) {
	   // resample particles	
           particles = resample(particles,weights);

           // reset weights after resample
       	   weights = VectorXd::Ones(N)/N; 
       } 

       // At t=0 this is just initialization
       propagate(particles, weights, t);


  }

}

void PF::propagate(VectorXd &particles, VectorXd &weights, int t){
  for(int i = 0; i < N; i++) {
	double p = particles[i];
  	boost::normal_distribution<> f_rng(p, f_std); // sample from f = q
  	particles[i] = f_rng(rng); 
  	boost::math::normal g(p, g_std); 
        weights[i] *= pdf(g, y[t]);
  }
  weights /= weights.sum();  
}




VectorXd PF::resample(const VectorXd &particles, const VectorXd &weights)
{
  VectorXd tmp_particles(N); // initialize updated particles X
  
  // cast weights to a double array tmp
  //double tmp[N];
  std::vector<double> tmp;
  tmp.resize(N);
  for(int i = 0; i < N; i++){
  	tmp[i] = weights[i];
  }
  
  // sample from weights
  //boost::random::discrete_distribution<> dist(tmp); 
  boost::random::discrete_distribution<> dist(tmp.begin(), tmp.end());
  for(int i = 0; i < N; i++){
  	 tmp_particles[i] = particles[dist(rng)];
  }
 
  return tmp_particles;
}
 
PF::PF(const PF &obj)
{
}

PF::~PF(void)
{
}

