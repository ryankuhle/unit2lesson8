import pandas as pd

#Which model is correct?
#Conflicting info between actual data frame results and the links below:
##http://stackoverflow.com/questions/33748031/multiple-transitions-of-markov-model (ignore the code in my initial post)
##https://en.wikipedia.org/wiki/Markov_chain#Example
#The  guy on stack overflow gave the same info as the Wikipedia example, which follows a different column/row set up then the Thinkful rainy/sunny comparison

#Model 1
df = pd.DataFrame({'Bull Market': [.9, .015, .25],
                   'Bear Market': [.075, .8, .25],
                   'Stagnant Market': [.025, .05, .50]
                  },
                  index=["Bull Market", "Bear Market", "Stagnant Market"])

#Model 2
altdf = pd.DataFrame({'Bull Market': [.9, .075, .025],
                      'Bear Market': [.15, .8, .05],
                      'Stagnant Market': [.25, .25, .50]
                     },
                  index=["Bull Market", "Bear Market", "Stagnant Market"])

print "After one transition of Markov's model"
print(df)
print "\n"
print "After two transitions of Markov's model"
print(df.dot(df))

#Create function asking for prompt of number of transitions, process

#What are the steady-state probabilities?

'''
#Real life examples
Pepsi wants to know what percentage of cola drinkers will drink Pepsi each year over course of time
Dice games


'''

#Finite probabilistic states not modeled as Markof chains
