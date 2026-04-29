import streamlit as st

st.set_page_config(page_title="Concrete AI Support Hub V2", page_icon="🗿")

# --- EXPANDED KNOWLEDGE BASE ---
KNOWLEDGE_BASE = {
    "xp levels": "Concrete ecosystem mein 1 se 25 levels hain. Har level par XP requirement barhti hai. Total Level 25 tak pohnchne ke liye 4180 XP (milestone) chahiye hoti hai.",
    "level 5": "Level 5 (380 XP) par aapko 'Newbie' role aur 50 Bags milte hain.",
    "level 10": "Level 10 (955 XP) par 'Vault Navigator' role aur 150 Bags milte hain.",
    "level 17": "Level 17 (2180 XP) par 'Lucky 17' role aur 250 Bags milte hain.",
    "level 25": "Level 25 (4180 XP) par 'Grindooor' role aur 1000 Bags milte hain (End of Season reward).",
    "how to get a key": "Access Key hasil karne ke liye 4 main conditions hain: 1. Sabko friendly support dein, 2. Rozana memes banayein, 3. Server clean rakhne mein help karein, 4. X (Twitter) par rozana 2-3 posts karein.",
    "moai role": "Elite Tier (Moais) roles season ke end par top contributors ko diye jate hain. Iske liye Concrete DeFi tag use karna lazmi hai.",
    "article rewards": "Aap Medium ya Mirror par quality articles likh kar weekly rewards earn kar sakte hain. #community-news channel check karein.",
    "how to earn xp": "Discord mein chat karne, tools share karne, aur helpful rehne se aapka XP barhta hai aur aap level up karte hain."
}

st.title("🤖 Concrete Intelligence Hub V2")
st.write("Ab main XP levels, Roles, aur Access Key ke rules bhi jaanta hoon. Poochiye kya poochna hai!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about XP, Roles, or the Access Key..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = "I'm still learning! For specific technical docs, check docs.concrete.xyz or tag a Moderator. 🗿"
    
    query = prompt.lower()
    # Advanced matching logic
    for key in KNOWLEDGE_BASE:
        if key in query:
            response = KNOWLEDGE_BASE[key]
            break

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

st.sidebar.markdown("""
### 🏛️ Milestones Overview
- **L5:** Newbie (+50 Bags)
- **L10:** Vault Navigator (+150 Bags)
- **L17:** Lucky 17 (+250 Bags)
- **L25:** Grindooor (+1000 Bags)
""")
  
