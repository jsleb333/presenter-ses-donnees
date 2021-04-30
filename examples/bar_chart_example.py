from python2latex import Plot, Palette, LinearColorMap, Document
import numpy as np

np.random.seed(42)

x = [1, 2, 3, 4]
y1 = [32, 43, 45, 61]
y2 = [45, 51, 43, 34]
labels = ['Dataset 1', 'Dataset 2', 'Dataset 3', 'Dataset 4']


plot = Plot(
    plot_path='./examples/',
    plot_name='bar_chart_example',
    as_float_env=False,
    marks=False,
    lines=False,
    grid='none',
    grid_style=('line width=.2pt', 'gray!50'),
    ymajorgrids='true',
    width='7cm',
    height='6cm',
    axis_line_style='{draw=none}',
    legend_cell_align='{left}',
    legend_style='{font=\\footnotesize, draw=none, fill=none}',
    ylabel_style='{yshift=-3.5mm}',
    bar_width='4mm',
    ybar='0mm',
    xticklabel_style='{font=\\footnotesize}',
    xtick_style='{draw=none}',
    ytick_style='{draw=none}',
)
plot.axis.options += (
    'nodes near coords',
    'every node near coord/.append style={font=\\scriptsize}',
)

plot.add_plot(x, y1, 'fill', draw='none', legend='Modèle 1')
plot.add_plot(x, y2, 'fill', draw='none', legend='Modèle 2')

plot.legend_position = 'north west'

plot.y_min = 0
plot.y_max = 79
plot.x_min = 0.5
plot.x_ticks = x
plot.x_ticks_labels = labels

plot.x_label = 'Datasets'
plot.y_label = "Précision (\%)"

doc = Document('bar_chart_example', filepath='./examples/', doc_type='standalone')

doc += plot

doc.build(delete_files=['log', 'aux'])
