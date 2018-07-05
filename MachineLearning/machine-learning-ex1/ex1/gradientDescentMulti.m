function [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCostMulti) and gradient here.
    %
    theta1=theta(1);
    theta2=theta(2);
    theta3=theta(3);
    prediction = theta1*X(:,1) + theta2*X(:,2) + theta3*X(:,3);
    derivative1 = sum((prediction - y).*(X(:, 1)));
    derivative2 = sum((prediction - y).*(X(:, 2)));
    derivative3 = sum((prediction - y).*(X(:, 3)));
    theta1 = theta1 - (alpha*(1/m))*(derivative1);
    theta2 = theta2 - (alpha*(1/m))*(derivative2);
    theta3 = theta3 - (alpha*(1/m))*(derivative3);
    theta = [theta1;theta2;theta3];
    cost = computeCostMulti(X, y, theta);
    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = cost;

end

end
