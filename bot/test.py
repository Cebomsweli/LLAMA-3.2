import streamlit as st

def landing_page():
    # Set the page title and layout
    st.set_page_config(page_title="Welcome to the Career Chatbot", layout="centered")

    # Add custom CSS for background animation
    st.markdown(
        """
        <style>
        body {
            background: black;
            color: black;
            overflow: hidden;
        }

        h1, h2, h3 {
            color: #ff7f50;
            font-family: 'Courier New', monospace;
        }

        h1 {
            text-shadow: 3px 3px #00ffff;
        }

        .rain {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background: black;
            overflow: hidden;
        }

        .rain span {
            position: absolute;
            top: -10px;
            font-size: 20px;
            animation: fall 5s linear infinite;
        }

        @keyframes fall {
            to {
                transform: translateY(100vh);
            }
        }
        </style>
        <div class="rain">
        """ + "".join(
            [
                f"<span style='left: {i}%; animation-delay: {i/10}s'>{icon}</span>"
                for i, icon in enumerate(
                    ["📚", "✏️", "💻", "📓", "🖊️", "📘", "📖", "📙", "📋", "🖥️"] * 10
                )
            ]
        ) + """</div>
        """,
        unsafe_allow_html=True
    )

    # Display a welcome header
    st.title("Welcome to Model-LLAMA 3.2")

    # Add a description of the bot's purpose
    st.markdown(
        """
        ### Your Career Companion
        Model-LLAMA 3.2 is your intelligent career assistant, designed to guide you through your career path with insightful advice and actionable recommendations. 
        Whether you're choosing a career, exploring new opportunities, or looking for growth strategies, this chatbot is here to help.

        **What You Can Expect:**
        - Personalized career pathways tailored to your interests and goals.
        - Expert advice to navigate your professional journey.
        - Tips and trends in various industries to stay ahead.

        Let us help you make informed decisions and achieve your dreams!
        """
    )

    # Display some images to make the page visually appealing
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.image("https://via.placeholder.com/150", caption="Explore Opportunities")
    with col2:
        st.image("https://via.placeholder.com/150", caption="Plan Your Path")
    with col3:
        st.image("https://via.placeholder.com/150", caption="Achieve Success")

    # Add creator details
    st.markdown(
        """
        ### Meet the Creators
        This chatbot was developed by:
        - [**Cebolenkosi Msweli**](https://www.linkedin.com/in/cebolenkosi-msweli)
        - [**Thabo**](https://www.linkedin.com/in/thabo)

        These passionate individuals worked together to bring you this powerful tool, aimed at empowering users in their career journeys.
        """
    )

    # Add a "Get Started" button
    if st.button("Get Started"):
        # Redirect to the chatbot interface
        chatbot_interface()

def chatbot_interface():
    st.title("Model-LLAMA 3.2 Chatbot")
    st.write("This is where the real chatbot interaction will occur.")

# Run the landing page
landing_page()
