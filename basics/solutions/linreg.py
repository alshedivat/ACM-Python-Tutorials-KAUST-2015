import numpy.linalg as la
def linreg(X, y):
    # 1. Add a column of 1's to X; now it has a total of p columns
    ones_column = np.ones((X.shape[0], 1), dtype=X.dtype)
    X = np.hstack((ones_column, X))

    # 2. Calculate the weight vector w (should have p columns too)
    A = np.dot(X.T, X)
    A_inv = la.inv(A)
    B = np.dot(X.T, y)
    w = np.dot(A_inv, B)
    #w = np.dot(np.dot(la.inv(np.dot(X.T,X)),X.T),y) #that is the model
        
    # 3. Calculate the predicted values of the target, y_pred
    y_pred = np.dot(X, w)

    # 4. Calculate the error, sse
    sse = np.sum((y_pred - y)**2)
    
    return w, y_pred, sse

X = auto[:, 1:3]
y = auto[:, 0]
print linreg(X, y)
