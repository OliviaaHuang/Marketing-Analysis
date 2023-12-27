# Marketing analytics Project – to select the most probable buyers

## 1.Problem Statement
Given the limited marketing budget, marketers can only select the most probably customer from the total target customers to run the marketing campaign to save money.

This is precisely how analytics-enablement can help any marketing function to maximum business revenue and optimize their marketing funnel by smartly allocating their funds, at scale.

## 2.Dataset

The entire dataset is divided into two parts ([Dataset_10Percent.xlsx](./Dataset_10Percent.xlsx)  and [Dataset_90Percent.xlsx](./Dataset_90Percent.xlsx)).  

[Dataset_10Percent.xlsx](./Dataset_10Percent.xlsx) is dataset for 10% loyalty program participants. This is the file we would use for [Logistic Regression Model](https://en.wikipedia.org/wiki/Logistic_regression "悬停显示")	 building.  
[Dataset_90Percent.xlsx](./Dataset_90Percent.xlsx) is dataset for marketer to make market plans by using [Logistic Regression Model](https://en.wikipedia.org/wiki/Logistic_regression "悬停显示").  

## 3.Data Modeling

<img width="905" alt="Columns" src="https://github.com/OliviaaHuang/Protfolio-Machine-Learning/assets/152938995/d7cce933-26e7-4751-8599-5d40caaeaf70">

This dataset contains 22K observations.  

[Independent variables](https://en.wikipedia.org/wiki/Dependent_and_independent_variables#In_modeling_and_statistics "悬停显示"): DemAffl, 
DemAge, DemClusterGroup, DemGender, DemReg, DemTVReg, LoyalClass, LoyalSpend, LoyalTime  
[Dependent variables](https://en.wikipedia.org/wiki/Dependent_and_independent_variables#In_modeling_and_statistics "悬停显示"): TargetBuy 
([Binary](https://en.wikipedia.org/wiki/Binary), 0 means no purchase, 1 means possible purchase)  

Checking the performance of the model: [Confusion Matrix](https://en.wikipedia.org/wiki/Confusion_matrix), Accuracy(81%)





## 4.Data visualization
Tableau is used (https://public.tableau.com/app/profile/qijia.huang/viz/MarketingCampaignAnalysis_17035489915940/1_1)


## 5.Conclusion
For profit maximisation, campany should run their marketing campaign on the top `30%`.  
For marketing penetration, campany can choose the top `40%` to run their marketing campaign.


<img width="913" alt="Result" src="https://github.com/OliviaaHuang/Protfolio-Machine-Learning/assets/152938995/172b94ab-1176-46b8-a9b7-70ce01730df3">

