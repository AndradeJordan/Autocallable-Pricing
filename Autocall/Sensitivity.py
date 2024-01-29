from Autocall.autocall import AutoCall
import numpy as np

from Autocall.displayer import DisplayerAutocall

class sensitivity(AutoCall):
    def __init__(self,r, s0, sigma, T, N, n, Coupon, B, H,tag):
        super().__init__(r, s0, sigma, T, N, n, Coupon, B, H)
        self.tag = tag
        self.nb_points = 100
        self.price_variation = np.zeros(self.nb_points)
        self.Spaths = None

    def ComputeSensitivityVal(self) :
        r, s0, sigma, T, N, n, Coupon, B, H = self.interest_rate, self.spot, self.sigma, self.maturity, self.MC_simulation, self.Time_step, self.Coupon, self.low_barrier, self.high_barrier

        for sensi in self.tag :
            print(sensi)
            if sensi == "Autocall_level_H_sensi" :
                Hmin = 100
                Hmax = 250
                H_sensi = np.linspace(Hmin, Hmax, self.nb_points)
                for i in range(self.nb_points):
                    self.high_barrier = H_sensi[i]
                    p, Z = self.premium()
                    self.price_variation[i] = np.mean(p)

                X = H_sensi

            if sensi == "Coupon_sensi":
                Cmin = 0.10
                Cmax = 0.6
                Coupon_sensi = np.linspace(Cmin, Cmax, self.nb_points)  # variation between 10% et 60%
                for i in range(self.nb_points):
                    self.Coupon = np.arange(1, 5) * Coupon_sensi[i]
                    p, Z = self.premium()
                    self.price_variation[i] = np.mean(p)

                X = Coupon_sensi

            if sensi == "Kick_In_level_B_sensi":
                Bmin = 15
                Bmax = 90
                B_sensi = np.linspace(Bmin, Bmax, self.nb_points)
                for i in range(self.nb_points):
                    self.low_barrier = B_sensi[i]
                    p, Z = self.premium()
                    self.price_variation[i] = np.mean(p)

                X = B_sensi

            if sensi == "Maturity_sensi":
                Tmin = 1
                Tmax = 50
                T_sensi = np.linspace(Tmin, Tmax, self.nb_points)  # variation between 10% et 60%
                for i in range(self.nb_points):
                    self.maturity = T_sensi[i]
                    p, Z = self.premium()
                    self.price_variation[i] = np.mean(p)

                X = T_sensi

            if sensi == "nb_observation_sensi":
                number_observation_sensi = np.arange(1, self.nb_points + 1)
                for i in range(self.nb_points):
                    self.Time_step = number_observation_sensi[i]
                    self.Coupon = 0.25 * np.arange(1, i + 1)
                    p, Z = self.premium()
                    self.price_variation[i] = np.mean(p)

                X = number_observation_sensi



            DisplayerAutocall.Display_sensi(X, self.price_variation, sensi)





