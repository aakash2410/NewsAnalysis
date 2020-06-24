from Scrapers import TOI, IndiaTV, TheHindu
import pandas as pd 
from textblob import TextBlob 
searched_term = "Modi"
df1 = pd.DataFrame(TOI(searched_term))[:50]
df2 = pd.DataFrame(IndiaTV(searched_term))[:50]
df3 = pd.DataFrame(TheHindu(searched_term))[:50]

def SentAn(df):
    Polarity = []
    Polarity_score = []
    neg = 0
    pos = 0
    neu = 0
    pos_sum = 0
    neg_sum = 0
    for headline in df["Headlines"]:
        analysis = TextBlob(headline)
        Polarity_score.append(analysis.sentiment.polarity)
        
        if analysis.sentiment.polarity >= 0.001:
            Polarity.append("Positive")
            pos_sum += analysis.sentiment.polarity
            pos +=1
        elif analysis.sentiment.polarity <= -0.001:
            Polarity.append("Negative")
            neg +=1
            neg_sum += analysis.sentiment.polarity
        else: 
            Polarity.append("Neutral")
            neu +=1
    Polarity = pd.DataFrame(Polarity)
    Polarity_score = pd.DataFrame(Polarity_score)
    df["Polarity"] = Polarity
    df['Polarity_score'] = Polarity_score
    print("Total P Bias % = " + str(pos_sum*2))
    print("Total N Bias % = " + str(neg_sum*2))
    return df, pos, neu, neg

if __name__ == "__main__":
    df1_new, pos, neu, neg = SentAn(df2)
    df1_new.to_csv(f"{searched_term}.csv")
    print(pos, neu, neg)
    
         

