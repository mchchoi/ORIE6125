ORIE6125 Project: Particle Filter
=================================

Team members: Michael Choi, Tom Fei

Introduction
------------
We implement the standard particle filter in C++ in our project.

Description of Particle Filter
----------------------------
Our main reference is Algorithm 3 in <sup>[1]</sup>.
We also look at Section 2.2 in <sup>[2]</sup> and Section 1.3 in <sup>[3]</sup>.

Description of files
--------------------
* [PF.h](PF.h) -- header file of our Particle Filter (PF)
* [PFInputs.h](PFInputs.h) -- header file of the inputs to PF
* [PF.cpp](PF.cpp) -- implements PF
* [main.cpp](main.cpp) -- unit test of PF, see the section below 

Unit Test
---------
To test our code, we implement a nonlinear time series model which is frequently used in benchmarking filtering techniques (see e.g. <sup>[1]</sup> Example 1). The time series model is the following:

![image](http://latex.codecogs.com/gif.latex?%24%24x_t%20%3D%20%5Cdfrac%7Bx_%7Bt-1%7D%7D%7B2%7D%20&plus;%2025%20%5Cdfrac%7Bx_%7Bt-1%7D%7D%7B1&plus;x_%7Bt-1%7D%5E2%7D%20&plus;%208%20cos%281.2t%29%20&plus;%20u_t%24%24)

![image](http://latex.codecogs.com/gif.latex?y_t%20%3D%20%5Cdfrac%7Bx_t%5E2%7D%7B20%7D%20&plus;%20v_t)

where u_t ~ N(0,10) for all t and v_t ~ N(0,1) for all t, and the initial distribution is x_0 ~ N(0,10). Broadly speaking, (y_t) is the series of observable data while (x_t) is the series of hidden state.

To run the above test case, we can execute
```
g++ main.cpp PF.cpp
```

We fix the following parameters in main.cpp:
```
N = 1000, T = 100, seed = 123, g_std = 1, f_std = sqrt(10)
```
and the outputs are the predicted X_{T+1} using PF and the true X_{T+1}.

We would like to investigate the effect of changing resample_interval in our PF, with T = 100. The true X_{T+1} is 6.4517. 

When resample_interval is set to 1, the predicted X_{T+1} is 5.7665, and when the resample_interval is 5, the predicted X_{T+1} is 6.5573. When the resample_interval is 10, the predicted X_{T+1} is 5.9096. It shows that the particle filter performs reasonably well, especially when the resample_interval is set to 5, which yields an error rate of less than 2%!

References
----------
<sup>[1]</sup>: Cappé, Olivier, Simon J. Godsill, and Eric Moulines. "[An overview of existing methods and recent advances in sequential Monte Carlo.](http://perso.telecom-paristech.fr/~cappe/Publications/Self-archive/06particle-cmg.pdf)" Proceedings of the IEEE 95.5 (2007): 899-924.

<sup>[2]</sup>: Johansen, Adam M. "[SMCTC: sequential Monte Carlo in C++.](http://wrap.warwick.ac.uk/2194/)" Journal of Statistical Software 30.6 (2009): 1-41.

<sup>[3]</sup>: Javaheri, Alireza, Delphine Lautier, and Alain Galli. "[Filtering in finance.](http://www.cis.upenn.edu/~mkearns/finread/filtering_in_finance.pdf)" Wilmott 3 (2003): 67-83.

