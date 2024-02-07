# Definition

*"Automatically Callable"* or its abbreviation **autocallable** is a structured product that is automatically reimbursed and issues coupons when certain market conditions are met.

# The Parameters and Structured

The parameters of autocallables are:

- **A set of observation dates** $(t)_{i \in [0, n]}$: The lifetime of the product is discretized in n observations such that $0 = t_0 < t_1 < ... < t_n = T$, and the $t_i$ are generally separated by the same period $\Delta_t = \frac{T}{n}$.
- **An underlying S**: A financial asset that serves as a benchmark to determine the conditions for reimbursement and issuance of coupons.
- **Coupons C**: The interest amounts that the autocallable can deliver to the investor.
- **A nominal value N**: The nominal value of the autocallable.
- **A maturity T**: The maturity T determines the maximum lifespan of the product.
- **Barriers B and H**: Respectively called "Kick In Level" and "Autocall level," these are thresholds that determine the conditions of reimbursement and issuance of coupons. The H barrier is commonly fixed at the initial performance of the underlying.

# Autocallables Pricing

The valuation model follows the Black-Scholes framework with risk-neutral assumptions. The reference asset’s price is modeled as a generalized Brownian motion.

$$dS_t = \mu S_t dt + \sigma S_t dW_t$$
with 
$S_0 \in \mathbb{R}^+$

where r is the risk-free rate, and $\sigma$ is the volatility of the price process.

Under $\mathbb{Q}$, the pay-off $P$ of an autocallable is as follows:

$\mathbb{E}^{\mathbb{Q}} [P]$

where

$$P = \sum_{i=1}^n {e^{-r t_i}(1+iC) 1_{R_{t_i}>H}} + e^{-rT}  N  (1-1_{R_T\leq B)}  (1- R_T)$$

I calculated the premium using the Monte Carlo approach with the following parameters:

- $S_0 = 100$
- $N = 10000$ (Monte Carlo)
- $B = 0.75 \cdot S_0$ (Kick-in level)
- $H = 1.25 \cdot S_0$ (Autocall level)
- Coupons = [0.14, 0.28, 0.42, 0.56, 0]

# Analysis of the Greeks of an autocollable

Whenever a bank trades a derivative product, it ends up with a position that has various sources of risk. 
Where do the various risks lie?

To answer this question, I will need to know the sensitivity of an autocollable to the market parameters.
These sentitivities are commonly referred to as the Greeks : Delta, Gamma, Theta, Vega also  Vega convexity and  skew.
We used Malliavin's method to calculate the Greeks, using the derivation under the integral sign.

Moreover, I consider the barriers H = 75 and B = 125 constant and I will vary S0 between 60 and 150.

- **Delta** $\frac{\partial P_0}{\partial S} =  \frac{1}{X_0\sigma T}\mathbb{E}^{\mathbb{Q}} [g(X_T)W_T]$.
- **Gamma**: $\frac{\partial^2 P_0}{\partial^2 R(0)} =  \frac{1}{X_0^2\sigma T}\mathbb{E}^{\mathbb{Q}} [g(X_T)(\frac{W_T^2}{\sigma T}-W_T-\frac{1}{\sigma}]$.
- **Vega**: $\nu = \frac{\partial P_0}{\partial \sigma} = \mathbb{E}^{\mathbb{Q}} [g(X_T)(\frac{W_T^2}{\sigma T}-W_T-\frac{1}{\sigma})]\$.
- **Theta**:  $\frac{\partial P}{\partial t} - r + rR(0)\frac{\partial P}{\partial R(0)} + \frac{\sigma^2}{2}R(0)\frac{\partial^2 P_0}{\partial^2 R(0)} = 0$ we get $\Theta = rP -rR(0)\Delta - \frac{\sigma^2}{2}R(0)\Gamma$ .

# Conclusion 
An Autocallable  is a structured product which allow its buyer to partially benefit from the performance of an underlying without bearing all the risks,  made up of 3 financial products (Down and-In Put, barrier options and bond). It is potentially more profitable thanks to the payment of coupons if certain market conditions, depending on two barriers are met. Following the study of the Greeks, the market would have to be long-term bullish and not very volatile to hope that its capital is guaranteed, to hope to receive as many coupons as possible

