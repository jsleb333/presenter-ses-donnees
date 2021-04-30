from python2latex import Plot, Palette, LinearColorMap, Document
import numpy as np

np.random.seed(42)

x1 = np.random.normal(1, 1.4, 20)
x1 -= min(x1) - .5
y1 = x1 + np.random.normal(0, .7, 20)

x2 = np.random.normal(6, 2, 15)
y2 = x2 + np.random.normal(0, .5, 15)


plot = Plot(
    plot_path='./examples/',
    plot_name='scatterplot',
    as_float_env=False,
    marks=True,
    lines=False,
    grid_style=('gray!35', 'ultra thin'),
    width='7cm',
    height='6cm',
    legend_cell_align='{left}',
    legend_style='{font=\\footnotesize,draw=gray!50}',
    ylabel_style='{yshift=-3.5mm}',
)

plot.add_plot(x1, y1+2, legend='Cercle indigo', fill_opacity=.5)
plot.add_plot(x2, y2+2, mark='triangle*', mark_size='2.5pt', legend='Triangle orange', fill_opacity=.5)

plot.legend_position = 'south east'

plot.y_min = 0
plot.x_min = 0
plot.x_ticks = (0,2,4,6,8)
plot.y_ticks = np.linspace(0,10,5)

plot.x_label = 'Abscisse (unité)'
plot.y_label = 'Ordonnée (unité)'

doc = Document('scatterplot_example', filepath='./examples/', doc_type='standalone')

doc += plot

doc.build(delete_files=['log', 'aux'])
