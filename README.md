# Marketing analytics Project – to select the most probable buyers

## 1.Problem Statement
Given the limited marketing budget, marketers can only select the most probably customer from the total target customers to run the marketing campaign to save money.

This is precisely how analytics-enablement can help any marketing function to maximum business revenue and optimize their marketing funnel by smartly allocating their funds, at scale.

## 2.Tools Used

`Jupyter Notebook` is used as IDE.   
`Pandas` and `NumPy` are used for Data Manipulation & Pre-processing and Mathematical functions respectively.  
`Sklearn` is used for building `Logistic Regression Model` to predict the purchase posibility of the customers.
Used the `Tableau` to build dashboard for data visualization.  
Uploaded the result to the `Azure`.




## 3.Dataset

The entire dataset is divided into two parts ([Dataset_10Percent.xlsx](./Dataset_10Percent.xlsx)  and [Dataset_90Percent.xlsx](./Dataset_90Percent.xlsx)).  

<img width="600" alt="Process" src="https://github.com/OliviaaHuang/Protfolio-Machine-Learning/assets/152938995/29ede503-8562-4096-bcc8-c732fe4d5486">

[Dataset_10Percent.xlsx](./Dataset_10Percent.xlsx) is dataset for 10% loyalty program participants. This is the file we would use for [Logistic Regression Model](https://en.wikipedia.org/wiki/Logistic_regression "悬停显示")	 building.  
[Dataset_90Percent.xlsx](./Dataset_90Percent.xlsx) is dataset for marketer to make market plans by using [Logistic Regression Model](https://en.wikipedia.org/wiki/Logistic_regression "悬停显示").  

## 4.Data Modeling

<img width="500" alt="Columns" src="https://github.com/OliviaaHuang/Protfolio-Machine-Learning/assets/152938995/d7cce933-26e7-4751-8599-5d40caaeaf70">


[Independent variables](https://en.wikipedia.org/wiki/Dependent_and_independent_variables#In_modeling_and_statistics "悬停显示"): DemAffl, 
DemAge, DemClusterGroup, DemGender, DemReg, DemTVReg, LoyalClass, LoyalSpend, LoyalTime  
[Dependent variables](https://en.wikipedia.org/wiki/Dependent_and_independent_variables#In_modeling_and_statistics "悬停显示"): TargetBuy 
([Binary](https://en.wikipedia.org/wiki/Binary), 0 means no purchase, 1 means possible purchase)  

Checking the performance of the model: [Confusion Matrix](https://en.wikipedia.org/wiki/Confusion_matrix), Accuracy(81%)





## 5.Data visualization
Tableau is used. [Click](https://public.tableau.com/app/profile/qijia.huang/viz/MarketingCampaignAnalysis_17035489915940/1_1) here.  

<img width="683" height="600" alt="Marketing Campaign" src="https://github.com/OliviaaHuang/Protfolio-Machine-Learning/assets/152938995/97dbe8c2-e6e2-49bd-b956-9772c0575985">

I also uploaded the result of data visualization to the Azure.  

<img width="1308" alt="Screenshot 2023-12-27 at 19 33 08" src="https://github.com/OliviaaHuang/Protfolio-Machine-Learning/assets/152938995/54989517-c295-4146-90a9-dea9c2fb1e3e">




## 6.Conclusion
For profit maximisation, campany should run their marketing campaign on the top `30%`.  
For marketing penetration, campany can choose the top `40%` to run their marketing campaign.


<img width="913" alt="Result" src="https://github.com/OliviaaHuang/Protfolio-Machine-Learning/assets/152938995/172b94ab-1176-46b8-a9b7-70ce01730df3">

