import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)

        sums : float = 0.0 ; maximum = max([v for v in z]) 

        for i in range(len(z)):
            sums += np.exp(z[i]-maximum)
            z[i] = np.exp(z[i]-maximum)


        return np.array([round(v/sums ,4) for v in z])     



         
        
