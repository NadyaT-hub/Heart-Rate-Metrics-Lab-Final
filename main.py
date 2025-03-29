"""
The main Python module that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits

import matplotlib.pyplot as plt


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics,
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, max, and standard deviation
    """ 
    data = []
    # open file and read it line by line into the `data` list
     
    # close the file after reading
    
      
    with open(filename, "r") as data_file:
            for line in data_file:
                    data.append(line) # Store values in list
                
    data_file.close()

    # Use `filter_nondigits` to clean the data and remove invalid entries, save the output to a new variable
    cleaned_data = filter_nondigits(data)

    # plot this data to explore changes in heart rate for this file, save this visualization to the "images" folder
    
    
    plt.plot(cleaned_data)
    plt.title("Heart Rate Over Time")
    plt.xlabel("Time")
    plt.ylabel("Heart Rate")
    plt.savefig("images/heart_rate_plot" + filename[5:] + ".png") # using slicing to name 4 images differently
    plt.close()
    
    # calculate the average, maximum, and standard deviation of this file using the functions in 'metrics'
    # return all 3 values

    avg_hr = average(cleaned_data)
     
    
    max_hr = maximum(cleaned_data)
    
    std_dev_hr = standard_deviation(cleaned_data)
    
    return avg_hr, max_hr, std_dev_hr

if __name__ == "__main__":
    print(run("data/phase2.txt"))


