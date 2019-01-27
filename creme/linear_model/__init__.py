"""
Generalized linear models optimized through stochastic gradient descent.
"""
from .linear_regression import LinearRegression
from .logistic_regression import LogisticRegression


__all__ = ['optimrs', 'LinearRegression', 'LogisticRegression']
