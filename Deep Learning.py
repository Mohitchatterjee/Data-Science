#!/usr/bin/env python
# coding: utf-8

# # Artificial Neural Network

# In[1]:


# Implement Or Gate


# In[13]:


# Initialize learning rate, bias and weights

lr = 1
bias = 1
weights = [-50,20,20]

# Perceptron Function

def perceptron(X_1, X_2, Output):
    output_P = bias*weights[0] + X_1*weights[1] + X_2*weights[2]
    if output_P > 4.6:
        output_P = 1
    else:
        output_P = 0
    error = 1/2 * (output_P - Output)**2
    weights[0] = weights[0] + error * bias * lr
    weights[1] = weights[1] + error * X_1 * lr
    weights[0] = weights[2] + error * X_2 * lr

# Predict Function
    
def predict(X_1, X_2):
    output_P = bias*weights[0] + X_1*weights[1] + X_2*weights[2]
    if output_P > 4.6:
        output_P = 1
    else:
        output_P = 0
    return output_P    


# In[14]:


for _ in range(50):
    perceptron(0,0,0)
    perceptron(0,1,1)
    perceptron(1,0,1)
    perceptron(1,1,1)


# In[20]:


print('Enter 1St input ')
X_1 = int(input())
print('Enter 2nd input')
X_2 = int(input())
Output_pred = predict(X_1, X_2)
print('Output is ',Output_pred)


# In[ ]:




