#  -*- coding: UTF-8 -*-
#
#  test.py
#
#  Created by Diego on 2022/08/15 19:51:33.
#  Copyright © Diego. All rights reserved.

import numpy as np
from sciplot import SciPlot
import matplotlib

if __name__ == '__main__':
    x = np.linspace(0, 10, 20)
    y = [(a+1) * x for a in range(8)]
    print(len(np.shape(x)))
    # SciPlot(x, y, label=['x-axis', 'y-axis'], legend=['legend'])
    diego = SciPlot()
    diego.manual_load(x, y, [], [n for n in range(8)])
    diego.plot_data()
    diego.plot_legend()
    # print(diego.ax.get_xticks())
    # print(diego.ax.get_xlim())
    # print(diego.ax.get_xticklabels())
    diego.show()
