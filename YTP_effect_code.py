import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import figure
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

@interact
def sinewave(Using_Percent = widgets.IntSlider(min = 0, max = 100, step = 1, value = 10),
             Helped_Percent = widgets.IntSlider(min = 0, max = 100, step = 1, value = 10)):

    p = np.linspace(0, 12, 100)
    y = 11.1 * np.exp(12 * np.log((1 - Using_Percent/100 * Helped_Percent/100/12)) * p)
    plt.figure(figsize = (20, 10))
    plt.plot(p, y)
    plt.ylim(0, 12)
    plt.ylabel('Total Unemployed (Millions)')
    plt.xlabel('Months Since October 2020')
    plt.title('Unemployment Over Time')
    plt.show()
    
p = np.linspace(0, 12, 100)
y = 11.1 * np.exp(12 * np.log((1 - 20/100 * 20/100/12)) * p)
plt.figure(figsize = (20, 10))
plt.plot(p, y)
plt.ylim(0, 12)
plt.ylabel('Total Unemployed (Millions)')
plt.xlabel('Months Since October 2020')
plt.title('Unemployment Over Time')
plt.show()
