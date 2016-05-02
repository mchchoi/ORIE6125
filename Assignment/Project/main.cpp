#include <iostream>
#include <vector>
#include <cmath>

#include "PF.h"
#include "PFInputs.h"

double toy_f(double x, int t) {
    return x/2 + 25*x/(1+pow(x,2)) + 8*cos(1.2*t);
}

int main(){
  using namespace std;

  // Inputs to PF
  PFInputs input;
  input.N = 1000;
  input.T = 100;
  input.resample_interval = 10;
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
