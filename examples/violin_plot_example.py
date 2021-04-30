from python2latex import Plot, holi_cmap, holi, Document, LinearColorMap
from python2latex.utils import JCh2rgb, rgb2JCh
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
features = ['petal_length',
            'petal_width',
            'sepal_length',
            'sepal_width']
data = [iris[feature] for feature in features]
# Using seaborn to produce the violin plots
ax = sns.violinplot(data=data, cut=2.3, gridsize=200, bw=.2)

plot = Plot(
    plot_path='./examples/',
    plot_name='violin_plot_example',
    as_float_env=False,
    grid='none',
    ymajorgrids='true',
    grid_style=('gray!35', 'ultra thin'),
    width='7cm',
    height='6cm',
    ylabel_style='{yshift=-4mm}',
    xlabel_style='{yshift=-3.5mm}',
    axis_line_style='{draw=none}',
    x_tick_label_style='{align=center, font=\\scriptsize}',
    xtick_style='{draw=none}',
    ytick_style='{draw=none}',
)

palette = holi(4)

for i, feature in enumerate(features):
    x, y = ax.collections[2*i]._paths[0]._vertices.T # Hacking into matplotlib objects to find the data defining the envelope

    q25, q50, q75 = np.percentile(data[i], [25, 50, 75])
    extrema = (i,i), (np.min(data[i]), np.max(data[i]))
    quartiles = (i,i), (q25, q75)
    median = (i,), (q50,)

    plot.add_plot(x, y, 'fill', line_cap='round', line_join='round', fill_opacity=.5, color=palette[i])
    plot.add_plot(*median,
                  'only marks',
                  mark_size='.4pt',
                  color=f'{palette[i]}!25')
    plot.add_plot(*extrema,
                  color=f'{palette[i]}!50!black',
                  line_cap='round',
                  line_width='1pt',
                  )
    plot.add_plot(*quartiles,
                  color=f'{palette[i]}!50!black',
                  line_cap='round',
                  line_width='2pt',
                  )

plot.x_label = 'Attribut'
plot.y_label = 'Taille (cm)'
plot.x_ticks = [0,1,2,3]
plot.x_ticks_labels = [
    'Longueur\\\\ pétale',
    'Largeur\\\\ pétale',
    'Longueur\\\\ sépale',
    'Largeur\\\\ sépale',
    ]
plot.y_ticks = list(range(0,11,2))
plot.y_min = -.6

doc = Document('violin_plot_example', filepath='./examples/', doc_type='standalone')

doc += plot

doc.build(delete_files=['log', 'aux'])
