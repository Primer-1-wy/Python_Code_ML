# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from sklearn import datasets #sklearn的数据集
from sklearn.neighbors import KNeighborsClassifier#sklearn模块类的KNN类
import numpy as np

np.random.seed(0)#设置随机种子
iris=datasets.load_iris()#获取鸢尾花数据集
iris_x