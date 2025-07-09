import pandas as pd
import plotly.express as px
from numba import typeof
from pandas.core.interchange.dataframe_protocol import DataFrame
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

def read_file():
    file = pd.read_csv('train.csv')
    return file

if __name__ == "__main__":
    file = pd.read_csv('train.csv')
    file_copy = file.copy()