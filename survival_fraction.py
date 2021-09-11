

from matplotlib import pyplot as plt
import pandas as pd


def survival_fraction(train_df, plot):
    # Proportion of survival by age
    survived = 'survived fraction'
    women = train_df[train_df['Sex']=='female']
    men = train_df[train_df['Sex']=='male']

    women_surviving = women[women['Survived']==1].Age.dropna()

    woman_survival_fraction = []
    men_survival_fraction = []
    for i in range(3, 60, 1):
        woman_survival_count = (women[women['Survived']==1].Age.dropna() == i).sum()
        men_survival_count = (men[men['Survived']==1].Age.dropna() == i).sum()

        woman_not_survival_count = (women[women['Survived']==0].Age.dropna() == i).sum()
        men_not_survival_count = (men[men['Survived']==0].Age.dropna() == i).sum()

        woman_survival_fraction.append([i, woman_survival_count / ( woman_survival_count + woman_not_survival_count)])
        men_survival_fraction.append([i, men_survival_count / ( men_survival_count + men_not_survival_count)])

    woman_survival_fraction = pd.DataFrame.from_records(woman_survival_fraction)
    men_survival_fraction = pd.DataFrame.from_records(men_survival_fraction)



    woman_survival_fraction = woman_survival_fraction.rename(columns={0: "Age", 1: 'survival_fraction'})
    men_survival_fraction = men_survival_fraction.rename(columns={0: "Age", 1: 'survival_fraction'})
    woman_survival_fraction = woman_survival_fraction.set_index("Age")
    men_survival_fraction = men_survival_fraction.set_index("Age")

    if plot:
        # ax = plt.plot(woman_survival_fraction, x="Age", bins=18, label = survived, ax = axes[0], kde =False)
        plt.plot(woman_survival_fraction, label = "Survival fraction by age")
        # ax.legend()
        # ax.set_title('Female')
        plt.show()
        plt.plot(men_survival_fraction, label = "Survival fraction by age")
        # ax.legend()
        # _ = ax.set_title('Male')
        plt.show()