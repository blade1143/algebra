import matplotlib.pyplot as plt
import numpy as np

X = np.array([1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50])
Y = np.array([0.160, 0.990, 3.095, 4.485, 3.075, 1.010, 0.145])

# X = np.array(np.random.randint(1, 50, 50))
# Y = np.array(np.random.randint(250, 300, 50))

def aproksymacja_wielomian_2():
    D_transponowane = np.array([[1 for _ in range(len(X))], X, X**2])
    D = D_transponowane.transpose()

    Dt_i_D = D_transponowane.dot(D)

    Dt_i_y = D_transponowane.dot(Y)

    Dt_odwrotne = np.linalg.inv(Dt_i_D)

    A_szukane = Dt_odwrotne.dot(Dt_i_y)

    return A_szukane

def metoda_najmniejszych_kwadratow():
    macierz_sum_x = np.array([[len(X), sum(X), sum(X**2)],
                              [sum(X), sum(X**2), sum(X**3)],
                              [sum(X**2), sum(X**3), sum(X**4)]])

    macierz_wyjsc = np.array([[sum(np.log(Y))],
                              [sum(np.log(Y)*X)],
                              [sum(np.log(Y)*X**2)]])

    macierz_sum_x_odwrotna = np.linalg.inv(macierz_sum_x)

    macierz_A = macierz_sum_x_odwrotna.dot(macierz_wyjsc)

    return macierz_A

def funkcja_kwadratowa(x, a):
    return a[0] + a[1]*x + a[2]*x**2

def funkcja_e(x, a):
    return np.exp(1*(a[0] + a[1]*x + a[2]*x**2))


def plots():
    a_wielomian = aproksymacja_wielomian_2()
    a_kwadraty = metoda_najmniejszych_kwadratow()

    x_range = np.linspace(X.min(), X.max(), 100)

    f_a_wielomian = funkcja_kwadratowa(x_range, a_wielomian)
    f_a_kwadraty = funkcja_e(x_range, a_kwadraty)

    plt.scatter(X, Y, c='black')
    plt.plot(x_range, f_a_wielomian, c='red', label='wielomian stopnia 2')
    plt.plot(x_range, f_a_kwadraty, c='green', label='metoda najmniejszych kwadratow')
    plt.legend()
    plt.show()

plots()