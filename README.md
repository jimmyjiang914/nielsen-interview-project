# nielsen-interview-project

## Getting started
This project's dependencies are managed by Python Poetry:
https://python-poetry.org/

1. cd into project directory: `cd nielsen-interview-project`
2. Have poetry spin up a virtual environment: `poetry shell`
3. Install dependencies using poetry: `poetry install`

## Project structure
- The main body of work can be found in `EDA/EDA.ipynb`, along with comments, code, visualizations, and summary at the bottom
- Utility functions can be found in `EDA/utility.py`
- Python dependencies can be found in `pyproject.toml`

## Project summary

Some initial exploration was performed on the raw census data to see if any useful insight could be extracted about the characteristics of the data, variable types, potential features and additional information about the target variable. 

The intention was to create an initial statistical model that will not only reasonably predict whether a given county population increased from 2015 to 2016, but also to allow us to interpret the relationship(s) between a set of features and the target. The model of choice to start out with therefore is a logistic regression.

If we were to deploy such a model into production, we may also choose to explore additional classifiers that may not be as easily interpretable, but might return more accurate predictions--such as a support vector machine (SVM), random forest (RF), XGboost, etc. A good rule of thumb to generally follow is to deploy the simplest model as possible while still returning acceptable performance.

While working through the data, the dataset was collapsed such that each row consisted of a unique county name and state combination. To this end, the rate of change for each feature was computing ((latest_value - earliest_value) / (latest year - earliest year)). The data was cleaned to enable such an approach, and upon analyzing the resulting processed data, it was discovered that a few of the new features exhibited collinearity (Pearson's coefficient > 0.5). There were multiple ways to deal with this, for this exercise, I chose to remove one feature out of each set of collinear features pairs. An argument could be made for performing a PCA to deal with an abundance of collinear data, but in that case, interpretability would decrease, and there is also a chance that the lower dimension features would make the subsequent model(s) perform worse since a PCA does not take into consideration the actual response (target) variable. 

The data was standardized, then fed through a logistic regression model via statsmodels, and a summary of coefficients and their respective p-values were returned. The follow features exhibited a strong relationship with our target variable.
- female_total_population_rate (relatively strong positive effect)
- female_age_under_5_pct_rate (relatively moderate negative effect)
- male_age_25_to_29_pct_rate (relatively moderate negative effect)
- male_age_75_to_79_pct_rate (relatively moderate positive effect)
- male_age_80_to_84_pct_rate (relatively moderate positive effect)

From these results, it seems logical that a historically positive total population rate would strongly indicate a subsequent continued increase in population. What is fascinating is that the last 4 features also seem to indicate that historical increases in the younger population seem to be correlated with a decrease in subsequent total population from 2015 to 2016, whereas increases in the older population seem to correlate with increase in total population from 2015 to 2016.

Finally, a logistic regression model from Sklearn was trained and tested, along with an XGBoost for comparison. Metrics observed were the accuracy, F1 score, and the AUC. In this case, the F1 score was particularly meaningful because our dataset is unbalanced, i.e. around twice as many counties saw increases from 2015 to 2016 than decreases. From our comparison, unsurprisingly XGBoost performed much better overall owing to the fact that XGBoost is generally a highly performant and versatile algorithm.

Improvement can be made to the predictive power of our models by exploring additional model forms-- i.e. RF, naive bayes, SVM, etc. Hyperparameter tuning (GridSearch or a tree parzen estimator) can also be implemented to optimize model performance along with k-fold cross validations to mitigate overfitting.

Further studies diving deeper into additional demographic implications of these results may surface more interesting insight about underlying mechanisms driving the propensity for population increase in a given county.
