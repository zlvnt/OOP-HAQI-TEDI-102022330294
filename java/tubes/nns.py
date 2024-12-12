import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Parameters
df = 8  # Degrees of freedom
critical_value = 15.507  # Chi-Square critical value
H_statistic = 24.19  # Calculated H statistic

# Generate Chi-Square distribution data
x = np.linspace(0, 30, 1000)
y = chi2.pdf(x, df)

# Plot the Chi-Square distribution
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Chi-Square Distribution (df=8)', color='blue')

# Add critical value line
plt.axvline(critical_value, color='red', linestyle='--', label=f'Critical Value ({critical_value})')

# Add H statistic line
plt.axvline(H_statistic, color='green', linestyle='--', label=f'H Statistic ({H_statistic})')

# Highlight rejection region
x_reject = np.linspace(critical_value, 30, 500)
y_reject = chi2.pdf(x_reject, df)
plt.fill_between(x_reject, y_reject, color='red', alpha=0.3, label='Rejection Region')

# Add labels and legend
plt.title('Chi-Square Distribution with H Statistic and Critical Value', fontsize=14)
plt.xlabel('Chi-Square Value', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.show()
