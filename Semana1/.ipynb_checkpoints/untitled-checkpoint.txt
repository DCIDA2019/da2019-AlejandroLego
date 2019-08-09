def f2(x,y):
    def cuadrado(x_):
        return x_ * x_
    tmp = cuadrado(x) + cuadrado(y)
    return x,y,tmp