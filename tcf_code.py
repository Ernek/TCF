import sys
import numpy as np
import matplotlib.pyplot as plt

fin = open("Output", 'r')
lines = fin.readlines()

print(len(lines))


tcf_duration = 5000
Ncol = 11
col_value = []

for i, line in enumerate(lines):
    line_split = line.split()
    #print(line_split[1])
    col_value.append(line_split[Ncol-1])
print(len(col_value))

col_array = np.array(col_value)

def cal_ave_var(data):
    """This function calculates the average and the variance of certain data
        arg --> data : is a numpy array containing only the data
    """
    col_sum = 0
    col_var = 0
    for i in range(len(data)):
        col_sum += float(data[i])
        col_var += float(data[i]) * float(data[i])
    average = (col_sum)/(len(data))
    variance = (col_var/(len(data))) - average * average
    return(average, variance)

print(cal_ave_var(col_array))


def tcf_cal(data, time):
    """Calculates the Time Correlation Function for data
       arg --> data : is a numpy array containing only the data
           --> time : how much time~data to use for the tcf
    """
    #tcf = []
    ave, var = cal_ave_var(data)
    print(ave,var, "second time")
    ensemble_norm = 0
    tcf_sum = np.zeros(time,dtype=float)
    for i in range(len(data)-time):
        ensemble_norm += 1
        for j in range(time):
            tcf_sum[j] += (float(data[i]) - ave ) * (float(data[i+j]) -  ave)
    #print(ensemble_norm * var, len(tcf), 'ja')
    tcf_array = np.array(tcf_sum) / ensemble_norm / var
    #print(tcf[0],tcf[1],tcf[-1], tcf_array[0],tcf_array[1],tcf_array[-1])
    #tcf_array_final = []
    #for k in range(time):
    #    tcf_array_final.append(tcf_array[k]/ensemble_norm / var)
    #print(tcf_array_final[0], tcf_array[0])
    #final = np.array(tcf_array_final)
    return(tcf_array, ave, var, ensemble_norm)
    
#print(tcf_cal(col_array, tcf_duration))
a = tcf_cal(col_array, tcf_duration)[0]

plt.plot(a)
plt.show()
        
        
        
    

