import streamlit as st
import datetime

st.set_page_config(page_title="Moai Milestone Tracker", page_icon="🗿")

st.title("🗿 Moai Milestone Tracker")
st.write("Track your journey to becoming a **Concrete Legend**.")

# User Inputs
st.sidebar.header("Your Progress")
username = st.sidebar.text_input("Discord Username", "mkashifalikcp")
current_streak = st.sidebar.number_input("Current Discord Streak (Days)", min_value=0, value=10)
current_bags = st.sidebar.number_input("Total Bags Secured", min_value=0, value=1000)
target_role = st.sidebar.selectbox("Target Role", ["Vault Navigator", "Moai Role 🗿", "Access Key Holder"])

# Logic for Milestones
streak_goal = 100 if target_role == "Access Key Holder" else 30
bags_goal = 5000 if target_role == "Access Key Holder" else 2000

streak_progress = min(current_streak / streak_goal, 1.0)
bags_progress = min(current_bags / bags_goal, 1.0)

# Dashboard
col1, col2 = st.columns(2)

with col1:
    st.metric("Streak Progress", f"{current_streak}/{streak_goal} Days")
    st.progress(streak_progress)

with col2:
    st.metric("Bags Progress", f"{current_bags}/{bags_goal} Bags")
    st.progress(bags_progress)

# Estimated Completion
days_left = max(streak_goal - current_streak, 0)
st.divider()

if days_left > 0:
    st.info(f"⚡ **{username}**, you are just **{days_left} days** away from your {target_role} milestone! Keep the consistency.")
else:
    st.success(f"🎉 Congratulations **{username}**! You have hit the streak requirement for {target_role}. Go claim it in #proof-of-work!")

# Motivational Quote
st.write("---")
st.subheader("Moai Wisdom")
quotes = [
    "Consistency is the only alpha.",
    "Bags are secured by builders, not lurkers.",
    "The Concrete floor is built one day at a time.",
    "A Moai never misses a daily check-in."
]
import random
st.info(f"🗿 *\"{random.choice(quotes)}\"*")

# Footer
st.caption("Developed by x.com/mkashifalikcp | Not an official Concrete tool, built for the community."mkashifalikcp
