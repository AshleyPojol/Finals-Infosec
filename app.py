import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))

model = pickle.load(open('model.pkl', 'rb'))

st.title("Spam Message Classifier")
st.caption("Group Name: AlaskaBears")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("SPAM Message Detected")
    else:
        st.header("NO SPAM Message Detected")

st.caption("Archog, Berbon, Mendoza, Pojol, Sarong")
st.markdown(
    "This module will let the system determine if the email content is a spam, and the user will determine if it is a phishing email but taking into consideration the criteria below:")
st.divider()
st.subheader("Mimicking Legitimate Sources")
st.caption("Phishing emails often impersonate trusted sources, such as banks, social media platforms, or government agencies, to trick recipients into believing the message is legitimate.")
st.subheader("Urgency or Threat")
st.caption("Phishing emails often create a sense of urgency or threat to prompt immediate action, such as claiming that an account will be suspended unless the recipient provides certain information.")
st.subheader("Request for Sensitive Information")
st.caption("Phishing emails typically request sensitive information, such as passwords, credit card numbers, or personal identification details.")
st.subheader("Mismatched URLs")
st.caption("Phishing emails often contain links that, when hovered over, do not match the claimed source. These malicious links direct recipients to fake websites designed to steal their information.")
st.subheader("Spelling and Grammar Errors")
st.caption("While not always the case, many phishing emails contain spelling and grammar mistakes, indicating a lack of professionalism.")
st.subheader("Unexpected Attachments or Downloads")
st.caption("Phishing emails might include unexpected attachments or downloads, which, when opened, can install malware on the recipient's device.")


st.divider()


