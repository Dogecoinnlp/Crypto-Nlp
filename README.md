# Crypto-Nlp

package requirement:

PushshiftAPI  
sentence_transformers  
gym  
stable_baselines3  
scilearn
pytorch

Running Instructions:  

Data Prepration:  
Run essembled.py in Vectorization folder, change the name of the asset and the time. All the data downloaded is saved in the folder. The code will auto download posts and embede 
them into vectors using SBERT. We didn't download any of the posts or comments into string and save in our computer. We thought I will be too big. Instead everyday we save them in memory and perform the embedding. We just saved all the vectors instead.  

For model evaluation, run model_eval.py in Vectorization folder to test the cosine similarities among different strings, sentences used in evaluation is included in the excel file in the same folder.  

Benchmark_models.ipynb, runs cells in order. This file sets up logistic and linearing regression. The benchmark models are also included in here

Attention Learning:
run attention_learning.ipynb, run cells in order. This file builds the attention neural network and uses it to predict stock price.

LSTM:
run lstm_learning.ipynb, run cells in order. his file builds the LSTM model and uses it to predict stock price.

Reinforcement learning:  
Run BTC_data_merge.ipynb and ETH_data_merge.ipynb to merge the price data and samentic vector data. Merged csv is included in the folder. Then run RL_NLP_BTC.py to run the reinforcement  
learning model for BTC, and RL_NLP_ETH.py for model of Ethereum.  

Random Forest and Boosting:  
Run BTC_RF_Boosting.ipynb and import data from BTC_total.csv to get model results for Bitcoin.
Run ETH_RF_Boosting.ipynb and import data from ETH_total.csv to get model results for Ethereum.
