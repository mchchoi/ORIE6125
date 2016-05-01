#include <iostream>
#include <vector>
#include <cmath>

#include <Eigen/Dense>

// boost headers
#include <boost/random.hpp>
#include <boost/math/distributions.hpp> // import all distributions
#include <boost/random/normal_distribution.hpp>
#include <boost/random/mersenne_twister.hpp>

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

// Constructor
PF::PF(const PFInputs &input) : rng(input.seed)
{
  N = input.N;
  T = input.T;
  resample_interval = input.resample_interval; 
  seed = input.seed;
  y = input.y;
  g_std = input.g_std;
  f_std = input.f_std;
}

// Run particle filter
void PF::run()
{
  particles = VectorXd::Zero(N); // particle X
  weights = VectorXd::Ones(N); // weights

  for(int t = 0; t <= T; t++){
       if (resample_interval > 0 && t % resample_interval == 0 && t > 0) {
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
  std::vector<double> tmp;
  tmp.resize(N);
  for(int i = 0; i < N; i++){
  	tmp[i] = weights[i];
  }
  
  // sample from weights
  boost::random::discrete_distribution<> dist(tmp.begin(), tmp.end());
  for(int i = 0; i < N; i++){
  	 tmp_particles[i] = particles[dist(rng)];
  }
 
  return tmp_particles;
}

double toy_f(double x, int t) {
    return x/2 + 25*x/(1+pow(x,2)) + 8*cos(1.2*t);
}

int main(){
  using namespace std;

  // Inputs to PF
  PFInputs input;
  input.N = 1000;
  input.T = 100;
  input.resample_interval = 5;
  input.seed = 123;
  input.g_std = 1;
  input.f_std = sqrt(10);

  // generate artificial time series of X_t
  boost::mt19937 rng;
  boost::normal_distribution<> f_rng(0, input.f_std);
  VectorXd X = VectorXd::Zero(input.T+1);
  X[0] = f_rng(rng);
  for (int i = 1; i <= input.T; i++) {
    X[i] = toy_f(X[i-1], i) + f_rng(rng);
  }

  // generate artificial time series of Y_t
  boost::normal_distribution<> g_rng(0,input.g_std);
  VectorXd Y = VectorXd::Zero(input.T+1);
  for (int i = 0; i <= input.T; i++) {
    Y[i] = pow(X[i],2)/20 + g_rng(rng); 
  }

  input.y = Y;

  // Run PF  
  PF pf(input);
  pf.run();
  //cout << "Output particles\n";
  //cout << pf.particles << endl;
  //cout << "Output weights\n";
  //cout << pf.weights << endl;
  //cout << "weights sum\n";
  //cout << pf.weights.sum() << endl;
  
  // Predict X_{T+1}
  VectorXd estm(input.N);
  for (int i = 0; i < input.N; i++) {
    estm[i] = toy_f(pf.particles[i], input.T+1) * pf.weights[i];
  }
  cout << "Our estimator\n";
  cout << estm.sum() << endl;
  cout << "True param\n";
  cout << toy_f(X[input.T], input.T+1) << endl;
 
  return 1; 
}
