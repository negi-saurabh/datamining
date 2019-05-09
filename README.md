# datamining

Data Mining Assignment(Basic) Group 45

Negi, Saurabh [student number: 2635338 ] [vu-netID:sni580]
Bleeker, Tom [student number: 2632638 ] [vu-netID:tbr264]
Jakoby, Abdulla [student number:2548344 ] [vu-netID:ajy200]


Vrije Universiteit Amsterdam

Introduction

This paper gives a brief description of the results we obtained for the first as- signment of the course Data Mining. All programming was done in Python.
Task 1.A
In the analysis of the ODI-2019 dataset we decided to start cleaning it properly in order to conduct important data science analysis. The restructure of our DataFrame has been as follows: firstly, converting every closed response columns such as Have you taken a course on Machine Learning? etc into numbers 1, 2 and 3. Secondly, applying fuzzy wuzzy on the course column and group studies together. Thirdly, for the column Birthday we grouped the birth years for each participant of this course.
Next, we will demonstrate some basic data descriptions of the cleaned DataFrame below:
Fig. 1: Plots of Studies with other CategoryFig. 2: Others category of students educa- tion
We used python with additional packages like pandas, matplotlib and wordcloud to extract meaningful information and the plots. The ODI data-set consisted
  
2 Group 45
of 277 row in total out of which the 1st row is the labels which consisted of the question asked in the class and interestingly by checking the timestamp we realized that the first row was the trail row done by the professor so that was the wrong data row. Out of all the data, the percentage of men consisted of 0.66 percent, the amount of female was equal to 0.29 percent and the unknown category consisted of 0.05 percent. The average age of the students in total was equal to 24 including unknown. This average age is the same for male and female across all studies. The maximum age is 48 and it is a male, while the maximum age for woman is 28. The median value consists of 24 for both male and females as well. It was also interesting to note that the median age of Data science was 25 and average 28 while for the other studies the average age was 24 or 0.5 values apart for the median value. For the other category we thought it would be interesting to categorize the interests of men and women students in the class separately. For that we created world cloud separately for each of the gender.
Fig. 3: Men Fig. 4: Women Fig. 5: Unknown
For getting idea of how many students out of 277, have already done the courses in Machine learning, Information retrieval, statistics and databases, we prepared a stacked bar chart after categorizing each course description under one umbrella. By looking at the stacked bar chart we can see the relative number of students from each area which have already completed courses in the given subjects.
It was also interesting to find the age distribution in the Data Mining class of 2019, so for this we prepared a bar chart histogram of the age distribution. In this we have replaced all of the corrupted data by the year 1995.
   
Fig. 6: Student from each course who have done the subject
Task 1.B
Data Mining Assignment(Basic) Group 45 3
  The cleaned ODI data with length 277 which has been described in part 1A has been used to perform two classification experiments with cross validation. The first algorithm was conducted with the logistic regression model. This choice was motivated due to the nature of the dataset, which consisted of multinomial values i.e. more than binary numbers [1]. For the analysis we have used the as dependent variable y = CourseDatabase, in order to predict the relationship of students who followed this course prior to atending this course. The explanatory variables where as follows: X = Course ML, Course statistics, Gender, Course information retrievel, Age number the values were are transformed into numbers 0,1,2. The analysis started with splitting the data into the test part (70 percent) and training part (30 percent). The accuracy level on the test set consisted of 0.71. The confusion matrix consists of a 3x3 matrix with on the diagonal the correctly predicted values 0, 1 and 2. For zero which was for men and yes 34 are correctly predictions, for one which was for woman and no 25 are correctly predictions and for unknown we have zero correctly predictions due to the low occurrence of the answer. For the second algorithm we applied the decision tree. The same data structure as for the logistic regression has been applied in the analysis and is also recommended for multinomial data predictions [2]. The accuracy decision tree has a score of 0.61 which implies that our test set can predict around this ratio. The main advantage of applying the decision tree is due to the pruning process. In here unnecessary splits in the data would be eliminated. The output of the decision tree could not fit in this report but is produced in the code. The accuracy is less compared to the logistic regression which could be explained by the minimum scale used for the pruning process to counter under fitting or over fitting.
Fig. 7: Age Distribution in the class

4 Group 45
Task 2.A
Having downloaded the training set, we proceeded to explore the data to get an idea of how the data was distributed. Fig. 8 shows a selection of various bar graphs and histograms that we used to check if we could find any obvious corre- lations. These are shown in . Looking at these figures, it becomes apparent that several attributes are very relevant to a learning algorithm. Gender in particular appears to be a good indicator, with approximately 75% of women surviving, as opposed to less than 20% of men. This effect is made more marked since men significantly outnumber females on board. Age also appears to be signifi- cant. Passengers between the ages of 17-35 are vastly over-represented on board, which can be explained because a lot of passengers would be young people plan- ning to build up a new life in America. This same age group appears to suffer disproportionately high losses when compared to children, but surprisingly also elderly people. Ticket prices and passenger class likewise show significant differ- ences in survival rates, with survival rates increasing dramatically with increases in ticket prices. The amount of relatives on board seems also to have some in- fluence, with passengers with a small amount of relatives on board marginally more likely to survive than those with no relatives and, tragically, also more likely than passengers with large amounts of relatives on board. This seems to indicate that many members of larger families choose to die together rather than be split up. Although not included in Fig. 8, we also saw a small correlation be- tween survival and the port of embarkation. Perhaps this can be explained by the fact that some embarkation ports were used relatively more by wealthier passengers.
To prepare the training set for a learning algorithm we selected the following attributes: Passenger class, Age, Sex, Fare, Embarkation point, and family size. Family size was created by adding up the original categories of SibSp (siblings and spouses) and Parch (parents and children). Adding up these values created a clearer correlation with survival than they did separately. The remaining at- tributes (Passenger name, Ticket number, cabin number, and ID) were dropped, since they were assessed as not correlating to survival, or being somehow already linked to a remaining attribute. NaN values in the data were replaced with -0.5, and several attributes (Age, Fare) were changed into a limited amount of cate- gories, to avoid the risk of over-fitting the learning algorithm.
Task 2.B
In order to be able to evaluate and choose a classifier with which to enter into the Titanic competition, the training data set was split up into a training set (66% of data) and a testing set (34% of data). We made use of two different classifi- cation algorithms from the sklearn package [3]: a Support Vector Machine and a RandomForrestClassifier (RF). Both of these algorithms were applied to the training set and evaluated based on the testing set. The algorithms were tested

Data Mining Assignment(Basic) Group 45 5
 Fig. 8: Exploration of Titanic data set
with various parameter settings by making use of the GridSearchCV function (also from sklearn), which allows the alogithm to be tried on the trainingdata us- ing a multidimensional grid of different parameter settings. The optimal settings were then selected to be evaluated on the testing data. To avoid overfitting on the training data, and to give us an estimate of how well either alogrithm would perform on new data, a 5-fold cross validation was then conducted. The SVM was given an average score of 0.78, whereas the RandomForest was given a score of 0.82. With this in mind, the RandomForest classifier with the best evaluated parameters was chosen to predict the survival of the official test set. We sub- mitted our results and obtained the following score and ranking: At the time of
Fig. 9: Latest score for our group
writing this ranking was of 11097 teams participating, meaning our team’s efforts were in the lower segment of the leaderboard. One of the reasons for this could be that we chose fairly popular algorithms which probably fail to distinguish
 
6 Group 45
us from other participants. Another reason could be that with more experience and perhaps a lot more time, more efficient use of parameter settings could have been made, which would no doubt have raised our score.
Task 3.A
For this task the Kaggle Microsoft Malware Prediction competition was selected. In this competition, Microsoft issued a challenge to develop techniques to pre- dict if a computer will be hit with malware. Microsoft provided competition participants with a dataset, which included information about approximately 17 million computers. [4] The data was split into a training and testing set. The dataset included over a hundred different attributes per entry, including information about the machine specs, its anti-virus software and its firewall, the location of the machine, etc. Lastly, the training set included the attribute that mentioned whether or not the machine in question had any malware detections. Participants had to submit a dataframe outlining for each machine whether their algorithm predicted a malware detection or not.
The winner of this competition did not share his method of winning. Instead, it was decided to focus on a team called ThunderBYTE which had finished sixth, which considering the competition (2426 teams) is still an impressive score. The two members of ThunderBYTE looked into the distribution of attributes of the test dataset, and compared this with the distribution in the training set. They found that hat the distributions of attributes varied significantly between the training, public and private set; they also worked out where the public set would end and the private set would begin. To prepare for this, they adjusted their trainingset to better represent the (private) testing set.[5] For making the actual models, ThunderBYTE teste a whole scala of different ML algorithms, but eventually stuck with a combinations of Neural Network algorithms (from Keras) and boosted tree based algorithms (from LightGBM). ThunderBYTE’s final solution used around 10x LGBs and 4x Keras DL models in a ranked geometric weighted average.[6].
The approach of ThunderBYTE does not necessarily stand out among the top entries. Most of them stand out in their thoroughness by both the meticulous preparation of the data-set, and the application of a combination of many dif- ferent algorithms, generally LGB and Keras. ThunderBYTE does stand out in having a great score both on the public and private leader board, suggesting their model is actually best overall.
Task 3.B
We will describe the mathematical notation for the two error measures resp.: mean squared error (MSE) and mean absolute error (MAE). MSE = 1 􏰀n (Yi−
 n i=0 Yˆ)2 andtheMAE= 1 􏰀n |(Y −Yˆ |.Themaindifferencebetweenthetwo
i n i=0 i i
measurements lies in the their respective properties. The MSE property will con-
 sists of placing more weight on extreme values compared to the MAE. Thus in

Data Mining Assignment(Basic) Group 45 7
this case the MAE would be more robust due to the non-square property. This is demonstrated in the output of the calculated prediction errors with using the ARMA(1,1) regression model on stationary data and for the second model we applied a state space model with filtered and smoothed states. The data for these two regression models was chosen to be a time series data. The data con- sists of one column with daily dates and the other column with daily return values extending from 2012-12-11 to 2018-06-29 for International Business Ma- chines Corporation (IBM) [7]. We had chosen this company due to its history of being the first one to introduce machine learning concepts. The results are given in the following Table 2 below:
The main difference in outcome is due to reparameterization [8]. The ARMA(p,q) model is a reduced form of a state space model and does not account much for convergence for different states. However, there exists the possibility when the MSE and MAE will be equal to each other. This case will occur when there exists zeros and ones as values since squaring the values will not make a difference then for the prediction. This will lead to to the fact MSE = MAE.
Task 3.C
The Dataset SmsCollection.csv contains total of 5574 text messages. After initial analysis we found that this data set has around 86% messages labelled as “ham” and 14% messages labelled as “spam”. It can be an important factor to assess the strength of the classifier. The data-set looks like:
Fig. 10: A Peek into the sms data-set
Modelling Techniques: To identify the category to which a messages belongs to we need to used a supervised classification modeling framework.The data consist of text so, we will be using natural language processing (NLP). Before applying all the NLP techniques, we need to keep in mind that the text we are working with is colloquial English and regular techniques might not be very effective if not used properly.
Data Transformation
Data Cleaning: In text analysis, text normalisation is important as compared to other analysis where removing outliers or leverage points holds a good place.
  Model ARMA(1,1) State Space
    MSE 0.00013 0.00019
     MAE 0.00741 0.00913
    
8 Group 45
For this particular classification problem, we only used case normalisation. The rationale is that it will be hard to apply a stemmer or lemmatiser onto colloquial English and that since the text messages are so short, removing stop words might not also be a good idea to follow.
Vectorizing the Text: For converting a text to a vector, the Bag of Words Model, might not work very well for our Spam or Ham classifier due to its simplicity. Instead, we used the TF-IDF vectorizer (Term Frequency—Inverse Document Frequency), a similar embedding technique which takes into account the importance of each term to document. Next, we need to classify the text whether it belongs to a spam or ham. For this we need to use a classification algorithms.
Building and testing classifier: The next step is to select the type of classifier to use. So, in this step, we chose several candidate classifiers and evaluate them against the testing set to see which one works the best. First, We used Na ̈ıve Bayes classifier to do the classification. Before training the vectorizer, we split our data into a training set and a testing set. 25% of our data is allocated for testing. After this, we tried Support Vector Machine Classifier to classify the data and then we compared the results.
Fig. 11: Naive Bayes Classifier Fig. 12: Support Vector Machine Classifier
From the above figures, if we consider precision, we can see that Naive Bayes gives a performance of 97.5 and SVM gives a little better 98.5. keeping other factors in mind we finally think that for our case it would be better to use SVM classfier for our current problem.
Improvements
1) Case Normalization : We can say that the spam messages tend to use more upper casing to capture the readers’ attention. So we can use this additional information while training our classifiers. 2) Length of the message : Spam a lot of times contains long messages about different deals and things that you can win, we nticed that the spams SMS should be longer on average: Spam mean- 138.790885 and Ham Mean- 67.774237. We can use the length to improve the model.
3) tokenizer :A popular alternative to assigning each word as its own term is to use a tokenizer. A tokenizer splits documents into tokens.The tokenizer is able to extract more information than word level analysers. However, tokenizers do not work well with colloquial English and may encounter issues splitting URLs or emails.
  
Data Mining Assignment(Basic) Group 45 9
4) Word Cloud :We can also use word cloud.Word cloud is a straight forward way to demonstrate the most common words in spam and ham text. we can further boost our classifiers using this. [9]
References
1. L. H. A. Krishnaparum, B. Carin, “Sparse multinomial logistic regression: fast al- gorithms and generalization bounds,” Jul 2015.
2. S. S.R. and L. D, “A survey of decision tree classifier methodology ),” Jun 1991.
3. F.Pedregosa,G.Varoquaux,A.Gramfort,V.Michel,B.Thirion,O.Grisel,M.Blon- del, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Courna- peau, M. Brucher, M. Perrot, and E. Duchesnay, “Scikit-learn: Machine learning in
Python,” Journal of Machine Learning Research, vol. 12, pp. 2825–2830, 2011.
4. R. McCann, C. Seifert, S. Higgs, M. Duncan, M. Ahmadi, B. Saltaformaggio, and T. Kim, “Microsoft malware prediction,” Dec 2018. [Online]. Available:
https://www.kaggle.com/c/microsoft-malware-prediction
5. CPMP, “Our solution (cpmp view),” Mar 2019. [Online]. Available:
https://www.kaggle.com/c/microsoft-malware-prediction/discussion/84069
6. Giba, “6 solution (giba view),” Mar 2019. [Online]. Available:
https://www.kaggle.com/c/microsoft-malware-prediction/discussion/84112
7. “Crsp data ibm stocks,” Apr 2019. [Online]. Available: https://wrds-web-wharton-
upenn-edu.vu-nl.idm.oclc.org/wrds/ds/crsp/stocka/dsf.cfm?navId = 128
8. S. Durbin, J. Koopman, “Time series analysis by state space methods,” Jul 2012.
9. M. Gu, “Spam or ham,” Dec 2018. [Online]. Available: https://medium.com/analytics-
vidhya/introduction-to-natural-language-processing-part-1-777f972cc7b3

