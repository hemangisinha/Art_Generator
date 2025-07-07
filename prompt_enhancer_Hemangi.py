# prompt_enhancer.py

import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="✨ Prompt Enhancer App")

st.title("✨ Prompt Enhancer App")

# Ask user for OpenAI API Key in the UI
api_key = st.text_input(
    "🔑 Enter your OpenAI API Key:",
    type="password",
    placeholder="sk-...",
    help="You can get yours from https://platform.openai.com/account/api-keys"
)

# Collect user inputs
role = st.text_input(
    "🧑‍💻 Role:",
    placeholder="e.g., You are an experienced Python coder."
)

context = st.text_area(
    "📚 Context:",
    placeholder="e.g., I am a beginner learning AI app development."
)

task = st.text_area(
    "🎯 Task:",
    placeholder="e.g., I want to create a Python app to enhance prompts."
)

# Enhance prompt on button click
if st.button("✨ Enhance Prompt"):
    if not api_key:
        st.error("Please enter your OpenAI API Key.")
    elif not role or not context or not task:
        st.warning("Please fill in all fields (Role, Context, Task).")
    else:
        # Initialize OpenAI client with user-provided key
        client = OpenAI(api_key=api_key)

        # Compose the prompt for GPT
        enhanced_prompt = f"""
Role: {role}

Context: {context}

Task: {task}

Now, enhance this prompt for GPT by:
- Adding clear answer format instructions.
- Asking GPT to clarify any assumptions before responding.
- Output the final prompt in a clear block.
"""

        try:
            # Call OpenAI
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a prompt engineering assistant."},
                    {"role": "user", "content": enhanced_prompt}
                ]
            )

            final_prompt = response.choices[0].message.content

            st.subheader("✅ Enhanced Prompt:")
            st.code(final_prompt, language="markdown")

        except Exception as e:
            st.error(f"❌ API call failed: {e}")
