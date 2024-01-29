from Autocall.autocall import AutoCall
import numpy as np

from Autocall.displayer import DisplayerAutocall

class GreeksOutput(AutoCall):
    def __init__(self,r, s0, sigma, T, N, n, Coupon, B, H,tag):
        super().__init__(r, s0, sigma, T, N, n, Coupon, B, H)
        self.tag = tag
        self.nb_points = 250
        self.greeks_val = None
        self.Spaths = None

    def ComputeGreeksVal(self) :
        r, s0, sigma, T, N, n, Coupon, B, H = self.interest_rate, self.spot, self.sigma, self.maturity, self.MC_simulation, self.Time_step, self.Coupon, self.low_barrier, self.high_barrier

        for greeks in self.tag :
            print(greeks)
            if greeks == "Delta" :
                S0_grecque = np.linspace(0.6, 1.50, self.nb_points + 1)
                Delta_grec = np.zeros(self.nb_points)
                for i in range(self.nb_points):
                    self.spot = S0_grecque[i]
                    #my_Autocall = AutoCall(r, S0_grecque[i], sigma, T,N, n, Coupon, B, H)
                    payoff_MC, Z = self.premium()
                    pay = payoff_MC*np.sum(Z,axis=1)/(S0_grecque[i]*sigma*T)
                    Delta_grec[i] = np.mean(pay)
                greeks_val = Delta_grec

            if greeks == "Gamma" :
                S0_grecque = np.linspace(0.6, 1.50, self.nb_points + 1)
                Gamma_grec = np.zeros(self.nb_points)
                for i in range(self.nb_points):
                    self.spot = S0_grecque[i]
                    # my_Autocall = AutoCall(r, S0_grecque[i], sigma, T,N, n, Coupon, B, H)
                    payoff_MC, Z = self.premium()
                    pay = payoff_MC*((np.sum(Z,axis=1))**2/(sigma*T)-np.sum(Z,axis=1)-1/sigma)/(S0_grecque[i]**2*sigma*T)
                    Gamma_grec[i] = np.mean(pay)

                greeks_val = Gamma_grec

            if greeks == "Theta" :
                S0_grecque = np.linspace(0.6, 1.50, self.nb_points + 1)
                Theta_grec = np.zeros(self.nb_points)
                for i in range(self.nb_points):
                    self.spot = S0_grecque[i]
                    # my_Autocall = AutoCall(r, S0_grecque[i], sigma, T,N, n, Coupon, B, H)
                    payoff_MC, Z = self.premium()
                    pay = r * payoff_MC - r * S0_grecque[i] * payoff_MC * np.sum(Z, axis=1) / (
                                S0_grecque[i] * sigma * T) - sigma ** 2 / 2 * S0_grecque[i] * payoff_MC * (
                                      (np.sum(Z, axis=1)) ** 2 / (sigma * T) - np.sum(Z, axis=1) - 1 / sigma) / (
                                      S0_grecque[i] ** 2 * sigma * T)
                    Theta_grec[i] = np.mean(pay)

                greeks_val = Theta_grec

            if greeks == "Vega":
                S0_grecque = np.linspace(0.6, 1.50, self.nb_points + 1)
                Vega_grec = np.zeros(self.nb_points)
                for i in range(self.nb_points):
                    self.spot = S0_grecque[i]
                    # my_Autocall = AutoCall(r, S0_grecque[i], sigma, T,N, n, Coupon, B, H)
                    payoff_MC, Z = self.premium()
                    pay = payoff_MC * ((np.sum(Z, axis=1)) ** 2 / (sigma * T) - np.sum(Z, axis=1) - 1 / sigma)
                    Vega_grec[i] = np.mean(pay)

                greeks_val = Vega_grec

            if greeks == "Vega Convexity":
                S0_grecque = np.linspace(0.6, 1.50, self.nb_points + 1)
                Vega_conv_grec = np.zeros(self.nb_points)
                for i in range(self.nb_points):
                    self.spot = S0_grecque[i]
                    # my_Autocall = AutoCall(r, S0_grecque[i], sigma, T,N, n, Coupon, B, H)
                    payoff_MC, Z = self.premium()
                    pay = payoff_MC * ((np.sum(Z, axis=1)) ** 2 / (sigma * T) - np.sum(Z, axis=1) - 1 / sigma) ** 2 \
                          - 3 / sigma * (payoff_MC * (np.sum(Z, axis=1) - np.sum(Z, axis=1)) ** 2 / (sigma * T)) + payoff_MC * (
                                      1 / sigma ** 2 - T)
                    Vega_conv_grec[i] = np.mean(pay)

                greeks_val = Vega_conv_grec

            if greeks == "Vega Skew":
                S0_grecque = np.linspace(0.6, 1.50, self.nb_points + 1)
                Vega_Skew_grec = np.zeros(self.nb_points)
                for i in range(self.nb_points):
                    self.spot = S0_grecque[i]
                    # my_Autocall = AutoCall(r, S0_grecque[i], sigma, T,N, n, Coupon, B, H)
                    payoff_MC, Z = self.premium()
                    pay = payoff_MC / (S0_grecque[i] * sigma) - 3 * payoff_MC * np.sum(Z, axis=1) / (S0_grecque[i] * sigma * T) / sigma \
                          + 1 / (S0_grecque[i] * sigma * T) * payoff_MC * (
                                      np.sum(Z, axis=1) ** 3 / (sigma * T) - np.sum(Z, axis=1) ** 2)
                    Vega_Skew_grec[i] = np.mean(pay)

                greeks_val = Vega_Skew_grec

            DisplayerAutocall.Display_Greeks(S0_grecque, greeks_val, greeks)





