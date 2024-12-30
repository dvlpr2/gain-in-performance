# Statistical Proof of a Gain in Performance

Assume that the code of a computing engine has been improved.  
How do you prove that the execution time has been improved?  
And by how much?  

### Compare base/new

The methodology consists in comparing the execution times before and after the change.  
Comparing only 2 runs, before and after, is not enough, especially when a cluster is involved,  
because part of the variations come from the variations of the cluster activity, the network ...   

Then, it is more precise to run equivalent tasks multiple times, before and after the change,  
to determine the sample distributions before and after, and to compare the before/after  
distributions in pairs.  

![alt text](img/image.png)
![alt text](img/image-1.png)

The pairwise comparison is represented as a :
* matrix of `---` (success) and `XXX` (failure)  
<img src= "img/image-2.png" alt="matrix of --- and XXX" style="border: 2px solid grey;">
* matrix of pvalues (except for the naiv test)  
<img src= "img/image-3.png" alt="matrix of pvalues" style="border: 2px solid grey;">


The `data/run_data.csv` file contains the runtimes of 10 batches of 30 tasks, 5 before and 5 after the change.  
The code before change is called : `base` or `bas`. The code after change is called : `new`.  

### Statistical comparison

The the distributions are ploted and compared. It is obvious that the new code is faster, i.e. `new < base`.  
To determine by how much, a factor k is used and manually determined to test the following : `new < k * base`.  
The best value of k is manually determined by dichotomy.  

To prove this, 3 statistical tests are performed:
1. **naiv test** : `new` is simply compared to `k*base`  
2. **t-test** : this test is valid when the sample size is large, even when the distribution is not normal  
3. **Mann-Whitney-U test** : this test is non-parametric  


### Results


| Test              | Results            |
| ----------------- | ------------------ |
| 1- naiv test      | new < **0.59** * base  |
| 2- t-test         | new < **0.648** * base |
| 3- Mann-Whitney-U | new < **0.655** * base |

Each test gives a similar best k factor : **0.59 -- 0.648 -- 0.655**  
Since the worst factor, **0.655**, is greater than 0.57 and 0.638, it passes all tests.

#### Conclusion

It has been statistically proved that the runtime has been improved by at least a factor of **0.655.**  
In other terms, there is at least a **34.5 % runtime improvement**.

