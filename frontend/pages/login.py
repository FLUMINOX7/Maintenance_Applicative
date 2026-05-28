import streamlit as st

VALID_USERNAME = "admin"
VALID_PASSWORD = "admin123"


def go_to_todolist() -> None:
	st.switch_page("pages/todolist.py")


if st.session_state.get("authenticated"):
	go_to_todolist()

st.title("Connexion")
st.caption("Connecte-toi pour accéder à la todolist.")

with st.form("login_form"):
	username = st.text_input("Nom d'utilisateur")
	password = st.text_input("Mot de passe", type="password")
	submitted = st.form_submit_button("Se connecter")

if submitted:
	if username == VALID_USERNAME and password == VALID_PASSWORD:
		st.session_state["authenticated"] = True
		st.session_state["username"] = username
		go_to_todolist()
	else:
		st.error("Nom d'utilisateur ou mot de passe incorrect.")