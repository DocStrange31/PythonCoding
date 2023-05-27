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

def gradient_descent(x,y,w_in,b_in,alpha,iters,grad_func):
    b=b_in
    w=w_in

    for i in range(iters):
        dj_dw,dj_db=grad_func(x,y,w,b)
        w-=alpha*dj_dw
        b-=alpha*dj_db
    return w,b
w_in=0
b_in=0
iters=5000
alpha=1.0e-2
w_final,b_final=gradient_descent(x_train,y_train,w_in,b_in,alpha,iters,compute_gradient)

print("w=",w_final)
print("b=",b_final)
