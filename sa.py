#Jacob Anderson

import sys
import random
import SumofGaussians as SG
import numpy as np, sys
import math

class SumofGaussians():
    def __init__(self,dimensions,number_of_centers):
        if (dimensions < 1 or number_of_centers < 1):
            self.centers = None
            return
        self.centers = np.array([np.random.ranf(dimensions) * 10.0 for i in range(number_of_centers)])
        return
    def Eval(self,point):
        return np.sum(np.exp(-np.sum(np.apply_along_axis(lambda x: (point - x)**2.0,1,self.centers),1)))
    def Deriv(self,point):
        return np.sum(-1.0 * np.apply_along_axis(lambda x: np.exp(-np.sum((point-x)**2.0))*(2.0*(point-x)),1,self.centers),0)


def main():
    
    #take 3 command line arguments for random seed number, number of dimensions, and number of gaussians
    seed = int(sys.argv[1])
    dims = int(sys.argv[2])
    ncenters = int(sys.argv[3])
    max_val = 0
    
    np.random.seed(seed)
    
    sog = SG.SumofGaussians(dims,ncenters)
    
    epsilon = 1e-8

    # Data
    #Get Random Location
    current_location = np.random.ranf(dims) * 10
    next_location = 0
    final_location = 0
    final_val = 0
    uniform = np.random.uniform(-0.01, 0.01,dims) 
    T = 10000000
    Tmin = 0.000000000000000001
    
    #max_val = sog.Eval(current_location)
    print(" ".join(["%.8f"%(x) for x in current_location ], ), end = " ")
    print("%.8f"%max_val)
    
   
    counter = 0
     
    while T > Tmin or counter < 2000:

        next_location = current_location + np.random.uniform(-0.01, 0.01,dims) 
            
        if(sog.Eval(next_location) > sog.Eval(current_location)): 
            current_location = next_location
            max_val = sog.Eval(current_location)
            if(sog.Eval(current_location) > sog.Eval(final_location)):
                final_location = next_location
                final_val = sog.Eval(current_location)
            print(" ".join(["%.8f"%(x) for x in current_location ], ), end = " ")
            print("%.8f"%max_val)
             
            
        elif(math.exp((sog.Eval(next_location) - sog.Eval(current_location))/ T) > np.random.random_sample()): 
            current_location = next_location
            
            max_val = sog.Eval(current_location)
            print(" ".join(["%.8f"%(x) for x in current_location ], ), end = " ")
            print("%.8f"%max_val) 
        
        if(T > Tmin):
            T = T - (T * 0.09)
        counter += 1
    
    print(" ".join(["%.8f"%(x) for x in final_location ], ), end = " ")
    print("%.8f"%final_val)
    
    
main()

