import pandas as pd
import numpy as np

#-----------------------------------------------------------------------------------------------------------------------
# Generate random data with 2 modes
# A random ratio is first generated to define the ratio of the 2 modes
# A random draw is then compared to that ratio to pick data from one of the 2 modes
def generate(mean1: float, mean2: float, std_dev: float, run_size: int) -> list[float]:
    # generate random ratio for mode 1
    ratio1 = np.random.uniform()
    
    # generate 2 series with mean1 & mean2
    rnd1 = np.random.normal(loc = mean1, scale = std_dev, size = run_size)
    rnd1 = [round(x, 2) for x in rnd1]
    rnd2 = np.random.normal(loc = mean2, scale = std_dev, size = run_size)
    rnd2 = [round(x, 2) for x in rnd2]
    
    # random mix rnd1 and rnd2 
    #  - generate random number
    #  - if number under ratio for mode 1
    #      add 
    res = []
    for i in range(run_size):
        keep1 = (np.random.uniform() <= ratio1)
        if keep1:
            res.append(rnd1[i])
        else:
            res.append(rnd2[i])
    return(res)

#-----------------------------------------------------------------------------------------------------------------------
def create_run_data():
    run_size = 30
    bas_run_ids = ['bas1', 'bas2', 'bas3', 'bas4', 'bas5']
    new_run_ids = ['new1', 'new2', 'new3', 'new4', 'new5']

    bas_mean1 = 120
    bas_mean2 = 160
    bas_stdev = 10
    new_mean1 = 70
    new_mean2 = 70
    new_stdev = 10

    run_data_dict = {
        bas_run_ids[0]: generate(mean1 = bas_mean1, mean2 = bas_mean2, std_dev = bas_stdev, run_size = run_size),
        bas_run_ids[1]: generate(mean1 = bas_mean1, mean2 = bas_mean2, std_dev = bas_stdev, run_size = run_size),
        bas_run_ids[2]: generate(mean1 = bas_mean1, mean2 = bas_mean2, std_dev = bas_stdev, run_size = run_size),
        bas_run_ids[3]: generate(mean1 = bas_mean1, mean2 = bas_mean2, std_dev = bas_stdev, run_size = run_size),
        bas_run_ids[4]: generate(mean1 = bas_mean1, mean2 = bas_mean2, std_dev = bas_stdev, run_size = run_size),
        #---------------------------------------------------------------------------------------------------------------
        new_run_ids[0]: generate(mean1 = new_mean1, mean2 = new_mean2, std_dev = new_stdev, run_size = run_size),
        new_run_ids[1]: generate(mean1 = new_mean1, mean2 = new_mean2, std_dev = new_stdev, run_size = run_size),
        new_run_ids[2]: generate(mean1 = new_mean1, mean2 = new_mean2, std_dev = new_stdev, run_size = run_size),
        new_run_ids[3]: generate(mean1 = new_mean1, mean2 = new_mean2, std_dev = new_stdev, run_size = run_size),
        new_run_ids[4]: generate(mean1 = new_mean1, mean2 = new_mean2, std_dev = new_stdev, run_size = run_size),
    }

    run_data = pd.DataFrame(run_data_dict)
    run_data.to_csv("data/run_data.csv", index = False)

#-----------------------------------------------------------------------------------------------------------------------
create_run_data()
