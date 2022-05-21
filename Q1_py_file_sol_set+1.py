

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.Series([24.23, 25.53, 25.41, 24.14, 29.62, 28.25, 25.81, 24.39, 40.26, 32.95,91.36, 25.99, 39.42, 26.71, 35.00])
name = ["Allied Signal","Bankers Trust","General Mills","ITT Industries","J.P.Morgan & Co.","Lehman Brothers","Marriott","MCI","Merrill Lynch",
         "Micrsoft","Morgan Stanley","Sun Microsystems","Travelers","US Airways","Warner-Lambert"]

# Box Plot
import seaborn as sns
sns.boxplot(df)
plt.show()
print(df.mean())
print(df.std())
print(df.var())