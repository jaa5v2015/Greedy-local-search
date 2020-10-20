# Jacob Anderson


import sys
import random
import SumofGaussians as SG
import numpy as np, sys


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
    step_size = 0.0
    inc = True
  
    
    
    
    
    np.random.seed(seed)
    
    sog = SG.SumofGaussians(dims,ncenters)
    
    epsilon = 1e-8

    # Data
    #data_input = np.loadtxt(sys.stdin)

    
    current_location = np.random.ranf(dims)
    current_location = current_location * 10
    max_val = 0
    temp_val = 0
    step_size = 0
    inc = True
    location = 0
    counter = 0
    temp_loc = current_location
    
    step_size = 0.01 * sog.Deriv(current_location)
    x_left = temp_loc - step_size
    x_right = temp_loc + step_size

    right_val = sog.Eval(x_right)
    left_val = sog.Eval(x_left)


    
    if(right_val > left_val):
        current_location = x_right
        
        while inc == True and counter < 10000:
            current_location = current_location + step_size
            temp_val = sog.Eval(current_location)
    
            if "%.8f"%temp_val > "%.8f"%max_val:
                max_val = temp_val 
                
                step_size = 0.01*sog.Deriv(current_location)
                print(" ".join(["%.8f"%(x) for x in current_location ], ), end = " ")
                print("%.8f"%max_val)
            
           
                counter += 1
            
            else:
                print(" ".join(["%.8f"%(x) for x in current_location ], ), end = " ")
                print("%.8f"%max_val)
                inc = False
            #x_right += step_size

        
    else:
        current_location = x_left
    
        while inc == True and counter < 10000:
            current_location = current_location - step_size
            temp_val = sog.Eval(current_location)
            
        
            if "%.8f"%temp_val > "%.8f"%max_val:
                max_val = temp_val 
            
                step_size = 0.01*sog.Deriv(current_location)
                print(" ".join(["%.8f"%(x) for x in current_location ], ), end = " ")
                print("%.8f"%max_val)
            
           
                counter += 1
            
            else:
                print(" ".join(["%.8f"%(x) for x in current_location ], ), end = " ")
                print("%.8f"%max_val)
                inc = False
            #x_left -= step_size
        
    
main()
