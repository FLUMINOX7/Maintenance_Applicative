import streamlit as st

if not st.session_state.get("authenticated"):
    st.switch_page("app.py")

# Stockage des tâches en mémoire (disparaît si on relance l'app)
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

st.title("Ma TodoList")

col1, col2 = st.columns([0.8, 0.2])
with col2:
    if st.button("Se déconnecter"):
        st.session_state["authenticated"] = False
        st.session_state.pop("username", None)
        st.session_state.pop("tasks", None)
        st.switch_page("app.py")

with st.form("add_task_form"):
    new_task = st.text_input("Ajouter une tâche")
    add_task = st.form_submit_button("Ajouter")

if add_task and new_task.strip() != "":
    st.session_state["tasks"].append({"task": new_task.strip(), "done": False})
    st.rerun()

st.subheader("Liste des tâches")

if not st.session_state["tasks"]:
    st.info("Aucune tâche pour le moment.")

for i, task in enumerate(st.session_state["tasks"]):
    left_column, right_column = st.columns([0.8, 0.2])
    with left_column:
        st.write(("Terminé - " if task["done"] else "À faire - ") + task["task"])
    with right_column:
        if not task["done"] and st.button("Marquer comme fait", key=f"done_{i}"):
            st.session_state["tasks"][i]["done"] = True
            st.rerun()