import streamlit as st
import joblib
import string

# Load the trained model and the TF-IDF vectorizer
try:
    model = joblib.load('model.pkl')
    tfidf_vectorizer = joblib.load('vectorizer.pkl')
except FileNotFoundError:
    st.error("Model or vectorizer files not found.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the files: {e}")
    st.stop()

# Function to make predictions
def predict_news(text):
    """
    Takes a string of news text and returns the prediction.
    """
    # Pre-process and vectorize the input text using the loaded vectorizer
    text_vectorized = tfidf_vectorizer.transform([text])
    
    # Predict using the loaded model
    prediction = model.predict(text_vectorized)[0]
    
    # Return the prediction label
    return "REAL NEWS" if prediction == 1 else "FAKE NEWS"

# --- Streamlit App Interface ---

# Set the title and a small description
st.set_page_config(page_title="Fake News Detector", page_icon="📰")
st.title("📰 Fake News Detector")
st.write(
    "Enter a news article or text below to determine whether it is likely to be real or fake. "
    "The model uses a Passive-Aggressive Classifier trained on a public dataset."
)

# Text area for user input
user_input = st.text_area(
    "Enter the news text here:",
    height=250,
    placeholder="Type or paste your news article here..."
)

# Prediction button
if st.button("Analyze News"):
    if user_input.strip():
        # If there is input, make a prediction
        with st.spinner('Analyzing...'):
            prediction = predict_news(user_input)
        
        st.subheader("Analysis Result")
        if prediction == "REAL NEWS":
            st.success(f"Prediction: *{prediction}*")
            st.markdown("This article appears to be genuine based on the analysis.")
        else:
            st.error(f"Prediction: *{prediction}*")
            st.markdown("This article shows characteristics of fake news. Please verify the source.")
    else:
        # If the input is empty
        st.warning("Please enter some text to analyze.")

# Add a sidebar with more information
st.sidebar.header("About the App")
st.sidebar.info(
    "This web application leverages a machine learning model to classify news articles. "
    "It uses a TF-IDF Vectorizer to process the text and a Passive-Aggressive Classifier "
    "to make the final prediction."
)
st.sidebar.header("How to Use")
st.sidebar.markdown(
    """
    1.  *Enter Text*: Paste or type the news article text into the text box.
    2.  *Analyze*: Click the 'Analyze News' button.
    3.  *Get Result*: The model will predict if the news is REAL or FAKE.
    """

)
