# -*- coding: utf-8 -*-
import torch
import pandas as pd
from try2 import SIRDvnModel
import plotly.graph_objects as go



from scipy.stats import gaussian_kde
from plotly.subplots import make_subplots
import numpy as np
import time

torch.manual_seed(25039) # set seed
start_time = time.time()

##############################################################################################################################################################################
################################################## COMPARTMENTS: 'OBSERVED DATA' SIMULATED USING THETA.TRUE (Munelli's thesis) #############################
model = SIRDvnModel()
simulator_data = lambda inputs : model.simulateModel(inputs)
# take the posterior means of Munelli's thesis
R0_true= 0.78
c2_true= 0.67
c3_true= 0.66
c4_true= 0.67
true_inputs = torch.tensor([[R0_true, c2_true, c3_true, c4_true, 0.0003, 0.0005, 10, 10, 14, 14]])

Sobs_v,Iobs_v,Robs_v, Dobs_v,Sobs_n,Iobs_n,Robs_n, Dobs_n, i_v_obs, i_n_obs = simulator_data(true_inputs) # we are simulating ( see arrays)
max_time = 157
times = torch.linspace(0,max_time-1,max_time)



############################################# REPORT:  'OBSERVED DATA' (SIMULATED) USING THETA.TRUE  #################################


start_date= "2022-05-26"  # t0 =26/05/2022; t1 = 27/05/2022
end_date = "2022-10-31"  # T = 31/10/2022
date_range = pd.date_range(start=start_date, end=end_date, freq='D') # sequence of dates from start_date to end_date (day by day)
dates = pd.DatetimeIndex(date_range) # Convert the range to a pandas datetime object

# create a vector [(D1, D1b, D1e), ..., (DR, DRb, DRe)]

reports = [
    ("2022-07-20", "2022-05-27", "2022-06-26"), # più o meno 1 mese di infetti
    ("2022-07-27", "2022-06-03", "2022-07-03"),
    ("2022-08-03", "2022-06-10", "2022-07-10"),
    ("2022-08-10", "2022-06-17", "2022-07-17"),
    ("2022-08-17", "2022-06-24", "2022-07-24"),
    ("2022-08-23", "2022-07-01", "2022-07-31"),
    ("2022-08-31", "2022-07-08", "2022-08-07"),
    ("2022-09-07", "2022-07-15", "2022-08-14"),
    ("2022-09-14", "2022-07-22", "2022-08-21"),
    ("2022-09-21", "2022-07-29", "2022-08-28"),
    ("2022-09-28", "2022-08-05", "2022-09-04"),
    ("2022-10-05", "2022-08-12", "2022-09-11"),
    ("2022-10-12", "2022-08-19", "2022-09-18"),
    ("2022-10-19", "2022-08-26", "2022-09-25"),
    ("2022-10-26", "2022-09-02", "2022-10-02")
]

#reports = [ ("2022-07-20", "2022-05-27", "2022-06-26")]

reports = [(pd.to_datetime(d1), pd.to_datetime(d2), pd.to_datetime(d3)) for d1, d2, d3 in reports]

D_PC_obs = Dobs_v + Dobs_n # 1x157
#D_ISS_v_obs, D_ISS_n_obs = model.PseudoData(model.SimulateReport, dates, reports, i_v_obs, i_n_obs)
D_ISS_obs = model.PseudoData(model.SimulateReport, dates, reports, i_v_obs, i_n_obs) # 15 * window



##############################################################################################################################################################################
#################################################################### IS ABC PROCEDURE #####################################################

######################################################## PRIORS
# generate samples from the prior distributions to understand and visualize the prior beliefs about the parameters

prior_R0 = torch.distributions.uniform.Uniform(0.1, 3)
prior_c2 = torch.distributions.uniform.Uniform(0.5,2)
prior_c3 = torch.distributions.uniform.Uniform(0.5,2)
prior_c4 = torch.distributions.uniform.Uniform(0.5,2)

prior_R0_sample = prior_R0.sample(torch.tensor([1000])) # 1000 samples from the prior distribution
prior_c2_sample = prior_c2.sample(torch.tensor([1000]))
prior_c3_sample = prior_c3.sample(torch.tensor([1000]))
prior_c4_sample = prior_c4.sample(torch.tensor([1000]))

prior_sample = pd.DataFrame({'R0': prior_R0_sample,
                                'c2': prior_c2_sample, 'c3': prior_c3_sample, 'c4': prior_c4_sample})

###################################################################################### OBSERVED DATA: y_obs ########################################################
y_obs = [D_PC_obs, D_ISS_obs]

############################################################## PROPOSALS
proposal_R0 = prior_R0
proposal_c2 = prior_c2
proposal_c3 = prior_c3
proposal_c4 = prior_c4

###########################################################################################  IS algorithm
###########################################################################################
S = 10000
# proposals samples
# Since the proposal distribution is set equal to the prior distribution, you are effectively sampling from the prior distribution
#This step is part of the IS algorithm where you sample from the proposal distribution to approximate the posterior distribution. Since the proposal is set to the prior, you are sampling from the prior again
proposal_R0_sample =  proposal_R0.sample(torch.tensor([S])).reshape([S, 1])
proposal_c2_sample = proposal_c2.sample(torch.tensor([S])).reshape([S, 1])
proposal_c3_sample= proposal_c3.sample(torch.tensor([S])).reshape([S,1])
proposal_c4_sample = proposal_c4.sample(torch.tensor([S])).reshape([S,1])

thetas_is = torch.cat([proposal_R0_sample, proposal_c2_sample, proposal_c3_sample, proposal_c4_sample], 1) # THETA IS from the proposals

########################################################################################## SIMULATED DATA: y_sim ########################################################
##### simulate the model for each set of parameters

S_sim_v, I_sim_v, R_sim_v, D_sim_v, S_sim_n, I_sim_n, R_sim_n, D_sim_n, i_sim_v, i_sim_n = simulator_data(thetas_is)



D_PC_is = D_sim_v + D_sim_n # Sx157
# D_PC[0]= 0 ok.
# FOR R IN REPORTS: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# per come hai scritto ora il codice dovretsi campionare 1 milione di campioni da una esponenziale
start_time = time.time()
D_ISS_sim = model.PseudoData(model.SimulateReport, dates, reports, i_sim_v, i_sim_n) #


end_time = time.time()
execution_time = end_time - start_time
print(f"Total execution time: {execution_time / 60:.2f} minutes")




y_sim = [D_PC_is, D_ISS_sim]
print(y_sim[0])
print(y_sim[1])




# To compare y_obs[0] with each row of y_sim[0] and y_obs[1] with each row of y_sim[1], we need to calculate the distances separately for each pair and then combine them.
get_distance = lambda y1, y2: torch.norm(y1 - y2, 2, dim=1)  # sqrt( SUM (y.t,obs - y.t,sim)^2) )
distances_0 = get_distance(y_sim[0], y_obs[0]) # btw the observed PC and the simulated PC
# D_ISS_is[0] contains the 5 reports under theta.is(0)
# Calculate the distances for each report and sum them up


# verify
#first_scenario= distances_0[0] + distances_1[0] == distances_is[0] # True ( you combine the 2 data sources)
#distances_0[0]--> Euclidean distance between the first row of y_sim[0] and of y_obs[0]
# distances_0[1] --> Euclidean distance between the second row of y_sim[0] and y_obs[0]
# distances_1[0] --> Euclidean distance between the first row of y_sim[1] and y_obs[1]
def compute_report_distance(sim_report, obs_report):
    # Unpack the simulated and observed death counts for vaccinated (v) and non-vaccinated (n)
    sim_v, sim_n = sim_report  # each is a tensor of shape [S, window_length]
    obs_v, obs_n = obs_report

    # Combine the two counts (e.g., total deaths in the reporting window)
    sim_total = sim_v + sim_n
    obs_total = obs_v + obs_n

    # Compute the Euclidean distance along the reporting window dimension (dim=1)
    return torch.norm(sim_total - obs_total, p=2, dim=1)

# Now, assuming y_sim[1] and y_obs[1] are lists of reports (one per reporting period),
# compute the distance for each report:
distances_1 = [
    compute_report_distance(sim_report, obs_report)
    for sim_report, obs_report in zip(y_sim[1], y_obs[1])
]

# If you only have one report (as in your current setup), you can extract it:
distance_1 = distances_1[0]
print(distance_1)

distances_is = distances_0 + distance_1

epsilon = torch.kthvalue(distances_is, 100).values

# FINAL SAMPLE
sample_IS = thetas_is[distances_is < epsilon, :]

sample_is = pd.DataFrame(thetas_is.reshape(S, 4))