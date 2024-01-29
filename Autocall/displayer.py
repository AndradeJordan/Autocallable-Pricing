import numpy as np
import matplotlib.pyplot as plt



class DisplayerAutocall:
    @staticmethod
    def displayPremium(payoff, standard_deviation, MonteCarlo_simulation_number):
        confidence_interval = 1.96 * standard_deviation / np.sqrt(MonteCarlo_simulation_number)

        lower_bound = 100 * (payoff - confidence_interval)
        upper_bound = 100 * (payoff + confidence_interval)

        print('autocollable\'s payoff (%)  : ', payoff * 100)
        print('confidence Interval (%): [', lower_bound, ',', upper_bound, ']')

    def Display_Greeks(Spot,Y,tag):
        plt.figure()
        poly = np.polyfit(Spot[:-1],Y,5)
        poly_y = np.poly1d(poly)(Spot[:-1])
        plt.plot(Spot[:-1], poly_y, color="brown")
        plt.xlabel("Rendement (t=0)")
        plt.ylabel(tag)
        plt.title("Autocollable's "+" "+tag)
        plt.show()

    def Display_sensi(Sensi, Y, tag):
        plt.figure()
        plt.plot(Sensi * 100, Y * 100)
        plt.xlabel(tag)
        plt.ylabel("Price (%)")
        plt.title("Autocollable's " + " " + tag)
        plt.show()
