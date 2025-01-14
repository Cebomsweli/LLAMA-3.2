import streamlit as st
from langchain_ollama import OllamaLLM  # Imported from Ollama
from langchain_core.prompts import ChatPromptTemplate  # To easily assemble chats


# Initialize model
model = OllamaLLM(model="llama3.2")  # The model you are working with

# Define template for conversation
template = """
Answer the question below.

Here is the conversation history: {context}
Question: {question}
Answer:
"""

# Prepare the prompt and chain
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Streamlit application
def chatbot_interface():
    """
    Streamlit interface for the chatbot with dynamic navbar.
    """
    st.set_page_config(page_title="career advicer", layout="wide")
    # Set title with color
    st.markdown("<h1 style='color: #4CAF50;'>Career Path Adviser ChatBot</h1>", unsafe_allow_html=True)

    # Set description with color
    st.markdown(
         """
         <p style='color: #3f51b5; font-size: 18px;'>Welcome to the Career Adviser ChatBot! Ask me anything about career paths, job recommendations, or industry trends. Type your queries below🫡.</p>
         """,
        unsafe_allow_html=True,
    )


    # Initialize session state for context, messages, and sidebar visibility
    if "context" not in st.session_state:
        st.session_state.context = ""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "sidebar_visible" not in st.session_state:
        st.session_state.sidebar_visible = True

    
    # Sidebar toggler
    with st.sidebar:
    # Sidebar toggler button
        #if st.button("☰" if not st.session_state.sidebar_visible else "✖"):
            #st.session_state.sidebar_visible = not st.session_state.sidebar_visible

        # Dynamic sidebar content
        if st.session_state.sidebar_visible:
            with st.sidebar:
                # Apply custom styles for icons and hover effect
                st.markdown(
            """
            <style>
            .nav-item {
                font-size: 16px;
                margin: 10px 0;
                display: flex;
                align-items: center;
            }
            .nav-item a {
                text-decoration: none;
                color: black;
                display: flex;
                align-items: center;
                padding: 5px 10px;
                border-radius: 5px;
            }
            .nav-item a:hover {
                background-color: #9C29B0;
            }
            .nav-item i {
                margin-right: 10px;
                font-size: 18px;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Navigation header
        st.header("Model-llama 3.2")

        # Navigation items with icons and links
        st.markdown(
            """
            <div class="nav-item">
                <i>🏠</i> <a href="#home">Home</a>
            </div>
            <div class="nav-item">
                <i>⚙️</i> <a href="#settings">Settings</a>
            </div>
            <div class="nav-item">
                <i>❓</i> <a href="https://docs.streamlit.io/" target="_blank">Help</a>
            </div>
            <div class="nav-item">
                <i>ℹ️</i> <a href="https://cebomsweli.github.io/PortFolio/Profile.html" target="_blank">About Me</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input field
    if user_input := st.chat_input("Type your message here..."):
        # Add user input to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate AI response
        result = chain.invoke({"context": st.session_state.context, "question": user_input})

        # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": result})
        with st.chat_message("assistant"):
            st.markdown(result)

        # Update context with the latest conversation
        st.session_state.context += f"\nUser: {user_input}\nAI: {result}"

# Run the chatbot interface
if __name__ == "__main__":
    chatbot_interface()
