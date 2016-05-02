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

Unit Test
---------
To test our code, we implement a nonlinear time series model which is frequently used in benchmarking filtering techniques (see e.g. <sup>[1]</sup> Example 1). The time series model is the following:

$$x_t = \dfrac{x_{t-1}}{2} + 25 \dfrac{x_{t-1}}{1+x_{t-1}^2} + 8 cos(1.2t) + u_t$$

$$y_t = \dfrac{x_t^2}{20} + v_t$$

where $$u_t \sim N(0,10)$$ for all t and $$v_t \sim N(0,1)$$ for all t, and the initial distribution is $$x_0 \sim N(0,10)$$. Broadly speaking, $$(y_t)$$ is the series of observable data while $$(x_t)$$ is series of hidden state.

To run the above test case, we can execute
```
g++ main.cpp PF.cpp
```



Reference
---------
<sup>[1]</sup>: Cappé, Olivier, Simon J. Godsill, and Eric Moulines. "[An overview of existing methods and recent advances in sequential Monte Carlo.](http://perso.telecom-paristech.fr/~cappe/Publications/Self-archive/06particle-cmg.pdf)" Proceedings of the IEEE 95.5 (2007): 899-924.

<sup>[2]</sup>: Johansen, Adam M. "[SMCTC: sequential Monte Carlo in C++.](http://wrap.warwick.ac.uk/2194/)" Journal of Statistical Software 30.6 (2009): 1-41.

<sup>[3]</sup>: Javaheri, Alireza, Delphine Lautier, and Alain Galli. "[Filtering in finance.](http://www.cis.upenn.edu/~mkearns/finread/filtering_in_finance.pdf)" Wilmott 3 (2003): 67-83.

