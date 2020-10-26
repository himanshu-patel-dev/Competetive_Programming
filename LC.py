import pandas as pd
import numpy as np
from tqdm import tqdm
# from tqdm.auto import tqdm  # for notebooks

df = pd.DataFrame(np.random.randint(0, int(1e8), (10000, 1000)))

# Create and register a new `tqdm` instance with `pandas`
# (can use tqdm_gui, optional kwargs, etc.)
tqdm.pandas()

# Now you can use `progress_apply` instead of `apply`
df.groupby(0).progress_apply(lambda x: x**2)