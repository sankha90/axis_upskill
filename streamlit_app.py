import streamlit as st
from google.cloud import firestore
import json

#key_dict = json.loads(st.secrets["textkey"])
#creds = service_account.Credentials.from_service_account_info(key_dict)
#db = firestore.Client(credentials=creds, project="axis_upskill")


db = firestore.Client.from_service_account_json("firestore-key.json")

st.markdown("<h1 style='text-align: center; color: black;'>Axis Tech-Know Transfer 💻</h1>","<h1 style='text-align: center; color: black;'>Axis Tech-Know Transfer 💻</h1>" unsafe_allow_html=True)

# You can use a column just like st.sidebar:


add_selectbox = st.sidebar.selectbox(
    "What are you planning to do today?",
    ("Write Something", "Read Something")
)

st.sidebar.markdown('[![Saiteja Kura]\
                    (https://img.shields.io/badge/Made%20with-Python-red)]\
                    (https://python.org)')


if add_selectbox == 'Write Something':
    # Streamlit widgets to let a user create a new post
    title = st.text_input("What's it about 📚")
    name = st.text_input("What do we call you 👀")
    Emp_ID = st.text_input("Your unique identifer , employee id , duh!! 👷")
    url = st.text_input("Anywhere else we can visit 🔖 if you dont have any url to share , please enter NA.")
    analysis = st.text_input("Cant wait to hear your thoughts ✍ ")
#
#    if not url:
#        st.warning('if you dont have any url to share , please enter NA.')
    submit = st.button("Submit 🚩")

    # Once the user has submitted, upload it to the database
    if title and name and Emp_ID and analysis and url and submit:
	    doc_ref = db.collection("posts").document(title)
	    doc_ref.set({
		    "title": title,
            "Name" : name,
            "Emp_ID" : Emp_ID,
            "Analysis" : analysis,
		    "url": url
	    })

if add_selectbox == "Read Something":
    blg_ref = db.collection("posts")

# For a reference to a collection, we use .stream() instead of .get()
    for doc in blg_ref.stream():
        t2 = doc.to_dict()
        st.write(t2['Name'])
        with st.beta_expander("Expand to see what's beyond 🕵️‍♂️"):
            st.write(t2['Analysis'])
        st.write(t2['Emp_ID'])
        st.write(t2['url'])
        st.markdown("---")
