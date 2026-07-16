import numpy as np
from numpy.typing import NDArray


class Solution:
    def forward(self, x: NDArray[np.float64], w: NDArray[np.float64], b: float, activation: str) -> float:
        
        # activation Methods :

        # ReLu
        def relu(z :float = 0)->float:
            return max(0,z)
        
        # sigmoid
        def sigmoid(z: float = 0 )->float : 
            return 1/(1+np.exp(-z))
        ''' w = [W1,......Wn ]
                 * * * * * *
            x = [X1,......Xn ]
                    ||
                    ||
        INPUT = X1*W1 + ...... + Xn*Wn
                    +
                    +
                  BIAIS
                    ||
                    ||
                  OUTPUT  
                            
            
        '''
        input = sum(w1*x1 for w1,x1 in zip(w,x)) + b

        output :float = relu(input) if activation == "relu" else sigmoid(input)


        return float(round(output,5))




                 


        

        

