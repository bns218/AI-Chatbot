import streamlit as st
import os
import google.generativeai as genai

os.environ["GOOGLE_API_KEY"] = "AIzaSyCERHsX8QoO3Zg0jDsBNfdBW_ofsRvfpIU"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[ ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")



# Streamlit interface
st.title("Generative AI Chat")

# Text input box for user input
user_input = st.text_input("Enter your prompt:")

if st.button("Generate Response"):
    if user_input:
        # Start chat session
        chat_session = model.start_chat(history=[])
        
        # Send the message and get the response
        response = chat_session.send_message(user_input)
        
        # Display the response in the Streamlit app
        st.write("### Response:")
        st.write(response.text)
    else:
        st.write("Please enter a prompt.")
