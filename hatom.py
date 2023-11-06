import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.special import sph_harm
plt.rc('text', usetex=True)


theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)

theta, phi = np.meshgrid(theta, phi)

def plot_Y(ax, l, m):
    Y = sph_harm(abs(m), l, phi, theta)

    # separates "clouds"
    if m < 0:
        Y = Y.imag
    elif m > 0:
        Y = Y.real

    # cartesian coordinates
    Yx = np.abs(Y) * np.sin(theta) * np.cos(phi)
    Yy = np.abs(Y) * np.sin(theta) * np.sin(phi)
    Yz = np.abs(Y) * np.cos(theta)

    # color mapping (sign of Y)
    cmap = plt.cm.ScalarMappable(cmap=plt.get_cmap('PRGn'))
    cmap.set_clim(-0.5, 0.5)

    ax.plot_surface(Yx, Yy, Yz,
                    facecolors=cmap.to_rgba(Y.real),
                    rstride=2, cstride=2)

    # Axes for visualization
    ax_lim = 0.5
    ax.plot([-ax_lim, ax_lim], [0,0], [0,0], c='0.5', lw=1, zorder=10)
    ax.plot([0,0], [-ax_lim, ax_lim], [0,0], c='0.5', lw=1, zorder=10)
    ax.plot([0,0], [0,0], [-ax_lim, ax_lim], c='0.5', lw=1, zorder=10)

    ax.set_title(r'$Y_{{{},{}}}$'.format(l, m))
    ax_lim = 0.5
    ax.set_xlim(-ax_lim, ax_lim)
    ax.set_ylim(-ax_lim, ax_lim)
    ax.set_zlim(-ax_lim, ax_lim)
    ax.axis('off')

l_max = 3
figsize_px, DPI = 800, 100
figsize_in = figsize_px / DPI
fig = plt.figure(figsize=(figsize_in, figsize_in), dpi=DPI)
spec = gridspec.GridSpec(ncols=2*l_max+1, nrows=l_max+1, figure=fig)
for l in range(l_max+1):
    for m_l in range(-l, l+1):
        print(l, m_l)
        ax = fig.add_subplot(spec[l, m_l+l_max], projection='3d')
        plot_Y(ax, l, m_l)
plt.tight_layout()
plt.savefig('sph_harm.png')
plt.show()
