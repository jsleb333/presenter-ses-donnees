from python2latex import LinearColorMap, Palette, holi, holi_cmap, build
from python2latex import Document, TexEnvironment, JCh2rgb

def plot_palette(doc_name,
                 palette,
                 n_colors=5,
                 width=5,
                 height=1,
                 ):
    palette.n_colors = n_colors
    palette.tex_colors = []
    palette._init_colors()

    color_width = width/n_colors

    tikzpic = TexEnvironment('tikzpicture')
    tikzpic.add_package('tikz')

    for i, color in zip(range(n_colors), palette):
        pos = i*color_width
        tikzpic += f'\\fill[draw, {build(color, tikzpic)}] ({pos},0) rectangle ({pos+color_width},{height});'

    doc = Document(doc_name, filepath='./palettes/', doc_type='standalone')
    doc += tikzpic
    doc.build(delete_files=['log', 'aux'])


if __name__ == "__main__":
    # Sequential palette
    cmap = LinearColorMap(color_anchors=[(100, 20, 260), # White
                                         (15, 50, 320)], # Indigo
                          color_model='JCh')

    palette = Palette(colors=cmap,
                      cmap_range=(.05,1),
                      color_model='rgb',
                      color_transform=JCh2rgb)

    plot_palette('sequential_discrete', palette, n_colors=5)
    plot_palette('sequential_continuous', palette, n_colors=100)


    # Diverging palette
    starting_hue = 30
    cmap = LinearColorMap(color_anchors=[(30, 70, starting_hue), # Red
                                         (100, 0, starting_hue+40), # White
                                         (100, 0, starting_hue+220), # White
                                         (30, 70, starting_hue+180)], # Blue
                          anchor_pos=(0,.5,.5001,1),
                          color_model='JCh')

    palette = Palette(colors=cmap,
                      cmap_range=(0,1),
                      color_model='rgb',
                      color_transform=JCh2rgb)

    plot_palette('diverging_discrete', palette, n_colors=5)
    plot_palette('diverging_continuous', palette, n_colors=100)


    # Qualitative palette
    plot_palette('qualitative_discrete', holi(), n_colors=5)
    plot_palette('qualitative_continuous', holi(), n_colors=100)
