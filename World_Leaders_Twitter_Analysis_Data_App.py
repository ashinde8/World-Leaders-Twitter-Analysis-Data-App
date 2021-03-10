# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 07:07:15 2021

@author: Lenovo
"""

import streamlit as st
import pandas as pd
import matplotlib.image as mpimg

pd.options.display.width = 0
pd.set_option('display.width', 20)

imagew1 = mpimg.imread('w1.jpg')
imagew2 = mpimg.imread('w2.jpg')
imagew3 = mpimg.imread('w3.png')
imagew4 = mpimg.imread('w4.jpg')
imagew5 = mpimg.imread('uss4.jpg')

image11 = mpimg.imread('joe_sentiment_distribution.png')
image12 = mpimg.imread('joe_total_tweets_wc.png')
image13 = mpimg.imread('joe_total_tweets_wf.png')
image14 = mpimg.imread('joe_positive_tweets_wc.png')
image15 = mpimg.imread('joe_positive_tweets_wf.png')
image16 = mpimg.imread('joe_neutral_tweets_wc.png')
image17 = mpimg.imread('joe_neutral_tweets_wf.png')

image21 = mpimg.imread('justin_sentiment_distribution.png')
image22 = mpimg.imread('kamala_total_tweets_wc.png')
image23 = mpimg.imread('kamala_total_tweets_wf.png')
image24 = mpimg.imread('kamala_positive_tweets_wc.png')
image25 = mpimg.imread('kamala_positive_tweets_wf.png')
image26 = mpimg.imread('kamala_neutral_tweets_wc.png')
image27 = mpimg.imread('kamala_neutral_tweets_wf.png')

image31 = mpimg.imread('jacinda_sentiment_distribution.png')
image32 = mpimg.imread('jacinda_total_tweets_wc.png')
image33 = mpimg.imread('jacinda_total_tweets_wf.png')
image34 = mpimg.imread('jacinda_positive_tweets_wc.png')
image35 = mpimg.imread('jacinda_positive_tweets_wf.png')
image36 = mpimg.imread('jacinda_neutral_tweets_wc.png')
image37 = mpimg.imread('jacinda_neutral_tweets_wf.png')
image38 = mpimg.imread('jacinda_negative_tweets_wc.png')
image39 = mpimg.imread('jacinda_negative_tweets_wf.png')

image41 = mpimg.imread('boris_sentiment_distribution.png')
image42 = mpimg.imread('boris_total_tweets_wc.png')
image43 = mpimg.imread('boris_total_tweets_wf.png')
image44 = mpimg.imread('boris_positive_tweets_wc.png')
image45 = mpimg.imread('boris_positive_tweets_wf.png')
image46 = mpimg.imread('boris_neutral_tweets_wc.png')
image47 = mpimg.imread('boris_neutral_tweets_wf.png')
image48 = mpimg.imread('boris_negative_tweets_wc.png')
image49 = mpimg.imread('boris_negative_tweets_wf.png')

image51 = mpimg.imread('aus_sentiment_distribution.png')
image52 = mpimg.imread('aus_total_tweets_wc.png')
image53 = mpimg.imread('aus_total_tweets_wf.png')
image54 = mpimg.imread('aus_positive_tweets_wc.png')
image55 = mpimg.imread('aus_positive_tweets_wf.png')
image56 = mpimg.imread('aus_neutral_tweets_wc.png')
image57 = mpimg.imread('aus_neutral_tweets_wf.png')
image58 = mpimg.imread('aus_negative_tweets_wc.png')
image59 = mpimg.imread('aus_negative_tweets_wf.png')

st.title('World Leaders Twitter Analysis Data App')

st.sidebar.title("Navigation")
category = ["World Leaders Twitter Analysis Data App","Source Code"]
choice = st.sidebar.radio("Select the Navigation", category)

if choice == "World Leaders Twitter Analysis Data App":
    
    st.info("Do you want to find out the Analysis of what these World Leaders are tweeting about ? ")
    
    st.sidebar.title("World Leaders")
    Candidate_choice = st.sidebar.radio("Select the World Leader", ["New Zealand PM Jacinda Ardern","US Vice President Kamala Harris","US President Joe Biden","United Kingdom PM Boris Johnson","Australia PM Scott Morrison"])
    
    if Candidate_choice == "US President Joe Biden":
        
    
        st.subheader("Joe Biden - President of The United States of America") 
        st.image(imagew5, height = 750, width = 750)

        st.subheader("The Analysis has been performed on the tweets sent from US President Joe Biden's Twitter Account recently.")
        
        st.write("1. Displays the Sentiment Distribution of President Joe Biden's Tweets")
        st.write("2. Generates a wordcloud for all the Tweets")
        st.write("3. Displays the Most Frequent Words used in all the Tweets")
        
        Analyzer_choice1 = st.selectbox("Select the Option",  ["Display the Sentiment Distribution of President Joe Biden's Tweets","Generate a wordcloud for all the Tweets","Display the Most Frequent Words used in all the Tweets"])
                                                                         
        if st.button("Analyze"):
                
            if Analyzer_choice1 == "Display the Sentiment Distribution of President Joe Biden's Tweets":                                                      
                
                st.write("Sentiment Distribution of the Tweets")                                                  
                st.image(image11, height = 1000, width = 1000)
                    
            elif Analyzer_choice1 == "Generate a wordcloud for all the Tweets":                                                      
                
                st.write("WordCloud for All the Tweets")                                                  
                st.image(image12, height = 1000, width = 1000)              
                    
            else:                                                      
                
                st.write("Most Frequent Words used in All the Tweets")                                                  
                st.image(image13, height = 1000, width = 1000)
        
        st.write("4. Generates a wordcloud for the Positive Tweets")            
        st.write("5. Displays the Most Frequent Words used in the Positive Tweets")
            
        Analyzer_choice2 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Positive Tweets", "Display the Most Frequent Words used in the Positive Tweets"])
                                                               
        if st.button("Analyze."):        
                    
            if Analyzer_choice2 == "Generate a wordcloud for the Positive Tweets":                                                      
                
                st.write("WordCloud for All the Positive Tweets")                                                  
                st.image(image14, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Positive Tweets")                                                  
                st.image(image15, height = 1000, width = 1000)                
                        
        st.write("6. Generates a wordcloud for the Neutral Tweets")            
        st.write("7. Displays the Most Frequent Words used in the Neutral Tweets")
            
        Analyzer_choice3 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Neutral Tweets", "Display the Most Frequent Words used in the Neutral Tweets"])
                                                                  
        if st.button("Analyze "): 
                    
            if Analyzer_choice3 == "Generate a wordcloud for the Neutral Tweets":                                                      
                
                st.write("WordCloud for All the Neutral Tweets")                                                  
                st.image(image16, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Neutral Tweets")                                                  
                st.image(image17, height = 1000, width = 1000)
                        
        
    elif Candidate_choice == "US Vice President Kamala Harris":
        
        st.subheader("Kamala Harris - Vice President of The United States of America") 
        st.image(imagew1, height = 750, width = 750)

        
                   
        st.subheader("The Analysis has been performed on the tweets sent from US Vice President, Kamala Harris's Twitter Account recently.")
        
        st.write("1. Displays the Sentiment Distribution of Vice President Kamala Harris's Tweets")
        st.write("2. Generates a wordcloud for all the Tweets")
        st.write("3. Displays the Most Frequent Words used in all the Tweets")
        
        Analyzer_choice1 = st.selectbox("Select the Option",  ["Display the Sentiment Distribution of Vice President Kamala Harris's Tweets","Generate a wordcloud for all the Tweets","Display the Most Frequent Words used in all the Tweets"])
        
        if st.button("Analyze"):
                
            if Analyzer_choice1 == "Display the Sentiment Distribution of Vice President Kamala Harris's Tweets":                                                      
                
                st.write("Sentiment Distribution of the Tweets")                                                  
                st.image(image21, height = 1000, width = 1000)
                    
            elif Analyzer_choice1 == "Generate a wordcloud for all the Tweets":                                                      
                
                st.write("WordCloud for All the Tweets")                                                  
                st.image(image22, height = 1000, width = 1000)              
                    
            else:                                                      
                
                st.write("Most Frequent Words used in All the Tweets")                                                  
                st.image(image23, height = 1000, width = 1000)
        
        st.write("4. Generates a wordcloud for the Positive Tweets")            
        st.write("5. Displays the Most Frequent Words used in the Positive Tweets")
            
        Analyzer_choice2 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Positive Tweets", "Display the Most Frequent Words used in the Positive Tweets"])

        if st.button("Analyze."):        
                    
            if Analyzer_choice2 == "Generate a wordcloud for the Positive Tweets":                                                      
                
                st.write("WordCloud for All the Positive Tweets")                                                  
                st.image(image24, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Positive Tweets")                                                  
                st.image(image25, height = 1000, width = 1000)                
        
        st.write("6. Generates a wordcloud for the Neutral Tweets")            
        st.write("7. Displays the Most Frequent Words used in the Neutral Tweets")
            
        Analyzer_choice3 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Neutral Tweets", "Display the Most Frequent Words used in the Neutral Tweets"])

        if st.button("Analyze "): 
                    
            if Analyzer_choice3 == "Generate a wordcloud for the Neutral Tweets":                                                      
                
                st.write("WordCloud for All the Neutral Tweets")                                                  
                st.image(image26, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Neutral Tweets")                                                  
                st.image(image27, height = 1000, width = 1000)
                         
        
    elif Candidate_choice == "New Zealand PM Jacinda Ardern":
        
        st.subheader("Jacinda Ardern - Prime Minister of New Zealand")
        st.image(imagew2, height = 500, width = 500)

        st.subheader("The Analysis has been performed on the tweets sent from Prime Minister of New Zealand, Jacinda Ardern's Twitter Account recently.")
        
        st.write("1. Displays the Sentiment Distribution of New Zealand Prime Minister Jacinda Ardern's Tweets")
        st.write("2. Generates a wordcloud for all the Tweets")
        st.write("3. Displays the Most Frequent Words used in all the Tweets")
        
        Analyzer_choice1 = st.selectbox("Select the Option",  ["Display the Sentiment Distribution of New Zealand Prime Minister Jacinda Ardern's Tweets","Generate a wordcloud for all the Tweets","Display the Most Frequent Words used in all the Tweets"])
                                                                                 
        if st.button("Analyze"):
                
            if Analyzer_choice1 == "Display the Sentiment Distribution of New Zealand Prime Minister Jacinda Ardern's Tweets":                                                      
                
                st.write("Sentiment Distribution of the Tweets")                                                  
                st.image(image31, height = 1000, width = 1000)
                    
            elif Analyzer_choice1 == "Generate a wordcloud for all the Tweets":                                                      
                
                st.write("WordCloud for All the Tweets")                                                  
                st.image(image32, height = 1000, width = 1000)              
                    
            else:                                                      
                
                st.write("Most Frequent Words used in All the Tweets")                                                  
                st.image(image33, height = 1000, width = 1000)
        
        st.write("4. Generates a wordcloud for the Positive Tweets")            
        st.write("5. Displays the Most Frequent Words used in the Positive Tweets")
            
        Analyzer_choice2 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Positive Tweets", "Display the Most Frequent Words used in the Positive Tweets"])
                                                                       
        if st.button("Analyze."):        
                    
            if Analyzer_choice2 == "Generate a wordcloud for the Positive Tweets":                                                      
                
                st.write("WordCloud for All the Positive Tweets")                                                  
                st.image(image34, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Positive Tweets")                                                  
                st.image(image35, height = 1000, width = 1000)                
        
        st.write("6. Generates a wordcloud for the Neutral Tweets")            
        st.write("7. Displays the Most Frequent Words used in the Neutral Tweets")
            
        Analyzer_choice3 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Neutral Tweets", "Display the Most Frequent Words used in the Neutral Tweets"])
                                                                                  
        if st.button("Analyze "): 
                    
            if Analyzer_choice3 == "Generate a wordcloud for the Neutral Tweets":                                                      
                
                st.write("WordCloud for All the Neutral Tweets")                                                  
                st.image(image36, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Neutral Tweets")                                                  
                st.image(image37, height = 1000, width = 1000)
        
        st.write("8. Generates a wordcloud for the Negative Tweets")            
        st.write("9. Displays the Most Frequent Words used in the Negative Tweets")
            
        Analyzer_choice4 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Negative Tweets", "Display the Most Frequent Words used in the Negative Tweets"])
                
        if st.button("Analyze  "):       
                    
            if Analyzer_choice4 == "Generate a wordcloud for the Negative Tweets":                                                      
                                                                  
                st.write("WordCloud for All the Negative Tweets")
                st.image(image38, height = 1000, width = 1000)
                    
            else:                                                      
                                                                  
                st.write("Most Frequent Words used in the Negative Tweets")
                st.image(image39, height = 1000, width = 1000)
                
    elif Candidate_choice == "United Kingdom PM Boris Johnson":
         
        st.subheader("Boris Johnson - Prime Minister of United Kingdom")
        st.image(imagew3, height = 500, width = 500)
        st.subheader("The Analysis has been performed on the tweets sent from Prime Minister of United Kingdom, Boris Johnson's Twitter Account recently.")
        
        st.write("1. Displays the Sentiment Distribution of UK Prime Minister Boris Johnson's Tweets")
        st.write("2. Generates a wordcloud for all the Tweets")
        st.write("3. Displays the Most Frequent Words used in all the Tweets")
        
        Analyzer_choice1 = st.selectbox("Select the Option",  ["Display the Sentiment Distribution of UK Prime Minister Boris Johnson's Tweets","Generate a wordcloud for all the Tweets","Display the Most Frequent Words used in all the Tweets"]) 
        
        if st.button("Analyze"):
                
            if Analyzer_choice1 == "Display the Sentiment Distribution of UK Prime Minister Boris Johnson's Tweets":                                                      
                
                st.write("Sentiment Distribution of the Tweets")                                                  
                st.image(image41, height = 1000, width = 1000)
                    
            elif Analyzer_choice1 == "Generate a wordcloud for all the Tweets":                                                      
                
                st.write("WordCloud for All the Tweets")                                                  
                st.image(image42, height = 1000, width = 1000)              
                    
            else:                                                      
                
                st.write("Most Frequent Words used in All the Tweets")                                                  
                st.image(image43, height = 1000, width = 1000)
        
        st.write("4. Generates a wordcloud for the Positive Tweets")            
        st.write("5. Displays the Most Frequent Words used in the Positive Tweets")
            
        Analyzer_choice2 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Positive Tweets", "Display the Most Frequent Words used in the Positive Tweets"])
                                                                           
        if st.button("Analyze."):        
                    
            if Analyzer_choice2 == "Generate a wordcloud for the Positive Tweets":                                                      
                
                st.write("WordCloud for All the Positive Tweets")                                                  
                st.image(image44, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Positive Tweets")                                                  
                st.image(image45, height = 1000, width = 1000)                
        
        st.write("6. Generates a wordcloud for the Neutral Tweets")            
        st.write("7. Displays the Most Frequent Words used in the Neutral Tweets")
            
        Analyzer_choice3 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Neutral Tweets", "Display the Most Frequent Words used in the Neutral Tweets"])
                                                                                  
        if st.button("Analyze "): 
                    
            if Analyzer_choice3 == "Generate a wordcloud for the Neutral Tweets":                                                      
                
                st.write("WordCloud for All the Neutral Tweets")                                                  
                st.image(image46, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Neutral Tweets")                                                  
                st.image(image47, height = 1000, width = 1000)
        
        st.write("8. Generates a wordcloud for the Negative Tweets")            
        st.write("9. Displays the Most Frequent Words used in the Negative Tweets")
            
        Analyzer_choice4 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Negative Tweets", "Display the Most Frequent Words used in the Negative Tweets"])
                
        if st.button("Analyze  "):       
                    
            if Analyzer_choice4 == "Generate a wordcloud for the Negative Tweets":                                                      
                                                                  
                st.write("WordCloud for All the Negative Tweets")
                st.image(image48, height = 1000, width = 1000)
                    
            else:                                                      
                                                                  
                st.write("Most Frequent Words used in the Negative Tweets")
                st.image(image49, height = 1000, width = 1000)
    
    else:
                
        st.subheader("Scott Morrison - Prime Minister of Australia")
        st.image(imagew4, height = 600, width = 600)
        st.subheader("The Analysis has been performed on the tweets sent from Prime Minister of Australia, Scott Morrison's Twitter Account recently.")
        
        st.write("1. Displays the Sentiment Distribution of Australia Prime Minister Scott Morrison's Tweets")
        st.write("2. Generates a wordcloud for all the Tweets")
        st.write("3. Displays the Most Frequent Words used in all the Tweets")
        
        Analyzer_choice1 = st.selectbox("Select the Option",  ["Display the Sentiment Distribution of Australia Prime Minister Scott Morrison's Tweets","Generate a wordcloud for all the Tweets","Display the Most Frequent Words used in all the Tweets"])
        
        if st.button("Analyze"):
                
            if Analyzer_choice1 == "Display the Sentiment Distribution of Australia Prime Minister Scott Morrison's Tweets":                                                      
                
                st.write("Sentiment Distribution of the Tweets")                                                  
                st.image(image51, height = 1000, width = 1000)
                    
            elif Analyzer_choice1 == "Generate a wordcloud for all the Tweets":                                                      
                
                st.write("WordCloud for All the Tweets")                                                  
                st.image(image52, height = 1000, width = 1000)              
                    
            else:                                                      
                
                st.write("Most Frequent Words used in All the Tweets")                                                  
                st.image(image53, height = 1000, width = 1000)
        
        st.write("4. Generates a wordcloud for the Positive Tweets")            
        st.write("5. Displays the Most Frequent Words used in the Positive Tweets")
            
        Analyzer_choice2 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Positive Tweets", "Display the Most Frequent Words used in the Positive Tweets"])
                                                                          
        if st.button("Analyze."):        
                    
            if Analyzer_choice2 == "Generate a wordcloud for the Positive Tweets":                                                      
                
                st.write("WordCloud for All the Positive Tweets")                                                  
                st.image(image54, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Positive Tweets")                                                  
                st.image(image55, height = 1000, width = 1000)                
        
        st.write("6. Generates a wordcloud for the Neutral Tweets")            
        st.write("7. Displays the Most Frequent Words used in the Neutral Tweets")
            
        Analyzer_choice3 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Neutral Tweets", "Display the Most Frequent Words used in the Neutral Tweets"])

        if st.button("Analyze "): 
                    
            if Analyzer_choice3 == "Generate a wordcloud for the Neutral Tweets":                                                      
                
                st.write("WordCloud for All the Neutral Tweets")                                                  
                st.image(image56, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Neutral Tweets")                                                  
                st.image(image57, height = 1000, width = 1000)
        
        st.write("8. Generates a wordcloud for the Negative Tweets")            
        st.write("9. Displays the Most Frequent Words used in the Negative Tweets")
            
        Analyzer_choice4 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Negative Tweets", "Display the Most Frequent Words used in the Negative Tweets"])
                
        if st.button("Analyze  "):       
                    
            if Analyzer_choice4 == "Generate a wordcloud for the Negative Tweets":                                                      
                                                                  
                st.write("WordCloud for All the Negative Tweets")
                st.image(image58, height = 1000, width = 1000)
                    
            else:                                                      
                                                                  
                st.write("Most Frequent Words used in the Negative Tweets")
                st.image(image59, height = 1000, width = 1000)
        
else:
    
    st.graphviz_chart("""
        digraph{
        Tweet -> Sentiment
        Sentiment -> Positive
        Sentiment -> Neutral 
        Sentiment -> Negative
        Positive -> MostPositiveTweet
        Positive -> WordCloud
        Positive -> WordFrequency
        Negative -> MostNegativeTweet
        Negative -> WordCloud
        Negative -> WordFrequency
        Neutral -> WordCloud
        Neutral -> WordFrequency
        }
        """)
        
    st.subheader("Source Code")
    
    code = """

import streamlit as st
import pandas as pd
import matplotlib.image as mpimg

pd.options.display.width = 0
pd.set_option('display.width', 20)

imagew1 = mpimg.imread('w1.jpg')
imagew2 = mpimg.imread('w2.jpg')
imagew3 = mpimg.imread('w3.png')
imagew4 = mpimg.imread('w4.jpg')
imagew5 = mpimg.imread('uss4.jpg')

##

image11 = mpimg.imread('joe_sentiment_distribution.png')
image12 = mpimg.imread('joe_total_tweets_wc.png')
image13 = mpimg.imread('joe_total_tweets_wf.png')
image14 = mpimg.imread('joe_positive_tweets_wc.png')
image15 = mpimg.imread('joe_positive_tweets_wf.png')
image16 = mpimg.imread('joe_neutral_tweets_wc.png')
image17 = mpimg.imread('joe_neutral_tweets_wf.png')


##

image21 = mpimg.imread('justin_sentiment_distribution.png')
image22 = mpimg.imread('kamala_total_tweets_wc.png')
image23 = mpimg.imread('kamala_total_tweets_wf.png')
image24 = mpimg.imread('kamala_positive_tweets_wc.png')
image25 = mpimg.imread('kamala_positive_tweets_wf.png')
image26 = mpimg.imread('kamala_neutral_tweets_wc.png')
image27 = mpimg.imread('kamala_neutral_tweets_wf.png')


##

image31 = mpimg.imread('jacinda_sentiment_distribution.png')
image32 = mpimg.imread('jacinda_total_tweets_wc.png')
image33 = mpimg.imread('jacinda_total_tweets_wf.png')
image34 = mpimg.imread('jacinda_positive_tweets_wc.png')
image35 = mpimg.imread('jacinda_positive_tweets_wf.png')
image36 = mpimg.imread('jacinda_neutral_tweets_wc.png')
image37 = mpimg.imread('jacinda_neutral_tweets_wf.png')
image38 = mpimg.imread('jacinda_negative_tweets_wc.png')
image39 = mpimg.imread('jacinda_negative_tweets_wf.png')

##

image41 = mpimg.imread('boris_sentiment_distribution.png')
image42 = mpimg.imread('boris_total_tweets_wc.png')
image43 = mpimg.imread('boris_total_tweets_wf.png')
image44 = mpimg.imread('boris_positive_tweets_wc.png')
image45 = mpimg.imread('boris_positive_tweets_wf.png')
image46 = mpimg.imread('boris_neutral_tweets_wc.png')
image47 = mpimg.imread('boris_neutral_tweets_wf.png')
image48 = mpimg.imread('boris_negative_tweets_wc.png')
image49 = mpimg.imread('boris_negative_tweets_wf.png')

##

image51 = mpimg.imread('aus_sentiment_distribution.png')
image52 = mpimg.imread('aus_total_tweets_wc.png')
image53 = mpimg.imread('aus_total_tweets_wf.png')
image54 = mpimg.imread('aus_positive_tweets_wc.png')
image55 = mpimg.imread('aus_positive_tweets_wf.png')
image56 = mpimg.imread('aus_neutral_tweets_wc.png')
image57 = mpimg.imread('aus_neutral_tweets_wf.png')
image58 = mpimg.imread('aus_negative_tweets_wc.png')
image59 = mpimg.imread('aus_negative_tweets_wf.png')

st.title('World Leaders Twitter Analysis Data App')

category = ["World Leaders Twitter Analysis Data App","Source Code"]
choice = st.sidebar.radio("Navigation", category)

if choice == "World Leaders Twitter Analysis Data App":
    
    st.info("Do you want to find out the Analysis of what the World Leaders are tweeting about ? ")
    
    Candidate_choice = st.sidebar.radio("Select the Leader", ["New Zealand PM Jacinda Ardern","US Vice President Kamala Harris","US President Joe Biden","United Kingdom PM Boris Johnson","Australia PM Scott Morrison"])
    
    if Candidate_choice == "US President Joe Biden":
        
    
        st.subheader("Joe Biden - President of The United States of America") 
        st.image(imagew5, height = 750, width = 750)

        st.subheader("The Sentiment Analysis has been performed on the tweets sent from US President Joe Biden's Twitter Account recently.")
        
        st.write("1. Displays the Sentiment Distribution of President Joe Biden's Tweets")
        st.write("2. Generates a wordcloud for all the Tweets")
        st.write("3. Displays the Most Frequent Words used in all the Tweets")
        
        Analyzer_choice1 = st.selectbox("Select the Option",  ["Display the Sentiment Distribution of President Joe Biden's Tweets","Generate a wordcloud for all the Tweets","Display the Most Frequent Words used in all the Tweets"])
                                                                         
        if st.button("Analyze"):
                
            if Analyzer_choice1 == "Display the Sentiment Distribution of President Joe Biden's Tweets":                                                      
                
                st.write("Sentiment Distribution of the Tweets")                                                  
                st.image(image11, height = 1000, width = 1000)
                    
            elif Analyzer_choice1 == "Generates a wordcloud for all the Tweets":                                                      
                
                st.write("WordCloud for All the Tweets")                                                  
                st.image(image12, height = 1000, width = 1000)              
                    
            else:                                                      
                
                st.write("Most Frequent Words used in All the Tweets")                                                  
                st.image(image13, height = 1000, width = 1000)
        
        st.write("4. Generates a wordcloud for the Positive Tweets")            
        st.write("5. Displays the Most Frequent Words used in the Positive Tweets")
            
        Analyzer_choice2 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Positive Tweets", "Display the Most Frequent Words used in the Positive Tweets"])
                                                               
        if st.button("Analyze."):        
                    
            if Analyzer_choice2 == "Generate a wordcloud for the Positive Tweets":                                                      
                
                st.write("WordCloud for All the Positive Tweets")                                                  
                st.image(image14, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Positive Tweets")                                                  
                st.image(image15, height = 1000, width = 1000)                
                        
        st.write("6. Generates a wordcloud for the Neutral Tweets")            
        st.write("7. Displays the Most Frequent Words used in the Neutral Tweets")
            
        Analyzer_choice3 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Neutral Tweets", "Display the Most Frequent Words used in the Neutral Tweets"])
                                                                  
        if st.button("Analyze "): 
                    
            if Analyzer_choice3 == "Generate a wordcloud for the Neutral Tweets":                                                      
                
                st.write("WordCloud for All the Neutral Tweets")                                                  
                st.image(image16, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Neutral Tweets")                                                  
                st.image(image17, height = 1000, width = 1000)
                        
        
    elif Candidate_choice == "US Vice President Kamala Harris":
        
        st.subheader("Kamala Harris - Vice President of The United States of America") 
        st.image(imagew1, height = 750, width = 750)

        
                   
        st.subheader("The Sentiment Analysis has been performed on the tweets sent from US Vice President, Kamala Harris's Twitter Account recently.")
        
        st.write("1. Displays the Sentiment Distribution of Vice President Kamala Harris's Tweets")
        st.write("2. Generates a wordcloud for all the Tweets")
        st.write("3. Displays the Most Frequent Words used in all the Tweets")
        
        Analyzer_choice1 = st.selectbox("Select the Option",  ["Display the Sentiment Distribution of Vice President Kamala Harris's Tweets","Generate a wordcloud for all the Tweets","Display the Most Frequent Words used in all the Tweets"])
        
        if st.button("Analyze"):
                
            if Analyzer_choice1 == "Display the Sentiment Distribution of Vice President Kamala Harris's Tweets":                                                      
                
                st.write("Sentiment Distribution of the Tweets")                                                  
                st.image(image21, height = 1000, width = 1000)
                    
            elif Analyzer_choice1 == "Generate a wordcloud for all the Tweets":                                                      
                
                st.write("WordCloud for All the Tweets")                                                  
                st.image(image22, height = 1000, width = 1000)              
                    
            else:                                                      
                
                st.write("Most Frequent Words used in All the Tweets")                                                  
                st.image(image23, height = 1000, width = 1000)
        
        st.write("4. Generates a wordcloud for the Positive Tweets")            
        st.write("5. Displays the Most Frequent Words used in the Positive Tweets")
            
        Analyzer_choice2 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Positive Tweets", "Display the Most Frequent Words used in the Positive Tweets"])

        if st.button("Analyze."):        
                    
            if Analyzer_choice2 == "Generate a wordcloud for the Positive Tweets":                                                      
                
                st.write("WordCloud for All the Positive Tweets")                                                  
                st.image(image24, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Positive Tweets")                                                  
                st.image(image25, height = 1000, width = 1000)                
        
        st.write("6. Generates a wordcloud for the Neutral Tweets")            
        st.write("7. Displays the Most Frequent Words used in the Neutral Tweets")
            
        Analyzer_choice3 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Neutral Tweets", "Display the Most Frequent Words used in the Neutral Tweets"])

        if st.button("Analyze "): 
                    
            if Analyzer_choice3 == "Generate a wordcloud for the Neutral Tweets":                                                      
                
                st.write("WordCloud for All the Neutral Tweets")                                                  
                st.image(image26, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Neutral Tweets")                                                  
                st.image(image27, height = 1000, width = 1000)
                         
        
    elif Candidate_choice == "New Zealand PM Jacinda Ardern":
        
        st.subheader("Jacinda Ardern - Prime Minister of New Zealand")
        st.image(imagew2, height = 500, width = 500)

        st.subheader("The Sentiment Analysis has been performed on the tweets sent from Prime Minister of New Zealand, Jacinda Ardern's Twitter Account recently.")
        
        st.write("1. Displays the Sentiment Distribution of New Zealand Prime Minister Jacinda Ardern's Tweets")
        st.write("2. Generates a wordcloud for all the Tweets")
        st.write("3. Displays the Most Frequent Words used in all the Tweets")
        
        Analyzer_choice1 = st.selectbox("Select the Option",  ["Display the Sentiment Distribution of New Zealand Prime Minister Jacinda Ardern's Tweets","Generate a wordcloud for all the Tweets","Display the Most Frequent Words used in all the Tweets"])
                                                                                 
        if st.button("Analyze"):
                
            if Analyzer_choice1 == "Display the Sentiment Distribution of New Zealand Prime Minister Jacinda Ardern's Tweets":                                                      
                
                st.write("Sentiment Distribution of the Tweets")                                                  
                st.image(image31, height = 1000, width = 1000)
                    
            elif Analyzer_choice1 == "Generate a wordcloud for all the Tweets":                                                      
                
                st.write("WordCloud for All the Tweets")                                                  
                st.image(image32, height = 1000, width = 1000)              
                    
            else:                                                      
                
                st.write("Most Frequent Words used in All the Tweets")                                                  
                st.image(image33, height = 1000, width = 1000)
        
        st.write("4. Generates a wordcloud for the Positive Tweets")            
        st.write("5. Displays the Most Frequent Words used in the Positive Tweets")
            
        Analyzer_choice2 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Positive Tweets", "Display the Most Frequent Words used in the Positive Tweets"])
                                                                       
        if st.button("Analyze."):        
                    
            if Analyzer_choice2 == "Generate a wordcloud for the Positive Tweets":                                                      
                
                st.write("WordCloud for All the Positive Tweets")                                                  
                st.image(image34, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Positive Tweets")                                                  
                st.image(image35, height = 1000, width = 1000)                
        
        st.write("6. Generates a wordcloud for the Neutral Tweets")            
        st.write("7. Displays the Most Frequent Words used in the Neutral Tweets")
            
        Analyzer_choice3 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Neutral Tweets", "Display the Most Frequent Words used in the Neutral Tweets"])
                                                                                  
        if st.button("Analyze "): 
                    
            if Analyzer_choice3 == "Generate a wordcloud for the Neutral Tweets":                                                      
                
                st.write("WordCloud for All the Neutral Tweets")                                                  
                st.image(image36, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Neutral Tweets")                                                  
                st.image(image37, height = 1000, width = 1000)
        
        st.write("8. Generates a wordcloud for the Negative Tweets")            
        st.write("9. Displays the Most Frequent Words used in the Negative Tweets")
            
        Analyzer_choice4 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Negative Tweets", "Display the Most Frequent Words used in the Negative Tweets"])
                
        if st.button("Analyze  "):       
                    
            if Analyzer_choice4 == "Generate a wordcloud for the Negative Tweets":                                                      
                                                                  
                st.write("WordCloud for All the Negative Tweets")
                st.image(image38, height = 1000, width = 1000)
                    
            else:                                                      
                                                                  
                st.write("Most Frequent Words used in the Negative Tweets")
                st.image(image39, height = 1000, width = 1000)
                
    elif Candidate_choice == "United Kingdom PM Boris Johnson":
         
        st.subheader("Boris Johnson - Prime Minister of United Kingdom")
        st.image(imagew3, height = 500, width = 500)
        st.subheader("The Sentiment Analysis has been performed on the tweets sent from Prime Minister of United Kingdom, Boris Johnson's Twitter Account recently.")
        
        st.write("1. Displays the Sentiment Distribution of UK Prime Minister Boris Johnson's Tweets")
        st.write("2. Generates a wordcloud for all the Tweets")
        st.write("3. Displays the Most Frequent Words used in all the Tweets")
        
        Analyzer_choice1 = st.selectbox("Select the Option",  ["Display the Sentiment Distribution of UK Prime Minister Boris Johnson's Tweets","Generate a wordcloud for all the Tweets","Display the Most Frequent Words used in all the Tweets"]) 
        
        if st.button("Analyze"):
                
            if Analyzer_choice1 == "Display the Sentiment Distribution of UK Prime Minister Boris Johnson's Tweets":                                                      
                
                st.write("Sentiment Distribution of the Tweets")                                                  
                st.image(image41, height = 1000, width = 1000)
                    
            elif Analyzer_choice1 == "Generate a wordcloud for all the Tweets":                                                      
                
                st.write("WordCloud for All the Tweets")                                                  
                st.image(image42, height = 1000, width = 1000)              
                    
            else:                                                      
                
                st.write("Most Frequent Words used in All the Tweets")                                                  
                st.image(image43, height = 1000, width = 1000)
        
        st.write("4. Generates a wordcloud for the Positive Tweets")            
        st.write("5. Displays the Most Frequent Words used in the Positive Tweets")
            
        Analyzer_choice2 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Positive Tweets", "Display the Most Frequent Words used in the Positive Tweets"])
                                                                           
        if st.button("Analyze."):        
                    
            if Analyzer_choice2 == "Generate a wordcloud for the Positive Tweets":                                                      
                
                st.write("WordCloud for All the Positive Tweets")                                                  
                st.image(image44, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Positive Tweets")                                                  
                st.image(image45, height = 1000, width = 1000)                
        
        st.write("6. Generates a wordcloud for the Neutral Tweets")            
        st.write("7. Displays the Most Frequent Words used in the Neutral Tweets")
            
        Analyzer_choice3 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Neutral Tweets", "Display the Most Frequent Words used in the Neutral Tweets"])
                                                                                  
        if st.button("Analyze "): 
                    
            if Analyzer_choice3 == "Generate a wordcloud for the Neutral Tweets":                                                      
                
                st.write("WordCloud for All the Neutral Tweets")                                                  
                st.image(image46, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Neutral Tweets")                                                  
                st.image(image47, height = 1000, width = 1000)
        
        st.write("8. Generates a wordcloud for the Negative Tweets")            
        st.write("9. Displays the Most Frequent Words used in the Negative Tweets")
            
        Analyzer_choice4 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Negative Tweets", "Display the Most Frequent Words used in the Negative Tweets"])
                
        if st.button("Analyze  "):       
                    
            if Analyzer_choice4 == "Generate a wordcloud for the Negative Tweets":                                                      
                                                                  
                st.write("WordCloud for All the Negative Tweets")
                st.image(image48, height = 1000, width = 1000)
                    
            else:                                                      
                                                                  
                st.write("Most Frequent Words used in the Negative Tweets")
                st.image(image49, height = 1000, width = 1000)
    
    else:
                
        st.subheader("Scott Morrison - Prime Minister of Australia")
        st.image(imagew4, height = 600, width = 600)
        st.subheader("The Sentiment Analysis has been performed on the tweets sent from Prime Minister of Australia, Scott Morrison's Twitter Account recently.")
        
        st.write("1. Displays the Sentiment Distribution of Australia Prime Minister Scott Morrison's Tweets")
        st.write("2. Generates a wordcloud for all the Tweets")
        st.write("3. Displays the Most Frequent Words used in all the Tweets")
        
        Analyzer_choice1 = st.selectbox("Select the Option",  ["Display the Sentiment Distribution of Australia Prime Minister Scott Morrison's Tweets","Generate a wordcloud for all the Tweets","Display the Most Frequent Words used in all the Tweets"])
        
        if st.button("Analyze"):
                
            if Analyzer_choice1 == "Display the Sentiment Distribution of Australia Prime Minister Scott Morrison's Tweets":                                                      
                
                st.write("Sentiment Distribution of the Tweets")                                                  
                st.image(image51, height = 1000, width = 1000)
                    
            elif Analyzer_choice1 == "Generate a wordcloud for all the Tweets":                                                      
                
                st.write("WordCloud for All the Tweets")                                                  
                st.image(image52, height = 1000, width = 1000)              
                    
            else:                                                      
                
                st.write("Most Frequent Words used in All the Tweets")                                                  
                st.image(image53, height = 1000, width = 1000)
        
        st.write("4. Generates a wordcloud for the Positive Tweets")            
        st.write("5. Displays the Most Frequent Words used in the Positive Tweets")
            
        Analyzer_choice2 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Positive Tweets", "Display the Most Frequent Words used in the Positive Tweets"])
                                                                          
        if st.button("Analyze."):        
                    
            if Analyzer_choice2 == "Generate a wordcloud for the Positive Tweets":                                                      
                
                st.write("WordCloud for All the Positive Tweets")                                                  
                st.image(image54, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Positive Tweets")                                                  
                st.image(image55, height = 1000, width = 1000)                
        
        st.write("6. Generates a wordcloud for the Neutral Tweets")            
        st.write("7. Displays the Most Frequent Words used in the Neutral Tweets")
            
        Analyzer_choice3 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Neutral Tweets", "Display the Most Frequent Words used in the Neutral Tweets"])

        if st.button("Analyze "): 
                    
            if Analyzer_choice3 == "Generate a wordcloud for the Neutral Tweets":                                                      
                
                st.write("WordCloud for All the Neutral Tweets")                                                  
                st.image(image56, height = 1000, width = 1000)
                    
            else:                                                     
                
                st.write("Most Frequent Words used in the Neutral Tweets")                                                  
                st.image(image57, height = 1000, width = 1000)
        
        st.write("8. Generates a wordcloud for the Negative Tweets")            
        st.write("9. Displays the Most Frequent Words used in the Negative Tweets")
            
        Analyzer_choice4 = st.selectbox("Select the Option",  ["Generate a wordcloud for the Negative Tweets", "Display the Most Frequent Words used in the Negative Tweets"])
                
        if st.button("Analyze  "):       
                    
            if Analyzer_choice4 == "Generate a wordcloud for the Negative Tweets":                                                      
                                                                  
                st.write("WordCloud for All the Negative Tweets")
                st.image(image58, height = 1000, width = 1000)
                    
            else:                                                      
                                                                  
                st.write("Most Frequent Words used in the Negative Tweets")
                st.image(image59, height = 1000, width = 1000)

"""
    st.code(code, language='python')


st.sidebar.title("Created By:")
st.sidebar.subheader("Ashutosh Shinde")
st.sidebar.subheader("[LinkedIn Profile](https://www.linkedin.com/in/ashutoshashinde/)")
st.sidebar.subheader("[GitHub Repository](https://github.com/AshutoshAShinde/World-Leaders-Twitter-Analysis-Data-App)")       
    
                      
         