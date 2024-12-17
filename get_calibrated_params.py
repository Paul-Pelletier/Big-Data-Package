import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from SVIModel import SVIModel
import math

folder_path = "E:\OutputParamsFiles\OutputFiles"
file_path = os.path.join(folder_path, "output 1604511180.csv")

calibrated_params_term_structure = pd.read_csv(file_path, sep = ",")
spot_price = 100
max_strike_spot_distance = 0.1
log_moneyness = np.log(np.linspace(spot_price*(1-max_strike_spot_distance), spot_price*(1+max_strike_spot_distance), 100)/spot_price)
fitted_smile = []

def plot_rows_against_x(df, x, n_cols = 6):
    """
    Plots each row of the DataFrame against the same x-axis.

    Parameters:
    df (pd.DataFrame): DataFrame containing the data to plot.
    x (array-like): List, array, or Series to be used as the common x-axis.
    """
    n_rows = math.ceil(df.shape[0] / n_cols)  # Number of rows in DataFrame
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(8, 2 * n_rows), sharex=True)  # Subplots configuration

    # Flatten axes for easy iteration (handles 2D axes array)
    axes = axes.flatten()

    # Iterate over rows
    for idx, row in df.iterrows():
        fitted = SVIModel().svi(x, 
                    calibrated_params_term_structure['a'][idx],
                    calibrated_params_term_structure['b'][idx],
                    calibrated_params_term_structure['rho'][idx],
                    calibrated_params_term_structure['m'][idx],
                    calibrated_params_term_structure['sigma'][idx],
                    )
        axes[idx].plot(x, fitted, marker = 'o')
        axes[idx].set_title(f"idx")
        axes[idx].grid(True)
        
# Remove empty subplots if any
    for i in range(df.shape[0], len(axes)):
        fig.delaxes(axes[i])

    plt.tight_layout()
    plt.show()

plot_rows_against_x(calibrated_params_term_structure, log_moneyness)
#for i,row in calibrated_params_term_structure.iterrows():
#    fitted_smile.append()
#print(calibrated_params_term_structure['a'][1])