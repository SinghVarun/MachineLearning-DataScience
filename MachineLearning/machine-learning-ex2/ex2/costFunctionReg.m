function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta






% =============================================================
prediction = sigmoid(X*theta);
shiftThetaDownward = theta(2:size(theta)); %theta(1) remains unchanged. 
thetaCorrected = [0;shiftThetaDownward]; %for theta(1) we subsituted 0, there using Regularized Logistics regression remains unchanged. 
J = (1/m)*(-transpose(y)* log(prediction) - transpose(1 - y)* log(1-prediction)) + (lambda/(2*m))*thetaCorrected'*thetaCorrected;
grad = ((1/m)*transpose(X)*(prediction - y)) + (lambda/m)*thetaCorrected;

end
