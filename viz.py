from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import wrangle

def data_landscape():
    df = wrangle.get_zillow_data()
    df = wrangle.prepare(df)
    fips_count = pd.DataFrame(df.fips.value_counts())
    fips_count.reset_index(inplace=True)
    fips_count.rename(columns={'fips':'count','index':'fips'}, inplace=True)
    plt.figure(figsize=(10,10))
    sns.barplot(y = 'count', x = 'fips', data=fips_count)
    plt.xlabel('County')
    plt.xticks([0,1,2],['Los Angeles, CA','Orange, CA', 'Ventura, CA'])
    plt.ylabel('Number of Properties')
    plt.title('Properties by County')
    return plt.show()

def baseline_viz(y_train, pred_mean):
    '''
    Plots a histogram of the actual tax value and the baseline prediction
    '''
    plt.vlines(ymin = 0, ymax = 25000, x = pred_mean, color='red', alpha=.5)

    plt.hist(y_train.taxvaluedollarcnt, color='blue', alpha=.5, label="Actual Tax Value")
    plt.hist(y_train.baseline_pred_mean, bins=1, color='red', alpha=.5, rwidth=100, label="Predicted Tax Value - Mean")

    plt.title('Baseline Prediction ')
    plt.xlabel('Tax Value')
    plt.ylabel('Number of Houses')
    plt.legend()
    return plt.show()

def validate_scatter(y_validate, pred_mean):
    '''
    Creates scatterplot to display models and baseline 
    '''
    plt.figure(figsize=(16,8))
    plt.plot(y_validate.taxvaluedollarcnt, y_validate.baseline_pred_mean, alpha=.5, color="black", label='_nolegend_')
    plt.annotate("Baseline: Predict Using Mean", (16, (pred_mean + 1000)))
    plt.plot(y_validate.taxvaluedollarcnt, y_validate.taxvaluedollarcnt, alpha=.5, color="blue", label='_nolegend_')
    plt.annotate("The Ideal Line: Predicted = Actual", (30000, 0), rotation=25)

    plt.scatter(y_validate.taxvaluedollarcnt, y_validate.taxvalue_pred_lm, 
                alpha=.5, color="red", s=100, label="Model: LinearRegression")
    plt.scatter(y_validate.taxvaluedollarcnt, y_validate.taxvalue_pred_lm2, 
                alpha=.5, color="yellow", s=100, label="Model: Polynomial")
    plt.scatter(y_validate.taxvaluedollarcnt, y_validate.taxvalue_pred_lars, 
                alpha=.5, color="green", s=100, label="Model LassoLars")
    plt.xlabel('Tax Value')
    plt.ylabel('Model Predictions')
    plt.legend()
    return plt.show()

def plot_residuals(y_validate):
    plt.figure(figsize=(16,8))
    plt.axhline(label="No Error")
    plt.scatter(y_validate.taxvaluedollarcnt, y_validate.taxvalue_pred_lm-y_validate.taxvaluedollarcnt, 
                alpha=.5, color="red", s=100, label="Model: LinearRegression")
    plt.scatter(y_validate.taxvaluedollarcnt, y_validate.taxvalue_pred_glm-y_validate.taxvaluedollarcnt, 
                alpha=.5, color="yellow", s=100, label="Model: Polynomial")
    plt.scatter(y_validate.taxvaluedollarcnt, y_validate.taxvalue_pred_lars-y_validate.taxvaluedollarcnt, 
                alpha=.5, color="green", s=100, label="Model LassoLars")
    plt.legend()
    plt.xlabel("Actual Tax Value")
    plt.ylabel("Residuals")
    plt.title("Do the size of errors change as the actual value changes?")
    return plt.show()

def validate_hist(y_validate):
    '''
    Creates histogram to display models vs actual
    '''
    plt.figure(figsize=(10,10))
    plt.hist(y_validate.taxvaluedollarcnt, color = 'blue',alpha = 0.5, label = 'Actual Tax Value')
    plt.hist(y_validate.taxvalue_pred_lm, color = 'red',alpha = 0.5, label = 'Model: Linear Regression')
    plt.hist(y_validate.taxvalue_pred_lm2, color = 'yellow',alpha = 0.5, label = 'Model : Polynomial')
    plt.hist(y_validate.taxvalue_pred_lars, color = 'green',alpha=0.5,label='Model: LassoLars')
    plt.xlabel('Tax Value')
    plt.ylabel('Number of Houses')
    plt.legend()
    return plt.show()

def test_hist(y_test):
    plt.figure(figsize=(10,10))
    plt.hist(y_test.taxvaluedollarcnt, color = 'blue',alpha = 0.5, label = 'Actual Tax Value')
    plt.hist(y_test.taxvalue_pred_lm2, color = 'yellow',alpha=0.5,label='Model: Polynomial')
    return plt.show()