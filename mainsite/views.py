from django.shortcuts import render, render_to_response
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.transform import factor_cmap
# Create your views here.


def homepage(request):
    fruits = ["Apples", "Pears", "Nectarines", "Plums", "Grapes", "Strawberries"]
    years = ["2015", "2016", "2017"]

    data = {
        'fruits': fruits,
        '2015': [2, 1, 4, 3, 2, 4],
        '2016': [5, 3, 3, 2, 4, 6],
        '2017': [3, 2, 4, 4, 5, 3]
    }

    color_palette = ["#3288bd", "#99d594", "#e6f598", "#fee08b", "#fc8d59", "#d53e4f"]
    # _PalettesModule.Spectral6()

    x = [(fruit, year) for fruit in fruits for year in years]
    counts = sum(zip(data['2015'], data['2016'], data['2017']), ())
    source = ColumnDataSource(data=dict(x=x, counts=counts))

    plot = figure(x_range=FactorRange(*x), plot_height=250,
                  title="Fruits Counts by Year", toolbar_location=None, tools="")

    plot.vbar(x='x', top='counts', width=0.9, source=source, line_color="white",
              fill_color=factor_cmap('x', palette=color_palette, factors=years,
                                     start=1, end=2))

    plot.y_range.start = 0
    plot.x_range.range_padding = 0.1
    plot.xaxis.major_label_orientation = 1
    plot.xgrid.grid_line_color = None

    script, div = components(plot)
    content = {'script': script, 'div': div}
    return render_to_response("mainsite/base.html", content)

