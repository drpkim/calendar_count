import streamlit as st
import re 

#create a session state for QR image to remain upon download
if "submitted" not in st.session_state:
    st.session_state.submitted = False

#Regex to catch validation errors
phone_format = r"^[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4}$"
zip_format = "^[0-9]{5}(?:-[0-9]{4})?$"
email_format = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
url_format = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

#US state list
states = ['', 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

st.markdown('## Create QR Business VCard for iPhone and Android Contact')
st.write('This will produce a QR code in VCard format')

#title
profession_degree = ["DO", "MPH", "MD", "PhD"]


#better error check
def check_valid():
    st.session_state.submitted = True
    for k, v in st.session_state.items():
        if k == 'Address':
            if st.session_state[k]:
                if not st.session_state['City']:
                    st.session_state.submitted = False
                    st.error(f"Missing Address values: City")
                if not st.session_state['State']:
                    st.session_state.submitted = False
                    st.error(f"Missing Address values: State")
                if not st.session_state['Zip']:
                    st.session_state.submitted = False
                    st.error(f"Missing Address values: Zip")
                elif not re.match(zip_format, st.session_state['Zip']):
                    st.session_state.submitted = False
                    st.error(f"Incorrect Format: Zip")
                break         
        if k == 'City':
            if st.session_state[k]:
                if not st.session_state['Address']:
                    st.session_state.submitted = False
                    st.error(f"Missing Address values: Address")
                if not st.session_state['State']:
                    st.session_state.submitted = False
                    st.error(f"Missing Address values: State")
                if not st.session_state['Zip']:
                    st.session_state.submitted = False
                    st.error(f"Missing Address values: Zip")
                elif not re.match(zip_format, st.session_state['Zip']):
                    st.session_state.submitted = False
                    st.error(f"Incorrect Format: Zip")
                break             
        if k == 'State':
            if st.session_state[k]:
                if not st.session_state['Address']:
                    st.session_state.submitted = False
                    st.error(f"Missing Address values: Address")
                if not st.session_state['City']:
                    st.session_state.submitted = False
                    st.error(f"Missing Address values: City")
                if not st.session_state['Zip']:
                    st.session_state.submitted = False
                    st.error(f"Missing Address values: Zip")
                elif not re.match(zip_format, st.session_state['Zip']):
                    st.session_state.submitted = False
                    st.error(f"Incorrect Format: Zip")
                break
        if k == 'Zip':
            if st.session_state[k]: 
                if not re.match(zip_format, st.session_state[k]):
                    st.session_state.submitted = False
                    st.error(f"Incorrect Format: {k}")
                if not st.session_state['City']:
                    st.session_state.submitted = False
                    st.error(f"Missing Address values: City")
                if not st.session_state['State']:
                    st.session_state.submitted = False
                    st.error(f"Missing Address values: State")
                if not st.session_state['Address']:
                    st.session_state.submitted = False
                    st.error(f"Missing Address values: Address")
                break
    for k, v in st.session_state.items():
        if k == 'Cell':
            if st.session_state[k]:
                if not re.match(phone_format, st.session_state[k]):
                    st.session_state.submitted = False
                    st.error(f"Incorrect Number Format: {k}")
        if k == 'Work':
              if st.session_state[k]:
                if not re.match(phone_format, st.session_state[k]):
                    st.session_state.submitted = False
                    st.error(f"Incorrect Number Format: {k}")
        if k == 'Fax':
              if st.session_state[k]:
                if not re.match(phone_format, st.session_state[k]):
                    st.session_state.submitted = False
                    st.error(f"Incorrect Number Format: {k}")
        

    if not st.session_state['First']:
        st.session_state.submitted = False
        st.error(f"Missing Required Value: First")
    if not st.session_state['Last']:
        st.session_state.submitted = False
        st.error(f"Missing Required Value: Last")        
            
    if not st.session_state['Email']:
        st.session_state.submitted = False
        st.error(f"Missing Required Value: Email")
    if st.session_state['Email']:
        if not re.match(email_format, st.session_state['Email']):
            st.session_state.submitted = False
            st.error(f"Incorrect Email Format")
  
    if st.session_state['Website']:
        if not re.match(url_format, st.session_state['Website']):
            st.session_state.submitted = False
            st.error(f"Incorrect URL Format")
            



 
    
    

        
    
                


#form Error check function
def check_error():
    st.session_state.submitted = True
    mykeylist = ['First', 'Last']
    numbers = ['Cell', 'Work', 'Work_Fax']
    address = ['Address', 'City', 'Zip']
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
    if st.session_state.Address or st.session_state.City or st.session_state.State or st.session_state.Zip:
        for a in address:
            if not st.session_state[a]:
                st.session_state.submitted = False
                st.error(f"Missing Address Field: {a}")
    # if not re.match(zip_format, st.session_state['Zip']):
    #     st.session_state.submitted = False
    #     st.error(f"Incorrect Format: Zip")       

    if not st.session_state.Email:
        st.session_state.submitted = False
        st.error("Missing Email")
    elif not re.match(email_format, st.session_state.Email):
        st.session_state.submitted = False
        st.error("Incorrect email address format")

    if st.session_state.Website:
        if not re.match(url_format, st.session_state.Website): 
            st.session_state.submitted = False
            st.error("Incorrect URL Format")

    
    
        
                

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
    personal_cell = st.text_input("Cell Number", key='Cell', help='US Number Format (xxx)xxx-xxxxx')
    work_phone = st.text_input("Work Number", key='Work')
    work_fax = st.text_input("Work Fax", key='Fax')

    business_add = st.text_input("Business Address", key='Address')
    add1, add2, add3 = st.columns([4, 2, 4])
    with add1:
        city = st.text_input("City", key='City')
    with add2:
        state = st.selectbox("State", (states), key='State')
    with add3:
        zip_code = st.text_input("Zip", key='Zip')

    email = st.text_input("Email*", key='Email')
    website = st.text_input("Website", key='Website')


    submit = st.form_submit_button("Create VCard", on_click=check_valid)

    if st.session_state.submitted and submit:
        st.write('valid')

        st.write(first_name, last_name, ", ".join(degree))
        

##Sample Write output          
st.write (st.session_state["First"])
for item in st.session_state.items():
    st.write(item)
