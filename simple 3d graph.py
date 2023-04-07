import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd


fig = plt.figure()
ax=fig.add_subplot(111,projection="3d")

sr_cs=pd.read_excel("sr.xlsx",sheet_name=None,usecols="D", skiprows=1)
sst=pd.read_excel("sr.xlsx",sheet_name=None,usecols="G",skiprows=1)
dd180=pd.read_excel("sr.xlsx",sheet_name=None,usecols="I",skiprows=1)

x = sr_cs["New Text Document"].to_numpy()
y= sst["New Text Document"].to_numpy()
z=dd180["New Text Document"].to_numpy()

ax.set_xlabel("Sr/Ca")
ax.set_ylabel("sst")
ax.set_zlabel(" D 180")


plt.show()
