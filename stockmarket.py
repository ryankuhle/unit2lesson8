import pandas as pd
df = pd.DataFrame({'Bull Market': [.9, .075, .025],
                   'Bear Market': [.15, .8, .05],
                   'Stagnant Market': [.25, .25, .50]
                  },
                  index=["Bull Market", "Bear Market", "Stagnant Market"])

print "After one transition of Markov's model"
print(df)
print "\n"
print "After two transitions of Markov's model"
print(df.dot(df))

'''
Need to be able to do this X times
What are the transition probabilities after 2 transitions? After 5? After 10? What are the steady state probabilities (try raising the matrix to a higher and numbers until the probabilities converge)?
Can you a name some real-life examples that could be modeled by Markov chains? Can you name examples that cannot be treated as Markov chains? Can you name an example of finite probabilistic states that cannot be modeled as Markov chains?
'''
