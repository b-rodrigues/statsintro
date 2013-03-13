'''Linear Regression
Estimation of a linear regression model using the Spector and Mazzeo (1980) data set.

'''

'''
Author: Bruno Rodrigues
Date:   March-2013
Ver:    1.0
'''

# For this we only need to import statsmodels
import statsmodels.api as sm

# We load the spector dataset as a pandas dataframe
# Of course, you can load your own datasets 
spector = sm.datasets.spector.load_pandas()

# We define y as the endogenous variable, and x as the 
# exogenous variable
# Note that if you load your own data, the methods endog 
# and exog will not be available and you will have to 
# explicitly define the endogenous and exogenous variables
y, x = spector.endog, spector.exog

# We run the regression
reg = sm.OLS(y, x).fit()

# And here we can see the results in a very nice looking table
reg.summary()

# We can only take a look at the parameter values though
reg.params

# We can also extract the residuals
reg.resid