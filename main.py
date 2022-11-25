import streamlit as st
import pandas as pd
from datetime import date
import datetime

st.markdown("# Let's Count Dates from Days!")
st.write ("The following will give you dates based on defined alloted date intervals")

#create a form to avoid rerun based on changes in user input 

with st.form(key='find_date_form'):
    begin_date = st.date_input ("Pick a beginning date", date.today())
    end_date = st.date_input("Pick a end date", date.today())
    
    print (begin_date)
    print (end_date)

    interval_date = st.number_input("Enter Interval Days", step=1)
    delta = datetime.timedelta(days=interval_date)
    delta_less = datetime.timedelta(days=interval_date-1)

    submit = st.form_submit_button("Submit")

    if submit:
        if begin_date < end_date and interval_date > 0:
            start_count = begin_date
            column_a = []
            column_b = []
            while start_count <= end_date: 
                column_a.append(start_count)
                column_b.append(start_count + delta_less)
                start_count += delta
                if start_count + delta > end_date:
                    df= pd.DataFrame({
                        'Start Date': column_a,
                        'End Date': column_b
                    })
                    df.index += 1
                    df['Start Date'] = pd.to_datetime(df['Start Date'], format='%Y-%m-%d').dt.strftime('%m/%d/%Y')
                    df['End Date'] = pd.to_datetime(df['End Date'], format='%Y-%m-%d').dt.strftime('%m/%d/%Y')
                    st.table(df)
                    break

        else:
            st.error ('Invalid Input, Try Again')


