import streamlit as st
from Views.AddState import AddState
from Views.DisplayStates import DisplayStates
from Views.Login import Login
from API import API
import extra_streamlit_components as stx
import json
from streamlit_option_menu import option_menu

cookie_manager = stx.CookieManager()
cookies = cookie_manager.get_all()
authentication_token = cookies.get("token") if type(cookies) == dict else cookies

api = API("http://127.0.0.1:8000/api", authentication_token)


def manage_login(username, password):
    token = api.login(username, password)
    cookie_manager.set("token", token)
    return token is not None


#st.title("Voter CRM Admin Portal")

if api.is_logged_in():
    #st.subheader("Welcome")
    #st.write("______________")
    #AddState(api.add_state)
    #st.write("___________")
    #DisplayStates(api.get_states)'''
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Add State", "Display States"]
        )

    if selected == "Add State":
        AddState(api.add_state)
        #st.title("you have selected Add State")
    if selected == "Display States":
        #st.title("you have selected Display states")
        DisplayStates(api.get_states)


else:
    Login(manage_login)
