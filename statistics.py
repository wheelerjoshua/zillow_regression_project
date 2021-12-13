import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt
import seaborn as sns

def t_test_sqft_tax(train):
    '''
    Takes in train df as argument and runs an independent t-test for 
    first and third quartile calculated square feet and their tax value
    '''
    # establish alpha
    alpha = 0.5
    # create variables for 3rd and 1st quartile
    highsqf = train[train.calculatedfinishedsquarefeet >= train.calculatedfinishedsquarefeet.quantile(q=0.75)].taxvaluedollarcnt
    lowsqf = train[train.calculatedfinishedsquarefeet <= train.calculatedfinishedsquarefeet.quantile(q=0.25)].taxvaluedollarcnt
    # run test
    t, p = stats.ttest_ind(highsqf, lowsqf, equal_var=False)

    # return result
    if p / 2 > alpha:
        return print("We fail to reject the null hypothesis")
    elif t < 0:
        return print("We fail to reject the null hypothesis")
    else:
        return print("Higher square footage properties generally have a higher calculated tax amount.")

def t_test_bath_tax(train):
    '''
    Takes in train df as argument and calculates the mean taxvalue for each number category of bathrooms
    and runs an independent t-test for 1-2 bathrooms and 3-4 bathrooms tax values.
    '''
    # establish alpha
    alpha = 0.5
    # create variables for 1 bath and 4 baths
    one_two_bath = train[train.bathroomcnt < 2].taxvaluedollarcnt
    three_four_bath = train[train.bathroomcnt > 3 ].taxvaluedollarcnt
    # run test
    t, p = stats.ttest_ind(one_two_bath, three_four_bath, equal_var=False)
     # return result
    if p / 2 > alpha:
        return  print("There is no statistical evidence that higher bathroom count properties have higher tax values than lower bathroom count properties.")
    elif t < 0:
        return  print("There is no statistical evidence that higher bathroom count properties have higher tax values than lower bathroom count properties.")
    else:
        return  print("Higher bathroom count properties generally have a higher calculated tax amount.")

def t_test_bed_tax(train):
    '''
    Takes in train df as argument and calculates the mean taxvalue for each number category of bathrooms
    and runs an independent t-test for 1-2 bedrooms and 3-4 bedrooms tax values.
    '''
    # establish alpha
    alpha = 0.5
    # create variables for 2 bedrooms and 5 bedrooms
    two_bed = train[train.bedroomcnt == 2].taxvaluedollarcnt
    five_bed = train[train.bedroomcnt == 5].taxvaluedollarcnt
    # run test
    t, p = stats.ttest_ind(two_bed, five_bed, equal_var=False)
     # return result
    if p / 2 > alpha:
        return  print("There is no statistical evidence that higher bedroom count properties have higher tax values than lower bedroom count properties")
    elif t < 0:
        return  print("There is no statistical evidence that higher bedroom count properties have higher tax values than lower bedroom count properties")
    else:
        return  print("Higher bedroom count properties generally have a higher calculated tax amount.")

def test_lowbed_highsqf(train):
    '''
    Takes in train df as an argument and returns the means of low bedroom count and high sqft
    and high bedroom count and low square feet.
    '''
    # calculate means for categories
    mean1 = round(train[(train.bedroomcnt < 3) & (train.calculatedfinishedsquarefeet > 2000)].taxvaluedollarcnt.mean())
    mean2 = round(train[(train.bedroomcnt >= 3) & (train.calculatedfinishedsquarefeet < 2000)].taxvaluedollarcnt.mean())
    # create temporary df for plotting purposes
    temp = train[(train.bedroomcnt <= 3) & (train.calculatedfinishedsquarefeet > 2000)]
    temp2 = train[(train.bedroomcnt > 3) & (train.calculatedfinishedsquarefeet < 2000)]
    
    #create plot
    plt.figure(figsize=(10,10))
    plt.subplot(1,2,1)
    sns.boxplot(x='bedroomcnt',y='taxvaluedollarcnt',data=temp)
    plt.title('Less than 4 Bedrooms and More than 2k SqFt',loc='right')
    plt.subplot(1,2,2)
    sns.boxplot(x='bedroomcnt',y='taxvaluedollarcnt',data=temp2)
    plt.title('More than 3 bedrooms and Less than 2k SqFt',loc='right')
    plt.tight_layout()

    
    # return means
    return print(f'The mean tax value for properties with less than three bedrooms and more than 2000 square feet is {mean1}, \nThe mean tax value for properties with three or more bedrooms and less than 2000 square feet is {mean2}.'), plt.show()

def test_year_built(train):
    '''
    Takes in train df as an argument and runs a chi2 test to find correlation between yearbuilt and taxvalue
    Also plots a linepot to show taxvalue relating to year the property was built.
    '''
    # establish alpha
    alpha = 0.5
    # create crosstab observation
    observe = pd.crosstab(train.taxvaluedollarcnt, train.yearbuilt)
    # run chi2 test
    chi2, p, degf, expected = stats.chi2_contingency(observe)
    # create lineplot
    # sns.lineplot(x = 'yearbuilt',y='taxvaluedollarcnt',data=train)
    # plt.title('Tax Value by Year Built')
    # plt.ylabel('tax value')
    # plt.xlabel('year built')
    # return result based on p
    if p < alpha:
        return print("There is a correlation between year built and tax value.")
    else:
        return print("There is no correlation between year built and tax value.")

def test_fips(train):
    '''
    Takes train df as argument and runs chi2 test on fips and returns outcome
    '''
    # establish alpha
    alpha = 0.5
    # create observation crosstab
    observe = pd.crosstab(train.taxvaluedollarcnt, train.fips)
    # run chi2 test
    chi2, p, degf, expected = stats.chi2_contingency(observe)
    # return result
    if p < alpha:
        return print("There is a correlation between fips and tax value.")
    else:
        return print("There is no correlation between fips and tax value.")
