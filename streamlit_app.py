import streamlit as st
from google.cloud import firestore
import json

#key_dict = json.loads(st.secrets["textkey"])
#creds = service_account.Credentials.from_service_account_info(key_dict)
#db = firestore.Client(credentials=creds, project="axis_upskill")


db = firestore.Client.from_service_account_json("firestore-key.json")

st.markdown("<h1 style='text-align: center; color: black;'>Axis Upskill Program 💻</h1>", unsafe_allow_html=True)

# You can use a column just like st.sidebar:
add_selectbox = st.sidebar.selectbox(
    "What are you planning to do today?",
    ("Post Something", "Read Analysis")
)

if add_selectbox == 'Post Something':
    # Streamlit widgets to let a user create a new post
    title = st.text_input("Post title 📚")
    name = st.text_input("Name 👀")
    Emp_ID = st.text_input("Employee ID 👷")
    analysis = st.text_input("Analysis ✍ ")
    url = st.text_input("Post url if any 📎")
    if not url:
        st.warning('Please input some value , NA if you do not have any url.')
    submit = st.button("Submit new post 🚩")

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

if add_selectbox == "Read Analysis":
    blg_ref = db.collection("posts")

# For a reference to a collection, we use .stream() instead of .get()
    for doc in blg_ref.stream():
        t2 = doc.to_dict()
        st.write(t2['Name'])
        with st.beta_expander("see the analysis"):
            st.write(t2['Analysis'])
        st.write(t2['Emp_ID'])
        st.write(t2['url'])
