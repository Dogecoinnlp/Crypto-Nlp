# Crypto-Nlp

package requirement:

PushshiftAPI
sentence_transformers
gym
stable_baselines3

Running Instructions:

Data Prepration:
Run essembled.py in Vectorization folder, change the name of the asset and the time. All the data downloaded is saved in the folder. The code will auto download posts and embede 
them into vectors using SBERT

For model evaluation, run model_eval.py in Vectorization folder to test the cosine similarities among different strings, sentences used in evaluation is included in the excel file in the same folder.

Reinforcement learning:
Run BTC_data_merge.ipynb and ETH_data_merge.ipynb to merge the price data and samentic vector data. Merged csv is included in the folder. Then run RL_NLP_BTC.py to run the reinforcement
learning model for BTC, and RL_NLP_ETH.py for model of Ethereum.
