import streamlit as st
from utils.chatbot import get_response

# --------------------
# Page Config
# --------------------
st.set_page_config(
    page_title="CatGPT",
    page_icon="🐱",
    layout="centered"
)

# --------------------
# Session State
# --------------------
if "gamer_messages" not in st.session_state:
    st.session_state.gamer_messages = []

if "hacker_messages" not in st.session_state:
    st.session_state.hacker_messages = []

# --------------------
# Sidebar
# --------------------
with st.sidebar:

    st.title("🐱 CatGPT")

    st.markdown("### Personality")

    personality_mode = st.toggle(
        "🐱‍💻 Switch Personalities",
        value=False
    )

    if personality_mode:
        st.caption("Current: 🐱‍💻 Hacker Cat")
        current_messages = st.session_state.hacker_messages
        avatar_path = "assets/dark_cat.png"
    else:
        st.caption("Current: 😸 Gamer Cat")
        current_messages = st.session_state.gamer_messages
        avatar_path = "assets/light_cat.png"

    st.divider()

    if st.button("🗑️ Clear Chat"):

        if personality_mode:
            st.session_state.hacker_messages = []
        else:
            st.session_state.gamer_messages = []

        st.rerun()

    st.divider()

    st.markdown("### About")

    st.write(
        "A dual-personality AI avatar chatbot powered by Groq and Streamlit."
    )

    st.divider()

    st.markdown("### Features")

    st.markdown("""
- 😸 Gamer Cat Personality
- 🐱‍💻 Hacker Cat Personality
- 💬 Independent Memory
- ⚡ Groq LLM Backend
- 🎭 Dynamic Avatar
""")

# --------------------
# Main Header
# --------------------
st.title("🐱 CatGPT")

if personality_mode:
    st.markdown("##### 🐱‍💻 Hacker Cat Mode")
else:
    st.markdown("##### 😸 Gamer Cat Mode")

# --------------------
# Main Avatar
# --------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(
        avatar_path,
        width=220
    )

# --------------------
# Welcome Message
# --------------------
if len(current_messages) == 0:

    if personality_mode:
        st.info(
            "🐱‍💻 Connection established. Hacker Cat online."
        )
    else:
        st.info(
            "😸 Gamer Cat online. Ready to queue up!"
        )

# --------------------
# Display Chat History
# --------------------
for message in current_messages:

    if message["role"] == "user":

        with st.chat_message(
            "user",
            avatar="🧑"
        ):
            st.write(message["content"])

    else:

        with st.chat_message(
            "assistant",
            avatar=avatar_path
        ):
            st.write(message["content"])

# --------------------
# Chat Input
# --------------------
prompt = st.chat_input(
    "Talk to CatGPT..."
)

if prompt:

    current_messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message(
        "user",
        avatar="🧑"
    ):
        st.write(prompt)

    with st.spinner("🐾 Cat is thinking..."):

        response = get_response(
            current_messages,
            personality_mode
        )

    current_messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message(
        "assistant",
        avatar=avatar_path
    ):
        st.write(response)