from python2latex import Plot, holi_cmap, holi, Document, LinearColorMap
from python2latex.utils import JCh2rgb, rgb2JCh
import numpy as np

sentences = [
    "The black cat chases the white mouse".split(' '),
    "Le chat noir pourchasse la souris blanche".split(' ')
]

X = np.arange(len(sentences[0]))
Y = np.arange(len(sentences[1]))
XX, YY = np.meshgrid(X, Y)
Z = np.abs(np.random.normal(0,.2, XX.T.shape))
for i in range(len(X)):
    if i in (1,5):
        Z[i,i+1] += 1
        Z[i+1,i] += 1
    elif i not in (2,6):
        Z[i,i] += 1

Z = (Z-np.min(Z))/(np.max(Z)-np.min(Z))

cmap = LinearColorMap(color_anchors=[(100, 10, 220), # White
                                     (20, 50, 320)], # Indigo
                      color_model='JCh',
                      color_transform=lambda c:tuple(JCh2rgb(c)))

cmap_def = r'\pgfplotsset{compat=1.14, colormap={bint}{' + '\n\t'.join(f'rgb({i})={cmap(i)}' for i in np.linspace(0,1,25)) + '}}'


plot = Plot(
    plot_path='./examples/',
    plot_name='heatmap_example',
    as_float_env=False,
    lines=False,
    grid=False,
    width='7.5cm',
    height='7.5cm',
    axis_line_style='{draw=none}',
    enlargelimits='false',
    y_dir='reverse',
    axis_x='top',
    x_tick_label_style='{font=\\footnotesize}',
    y_tick_label_style='{font=\\footnotesize}',
    colorbar_style='{ylabel=Attention, ylabel style={rotate=180}, yticklabels={0.00,0.25,0.50,0.75,1.00}, ytick={0,0.25,0.5,0.75,1}}'
)

plot.add_matrix_plot(X, Y, Z)
for i, zz in enumerate(Z):
    for j, z in enumerate(zz):
        if z > .6:
            plot.axis += f'\\node[white] at ({i},{j}) {{\\scriptsize {z:.2f} }};'

plot.add_to_preamble(cmap_def)

plot.x_ticks = range(len(sentences[0]))
plot.x_ticks_labels = sentences[0]
plot.y_ticks = range(len(sentences[1]))
plot.y_ticks_labels = sentences[1]

doc = Document('heatmap_example', filepath='./examples/', doc_type='standalone')
doc.add_package('xcolor')

doc += plot

doc.build(delete_files=['log', 'aux'])
