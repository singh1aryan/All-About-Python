'''
It is a classification technique based on Bayes’ Theorem 
with an assumption of independence among predictors. 
In simple terms, a Naive Bayes classifier assumes that 
the presence of a particular feature in a class is unrelated 
to the presence of any other feature. For example, a fruit may 
be considered to be an apple if it is red, round, and about 3 
inches in diameter. Even if these features depend on each other 
or upon the existence of the other features, all of these properties 
independently contribute to the probability that this fruit is an 
apple and that is why it is known as ‘Naive’.


Step 1: Convert the data set into a frequency table

Step 2: Create Likelihood table by finding the probabilities 
like Overcast probability = 0.29 and probability of playing is 0.64.

P(Yes | Sunny) = P( Sunny | Yes) * P(Yes) / P (Sunny)

Here we have P (Sunny |Yes) = 3/9 = 0.33, P(Sunny) = 5/14 = 0.36, P( Yes)= 9/14 = 0.64

Now, P (Yes | Sunny) = 0.33 * 0.64 / 0.36 = 0.60, which has higher probability.
'''
#Import Library of Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB
import numpy as np

#assigning predictor and target variables
x = np.array([[-3,7],[1,5], [1,2], [-2,0], [2,3], [-4,0], 
             [-1,1], [1,1], [-2,2], [2,7], [-4,1], [-2,7]])
y = np.array([3, 3, 3, 3, 4, 3, 3, 4, 3, 4, 4, 4])

#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets 
model.fit(x, y)

#Predict Output 
predicted= model.predict([[1,2],[3,4]])
print(predicted)

#Output: ([3,4])
'''
The dataset is divided into two parts, namely, 
feature matrix and the response vector.

    1. Features are the attributes,usually the first row
    2. Each feature is independent and equal
    3. We use bayes theorem for probability
    
Now, we look at an implementation of Gaussian Naive Bayes classifier using scikit-learn.

'''

# load the iris dataset 
from sklearn.datasets import load_iris 
iris = load_iris() 
  
# store the feature matrix (X) and response vector (y) 
X = iris.data 
y = iris.target 
  
# splitting X and y into training and testing sets 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1) 
  
# training the model on training set 
from sklearn.naive_bayes import GaussianNB 
gnb = GaussianNB() 
gnb.fit(X_train, y_train) 
  
# making predictions on the testing set 
y_pred = gnb.predict(X_test) 
  
# comparing actual response values (y_test) with predicted response values (y_pred) 
from sklearn import metrics 
print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)

'''
using the bayes from a table
given: 
    A table of attributes - fruits
    first column is the fruit

Bayes theorem: P(A|B) = P(B|A)*P(A)/P(B)
 -- find the right side values from the table
 -- we have to multiply the probability for each attribute, as they are independent
 -- finally we choose the max probability fruit
 
'''