import streamlit as st
import pandas as pd
from datetime import date
import datetime

df = pd.DataFrame()
st.markdown("# Let's Count Dates from Days!")
st.write ("The following will give you period dates based on defined alloted date intervals")

if "submitted" not in st.session_state:
    st.session_state.submitted = False
    
#create a form to avoid rerun based on changes in user input 
with st.form(key='find_date_form'):
    begin_date = st.date_input ("Pick a beginning date", date.today(), key='begin_date')
    end_date = st.date_input("Pick a end date", date.today(), key='end_date')
    diff_date = begin_date - end_date

    interval_date = st.number_input("Enter Interval Days", step=1)
    delta = datetime.timedelta(days=interval_date)
    delta_less = datetime.timedelta(days=interval_date-1)

    count_days = ((end_date-begin_date).days)
    print (begin_date + delta)


    submit = st.form_submit_button("Submit")
    
    if submit or st.session_state.submitted:
        
        if begin_date < end_date and interval_date > 0 and count_days > interval_date:
            st.session_state.submitted = True
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
                   
                    break

        else:
            st.error ('Invalid Input, Try Again')

if not df.empty: 
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')
    csv = convert_df(df)
    st.table(df)
    st.session_state.submitted = True

    st.download_button(label="Download data as CSV", data=csv,
        file_name='calendar_table.csv',
        mime='text/csv', )

    
    


    


