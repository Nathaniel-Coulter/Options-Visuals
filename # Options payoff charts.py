# Options payoff charts 

import matplotlib.pyplot as plt
import numpy as np

# values
stock_price = 54
strikes = [50, 55, 60]
call_premiums = {50: 5, 55: 2, 60: 1}
put_premiums = {50: 2, 55: 3, 60: 7}

# intrinsic value / time value for 50 call
strike_call = 50
call_price = call_premiums[strike_call]
intrinsic_value_call_50 = max(stock_price - strike_call, 0)
time_value_call_50 = call_price - intrinsic_value_call_50

S = np.linspace(40, 70, 300)

payoff_call_50 = np.maximum(S - 50, 0) - call_premiums[50]
payoff_put_60 = np.maximum(60 - S, 0) - put_premiums[60]

# Bull spread using 50 and 60 calls
payoff_bull_spread = (np.maximum(S - 50, 0) - call_premiums[50]) - (np.maximum(S - 60, 0) - call_premiums[60])

# Bear spread using 50 and 60 puts
payoff_bear_spread = (np.maximum(60 - S, 0) - put_premiums[60]) - (np.maximum(50 - S, 0) - put_premiums[50])

# Straddle using 50 strike
payoff_straddle = (np.maximum(S - 50, 0) - call_premiums[50]) + (np.maximum(50 - S, 0) - put_premiums[50])

fig, axs = plt.subplots(3, 2, figsize=(14, 12))
axs = axs.flatten()

# Call 50
axs[0].plot(S, payoff_call_50, label="50 Call Payoff")
axs[0].axhline(0, color='black', linestyle='--')
axs[0].set_title("Payoff: 50 Call")
axs[0].set_xlabel("Stock Price")
axs[0].set_ylabel("Profit/Loss")
axs[0].legend()

# Put 60
axs[1].plot(S, payoff_put_60, label="60 Put Payoff", color='orange')
axs[1].axhline(0, color='black', linestyle='--')
axs[1].set_title("Payoff: 60 Put")
axs[1].set_xlabel("Stock Price")
axs[1].set_ylabel("Profit/Loss")
axs[1].legend()

# Bull Spread (Calls)
axs[2].plot(S, payoff_bull_spread, label="Bull Spread (50 & 60 Calls)", color='green')
axs[2].axhline(0, color='black', linestyle='--')
axs[2].set_title("Payoff: Bull Spread (Calls)")
axs[2].set_xlabel("Stock Price")
axs[2].set_ylabel("Profit/Loss")
axs[2].legend()

# Bear Spread (Puts)
axs[3].plot(S, payoff_bear_spread, label="Bear Spread (50 & 60 Puts)", color='red')
axs[3].axhline(0, color='black', linestyle='--')
axs[3].set_title("Payoff: Bear Spread (Puts)")
axs[3].set_xlabel("Stock Price")
axs[3].set_ylabel("Profit/Loss")
axs[3].legend()

# 5. Straddle (Strike 50)
axs[4].plot(S, payoff_straddle, label="Straddle (Strike 50)", color='purple')
axs[4].axhline(0, color='black', linestyle='--')
axs[4].set_title("Payoff: Straddle at 50")
axs[4].set_xlabel("Stock Price")
axs[4].set_ylabel("Profit/Loss")
axs[4].legend()

fig.delaxes(axs[5])

plt.tight_layout()
plt.show()

(intrinsic_value_call_50, time_value_call_50)
