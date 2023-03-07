import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError ("List must contain nine numbers.")

    lst = np.array(list).reshape(3,3)

    calculations = {'mean':[],
                    'variance':[],
                    'standard deviation':[],
                    'max':[],
                    'min':[],
                    'sum':[]}
    
    np_calculations = {'np.mean':'mean', 
                        'np.var':'variance',
                        'np.std':'standard deviation', 
                        'np.max':'max',
                        'np.min':'min',
                        'np.sum':'sum'}
    
    for key, value in np_calculations.items():
        func = eval(key)
        calculations[value].append(func(lst, axis=0).tolist()) 
        calculations[value].append(func(lst, axis=1).tolist())
        calculations[value].append(func(lst))

    return calculations
