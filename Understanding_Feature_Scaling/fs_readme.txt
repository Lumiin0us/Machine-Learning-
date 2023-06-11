Some insights and errors caused while practicing! 

- We used MinMaxScalar() from preprocessing module to normalize the data, normalize also takes a 2D array. 
- The given input was a normal 2D array as that's what it takes and returns a numpy array. 
- train_test_split can take either 1D or 2D array but does not takes 3D arrays. 

* I actually found out that since I am using a linear model feature scaling wont change any outputs or have any effect (which i learnt the hard way....),
its used for algorithms like K-Nearest Neighbor or the ones where distances are considered; i'll be attaching a screenshot for reference *
.."I further tested with more than 2 columns(features) & still feature scaling was ineffective."

Fact: It is true that outliers would still remain outliers even after feature scaling but having all the data on the same scale would help the 
model to converge faster & isolate the idea of prioritizing certain features over others ultimately causing faulty decisions. 

[
Errors:
    - ValueError: With n_samples=1, test_size=0.2 and train_size=0.8, the resulting train set will be empty. Adjust any of the aforementioned parameters.
    (This error suggests that the data i'm assigning to training/testing is not being split correctly because the samples are too low) 
    - another such possibility of this error is that normalize() expects a 2D array

    - got this error while plotting a graph -> ValueError: x and y must be the same size
    - pretty self explanatory but i got this not because my inputs sizes were different but because one of my input in the plot was a 2D array(consisted of two features)
    so I had to manually assign it one, otherwise would need to use a 3D graph for 3x relationship plotting.
]