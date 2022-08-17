#  -*- coding: UTF-8 -*-
#
#  test.py
#
#  Created by Diego on 2022/08/15 19:51:33.
#  Copyright © Diego. All rights reserved.
import numpy as np
from sciplot import SciPlot
from cycler import cycler

# # Figure 1a
# x = np.linspace(0, 10, 100)
# y = np.array([(a + 1) * np.sin(x) for a in range(4)])
# SciPlot(x, y,
#         label=['x-axis', 'y-axis'],
#         legend=['line {}'.format(n + 1) for n in range(4)],
#         tag='(a)')

# Figure 1b
x = np.linspace(0, 10, 30)
y = np.array([(a + 1) * np.sin(x) for a in range(4)])
sp = SciPlot()
sp.manual_load(x, y, ['x-axis', 'y-axis'], ['line {}'.format(n + 1) for n in range(4)])
sp.plot_data(1)
sp.plot_label()
sp.plot_legend(['1', '2'])
sp.plot_tag('(b)')
sp.show()

# # Figure 1c
# x = np.linspace(0, 10, 30)
# y = np.array([(a + 1) * (x) for a in range(7)])
# sp = SciPlot()
# sp.manual_load(x, y, ['x-axis', 'y-axis'], ['line {}'.format(n + 1) for n in range(7)])
# sp.plot_data(2)
# sp.plot_label()
# sp.plot_legend()
# sp.plot_tag('(c)', (0.8, 0.93))
# sp.show()

# # Figure 1d
# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = y1 + 0.2
# y3 = np.cos(x)
# y4 = y3 + 0.2
# y = np.array([y1, y2, y3, y4])
# sp = SciPlot()
# sp.manual_load(x, y, ['x-axis', 'y-axis'], ['line {}'.format(n + 1) for n in range(4)])
# style = cycler('linestyle', ['-', '--', '-', '--']) + cycler('color', [sp.colors[0], sp.colors[0], sp.colors[3], sp.colors[3]])
# sp.plot_data(0, cycler=style)
# sp.plot_label()
# sp.plot_legend()
# sp.ax.set_xlim(-1.6, 10.2)
# sp.plot_tag('(d)')
# sp.show()
