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
    # open file using file I/O and read it into the `data` list
    # read the file and store the contents as integer values in the `data_content` variable    
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
    plt.savefig("images/heart_rate_plot" + filename[5:] + ".png") # using slicing to receive 4 images with 4 different names
    plt.close()
    
    # calculate the average, maximum, and standard deviation of this file using the functions you've wrote
    # return all 3 values

    avg_hr = average(cleaned_data)
    # print(avg_hr) 
    # if needed, we can uncomment and print the values, changing the filename on line 61 to see metrics for each phase
    max_hr = maximum(cleaned_data)
    # print(max_hr)
    std_dev_hr = standard_deviation(cleaned_data)
    # print(std_dev_hr)
    return avg_hr, max_hr, std_dev_hr

if __name__ == "__main__":
    print(run("data/phase2.txt"))


