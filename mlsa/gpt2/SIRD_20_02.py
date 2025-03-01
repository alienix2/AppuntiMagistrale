# -*- coding: utf-8 -*-
import torch
from torch.distributions import binomial
from torch.distributions import poisson
from torch.distributions import exponential
from torch.multiprocessing import Pool


#from simulate_report import optimized_calculation



# OBSERVED PERIOD: 27/05/2022 --> 31/10/2022. t0 = 26/05/2022
# input = [R0, c2,c3,c4,p_v,p_n, Tr_v, Tr_n, Td_v, Td_n] = [R0, c2,c3,c4,0.0003, 0.0005, 10, 10, 14, 14]

class SIRDvnModel:
    def __init__(self, max_time=157, S0 = 59110000, S0_v= 46404936, I0=753748, p_v= 0.0003,p_n=0.0005 , Tr_v= 10, Tr_n= 10, Td_v= 14, Td_n= 14 ):
        # I0 refers to t0 = 26/05/2022
        # S.0.v =  46404936  number of people vaccinated with the 2nd dose as of May 27, 2022 (Munalli, code)
        # S.0.n = 12701409
        #  we observe a population of 59110000 inhabitants for 157 days
        # HP: R(O)= D(0)= 0
        self.max_time = max_time
        self.S0 = S0
        self.I0 = I0
        self.S0_v = S0_v
        self.S0_n = S0 - S0_v
        self.ev_n = (I0 * 11.98) / 100 # the 11.98% of the positive cases at t= 26/05/2022 was not vaccinated (computed by Munalli)
        # is the expected value of circulating non-vaccinated infected individuals
        self.ev_v = I0 - self.ev_n
        # Since we do not know I0_v and I0_n, we use Poisson samplings  to account for the uncertainty around their initial values.
        self.I0_v = poisson.Poisson(torch.tensor(self.ev_v).clone().detach()).sample()
        self.I0_n = poisson.Poisson(torch.tensor(self.ev_n).clone().detach()).sample()
        self.i0_v = 0
        self.i0_n = 0
        self.p_v = p_v
        self.p_n = p_n
        self.Tr_v = Tr_v
        self.Tr_n = Tr_n
        self.Td_v = Td_v
        self.Td_n = Td_n

    def simulateModel(self, inputs: torch.Tensor) -> tuple[
        torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        # create the matrices that keep the count of S,I,R,D for the 2 subpopulations
        S_v = torch.zeros(inputs.shape[0], self.max_time)  # Sx 157
        I_v = torch.zeros(inputs.shape[0], self.max_time)
        R_v = torch.zeros(inputs.shape[0], self.max_time)
        D_v = torch.zeros(inputs.shape[0], self.max_time)
        S_n = torch.zeros(inputs.shape[0], self.max_time)
        I_n = torch.zeros(inputs.shape[0], self.max_time)
        R_n = torch.zeros(inputs.shape[0], self.max_time)
        D_n = torch.zeros(inputs.shape[0], self.max_time)
        # save the 'new' infected
        i_v = torch.zeros(inputs.shape[0], self.max_time)
        i_n = torch.zeros(inputs.shape[0], self.max_time)
        # initialize the matrices
        S_v[:, 0] = self.S0_v  # time 0
        I_v[:, 0] = self.I0_v
        S_n[:, 0] = self.S0_n
        I_n[:, 0] = self.I0_n
        i_v[:, 0] = self.i0_v
        i_n[:, 0] = self.i0_n
        # define the inputs_sim
        R0 = inputs[:, 0]
        c2 = inputs[:, 1]
        c3 = inputs[:, 2]
        c4 = inputs[:, 3]
        R0_vv = R0  # how many susceptible vaccinated individuals we expect will be infected by single vaccinated infected individual
        R0_nv = R0 * c2  # Sx1
        R0_vn = R0 * c3
        R0_nn = R0 * c4

        alpha_v = (1 - self.p_v) / self.Tr_v
        alpha_n = (1 - self.p_n) / self.Tr_n
        pr_r_v = 1 - torch.exp(torch.tensor(-alpha_v))  # prob. of recovering for the vaccinated individuals
        pr_r_n = 1 - torch.exp(torch.tensor(-alpha_n))
        delta_v = self.p_v / self.Td_v
        delta_n = self.p_n / self.Td_n
        pr_d_v = 1 - torch.exp(torch.tensor(-delta_v))  # prob. of deceasing for the vaccinated individuals
        pr_d_n = 1 - torch.exp(torch.tensor(-delta_n))
        beta1 = R0_vv * (alpha_v + delta_v)  # Sx1
        beta2 = R0_nv * (alpha_n + delta_n)
        beta3 = R0_vn * (alpha_v + delta_v)
        beta4 = R0_nn * (alpha_n + delta_n)
        for t in range(1, self.max_time):
            lamda1 = beta1 * I_v[:, t - 1] / self.S0_v  # infection rate between a vaccinated (infected) individual and another vaccinated person
            lamda2 = beta2 * I_n[:, t - 1] / self.S0_v
            lamda3 = beta3 * I_v[:, t - 1] / self.S0_n
            lamda4 = beta4 * I_n[:, t - 1] / self.S0_n
            pr_inf_vv = 1 - torch.exp(-lamda1.clone().detach())  # prob. that a vaccinated infected individual infected another vaccinated (susceptible) individual if they come into contact
            pr_inf_nv = 1 - torch.exp(-lamda2.clone().detach())
            pr_inf_vn = 1 - torch.exp(-lamda3.clone().detach())
            pr_inf_nn = 1 - torch.exp(-lamda4.clone().detach())

            infection_vv = binomial.Binomial(S_v[:, t - 1],pr_inf_vv).sample()  # new infections among the vaccinated ones
            infection_nv = binomial.Binomial(S_v[:, t - 1],pr_inf_nv).sample()  # new cases of infections stem from the interaction non vaccinated infected/vaccinated susceptible
            total_count = torch.clamp(S_n[:, t - 1], min=0)
            infection_vn = binomial.Binomial(total_count, pr_inf_vn).sample()
            infection_nn = binomial.Binomial(total_count, pr_inf_nn).sample()
            recovery_v = binomial.Binomial(I_v[:, t - 1], pr_r_v).sample()  # new recoveries among the vaccinated ones
            recovery_n = binomial.Binomial(I_n[:, t - 1], pr_r_n).sample()
            deceased_v = binomial.Binomial(I_v[:, t - 1], pr_d_v).sample()  # new deaths among the vaccinated ones
            deceased_n = binomial.Binomial(I_n[:, t - 1], pr_d_n).sample()

            i_v[:, t] = infection_vv + infection_nv
            i_n[:, t] = infection_nn + infection_vn

            S_v[:, t] = S_v[:, t - 1] - infection_vv - infection_nv
            S_v[:, t] = torch.clamp(S_v[:, t], min=0)  # Ensure S_v is non-negative
            I_v[:, t] = I_v[:, t - 1] + infection_vv + infection_nv - recovery_v
            R_v[:, t] = R_v[:, t - 1] + recovery_v
            D_v[:, t] = D_v[:, t - 1] + deceased_v
            S_n[:, t] = S_n[:, t - 1] - infection_nn - infection_vn
            S_n[:, t] = torch.clamp(S_n[:, t], min=0)  # Ensure S_n is non-negative
            I_n[:, t] = I_n[:, t - 1] + infection_nn + infection_vn - recovery_n
            R_n[:, t] = R_n[:, t - 1] + recovery_n
            D_n[:, t] = D_n[:, t - 1] + deceased_n

        return S_v, I_v, R_v, D_v, S_n, I_n, R_n, D_n, i_v, i_n

    '''
    def simulate_report_worker(args):
        Dr_index, Db_index, De_index, i_v, i_n, Td_v, Td_n = args
        i_v_star = i_v[:, Db_index:De_index + 1].int()
        i_n_star = i_n[:, Db_index:De_index + 1].int()
        rate_v = 1 / Td_v
        rate_n = 1 / Td_n
        m_v = torch.sum(i_v_star, dim=1, keepdim=True)
        m_n = torch.sum(i_n_star, dim=1, keepdim=True)
        total_samples_v = m_v.sum().item()
        total_samples_n = m_n.sum().item()
        tau_v = torch.split(torch.ceil(exponential.Exponential(rate_v).sample((total_samples_v,))),
                            m_v.view(-1).tolist())
        tau_n = torch.split(torch.ceil(exponential.Exponential(rate_n).sample((total_samples_n,))),
                            m_n.view(-1).tolist())
        days = torch.arange(Db_index, De_index + 1).repeat(i_v_star.shape[0], 1)
        days_flat_v = days.flatten()
        repeats_v = i_v_star.flatten()
        i_tau_v = days_flat_v.repeat_interleave(repeats_v).split_with_sizes(m_v.view(-1).tolist())
        days_flat_n = days.flatten()
        repeats_n = i_n_star.flatten()
        i_tau_n = days_flat_n.repeat_interleave(repeats_n).split_with_sizes(m_n.view(-1).tolist())
        DD_v = [torch.add(t1, t2) for t1, t2 in zip(tau_v, i_tau_v)]
        DD_n = [torch.add(t1, t2) for t1, t2 in zip(tau_n, i_tau_n)]
        ND_v = torch.stack([torch.sum(tensor <= Dr_index).int() for tensor in DD_v]).view(-1, 1)
        ND_n = torch.stack([torch.sum(tensor <= Dr_index).int() for tensor in DD_n]).view(-1, 1)
        return ND_v, ND_n # Sx1

    def SimulateReport(self, Dr_index, Db_index, De_index, i_v: torch.Tensor, i_n: torch.Tensor):
        args = (Dr_index, Db_index, De_index, i_v, i_n, self.Td_v, self.Td_n)
        with Pool() as pool:
            results = pool.map(self.simulate_report_worker, [args])
        return results[0]
    '''



    def SimulateReport(self,Dr_index,Db_index, De_index, i_v:torch.Tensor, i_n: torch.Tensor):
        ## https://www.epicentro.iss.it/coronavirus/sars-cov-2-sorveglianza-dati-archivio , tables 4C
        # Goal: Count the number of deceased individuals infected between Db and De who died by Dr.
        i_v_star = i_v[:, Db_index:De_index+1].int()
        i_n_star = i_n[:, Db_index:De_index+1].int()
        rate_v = 1/self.Td_v
        rate_n = 1/self.Td_n
        # simulate when deaths will happen if infected
        m_v = torch.sum(i_v_star, dim=1, keepdim=True)  # Sx1, # Total infected individuals ( Diagnosis between Db and De)
        m_n = torch.sum(i_n_star, dim=1, keepdim=True)
        # simulate the time of death for each individual (how many days after the diagnosis)
        # torch.ceil = round up to the next integer because the report will count it on the next day
        total_samples_v = m_v.sum().item()
        total_samples_n = m_n.sum().item()
        # split the samples into S tensors, each with different lengths
        tau_v = torch.split(torch.ceil(exponential.Exponential(rate_v).sample((total_samples_v,))),m_v.view(-1).tolist())
        tau_n = torch.split(torch.ceil(exponential.Exponential(rate_n).sample((total_samples_n,))),m_n.view(-1).tolist())

        # Create i_tau_v and i_tau_n as lists of tensors
        days = torch.arange(Db_index, De_index + 1).repeat(i_v_star.shape[0], 1)
        days_flat_v = days.flatten()
        repeats_v = i_v_star.flatten()
        i_tau_v = days_flat_v.repeat_interleave(repeats_v).split_with_sizes(m_v.view(-1).tolist())

        days_flat_n = days.flatten()
        repeats_n = i_n_star.flatten()
        i_tau_n = days_flat_n.repeat_interleave(repeats_n).split_with_sizes(m_n.view(-1).tolist())

        DD_v = [torch.add(t1, t2) for t1, t2 in zip(tau_v, i_tau_v)] # PROBLEMA!!!
        DD_n = [torch.add(t1, t2) for t1, t2 in zip(tau_n, i_tau_n)]
        ND_v = torch.stack([torch.sum(tensor <= Dr_index).int() for tensor in DD_v]).view(-1, 1)
        ND_n = torch.stack([torch.sum(tensor <= Dr_index).int() for tensor in DD_n]).view(-1, 1)


        #DD_v, ND_v = optimized_calculation(tau_v, i_tau_v, Dr_index)
        #DD_n, ND_n = optimized_calculation(tau_n, i_tau_n, Dr_index)

        return ND_v, ND_n # Sx1
        # this function simulates the death time (day) of each individual infected between Db and De


    def PseudoData(self, simulateReport: callable, dates, reports, i_v: torch.Tensor, i_n: torch.Tensor):
        # GOAL =  [[D_v_report1, D_n_report1], ..[D_v_report15, D_n_report15]]
        D_ISS = []
        # verification_result = True
        for r in reports:
            Dr, Db, De = r
            Dr_index  = dates.get_loc(Dr)
            Db_index = dates.get_loc(Db)
            De_index = dates.get_loc(De)
            ND_v, ND_n = simulateReport(Dr_index, Db_index, De_index, i_v, i_n)
            D_ISS.append([ND_v, ND_n])
            #print(f"ND_v: {ND_v}, ND_n: {ND_n}, D_ISS_obs: {D_ISS_obs[-1]}")
            #print(f"ND_v: {ND_v}, ND_n: {ND_n}")


        return D_ISS # per ora ti stampa prima i V e poi gli N. com lo vogliamo fare?

