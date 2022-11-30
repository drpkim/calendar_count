import streamlit as st
import re 

phone_format = r"^((\([0-9]{3}\) ?|[0-9]{3}-)[0-9]{3}-[0-9]{4})|[0-9]{10}|^\Z$"

st.markdown('## Create QR Business VCard for iPhone and Android Contact')
st.write('This will produce a QR code in VCard format')

#title
profession_degree = ["DO", "MPH", "MD", "PhD"]
#create a session state for QR image to remain upon download
if "submitted" not in st.session_state:
    st.session_state.submitted = False

#form Error check function
def check_error():
    st.session_state.submitted = True
    mykeylist = ['First', 'Last']
    numbers = ['Cell', 'Work', 'Work_Fax']
    for mykey in mykeylist:
        if not st.session_state[mykey]:
            st.session_state.submitted = False
            st.error(f"Missing Value: {mykey}")
        elif not re.match(r'^[a-zA-Z\s]+$', st.session_state[mykey].strip()):
            st.session_state.submitted = False
            st.error(f"No numerics allowed: {mykey}")
    for number in numbers:
        if not re.match(phone_format, st.session_state[number]):
            st.session_state.submitted = False
            st.error(f"Incorrect Number Format: {number}")
        

        

with st.form('contact_info'):
    st.markdown("###### *Denotes Required")
    col1, bra, col2 = st.columns([3,1,3])
    with col1:
        first_name = st.text_input("First*", key="First").capitalize()
    with col2:
        last_name = st.text_input("Last*", key="Last").capitalize()
    
    degree = st.multiselect("Professional Degree(s)", options=profession_degree)
    title = st.text_input("Enter Occupation Title")
    org = st.text_input("Organization")
    personal_cell = st.text_input("Cell Number", key='Cell', help='US Number Format')
    work_phone = st.text_input("Work Number", key='Work')
    work_fax = st.text_input("Work Fax", key='Work_Fax')

    business_add = st.text_input("Business Address")
    add1, add2, add3 = st.columns([4, 2, 4])
    with add1:
        city = st.text_input("City")
    with add2:
        state = st.selectbox("State", ("", "CA", "MS", "AK"), key='State')
    with add3:
        zip_code = st.text_input("Zip")

    email = st.text_input("Email", key='Email')
    website = st.text_input("Website", key='Website')


    submit = st.form_submit_button("Create VCard", on_click=check_error)

    if st.session_state.submitted and submit:
        st.write('valid')

        st.write(first_name, last_name, ", ".join(degree))
        

##Sample Write output          
st.write (st.session_state["First"])
for item in st.session_state.items():
    st.write(item)
