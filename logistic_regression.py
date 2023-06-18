import numpy as np

X_train = np.array([[0.5, 1.5], [1,1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]])
y_train = np.array([0, 0, 0, 1, 1, 1])

def sigmoid(x):
    f=1/(1+np.exp(-x))
    return f

def logistic_cost(X,y,w,b):
    m=X.shape[0]
    cost=0.0
    for i in range(m):
        z=np.dot(X[i],w)+b
        f_wb=sigmoid(z)
        cost+=-y[i]*np.log(f_wb) - (1-y[i])*np.log(1-f_wb)
    cost/=m
    return cost

def logistic_cost_reg(X,y,w,b,lambda_=1):
    m,n=X.shape
    cost=0.0
    for i in range(m):
        z=np.dot(X[i],w)+b
        f_wb=sigmoid(z)
        cost+=-y[i]*np.log(f_wb) - (1-y[i])*np.log(1-f_wb)
    cost/=m
    reg_cost=0
    for j in range(n):
        reg_cost+=w[j]**2
    reg_cost/=lambda_/(2*m)
    cost+=reg_cost
    return cost

def compute_gradient_logistic(X,y,w,b):
    m,n=X.shape
    dj_dw=np.zeros(n)
    dj_db=0.0
    for i in range(m):
        f_wb=sigmoid(np.dot(X[i],w)+b)
        err=f_wb-y[i]
        for j in range(n):
            dj_dw+=err*X[i]
        dj_db+=err
    dj_dw/=m
    dj_db/=m
    return dj_dw,dj_db

def compute_gradient_logistic_reg(X,y,w,b,lambda_=1):
    m,n=X.shape
    dj_dw=np.zeros(n)
    dj_db=0
    for i in range(m):
        f_wb=sigmoid(np.dot(X[i],w)+b)
        err=f_wb-y[i]
        for j in range(n):
            dj_dw[j]+=err*X[i][j]
        dj_db+=err
    dj_dw/=m
    dj_db/=m
    for j in range(n):
        dj_dw[j]+=(lambda_/m)*w[j]
    return dj_dw,dj_db

def gradient_descent(X,y,w_in,b_in,alpha,iters):
    w=w_in
    b=b_in
    for i in range(iters):
        dj_dw,dj_db=compute_gradient_logistic(X,y,w,b)
        w-=alpha*dj_dw
        b-=alpha*dj_db

    return w,b
w_tmp  = np.zeros_like(X_train[0])
b_tmp  = 0.
alph = 0.1
iters = 10000

w_out, b_out = gradient_descent(X_train, y_train, w_tmp, b_tmp, alph, iters)
print(f"\nupdated parameters: w:{w_out}, b:{b_out}")