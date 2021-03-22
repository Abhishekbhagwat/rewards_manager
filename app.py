import streamlit as st
import pandas as pd

awards = ['Employee of the Month', 'Best Teammate', 'Creative Genius', 'Customer King / Queen', 'Greatest of all Time (GOAT)']
df =  pd.read_csv('data/dataset_new.csv')
awards_db = pd.DataFrame([{'Employee_Name': 'test_name', 'Department': 'test_department', 'Award': 'test_award', 'Reason': 'test_reason'}])


# st.title('Hi, from Leaderboard')

# st.header('Nomination Tab')
# st.text('Do a good deed and award your colleagues for a job well done \n\n')

# df =  pd.read_csv('data/dataset_new.csv')

# dpt_list = st.multiselect('Which department(s) does your colleague(s) work at ?', df.Department.unique().tolist())

# nominated_colleagues = st.multiselect('Choose the colleague(s) you want to nominate', df.query('Department in @dpt_list').Employee_Name.unique().tolist())


# nominated_awards = st.multiselect('Choose which award you want to give', awards)

# award_reason = st.text_input('Add a message and wish them well! ')


def get_employee_department(colleague):
    emp_dept = df.query('Employee_Name == @colleague').Department.item().strip()
    return emp_dept

def add_records(nominated_colleagues, nominated_awards, award_reason):    
    for colleague in nominated_colleagues:
        for award in nominated_awards:
            dept = get_employee_department(colleague)
            print(colleague, award, award_reason)

            if awards_db.empty == True:
                pass
            else:
                print(awards_db)


if __name__ == '__main__':
    st.title('Hi, from Leaderboard')
    st.header('Nomination Tab')
    st.text('Do a good deed and award your colleagues for a job well done \n\n')
    dpt_list = st.multiselect('Which department(s) does your colleague(s) work at ?', df.Department.unique().tolist())
    nominated_colleagues = st.multiselect('Choose the colleague(s) you want to nominate', df.query('Department in @dpt_list').Employee_Name.unique().tolist())
    nominated_awards = st.multiselect('Choose which award you want to give', awards)
    award_reason = st.text_input('Add a message and wish them well!')

    for colleague in nominated_colleagues:
        for award in nominated_awards:
            dept = get_employee_department(colleague)
            print(type(colleague), type(award), type(award_reason))

            if awards_db.empty == True:
                pass
            else:
                print(awards_db)
        # st.success('Thank you for awarding your colleagues! Keep up the good work')
                row = {'Employee_Name': colleague, 'Department': dept, 'Award': award, 'Reason': award_reason}
                awards_db = awards_db.append(row, ignore_index=True)

    # print(awards_db)
    st.write('\n \n')
    st.title('Hall of Fame')
    st.write(awards_db)