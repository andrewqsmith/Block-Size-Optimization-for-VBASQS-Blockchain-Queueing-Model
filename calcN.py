import numpy as np
import matplotlib.pyplot as plt
import Queueing_Model as qm

def calcN(lamdaList, mu):
	expectedLamda = sum(lamdaList) / \
		len(lamdaList)
		
	metric = float("inf")
	n = 10
	optN = n
	numIter = 89

	(LQ, WQ, Gamma) = qm.blockchain(n, \
		numIter, expectedLamda, mu)

	deltaWQ = WQ[1:] - WQ[:numIter-1]
	deltaGamma = Gamma[1:] - \
		Gamma[:numIter-1]

	for i in range(0, numIter-1):
		calcMetric = -(n + i) * \
			np.log2(n + i) * deltaGamma[i] / \
				deltaWQ[i]

		if calcMetric < metric:
			metric = calcMetric
            optN = n + i
        else:
            break

    return optN

def plotting(title, x, ySyn, yNsyn):
    plt.plot(x, ySyn, color=’b’, \
        label="Synchronous", linewidth=2)
    plt.plot(x, yNsyn, color=’orange’, \
        label="Non-Synchronous", linewidth=2)
    
    plt.title(title)
    plt.ylim(bottom=0)
    plt.xlabel("Iterations")
    plt.ylabel(title)
    plt.legend(loc=’best’)
    plt.show()