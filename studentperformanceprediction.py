#%% [markdown]
# # Student Performan Predictor with Seaborn(Countplot)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import sklearn
import io
import requests
import seaborn as sns
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

passmark=40
#%% [markdown]
# # Importing the dataset
# # In the repo
df=pd.read_csv('/home/rahul/Desktop/Link to rahul_environment/Projects/Machine_Learning Projects/Student_Performance/StudentsPerformance.csv')

df.head()

print(df.shape)

df.describe()

df.isnull().sum()

p=sns.countplot(x="math score",data=df,palette="muted")
_=plt.setp(p.get_xticklabels(),rotation=90)
#%% [markdown]
# # Now how many students were passed in the exam are?
# # Passed in the Math overall:

df['mathpass']=np.where(df['math score']<passmark,'F','P')
df.mathpass.value_counts()

p=sns.countplot(x='parental level of education',data=df,hue='mathpass',palette='bright')
_= plt.setp(p.get_xticklabels(), rotation=90) 
p=sns.countplot(x='reading score',data=df,palette='muted')
_= plt.setp(p.get_xticklabels(), rotation=90) 
p=sns.countplot(x='writing score',data=df,hue='mathpass')
_= plt.setp(p.get_xticklabels(), rotation=90) 
#%% [markdown]
# # Those who passed the reading are:
df['readpass']=np.where(df['reading score']<passmark,'F','P')
df.readpass.value_counts()
#%% [markdown]
# # Those who passed in the writing are and countplot:



df['writepass']=np.where(df['writing score']<passmark,'F','P')
df.writepass.value_counts()

sns.countplot(x='parental level of education', data = df, hue='writepass', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90) 
plt.savefig('countplot_parentaleducation')
#%% [markdown]
# # find overall pass or fail(it is very important as compared to other plots)
df['overallpass']=df.apply(lambda x:'F' if x['mathpass']=='F' or x['readpass']=='F' or x['writepass']=='F' else 'P',axis=1)
df.overallpass.value_counts()
p=sns.countplot(x='parental level of education',data=df,hue='overallpass')
_= plt.setp(p.get_xticklabels(), rotation=90) 
#%% [markdown]
# # find percentage of marks
df['Total_Marks'] = df['math score']+df['reading score']+df['writing score']
df['percentage'] = df['Total_Marks']/3
#%% [markdown]
# # The countplot which is on lunch vs parental level of education
p=sns.countplot(x='lunch',data=df,hue='parental level of education',palette='bright')
_= plt.setp(p.get_xticklabels(), rotation=90) 
plt.savefig('countplot_lunch')
#%% [markdown]
# ## Let us assign the grades
# ## Grading
# ## above 80 = A Grade
# ## 70 to 80 = B Grade
# ## 60 to 70 = C Grade
# ## 50 to 60 = D Grade
# ## 40 to 50 = E Grade
# ## below 40 = F Grade ( means Fail )

def GetGrade(percentage,overallpass):
    if(overallpass=='F'):
        return 'F'
    if(percentage>=80):
        return 'A'
    if(percentage>=70):
        return 'B'
    if(percentage>=60):
        return 'C'
    if(percentage>=50):
        return 'D'
    
    if(percentage)>=40:
        return 'E'
    else:
        return 'F'
#%% [markdown]
df['grade']=df.apply(lambda x: GetGrade(x['percentage'],x['overallpass']),axis=1)
df.grade.value_counts()
#%% [markdown]
# # the countplot grade vs lunch
sns.countplot(x='grade',data=df,hue='lunch')
plt.savefig('countplot_grade')

sns.countplot(x='grade',data=df,order=['A','B','C','D','E','F'],palette='muted')
plt.savefig('countplot_grade')
plt.show()

p=sns.countplot(x='parental level of education',data=df,hue='grade',palette='bright')
_= plt.setp(p.get_xticklabels(), rotation=90) 
plt.savefig('countplot_forparent_education')
# ## Basically we write it to make the xlabels vertical so that it is easily visable to us
