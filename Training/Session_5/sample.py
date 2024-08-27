import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




# Sample Example
import random
def sampleExample():
    world_space = ["Heads", "Tails"]
    coin_toss = random.choice(world_space)
    print(f"Probability of Getting {coin_toss}: {world_space.count(coin_toss) / len(world_space)}")
    print(f"Coin Toss Result: {coin_toss}")

# Two dice example Fair
# from fractions import Fraction
def sumTwoDiceF_Simple():
    die_outcomes = [1, 2, 3, 4, 5, 6]
    sum_counts = {i: 0 for i in range(2, 13)}
    for outcome1 in die_outcomes:
        for outcome2 in die_outcomes:
            total = outcome1 + outcome2
            sum_counts[total] += 1

    total_possible_outcomes = len(die_outcomes) ** 2
    probabilities = {sum_value: count / total_possible_outcomes for sum_value, count in sum_counts.items()}
    for sum_value, probability in probabilities.items():
        print(f"Probability of getting sum {sum_value}: {probability:.2f}")

# # defaultdictionary
#     #definition: 
#     # that's similar to a regular dictionary, 
#     # but it provides a default value for keys that don't exist 

from collections import defaultdict
def BasicDefaultDictInt():
    counter = defaultdict(int)
    counter["apple"] += 1
    print(counter["apple"])  
    print(counter["banana"])  
    
def BasicDefaultDicList():
    lis = defaultdict(list)
    lis["fruits"].append('apple')
    lis["fruits"].append('banana')
    lis['vegetable'].append('tomato') 
    print(lis)  
# # Sum TwoDice Fair
def sumTwoDiceF_Defdic():
#    P(3)=p(1,2)+P(2,1)=2/36
#    P(1,2)=P(d1=1)P(d2=2)= (1/6)(1/6)=1/36
#    P(2,1)=P(d1=2)P(d2=1)=(1/6)(1/6)=1/36
    d={(d1,d2):d1+d2 for d1 in range(1,7) for d2 in range(1,7)} #(1,1):2, (1,2):3,---,(6,1):7,(6,2):8
    dinv = defaultdict(list)
    for ds,sum in d.items():
        dinv[sum].append(ds) #d[3]=(1,2),(2,1)
    probabilities={sum:len(l)/36 for sum,l in dinv.items()}
    print(probabilities)

# #sum TwoDice Unfair with dictionary
def sumTwoDiceUF_dict():
    probabilities_die1 = [1/9, 1/9,1/9,2/9, 2/9, 2/9] #d1
    probabilities_die2 = [1/6,1/6,1/6,1/6,1/6,1/6] #d2
#    P(3)=p(1,2)+P(2,1)=(1/9)(1/6) +(1/9)(1/6) 
#    P(1,2)=P(d1=1)P(d2=2)= (1/9)(1/6) 
#    P(2,1)=P(d1=2)P(d2=1)=(1/9)(1/6)
    sum_counts = defaultdict(int)
    for roll1 in range(1, 7):
        for roll2 in range(1, 7):
            total_sum = roll1 + roll2
            sum_counts[total_sum] += probabilities_die1[roll1 - 1] * probabilities_die2[roll2 - 1]

    for total_sum, probability in sum_counts.items():
        print(f"Sum {total_sum}: Probability {probability:.4f}")

# # Sum TwoDice Unfair with dataframe
from pandas import DataFrame
def sumTwoDiceUF_Pandas():
    d=DataFrame(index=[(i,j) for i in range(1,7) for j in range(1,7)],columns=['sm','d1','d2','pd1','pd2','p'])
    d.d1=[i[0] for i in d.index]
    d.d2=[i[1] for i in d.index]
    d.sm=list(map(sum,d.index))
    d.loc[d.d1<3,'pd1']=1/9.
    d.loc[d.d1>= 3,'pd1']=2/9.
    d.pd2=1/6.
    # print (d.head(36))
    d.p = d.pd1 * d.pd2
    print (d.head(36))
    print( d.groupby('sm')['p'].sum())

# # Conditional Probability P(sum=7|d1=4)=p(sum=7 and d1=4)/p(4)

def ConditionalProbability_Simple():
    dice_outcomes = {(i, j): i + j for i in range(1, 7) for j in range(1, 7)}
    count_sum_7_and_first_4 = sum(1 for outcome in dice_outcomes if outcome[0] == 4 and dice_outcomes[outcome] == 7)
    count_first_4 = sum(1 for outcome in dice_outcomes if outcome[0] == 4)
    conditional_probability = count_sum_7_and_first_4 / count_first_4
    print(f"Conditional probability of getting a sum of 7 given the first die is 4: P(A|B) = {conditional_probability:.2f}")

# # Another Example: Suppose we send out a survey to 300 individuals asking them which sport they 
# # like best: baseball, basketball, football, or soccer. 
# # what the probability that an individual is male, given that they prefer baseball as their favorite sport?
# # p(g=male|s=baseball)
# # what is crosstab method
# #     A     B   all
# # X   2     1   3          
# # Y   1     1   2
# #all  3    2   0

import pandas as pd
def ExampleCrosstab():
    data = {
    'Category1': ['A', 'B', 'A', 'B', 'A'],
    'Category2': ['X', 'Y', 'X', 'X', 'Y']}
    df = pd.DataFrame(data)
    cross_tab = pd.crosstab(index=df['Category1'], columns= df['Category2'],margins=True)
    print(cross_tab)

import numpy as np
def ConditionProbability_AnotherExample():
    df = pd.DataFrame({'gender': np.repeat(np.array(['Male', 'Female']), 150),
                   'sport': np.repeat(np.array(['Baseball', 'Basketball', 'Football',
                                                'Soccer', 'Baseball', 'Basketball',
                                                'Football', 'Soccer']), 
                                    (34, 40, 58, 18, 34, 52, 20, 44))})
    survey_data = pd.crosstab(index=df['gender'], columns=df['sport'], margins=True)
    # print (survey_data)
    # print(survey_data.iloc[0, 1])
    print(f"Probability of male and given baseball as their favorite sport is {survey_data.iloc[1, 0] / survey_data.iloc[2, 0]}") #34/68 =p(Gender=M|s=Baseball)
    print(f"probability that an individual prefers basketball as their favorite sport, given that they’re female is {survey_data.iloc[0, 1] / survey_data.iloc[0, 4]}")