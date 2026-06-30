import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the file
df = pd.read_csv('length_log_gradientaccumulation_v2update216.csv')

# Set up the figure
metrics = ['avg_token_length']
fig_height = 7 * len(metrics)
fig, axes = plt.subplots(len(metrics), 1, figsize=(12, fig_height))

# Force axes to be a list if there is only 1 metric
if len(metrics) == 1:
    axes = [axes]

for i, metric in enumerate(metrics):
    x = df['step'].values
    y = df[metric].values
    
    # Linear Fit
    slope_lin, intercept_lin = np.polyfit(x, y, 1)
    # Quadratic Fit
    coeffs_quad = np.polyfit(x, y, 2)
    p_quad = np.poly1d(coeffs_quad)
    # Cubic Fit
    coeffs_cub = np.polyfit(x, y, 3)
    p_cub = np.poly1d(coeffs_cub)
    x_range = np.linspace(x.min(), x.max(), 100)

    # Plot lines and fits
    axes[i].plot(x, y, marker='o', linestyle='-', color='blue', alpha=0.8, label='Actual Data')
    axes[i].plot(x, slope_lin * x + intercept_lin, color='green', linestyle='--', label='Linear Fit')
    # axes[i].plot(x_range, p_quad(x_range), color='red', linestyle='--', label='Quadratic Fit')
    axes[i].plot(x_range, p_cub(x_range), color='red', linestyle='-', label='Cubic Fit')
    
    axes[i].set_title(f'{metric.replace("_", " ").title()} Trend Analysis')
    axes[i].set_xlabel('Step')
    axes[i].set_ylabel(metric.replace("_", " ").title())
    axes[i].legend()
    axes[i].grid(True)

plt.tight_layout()
plt.savefig('combined_analysis_withexploration.png')