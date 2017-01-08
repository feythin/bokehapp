# -*- coding: utf-8 -*-
# @Author : feythin lau
# Copyright (c) 2016 Feythin Lau <feythin.lau@gmail.com>

from bokeh.plotting import curdoc, figure
from bokeh.layouts import gridplot, row

# create a new plot with default tools, using figure
p1 = figure(title=u"haproxy监控")
# add a circle renderer with a size, color, and alpha
p1.line([1, 2, 3, 4, 5], [31, 14, 27, 18, 2], line_width=2)
p1.xaxis.axis_label = 'year'
p1.yaxis.axis_label = 'count'


p2 = figure(title=u"nginx监控")
# add a square renderer with a size, color, alpha, and sizes
p2.line([1, 2, 3, 4, 5], [21, 14, 17, 18, 23], line_width=2)
p2.xaxis.axis_label = 'year'
p2.yaxis.axis_label = 'count'


# create a new plot (with a title) using figure
p3 = figure(title=u"zookeper监控")
# add a line renderer
p3.line([1, 2, 3, 4, 5], [3, 4, 7, 8, 2], line_width=2)
p3.xaxis.axis_label = 'year'
p3.yaxis.axis_label = 'count'

# create a new plot (with a title) using figure
p4 = figure(title=u"redis监控")
# add a line renderer
p4.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)
p4.xaxis.axis_label = 'year'
p4.yaxis.axis_label = 'count'

p5 = figure(title=u"RabbitMQ监控")
p5.line([1, 2, 3, 4, 5], [9, 4, 3, 8, 6], line_width=2)
p5.xaxis.axis_label = 'year'
p5.yaxis.axis_label = 'count'



p6 = figure(title=u"openstack监控")
p6.line([1, 2, 3, 4, 5], [18, 12, 23, 21, 6], line_width=2)
p6.xaxis.axis_label = 'year'
p6.yaxis.axis_label = 'count'



p7 = figure(title=u"纵横客监控")
p7.line([1, 2, 3, 4, 5], [18, 23, 12, 26, 32], line_width=2)
p7.xaxis.axis_label = 'year'
p7.yaxis.axis_label = 'count'


p8 = figure(title=u"mall监控")
p8.line([1, 2, 3, 4, 5], [8, 9, 5, 10, 8], line_width=2)
p8.xaxis.axis_label = 'year'
p8.yaxis.axis_label = 'count'


# layout = row(controls, create_figure())
# layout1 = [[p1, p2], [p3, p2]]
laout1 = gridplot([[p1, p2, p4, p7], [p3, p5, p6, p8]], toolbar_location=None)
curdoc().add_root(laout1)
curdoc().title = "Crossfilter"
