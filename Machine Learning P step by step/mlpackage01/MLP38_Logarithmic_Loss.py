# Cross validation using classification LogLoss
import warnings
warnings.filterwarnings(action='ignore')
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
filename = 'indians-diabetes.data.csv'
hnames=['preg', 'plas','pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values
X = array[:, 0:8]
Y = array[:, 8]
kfold = KFold(n_splits=10)
model = LogisticRegression()
# this is default method of accuracy because it is so easy
scoringMethod = 'neg_log_loss'
results = cross_val_score(model, X, Y, cv=kfold,scoring=scoringMethod)
print("Accuracy :%.3f(%.3f)" % (results.mean(), results.std()))


