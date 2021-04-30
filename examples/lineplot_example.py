from python2latex import Plot, Palette, LinearColorMap, Document
import numpy as np

x = np.linspace(.1, .7, 200)
def f(x, a=1, b=1.5, c=400, d=8):
    return np.clip((1/(a*x)**4 - d/(a*x)**3)/c + b, -5, 6.3)

y1 = f(x)
y2 = f(x, .8, 2)
y3 = f(x, .65, 2.5)
y4 = f(x, .55, 3)
y5 = f(x, .5, 3.5)

plot = Plot(
    plot_path='./examples/',
    plot_name='lineplot_example',
    as_float_env=False,
    grid_style=('gray!35', 'ultra thin'),
    width='7cm',
    height='6cm',
    ylabel_style='{yshift=-3.5mm}',
)

plot.add_plot(x*1000, y1, label='\\scriptsize$p=10$')
plot.add_plot(x*1000, y2, label='\\scriptsize$p=30$')
plot.add_plot(x*1000, y3, label='\\scriptsize$p=50$')
plot.add_plot(x*1000, y4, label='\\scriptsize$p=75$')
plot.add_plot(x*1000, y5, label='\\scriptsize$p=100$')

plot.y_min = 0
plot.y_max = 6.2
plot.x_min = 0
plot.x_max = 900

plot.x_label = 'Abscisse (unité)'
plot.y_label = 'Ordonnée (unité)'

doc = Document('lineplot_example', filepath='./examples/', doc_type='standalone')

doc += plot

doc.build(delete_files=['log', 'aux'])
