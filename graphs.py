import math
import numpy as np
from bokeh.io import output_file
from bokeh import plotting as bkp
from bokeh.models import PrintfTickFormatter


    ## Disable autoscrolling

from IPython.display import display, Javascript

disable_js = """
IPython.OutputArea.prototype._should_scroll = function(lines) {
    return false;
}
"""
display(Javascript(disable_js))




bkp.output_notebook(hide_banner=True)

# sns.color_palette("PuBu", 15)

SIZE = 450
BLUE_COLORS = ((245, 238, 246),
               (235, 230, 241),
               (221, 219, 235),
               (207, 208, 229),
               (186, 198, 224),
               (165, 188, 218),
               (140, 178, 212),
               (115, 168, 206),
               ( 83, 156, 199),
               ( 53, 143, 191),
               ( 28, 127, 183),
               (  4, 111, 175),
               (  4, 100, 157),
               (  3,  89, 139),
               (  2,  72, 112))

RED_COLORS = ((255, 245, 181),
              (254, 236, 159),
              (254, 226, 138),
              (254, 216, 117),
              (254, 197,  96),
              (253, 177,  75),
              (253, 158,  67),
              (252, 140,  59),
              (252, 108,  50),
              (251,  76,  41),
              (238,  50,  34),
              (226,  25,  28),
              (207,  12,  33),
              (187,   0,  38),
              (156,   0,  38))


    ## Graphs

def colorbar(colors, inversed=False):
    img = np.zeros((len(colors)-1, 1), dtype=np.uint32)
    view = img.view(dtype=np.uint8).reshape(img.shape + (4,))

    for i, c in enumerate(colors[:-1]):
        r, g, b = c
        view[i, 0, 0] = r
        view[i, 0, 1] = g
        view[i, 0, 2] = b
        view[i, 0, 3] = 255

    if inversed:
        img = img[::-1]

    return img

def variance_map(perf_map, res, colors=RED_COLORS, title='performance map', **kwargs):
    #plot_map(perf_map, res, colors=colors, title=title, scale='log', **kwargs)
    plot_map(perf_map, res, colors=colors, title=title, **kwargs)

def distance_map(perf_map, res, colors=BLUE_COLORS, title='performance map on the intact arm (distance to target)', **kwargs):
    plot_map(perf_map, res, colors=colors, title=title, **kwargs)

EPSILON = 1e-10 # HACK for log scale

def plot_map(perf_map, res, title='performance map', colors=BLUE_COLORS, show=True, scale='default'):
    ps = list(perf_map.values())
    #p_min, p_max = np.min(ps), np.max(ps)
    p_min, p_max = 0.17, 0.45
    if scale == 'log':
        c_min, c_max = -math.log(-p_min+EPSILON), -math.log(-p_max+EPSILON)
    else:
        c_min, c_max = p_min, p_max

    img = np.zeros((res, res), dtype=np.uint32)
    view = img.view(dtype=np.uint8).reshape(img.shape + (4,))

    for (i, j), p in perf_map.items():
        if scale == 'log':
            p = -math.log(-p+EPSILON)
        c_idx = int(np.floor((len(colors)-1)*(p - c_min)/(c_max-c_min)))
        r, g, b = colors[c_idx]
        view[j, i, 0] = r
        view[j, i, 1] = g
        view[j, i, 2] = b
        view[j, i, 3] = 255

    #plot = bkp.figure(width=SIZE, height=SIZE, x_range=(-0.7, 0.7), y_range=(-0.7, 0.7), title=title, tools = "pan,box_zoom,reset,save")
    plot = bkp.figure(width=SIZE, height=SIZE, x_range=(0, 1), y_range=(0, 1), title=title, tools = "pan,box_zoom,reset,save")
    plot.title.text_font_size = '12pt'
    plot.yaxis.axis_label = "SS(x)"
    plot.xaxis.axis_label = "BS(x)"

    #plot.image_rgba([img], x=[-0.7],  y=[-0.7], dh=[1.4], dw=[1.4])
    plot.image_rgba([img], x=[0], y=[0], dh=[1], dw=[1])
    if scale == 'log':
        cbar = colorbar(colors, inversed=True)
        cb_plot = bkp.figure(width=100, height=SIZE, x_range=(0, 1.0), y_axis_type="log", y_range=(-p_max, -p_min))
        cb_plot.image_rgba([cbar], x=[0.0],  y=[-p_max], dw=[1.0], dh=[p_max-p_min])
    else:
        cbar = colorbar(colors)
        cb_plot = bkp.figure(title="DR(x)", width=100, height=SIZE, x_range=(0, 1.0), y_range=(p_min, p_max))
        cb_plot.image_rgba([cbar], x=[0.0],  y=[p_min], dw=[1.0], dh=[p_max-p_min])

    cb_plot.min_border_right = 25
    cb_plot.xgrid.grid_line_color = None
    cb_plot.xaxis.minor_tick_line_color = None
    cb_plot.xaxis.major_tick_line_color = None
    cb_plot.xaxis.axis_line_color = None
    cb_plot.xaxis[0].formatter = PrintfTickFormatter(format="")
    if scale == 'log':
        cb_plot.yaxis.formatter = PrintfTickFormatter(format="-%1.0e")

    if show:
        output_file("foo.html")
        bkp.show(bkp.gridplot([[plot, cb_plot]]))
    return [plot, cb_plot]