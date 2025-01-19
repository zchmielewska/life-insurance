import pandas as pd
from cashflower import ModelPointSet


policy = ModelPointSet(data=pd.DataFrame({
    "sum_assured": [100_000]
}))


assumption = {
  "INTEREST_RATE": 0.005,
  "DEATH_PROB": 0.003
}
