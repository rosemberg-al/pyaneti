#Input file for test problem for pyaneti
#Created by Barragan O.

#Relescope labels
#This vector has to be filled with the label that we use for each telescope in the RV data file
telescopes = ['S']
#This vector has to be filled with the name of each telescope telescopes[i]
telescopes_labels = ['Super_telescope']

#Input files
#fname_rv contains the RV data
fname_rv = ['earth_rv.dat']
#fname_tr contains the transit data
fname_tr = ['earth_lc.dat']

#MCMC controls
#the thin factor for the chains
thin_factor = 1
#The number of iterations to be taken into account
#The TOTAL number of iterations for the burn-in phase is thin_factor*niter
niter       = 500
#Number of independent Markov chains for the ensemble sampler
nchains     = 100

#Choose the method that we want to use
# mcmc -> runs the mcmc fit program
# plot -> this option create the plots only if a previus run was done
method = 'mcmc'
#method = 'plot'

#If you want a plot with the seaborn library, is_seaborn_plot has to be True
is_seaborn_plot = False

#Define the star parameters to calculate the planet parameters
mstar_mean  = 1.0
mstar_sigma = 0.1
rstar_mean  = 1.0
rstar_sigma = 0.1

#What units do you prefer for your planet parameters?
# earth, jupiter or solar
unit_mass = 'earth'

#If we want histogram, correlation and/or chain plots these options have to be set true
is_plot_histogram    = False
is_plot_correlations = False
is_plot_chains       = False

#Are we setting gaussian priors on the semi-major axis based on the stellar parameters?
a_from_kepler = [True]

#We want to fit transit and RV 
fit_rv = [True]
fit_tr = [True]

#Prior section
# f -> fixed value
# u -> Uniform priors
# g -> Gaussian priors
fit_t0 = ['u']   #We fit for t0 with uniform priors
fit_P  = ['u']   #We fit for P with uniform priors
fit_ew1= ['f']   #We fix sqrt(e) sin w
fit_ew2= ['f']   #We fix sqrt(e) cos w
fit_b  = ['f']   #We fix the impact factor
fit_a  = ['g']   #We fit a with gaussian priors (given by the stellar parameters)
fit_rp = ['u']   #We fit rp with uniform priors
fit_k  = ['u']   #We fit k with uniform priors
fit_v0 = 'u'     #We fit systemc velicities with uniform priors
fit_q1 = 'g'     #We fit q1 with gaussian priors
fit_q2 = 'g'     #We fit q2 with gaussian priors

#Prior ranges for a parameter A
#if 'f' is selected for the parameter A, A is fixed to the one given by min_A
#if 'u' is selected for the parameter A, sets uniform priors between min_A and max_A
#if 'g' is selected for the parameter A, sets gaussian priors with mean min_A and standard deviation max_A
min_t0  = [2448285.05] 
max_t0  = [2448285.15]  
min_P   = [365.206]
max_P   = [365.306]
min_e   = [0.0]
min_w   = [0.0]
min_ew1 = [0.0]
min_ew2 = [0.0]
min_b   = [0.0]
max_b   = [1.0]
min_a   = [200]
max_a   = [250]
min_k   = [0.0]
max_k   = [0.001]
min_rp  = [0.0]
max_rp  = [0.1]
min_q1  = 0.3464
max_q1  = 0.05
min_q2  = 0.2839
max_q2  = 0.05
