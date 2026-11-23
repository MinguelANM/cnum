import numpy as np


def bissecao(f,     # função que queremos encontrar a raiz
              a,    # a início do intervalo
              b,    # b fim do intervalo
              TOL,   # erro tolerado
              iter=16):  # número máximo de iterações
    c = (a + b) / 2  # ponto médio entre os valores a e b
    if f(a) * f(b) > 0:
        raise ValueError("Nenhuma raiz encontrada no intervalo.")
    else:
        i = 0  # variável contador
        ERRO = abs(f(b) - f(a))  # diferença entre os valores de y

        while ERRO > TOL and i < iter:  # loop iterativo com parada
            c = (a + b) / 2.0
            if f(c) == 0:
                return c, i
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c
            i += 1
            ERRO = abs(f(b) - f(a))
        return c, i


def newton(x, y):
    x = np.asarray(x, dtype=float)
    a = np.array(y, dtype=float)
    n = len(x)
    for j in range(1, n):
        a[j:] = (a[j:] - a[j - 1:-1]) / (x[j:] - x[:n - j])
    p = np.array([a[-1]])
    for k in range(n - 2, -1, -1):
        p = np.polysub(np.polymul(p, [1.0, -x[k]]), [-a[k]])
    return p


def lagrange(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    p = np.zeros(1)
    for i in range(len(x)):
        base = np.array([1.0])
        for j in range(len(x)):
            if j != i:
                base = np.polymul(base, [1.0, -x[j]]) / (x[i] - x[j])
        p = np.polyadd(p, y[i] * base)
    return p


def polinomial(x, y):
    x = np.asarray(x, dtype=float)
    return np.linalg.solve(np.vander(x, len(x)), np.asarray(y, dtype=float))


def regressao(x, y, v):
    V = v(np.asarray(x, dtype=float))
    return np.linalg.solve(V.T @ V, V.T @ np.asarray(y, dtype=float))


def dp(f, x, h):
    return (f(x + h) - f(x)) / h


def dr(f, x, h):
    return (f(x) - f(x - h)) / h


def dc(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def medio(f, a, b):
    return (b - a) * f((a + b) / 2)


def trapezio(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2


def simpson(f, a, b):
    return (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))


def integral(metodo, f, a, b, n):
    xs = np.linspace(a, b, n + 1)
    return sum(metodo(f, xs[i], xs[i + 1]) for i in range(n))