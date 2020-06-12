"""Simulating the simple pendulum."""

### Sahil Islam ###
### 12/06/2020 ###

import pygame
import numpy as np
import matplotlib.pyplot as plt


def f(l, theta, omega, t):
    a = 0.5

    fr = 0.1
    g = 9.8
    c = 1

    return -float(g / l) * np.sin(theta) - c * omega + a * np.sin(fr * t)


def calculationLoop(l, theta_init, omega_init):
    theta = theta_init
    omega = omega_init
    thetas = []
    omegas = []
    time = []
    t = 0
    step = 10000
    h = 0.1
    for i in range(step):
        theta += h * omega
        omega += h * f(l, theta, omega, t)
        t += h
        thetas.append(theta)
        omegas.append(omega)
        time.append(t)

    return thetas, omegas, time


def plot(l, theta_init, omega_init):
    thetas, omegas, time = calculationLoop(l, theta_init, omega_init)
    plt.subplot(2, 2, 1)
    plt.plot(time, thetas, label="l=" + str(l) + "${\ theta}_{init}= $ " + str(int(theta_init * 180. / np.pi)))
    plt.xlabel("time")
    plt.ylabel("theta")
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(time, omegas, label="l=" + str(l) + "${\ theta}_{init}= $ " + str(int(theta_init * 180. / np.pi)))
    plt.xlabel("time")
    plt.ylabel("omega")
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.plot(thetas, omegas, label="l=" + str(l) + "${\ theta}_{init}= $ " + str(int(theta_init * 180. / np.pi)))
    plt.xlabel("theta")
    plt.ylabel("omega")
    plt.legend()
    # plt.show()


def visual(l, theta_init, omega_init):
    thetas, omegas, time = calculationLoop(l, theta_init, omega_init)
    pygame.init()

    width = 1200
    height = 600
    screen = pygame.display.set_mode((width, height))
    surface = pygame.Surface((width, height))
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    blue = (0, 0, 255)

    clock = pygame.time.Clock()
    surface.fill(white)

    xo = width / 2.
    yo = height / 2.

    omega_scale = 70
    theta_scale = 6

    def bob(x, y):
        pygame.draw.circle(screen, red, (int(x), int(y)), 10, 0)

    def line(x1, y1, x2, y2, color):
        pygame.draw.line(screen, color, (x1, y1), (x2, y2), 2)

    def point(x, y, color):
        pygame.draw.circle(surface, color, (int(x), int(y)), 1)

    while True:
        screen.fill(white)
        for i in range(len(thetas)):
            screen.blit(surface, (0, 0))

            x = l * np.sin(thetas[i])
            y = l * np.cos(thetas[i])
            line(xo, yo, x + xo, y + yo, black)  # rope
            bob(x + xo, y + yo)

            point(time[i], theta_scale * thetas[i] + yo + 100, red)
            point(time[i], omega_scale * omegas[i] + yo - 200, black)

            point(theta_scale * thetas[i] + width / 2. + 250, omega_scale * omegas[i] + height / 2., blue)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()
            clock.tick(100)


plot(50, np.pi / 4, 0)

plt.show()

visual(100, np.pi / 4, 0)
