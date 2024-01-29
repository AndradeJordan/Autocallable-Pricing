from absProduct import AbsProduct
from Autocall import autocall,Greeks_Output, Sensitivity
from Autocall.displayer import DisplayerAutocall
import numpy as np

def main():
    S0 = 100  # spot
    N = 10000  # monte carlo
    B = 0.75 * S0  # #Kick-in level (85% du nominal S0)
    H = 1.25 * S0  # #Autocall level  (115% du nominal S0)
    Coupon = [0.14, 0.28, 0.42, 0.56,
              0.7]  # Coupons cumulés aux dates d'observations en % du nominal (prix du bond que tu payes)
    n = len(Coupon)
    T = 5
    r = 0.02  # Taux sans risque annuel r = 2%
    sigma = 0.3  # Volatilité σ = 30%

    # Autocall's PayOff
    my_Autocall = autocall.AutoCall(r, S0, sigma, T, N, n, Coupon, B, H)
    payoff, Z = my_Autocall.premium()
    payoff_MC = np.mean(payoff)
    standart_deviation = np.std(payoff)
    DisplayerAutocall.displayPremium(payoff_MC, standart_deviation, N)

    # Greek's plot :
    B = 0.75
    H = 1.25
    greeks_tag = ['Gamma','Delta','Vega','Theta','Vega Convexity','Vega Skew']
    greeks = Greeks_Output.GreeksOutput(r, S0, sigma, T, N, n, Coupon, B, H,greeks_tag)
    greeks.ComputeGreeksVal()

    #Sensitivity's plot :
    sensi_tag = ['Autocall_level_H_sensi', 'Kick_In_level_B_sensi', 'Coupon_sensi', 'nb_observation_sensi', 'Maturity_sensi']
    sensi = Sensitivity.sensitivity(r, S0, sigma, T, N, n, Coupon, B, H, sensi_tag)
    sensi.ComputeSensitivityVal()

if __name__ == "__main__":
    main()