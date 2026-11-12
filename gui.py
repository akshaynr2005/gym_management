import streamlit as st
from datetime import date
from memberview import GymMember

g1 = GymMember()

tab1, tab2 = st.tabs(["Add Member", "View Members"])

# ADD MEMBER
with tab1:

    st.header("Add New Gym Member")

    name = st.text_input("Enter Member Name")
    place = st.text_input("Enter Member Place")

    plan = st.selectbox(
        "Select Membership Plan",
        ("1 month", "3 months", "6 months", "1 year")
    )

    mobile = st.text_input("Enter Mobile Number")
    fee = st.number_input("Enter Membership Fee", min_value=0)

    joining_date = st.date_input("Select Joining Date")

    if st.button("Submit"):

        g1.post(
            name=name,
            place=place,
            plan=plan,
            mobile=mobile,
            fee=fee,
            joining_date=joining_date
        )

        st.success("Member added successfully!")


# VIEW MEMBERS
with tab2:

    st.header("View Gym Member Details")

    records = g1.get()

    if records:

        st.dataframe(
            records,
            use_container_width=True
        )

    else:

        st.warning("No members found!")