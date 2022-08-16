# sciplot
A scientific style plot tool based on matplotlib.

## mini demo

```python
import numpy as np
from sciplot import SciPlot

x = np.linspace(0, 10, 100)
y = np.array([(a + 1) * np.sin(x) for a in range(4)])
sp = SciPlot(x, y,
             label=['x-axis', 'y-axis'],
             legend=['line {}'.format(n + 1) for n in range(4)],
             tag='(a)')
sp.show()
```