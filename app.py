import streamlit as st
import database as db
import mailer
st.set_page_config(page_title="Bulk email sender", layout="wide", page_icon="📮")
db.create_database()
st.title("BULK EMAIL SENDER APP",text_alignment="center")
st.markdown("---")

left_col, right_col = st.columns(2, gap="large")

with left_col:
    st.header("Manage Recipients")
    with st.form("add_email_form", clear_on_submit=True):
        new_name = st.text_input("Enter your name", placeholder="ledger phonix")
        new_email = st.text_input("Enter your email", placeholder="username@example.com")
        submit_btn = st.form_submit_button("Add Email")
        if submit_btn:
            success, message = db.add_email(new_name , new_email)
            if success:
                st.toast(message)
            else:
                st.error(message)

    st.markdown("---")
    st.markdown("### Existing Recipients")
    emails_list = db.get_all_emails()
    
    if emails_list:
        # 1. Dropdown to pick the email
        selected_email = st.selectbox("Select an email:", emails_list)
        
        # 2. Simple Delete Button directly underneath
        if st.button("🗑️ Delete Selected Email", type="primary", use_container_width=True):
            success, message = db.delete_email(selected_email)
            if success:
                st.toast(message, duration= 5)
                # st.rerun()  # Refreshes page to instantly update the list
            else:
                st.error(message)
    else:
        st.info("No emails found in the database yet.")
        
with right_col:
    st.header("Bulk Email Sender 📤")
    with st.expander("SMTP Server Setting", expanded=False):
        smtp_server = st.text_input("SMTP Server", value="smtp.gmail.com")
        smtp_port = st.number_input("PORT", value=587)
        sender_email = st.text_input("Sender Email")
        sender_password = st.text_input("Sender App Password", type="password", help="Use app password not regular password!")
       
    #email content composition
    subject = st.text_input("Subject line:", placeholder="Enter email subject...") 
    body = st.text_area("Email Body:", placeholder="Type your message here...", height=150)
    upload_file = st.file_uploader("Attach a file (optional)", type=None)   
    st.markdown("---")
    send_btn = st.button("🚀 Send to All Existing Emails", use_container_width=True)
    if send_btn:
        if not sender_email or not sender_password:
            st.warning("Please fill out SMTP setting first")
        elif not subject or not body:
            st.warning("Please fill out both subject and body.")    
        else:
            all_recipients = db.get_all_emails()
            with st.spinner("Dispatching Emails..."):
                status , msg = mailer.send_bulk_email(
                    smtp_server = smtp_server,
                    smtp_port = smtp_port,
                    sender_email = sender_email,
                    sender_password = sender_password,
                    recipients = all_recipients,
                    subject =  subject,
                    body=body,
                    attachment = upload_file
                )   
                if status:
                    st.rerun()
                    st.success(msg)
                    
                else:
                    st.error(msg)    