from absProduct import AbsProduct
from Autocall.displayer import DisplayerAutocall
import numpy as np

class AutoCall(AbsProduct):
    def __init__(self,r, s0, sigma, T, N, n, Coupon, B, H):
        self.interest_rate, self.spot, self.sigma, self.maturity = r, s0, sigma, T
        self.MC_simulation, self.Time_step, self.Coupon, self.low_barrier, self.high_barrier = N, n, Coupon, B, H
        self.Spaths = None

    def simulation_Path(self):
        r, S0, sigma, T, N, n = self.interest_rate, self.spot, self.sigma, self.maturity, self.MC_simulation, self.Time_step
        delta = T / n
        spaths = np.zeros((N, n + 1))
        spaths[:, 0] = S0
        W = np.sqrt(delta) * np.random.randn(N, n + 1)
        for i in range(n):
            spaths[:, i + 1] = spaths[:, i] * np.exp((r - sigma ** 2 / 2) * delta + sigma * W[:, i + 1])
        self.Spaths = spaths

        return W, spaths


    def premium(self):
        r, S0, sigma, T,N, n, Coupon, B, H = self.interest_rate, self.spot, self.sigma, self.maturity, self.MC_simulation, self.Time_step, self.Coupon, self.low_barrier, self.high_barrier
        W, St = self.simulation_Path()
        delta = T / n
        Payoff = np.zeros(N)

        def Help(r, S0, T, Coupon, B, H, j, St):
            for k in range(len(Coupon)):
                if (St[j, k + 1] >= H):
                    return np.exp(-r * (k + 1) * delta) * (1 + Coupon[k])  # autocall's case at time ti

            return np.exp(-r * T) * ((St[j, -1] >= B) + (St[j, -1] / S0) * (St[j, -1] < B))  # not autocall's at time T

        for j in range(N):
            Payoff[j] = Help(r, S0, T, Coupon, B, H, j, St)

        return Payoff, W



