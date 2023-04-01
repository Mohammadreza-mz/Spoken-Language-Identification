import pandas as pd

train = pd.read_csv('train.csv')
validation = pd.read_csv('validation.csv')
test = pd.read_csv('test.csv')

print('Number of training samples: total, male, female', len(train), len(train[train['gender'] == 'male']), len(train[train['gender'] == 'female']))
print('Number of validation samples: total, male, female', len(validation), len(validation[validation['gender'] == 'male']), len(validation[validation['gender'] == 'female']))
print('Number of testing samples: total, male, female', len(test), len(test[test['gender'] == 'male']), len(test[test['gender'] == 'female']))