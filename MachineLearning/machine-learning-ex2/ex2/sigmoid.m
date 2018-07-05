function g = sigmoid(z)
%SIGMOID Compute sigmoid function
%   g = SIGMOID(z) computes the sigmoid of z.

% You need to return the following variables correctly 
g = zeros(size(z), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the sigmoid of each value of z (z can be a matrix,
%               vector or scalar).





% =============================================================save
%for i=1:size(z, 1)
 % g(i, 1)=1/(1 + e.^-(z(i,1)));
%endfor
g=1.0./(1.0 + e.^(-z));
end
