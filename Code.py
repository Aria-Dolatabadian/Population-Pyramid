import pandas as pd
import matplotlib.pyplot as plt

population_data = pd.DataFrame({'Age Group': ['0-9','10-19','20-29','30-39',
                           '40-49','50-59','60-69','70-79','80-89','90+'],
                    'Male': [9000, 14000, 22000, 26000, 34000,
                             32000, 29000, 22000, 14000, 3000],
                    'Female': [8000, 15000, 19000, 28000,
                               35000, 34000, 28000, 24000, 17000, 5000]})
print(population_data.head())
y = range(0, len(population_data))
x_male = population_data['Male']
x_female = population_data['Female']

fig, axes = plt.subplots(ncols=2, sharey=True, figsize=(10, 8))
fig.patch.set_facecolor('xkcd:light grey')
plt.figtext(.5, .9, "Population Pyramid", fontsize=15, ha='center')
axes[0].barh(y, x_male, align='center', color='maroon')
axes[0].set(title='Males')
axes[1].barh(y, x_female, align='center', color='magenta')
axes[1].set(title='Females')
axes[1].grid()
axes[0].set(yticks=y, yticklabels=population_data['Age Group'])
axes[0].invert_xaxis()
axes[0].grid()
plt.show()
