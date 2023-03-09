import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv(r'https://raw.githubusercontent.com/simica022/Python---FreeCodeCamp/master/Sea-Level-Predictor/epa-sea-level.csv')
    df_2000 = df.loc[df.Year >= 2000]


    # Create scatter plot
    fig, axes = plt.subplots(figsize = (10,10))
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err  = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], intercept + slope*df['Year'], 'r', label='fitted line')
    year = pd.Series([i for i in range(2000, 2050)])
    plt.plot(year, intercept + slope*year, 'b', label='fitted line')

    # Create second line of best fit
    slope, intercept, r_value, p_value, std_err  = linregress(x=df_2000['Year'], y=df_2000['CSIRO Adjusted Sea Level'])
    plt.plot(year, intercept + slope*year, 'g', label='fitted line')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
