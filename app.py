import streamlit as st
from datetime import datetime

# Daily affirmation rotation (9 affirmations)
affirmations = [
    "Every small step I take rebuilds my strength and freedom.",
    "My past does not define me. Each day, I am free to choose again.",
    "With each breath, I release fear. I am safe now.",
    "I build peace through simple, steady habits.",
    "I am capable. Each success proves I can move forward.",
    "Step by step, I am stronger and more confident.",
    "I am safe to try, and every effort brings me closer to peace.",
    "I deserve healing, peace, joy, and progress in my life.",
    "From now on, you will encounter a lot of joy and happiness in your life. 😊"
]

# Calculate today's affirmation
current_day = datetime.now().toordinal()
daily_index = current_day % len(affirmations)
daily_affirmation = affirmations[daily_index]

# Page Layout
st.set_page_config(page_title="MindTaxis - Healing & Affirmations", layout="centered")

# Header
st.title("MindTaxis: Daily Healing Affirmations")
st.markdown("### Your path to peace, confidence, and joy")

# Daily Affirmation Display
st.subheader("Today's Affirmation")
st.markdown(f"**{daily_affirmation}**")

# Optional audio playback (simulated)
st.button("▶ Play Affirmation Audio")

# Self-Healing Tools Section
st.markdown("---")
st.header("Self-Healing Tools")

st.write("Explore proven techniques to calm your mind, relieve tension, and rebuild your inner strength:")
st.markdown("- **Meditation Guides**: Simple steps for daily calm.")
st.markdown("- **Massage Techniques**: Relieve stress and tension headaches.")
st.markdown("- **Mindset Tools**: Exercises to shift from fear to confidence.")

# Legacy Site Section
st.markdown("---")
st.header("Legacy MindTaxis Site")
st.write("Explore the original MindTaxis.com as it was first created, preserved as a historical archive.")
st.button("Visit Legacy Site")
