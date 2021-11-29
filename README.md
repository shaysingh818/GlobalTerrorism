# Summary
This is a repository dedicated to researching global terrorism. This dataset was found on kaggle.com. This is the link to the dataset https://www.kaggle.com/START-UMD/gtd. With the provided data we will look at patterns in geography, resolution in terrorist attacks, effectiveness of law enforcment agencies and study victims of terrorism. We'll also look at bias towards race, gender and other immutable characteristics. 

## Suicide Classification
Implemented a decision tree that finds rules in terrorist attacks that lead to suicide. When looking at the data  (Statistically), we can see that bombings/explosions with a property value damage of over $60,000 lead to suicide. I wanted to create a tree that could confirm the stats and visualize how these rules are taken into account.

## Terrorist Group Classification
An important column attribute is the terrorist group that's associated with an attack. There are many algorithms that can be done to achieve this but KNN was the easiest to implement and interpret. We'll use the amount of wounded/killed and the terrorist group to create our classifier. The wounded/killed is our input data and the terrorist group is the class that we'll try to predict. We can tune the model by selecting different K values and feeding in different slices of X/Y column attributes. With the classifier that's been implemented, a K value of 25 with indexes 3,8 and 10 yields the highest accuracy. 

## Clustering
Using the amount of people harmed/killed and the property value, we can cluster the attacks into groups of severity. We'll use a K value of 3 to plot 3 distinct clusters on the graph. The 3 clusters represent, low, medium and high severity. Majorty of the cases fall under "low" priority since some attacks had high casualties with little property value damage. The goal of this cluster is to rank groups based on the amount of damage they incur. 

## Named Entity Recognition
With the given data set, there is a large portion of text data that wasn't looked at in previous kaggle competitions/reasearch. Using the SPACY NLP library, we can use the EN_CORE module to detect parts of speech to extract information such as people involved, locations, political figures etc. The novelty with this is that we can get more information about the targets in the attack. The dataset only supplies locations/institutes for the target type. With Named Entity Recognition, we can narrow down the targets by extracting people/names involved in the attack. 


 
