import numpy as np

x_train=np.array([1.0,2.0])
y_train=np.array([300,500])

def compute_cost(x,y,w,b):
    m=x.shape(x)
    cost=0
    for i in range(m):
        f_wb = w * x[i] + b
        cost+=(f_wb-y[i])**2
    cost=cost/(2*m)
    return cost

def compute_cost_reg(X,y,w,b,lambda=1):
    m=X.shape
    n=len(w)
    cost=0.0
    for i in range(m):
        f_wb=np.dot(X[i],w)+b
        cost+=(f_wb-y[i])**2
    cost/=2*m
    reg_cost=0.0
    for i in range(n):
        reg_cost+=w[i]**2
    reg_cost*=(lambda /(2*m))
    cost+=reg_cost
    return cost

def compute_gradient(x,y,w,b):
    m=x.shape[0]
    dj_dw=0
    dj_db=0
    for i in range(m):
        f_wb=w*x[i]+b
        dj_dw+=(f_wb-y[i])*x[i]
        dj_db+=(f_wb-y[i])
    dj_dw/=m
    dj_db/=m
    return dj_dw,dj_db

def compute_gradient_reg(X, y, w, b):
    m, n = X.shape
    dj_dw = np.zeros(n)
    dj_db = 0
    for i in range(m):
        err = np.dot(X[i], w) + b - y[i]
        for j in range(n):
            dj_dw[j] += err * X[i][j]
        dj_db += err
    dj_dw /= m
    dj_db /= m
    for j in range(n):
        dj_dw[j] += lambda *w[j] / m

    return dj_dw, dj_db

def gradient_descent(x,y,w_in,b_in,alpha,iters):
    b=b_in
    w=w_in

    for i in range(iters):
        dj_dw,dj_db=compute_gradient(x,y,w,b)
        w-=alpha*dj_dw
        b-=alpha*dj_db
    return w,b
w_in=0
b_in=0
iters=5000
alpha=1.0e-2
w_final,b_final=gradient_descent(x_train,y_train,w_in,b_in,alpha,iters)

print("w=",w_final)
print("b=",b_final)
