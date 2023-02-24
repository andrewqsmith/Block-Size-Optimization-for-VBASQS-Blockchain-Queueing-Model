import numpy as np
import Algorithm as alg
import Queueing_Model as qm

def process(draw, graphOut, avgOut):
    numPasses = 100
    mu = 1.0 / 15.0
    low = 0.005
    high = 0.1
    mean = 0.005
    stdev = 0.001
    nSyn = nNsyn = 90
    lamdaList = list()
    
    IterLQSyn = np.zeros(numPasses)
    IterWQSyn = np.zeros(numPasses)
    IterGammaSyn = np.zeros(numPasses)
    IterLQNsyn = np.zeros(numPasses)
    IterWQNsyn = np.zeros(numPasses)
    IterGammaNsyn = np.zeros(numPasses)
    IterNNsyn = np.zeros(numPasses)
    
    for i in range(0, numPasses):
        lamda = 0.0
        if draw == ’uniform’:
            lamda = np.random.uniform(low, high)
        elif draw == ’gaussian’:
            lamda = np.random.normal(mean, \
                stdev)
                
        (LQSyn, WQSyn, GammaSyn) = \
            qm.blockchain(nSyn, 1, lamda, mu)
        (LQNsyn, WQNsyn, GammaNsyn) = \
            qm.blockchain(nNsyn, 1, lamda, mu)
            
        IterLQSyn[i] = LQSyn[0]
        IterWQSyn[i] = WQSyn[0]
        IterGammaSyn[i] = GammaSyn[0]
        
        IterLQNsyn[i] = LQNsyn[0]
        IterWQNsyn[i] = WQNsyn[0]
        IterGammaNsyn[i] = GammaNsyn[0]
        
        IterNNsyn[i] = nNsyn
        
        lamdaList.append(lamda)
        nNsyn = alg.calcN(lamdaList, mu)
        if nNsyn > nSyn:
            nNsyn = nSyn
            
    if graphOut:
        alg.plotting(’$L_Q$’, \
            np.arange(numPasses), IterLQSyn, \
            IterLQNsyn)
        alg.plotting(’$W_Q$’, \
            np.arange(numPasses), IterWQSyn, \
            IterWQNsyn)
        alg.plotting(’$\gamma$’, \
            np.arange(numPasses), \
            IterGammaSyn, IterGammaNsyn)
            
    if avgOut:
        print(’(’ + draw + ’)average LQ: %f,\
            %f’%(np.average(IterLQSyn), \
            np.average(IterLQNsyn)))
        print(’(’ + draw + ’)average WQ: %f,\
            %f’%(np.average(IterWQSyn), \
            np.average(IterWQNsyn)))
        print(’(’ + draw + ’)average Gamma: \
            %f, %f’%(np.average(IterGammaSyn),\
            np.average(IterGammaNsyn)))
        print(’(’ + draw + ’)average N: %f, \
            %f’%(nSyn, np.average(nNsyn)))
        
if __name__ == ’__main__’:
    process(’uniform’, False, True)
    process(’gaussian’, False, True)