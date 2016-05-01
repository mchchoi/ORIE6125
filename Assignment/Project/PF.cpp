#include "PF.h"
#include "PFInputs.h"

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

void PF::propagate(VectorXd &particles, VectorXd &weights, int t)
{
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
