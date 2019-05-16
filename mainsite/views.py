from django.shortcuts import render, render_to_response
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

# Create your views here.


def homepage(request):
    x = np.linspace(-3, 3, 100)
    y = np.sin(x)

    plot = figure(title='Sine Graph', x_axis_label='x',
                  y_axis_label='sin(x)', plot_width=400, plot_height=400)
    plot.line(x, y, line_width=2)
    script, div = components(plot)
    content = {'script': script, 'div': div}
    return render_to_response("mainsite/base.html", content)

