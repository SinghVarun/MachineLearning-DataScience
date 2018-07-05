function J = computeCostMulti(X, y, theta)
%COMPUTECOSTMULTI Compute cost for linear regression with multiple variables
%   J = COMPUTECOSTMULTI(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta
%               You should set J to the cost.





% =========================================================================
theta1=theta(1);
theta2=theta(2);
theta3=theta(3);
prediction = theta1*X(:,1) + theta2*X(:,2) + theta3*X(:,3);
summation = sumsq(prediction-y);
J = (1/(2*m))*(summation);
end
