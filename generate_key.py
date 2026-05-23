import streamlit_authenticator as stauth

hashed_password = stauth.Hasher.hash("abc123")

print(hashed_password)