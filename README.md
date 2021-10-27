# FinalProject_Python

Ce projet presente l'analyse d'un dataset reliant les test de personnalités de personnes et leurs consommations de drogues. 
Voici le lien du dataset : https://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29

## The datas : 

Database contains records for 1885 respondents. For each respondent 12 attributes are known: Personality measurements which include NEO-FFI-R (neuroticism, extraversion, openness to experience, agreeableness, and conscientiousness), BIS-11 (impulsivity), and ImpSS (sensation seeking), level of education, age, gender, country of residence and ethnicity. All input attributes are originally categorical and are quantified. After quantification values of all input features can be considered as real-valued. In addition, participants were questioned concerning their use of 18 legal and illegal drugs (alcohol, amphetamines, amyl nitrite, benzodiazepine, cannabis, chocolate, cocaine, caffeine, crack, ecstasy, heroin, ketamine, legal highs, LSD, methadone, mushrooms, nicotine and volatile substance abuse and one fictitious drug (Semeron) which was introduced to identify over-claimers. For each drug they have to select one of the answers: never used the drug, used it over a decade ago, or in the last decade, year, month, week, or day.
Database contains 18 classification problems. Each of independent label variables contains seven classes: "Never Used", "Used over a Decade Ago", "Used in Last Decade", "Used in Last Year", "Used in Last Month", "Used in Last Week", and "Used in Last Day".


### Attribute Informations:

  -ID

  -Age (Real) is age of participant 

  -Gender (Real) is gender of participant

  -Education (Real)
  
  -Country (Real) is country of current residence of participant

  -Ethnicity (Real) is ethnicity of participant

  - Nscore (Real) is NEO-FFI-R Neuroticism

  - Escore (Real) is NEO-FFI-R Extraversion

  - Oscore (Real) is NEO-FFI-R Openness to experience

  - Ascore (Real) is NEO-FFI-R Agreeableness

  - Cscore (Real) is NEO-FFI-R Conscientiousness

  - Impulsive (Real) is impulsiveness measured by BIS-11

  - SS (Real) is sensation seeing measured by ImpSS
 
 
 ### The 18 drugs participants were asked about: 
  
  
  - Alcohol
   
  - Amphet
  
  - Amyl
  
  - Benzos
  
  - Caff
  
  - Cannabis
  
  - Choc
  
  - Coke
  
  - Crack
  
  - Ecstasy
  
  - Heroin 
  
  - Ketamine
  
  - Legalh
  
  - LSD
  
  - Mushromms
  
  - Nicotine
  
  - Semer
  
  - VSA
  
  
 ### The goal of the project :
 
 After analysing the dataset and trying to get some relevant visualizations, I decided to deploy a simple ML model to predict Cannabis consumption. 
 Here are the ML models used in this project : KNN, RandomForest, Gradient Boostig and Logistic Regression. Most of the time, without tuning my models, RandomFrest seems to be the most efficient to deal with precision and accuracy. So I decided to tune the hyperparameters to have better predictions. 
 
 
 The last step was to deploy a simple Flask API to test my ML model. 
 
  
  
  
  
  
  
  
  
  
  
  
  
  
