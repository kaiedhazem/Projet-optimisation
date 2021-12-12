import numpy.random as rnd
import numpy as np
a = 2
b = 3
noise = 5
x_min = 0
x_max = 20
n_data = 50
''''a method to calculate wofle step'''
def wolfe_rule(alpha_0,x,f,grad,f_x,grad_x,d_x,c_1,c_2): #d_x est la direction de descente  d_x . grad_x <= 0
    # test f(x_new) \leq f(x_0) + c_1 alpha ps{d_x}{grad_x} et \ps{x_new}{d_x} \geq c_2 \ps{x_0}{d_x}
    # sinon alpha <- alpha * beta
    # On cherche au fur et mesure un opt dans [minorant, majorant]
    test = 1
    iteration = 0
    alpha = alpha_0
    minorant = 0
    majorant = 1000
    while (test)&(iteration<=1000): 
        x_new = x+alpha*d_x;
        if (f(x_new)<=f_x+c_1*alpha*np.dot(grad_x,d_x))&(np.dot(grad(x_new),d_x) >= c_2*np.dot(grad_x,d_x) ):
            test = 0
        elif (f(x_new)>f_x+c_1*alpha*np.dot(grad_x,d_x)):
            majorant = alpha
            alpha = (majorant + minorant)/2
            iteration = iteration +1
        else:
            minorant = alpha
            alpha = (majorant + minorant)/2
            iteration = iteration +1
    return alpha
'''steepest descent using Wofe step'''
def steepest_descent_wolfe(f, grad, x0, iterations, error_point, error_grad, c_1=0.1,c_2=0.9,L=100):
    dim = np.max(np.shape(x0))
    x_list = np.zeros([dim,iterations])  
    f_list = np.zeros(iterations)  
    error_point_list = np.zeros(iterations)
    error_grad_list = np.zeros(iterations)    
    x = x0
    x_old = x
    grad_x = grad(x)
    d_x = -grad_x
    f_x = f(x)
    alpha_0 = -(1./L)*np.dot(d_x,grad_x)/np.power(np.linalg.norm(d_x),2)
    h = wolfe_rule(alpha_0,x,f,grad,f_x,grad_x,d_x,c_1,c_2)
    for i in range(iterations):
        x = x + h*d_x
        grad_x = grad(x)
        f_x = f(x)
        d_x = -grad_x
        alpha_0 = -(1./L)*np.dot(d_x,grad_x)/np.power(np.linalg.norm(d_x),2)
        h = wolfe_rule(alpha_0,x,f,grad,f_x,grad_x,d_x,c_1,c_2)
        x_list[:,i] = x
        f_list[i] = f_x
        error_point_list[i] = np.linalg.norm(x - x_old)
        error_grad_list[i] = np.linalg.norm(grad_x)
        
        if i % 1000 == 0:
            print("iter={}, x={}, f(x)={}".format(i+1, x, f(x)))

        if (error_point_list[i] < error_point)|(error_grad_list[i] < error_grad):
            break
        x_old = x
        
    print("point error={}, grad error={}, iteration={}, f(x)={}".format(error_point_list[i], error_grad_list[i],i+1,f(x)))
    return { 'x_list' : x_list[:,0:i], 'f_list' : f_list[0:i], 'error_point_list' : error_point_list[0:i], 'error_point_list' : error_point_list[0:i]}   
def mk_lin(a, b):
    def lin_fun(x):
        return a * x + b

    def lin_grad(x):
        grad = np.ones([2, x.size])
        grad[0,:] = x
        return grad

    def lin_hessian(x, method = 'newton', mu = 0.1):
        return np.zeros([2,2,x.size])
    return lin_fun, lin_grad

def mk_linreg(x_train, y_train):
    def linreg_fun(param):
        lin_fun = mk_lin(param[0], param[1])[0]
        return np.sum((lin_fun(x_train) - y_train) ** 2)

    def linreg_grad(param):
        lin_fun, lin_grad = mk_lin(param[0], param[1])[:2]
        grad = 2 * lin_grad(x_train) * (lin_fun(x_train) - y_train)
        return np.sum(grad, 1)
    return linreg_fun, linreg_grad

'''test on steepest descent step of Wolfe using linear regression functions'''
#generate the X and Y of the function ranging from [x_min,x_max] using step n_data
x_train = np.linspace(x_min, x_max, n_data)
y_train = a * x_train + b + noise * rnd.randn(x_train.size)

#calculating the function and the gradient 
f, grad = mk_linreg(x_train, y_train)

#error point , errors gradient, and number of iterations
error_point = 10 ** -10
error_grad = 10 ** -10
iterations = 1000
#initial X0
x0 = rnd.random(2)

result_wolfe = steepest_descent_wolfe(f, grad, x0, iterations, error_point, error_grad)
