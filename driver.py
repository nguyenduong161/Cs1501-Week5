import numpy as np
import logging 

    # define wahoovian function with input m for matrix
def wahoovian(m):

    logging.basicConfig(filename='logging-message.txt', level=logging.DEBUG,
                        filemode='w',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S')


    logging.info('Enter Wahoovian')

    #check if the input matrix has zero row and zero columns, if yes, return matrix unchanged
    if m.size == 0:
        logging.info('Leave Wahoovian')
        return m
        
        #check if the input matrix square, if no, return matrix unchanged
    elif m.shape[0] != m.shape[1]:
        logging.warning('Matrix is not square')
        logging.info('Leave Wahoovian')
        return m
        
        #if it input matrix is not empty and is square, transpose and negate 
    else:
        logging.info('Leave Wahoovian')
        return np.negative(m.transpose())
    # else:
    #     newM = m.transpose()
    #     newM = np.negative(newM)
    #     logging.info('Leave Wahoovian')
    #     return newM

    # Let's use nump arrays as matrices and do matrix-addition.
# m1 = np.array([[1, 2], [3, 4]])
# m2 = np.array([[-5, 6], [7, -8]])
# print(wahoovian(m1))
# print(wahoovian(m2))


if __name__ == '__main__':
    m1 = np.zeros((0))
    m2 = np.array([[1, 3, 2], [5, 4, 7]])
    m3 = np.array([[1, 2], [3, 4]])
    m4 = np.array([[-5, 6], [7, -8]])
    print(wahoovian(m1))
    print(wahoovian(m2))
    print(wahoovian(m3))
    print(wahoovian(m4))

# What's the magic of the code right before this?
#    If this file is named main.py and it's run with:  python main.py
#       then the if is True and main() is executed.
#    But, if this file is imported then the method main() is defined but not executed.

