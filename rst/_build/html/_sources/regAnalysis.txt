.. insert image here

.. Regression Analysis

Linear Regression
-----------------

In this chapter we will focus on regression analysis using the Python library `Statsmodels`_.

.. _Statsmodels: http://statsmodels.sourceforge.net/

We already discussed the hypotheses and definitions of regression analysis in the section `Statistical Models`_ and here we will illustrate regressions using data and functions from Statsmodels.

.. _Statistical Models: ../html/statsModels.html

Regression analysis has some underlying assumptions, and we invite you to read this section again if you don't remember these needed assumptions and also to familiarize yourself with the needed vocabulary.

A very general definition of a regression model is the following:

.. math::
   \label{eq:regmodel}
   Y = f(x,\varepsilon)
   

In the case of a linear regression model, the function f is simply the affine function, and the model can be rewritten as:

.. math::
    \label{eq:simplereg}
    Y = X \beta + \varepsilon
    
:math:`Y` is a vector of dimension :math:`(n \times 1)` and is called the endogenous variable, :math:`X` is a matrix of dimension :math:`(n \times k)` where each colum is  an explanatory variable and :math:`\varepsilon` is the error term. :math:`\beta` is the vector of dimension :math:`(k \times 1)` and contains the parameters we want to estimate.

Example: Program Effectiveness 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using data from Spector and Mazzeo (1980), we estimate a linear regression model with statsmodels.

.. literalinclude:: ../Code/regSpector.py

