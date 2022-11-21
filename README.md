# sciplot
A scientific style plot tool based on matplotlib.

![Style demonstration](./example/Figure_1.png)

## Features

- Plot figures for scientific articles painlessly, with right size, font, and others.
- Quick preview, quick as hell.
- Supporting three built in styles and custom style.
  - (a) Color cycle, looks cleaner for online journals.
  - (b) Color and marker cycle, support black-and-white view.
  - (c) Line style and marker cycle, support up to 16 lines without repeat.
  - (d) Custom style, easy to set and useful when you got several groups of curves.

## Install

Install by pip:
```shell
pip install sciplot
```

Import the package:
```python
from sciplot import sciplot
```
## mini demo

To preview the figure comes from your data, the fast way is just `SciPlot(x, y)`. 
No configurations needed, you'll get a pretty much finished figure. 
Optionally, label, legend, and tag could be given as keyword arguments.

```python
# This demo gives the figure (a) above.
import numpy as np
from sciplot import sciplot

x = np.linspace(0, 10, 100)
y = np.array([(a + 1) * np.sin(x) for a in range(4)])
sciplot.SciPlot(x, y,
                label=['x-axis', 'y-axis'],
                legend=['line {}'.format(n + 1) for n in range(4)],
                tag='(a)')
```

The data, `x` and `y`, could be in different kinds of.

- A single curve like `x = [x1, x2, ...]` and `y = [y1, y2, ...]` is fine.
- Multiple curves with same `x` coordinates should be given like `x = [x1, x2, ...]` and
  `y = [[curve1_y1, curve1_y2, ...], [curve2_y1, curve2_y2, ...], ...]`
- Of course, multiple curves can have different `x` coordinates,
  just give both `x` and `y` in the form of `[[...],[...],...]`.
  And make sure they are within the same length.

## Fine tuning

A fine-tuning is needed to generate the final product.
In this case, you are supposed to use the `sciplot` in a detailed way.
There are up to 6 steps: load data, plot data, plot label, plot legend, plot tag, and show.

```python
# This demo gives the figure (b) above.
import numpy as np
from sciplot import sciplot

x = np.linspace(0, 10, 30)
y = np.array([(a + 1) * np.sin(x) for a in range(4)])
sp = sciplot.SciPlot()
sp.manual_load(x, y, ['x-axis', 'y-axis'], ['line {}'.format(n + 1) for n in range(4)])
sp.plot_data(1)  # 1 for style 1. Currently, there are 3 built in styles, 0, 1, and 2. 
# Corresponding to figure (a), (b), and (c).

sp.plot_label()  # Optionally, label can be given here as a parameter.
sp.plot_legend()  # Optionally, legend can be given here as a parameter.

sp.plot_tag('(b)')  # The position of the tag is configurable, see annotation of this function.
sp.show()  # Comes with an auto-tight function. Pass through auto_tight=False to disable it.
```

Apart those steps means you can write your own, customized ones. Or add some operations before `show()`.
Change the range of axis is often used to make curves looks better, or avoid interfering with legend and tag.
This is change by `sp.ax`, which is exactly the axis object of `matplotlib`. 
You should see the documentation of `matplotlib` for more, but I'll list some useful functions.

```python
# axis span range
sp.ax.set_xlim([0, 1])
sp.ax.set_ylim([0, 1])
# where are the scale lines
sp.ax.set_xticks([0, 0.5, 1])
sp.ax.set_yticks([0, 0.5, 1])
# plot text, lines, annotates
sp.ax.text()
sp.ax.hline()
sp.ax.vline()
sp.ax.annotate()
# create another y-axis
ax2 = sp.ax.twinx()  
```

## Load data

Data can be load in different ways.
They can be load manually by `sp.manual_load()`, or load form `txt`, `npz`, and `csv` files.
For data generated by python, `npz` is strongly recommended.
`sciplot` have three built-in functions to load these data: `load_npz()`, `load_txt()`, `load_csv()`.
These functions are coding for my use case. 
Annotations are given about how the data are organized.