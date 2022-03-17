import pandas as pd
titanic = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')
pd.set_option('display.precision', 3)
titanic.columns = ['Name','Survived','Sex','Age','Class']
print(titanic.head())
print(titanic.tail())
print(titanic.describe())
print((titanic.Survived == 'yes').describe())
import matplotlib.pyplot as plt
plt.hist(titanic)
plt.show()
