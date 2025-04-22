import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        arr = np.array(list).reshape(3,3)

        # mean, variance, standard deviation, max, min, and sum along both axes and flattened

        # axis 0
        mean1 = np.mean(arr, axis=0)
        print(mean1)
        var1 = np.var(arr, axis=0)
        print(var1)
        std1 = np.std(arr, axis=0)
        print(std1)
        max1 = np.max(arr, axis=0)
        print(max1)
        min1 = np.min(arr, axis=0)
        print(min1)
        sum1 = np.sum(arr, axis=0)
        print(sum1)

        print("------")

        mean2 = np.mean(arr, axis=1)
        print(mean2)
        var2 = np.var(arr, axis=1)
        print(var2)
        std2 = np.std(arr, axis=1)
        print(std2)
        max2 = np.max(arr, axis=1)
        print(max2)
        min2 = np.min(arr, axis=1)
        print(min2)
        sum2 = np.sum(arr, axis=1)
        print(sum2)

        mean3 = np.mean(arr)
        print(mean3)
        var3 = np.var(arr)
        print(var3)
        std3 = np.std(arr)
        print(std3)
        max3 = np.max(arr)
        print(max3)
        min3 = np.min(arr)
        print(min3)
        sum3 = np.sum(arr)
        print(sum3)

        calculations = {
            'mean': [mean1.tolist(), mean2.tolist(), mean3.tolist()],
            'variance': [var1.tolist(), var2.tolist(), var3.tolist()],
            'standard deviation': [std1.tolist(), std2.tolist(), std3.tolist()],
            'max': [max1.tolist(), max2.tolist(), max3.tolist()],
            'min': [min1.tolist(), min2.tolist(), min3.tolist()],
            'sum': [sum1.tolist(), sum2.tolist(), sum3.tolist()]
        }
        #print(arr) 

    return calculations


print(calculate([2,6,2,8,4,0,1,5,7]))



