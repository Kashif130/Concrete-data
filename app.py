import streamlit as st
import anthropic

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Concrete Nexus AI",
    page_icon="🏛️",
    layout="centered",
)

# ── System Prompt ─────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are the Concrete Nexus AI — the official intelligent assistant for the Concrete Protocol ecosystem. You are knowledgeable, precise, and helpful. You can respond in BOTH English and Urdu (Roman Urdu) based on the user's language.

## ABOUT CONCRETE PROTOCOL

**What is Concrete?**
Concrete (concrete.xyz) is institutional-grade, on-chain DeFi infrastructure. It provides automated yield strategies through vaults, allowing users to deposit assets and earn competitive, risk-adjusted returns. The platform processes assets across multiple chains and money markets automatically.

**Key Stats:**
- Assets on Platform: ~$902.3M
- Assets Processed: ~$11.25B
- Backed by: Polychain, VanEck, YZi Labs, Portal Ventures, Hashed, Tribe Capital

**Audited By:** Cantina, Code4rena, Halborn, Zellic, Hypernative, ZeroShadow

---

## CORE PRODUCTS & LINKS

1. **Earn App** → app.concrete.xyz/earn
   - Deposit assets (WBTC, USDe, USDT, WeETH, EIGEN, etc.)
   - Get vault shares (CONC tokens)
   - Earn APY + Points
   - Use vault shares across DeFi (Pendle, Morpho, Euler)

2. **Points Program** → points.concrete.xyz
   - Track your "Bags" (points earned via quests)
   - Powered by Absinthe platform
   - Phase 1: Social Campaign (follow X, join Discord, write blogs)
   - Phase 2: Earn App leaderboard (coming soon)
   - Bags will convert to Concrete Points (ratio TBA)

3. **Docs** → docs.concrete.xyz
   - Full technical documentation
   - Earn V1 & V2 guides
   - Vaults, Fees, Risks, Audits

4. **Ecosystem** → concrete.xyz/ecosystem
   - Partner protocols and integrations

5. **Enterprise** → enterprise.concrete.xyz
   - Institutional-grade solutions
   - AssetCX: custody assets in CeFi while earning DeFi yield
   - Partners: BitGo, Fireblocks, Binance, Coinbase

6. **Community Tools:**
   - Vault tracker: https://concrete-vault--mkashifali130.replit.app/
   - Community guide: https://concrete-guide.streamlit.app/

---

## HOW IT WORKS

**Earn Vaults:**
- Deposit once → Concrete auto-allocates to best-performing protocols
- Continuously rebalances across money markets (Pendle, Morpho, Euler, etc.)
- No manual management needed
- Supported assets: WBTC, USDe, USDT, WeETH, EIGEN, and more

**Stability Floor (Future):**
- Protection mechanism to guard capital
- Formula: Stability = Net Yield / Volatility
- Will use automated vaults to protect against liquidation

**Future Products:**
- Borrowing without liquidation risk
- Multi-layered liquidation protection
- Stablecoin borrowing against vault deposits
- Complete DeFi suite (Earn + Borrow + Protect)

---

## POINTS SYSTEM (BAGS)

- Earn "Bags" by completing social quests on Absinthe
- Quests: Follow @ConcreteXYZ on X, Join Discord, Write blog articles
- Connect wallet + social accounts on Absinthe platform
- Leaderboard tracks XP and rank
- Future Phase 2: Bags earned through actual platform usage
- Conversion ratio from Bags → Concrete Points announced later

---

## FEES & RISKS

- Check docs.concrete.xyz/fees for current fee structure
- Risks: Smart contract risk, market risk, protocol risk
- All contracts audited by multiple top firms
- docs.concrete.xyz/risks for full risk disclosure
- Restricted jurisdictions: docs.concrete.xyz/restrictions

---

## SOCIAL & SUPPORT

- Twitter/X: x.com/ConcreteXYZ
- Discord: discord.gg/concretexyz
- Support: docs.concrete.xyz/support

---

## RESPONSE GUIDELINES

- If user writes in Urdu/Roman Urdu → respond in Roman Urdu (friendly, clear)
- If user writes in English → respond in English
- Always provide relevant links when discussing features
- Be accurate — if unsure, say so and point to docs
- Keep responses concise but complete
- Format with bullet points and sections for clarity
- Always be helpful and encouraging about the Concrete ecosystem"""

# ── Quick Questions ────────────────────────────────────────────────────────────
QUICK_QUESTIONS = {
    "en": [
        "What is Concrete Protocol?",
        "How do I earn points/bags?",
        "How do vaults work?",
        "What assets can I deposit?",
        "Show me all links",
        "What is Stability Floor?",
    ],
    "ur": [
        "Concrete Protocol kya hai?",
        "Points/bags kaise kamaein?",
        "Vaults kaise kaam karte hain?",
        "Kaun se assets deposit kar sakta hoon?",
        "Sare links dikhao",
        "Stability Floor kya hai?",
    ],
}

LINKS = [
    ("💎 Earn App", "https://app.concrete.xyz/earn"),
    ("🎯 Points", "https://points.concrete.xyz/home"),
    ("📚 Docs", "https://docs.concrete.xyz/Overview/welcome"),
    ("🌐 Ecosystem", "https://concrete.xyz/ecosystem"),
    ("🏛️ Enterprise", "https://enterprise.concrete.xyz"),
    ("💬 Discord", "https://discord.gg/concretexyz"),
]

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  /* Dark background */
  html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #050a0a !important;
    color: #eeeeee !important;
    font-family: 'Courier New', monospace !important;
  }

  [data-testid="stHeader"] { background: transparent !important; }
  [data-testid="stSidebar"] { background-color: #0a0f0f !important; }

  /* Hide Streamlit branding */
  #MainMenu, footer, header { visibility: hidden; }

  /* Title glow */
  .nexus-title {
    font-size: 22px;
    font-weight: bold;
    background: linear-gradient(90deg, #00ff88, #00ccff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 2px;
  }
  .nexus-sub {
    font-size: 10px;
    color: #555;
    letter-spacing: 3px;
  }

  /* Links bar */
  .link-bar a {
    display: inline-block;
    padding: 4px 14px;
    margin: 3px;
    border-radius: 20px;
    border: 1px solid rgba(0,255,136,0.25);
    background: rgba(0,255,136,0.05);
    color: #aaa !important;
    text-decoration: none !important;
    font-size: 12px;
    transition: all 0.2s;
  }
  .link-bar a:hover {
    border-color: #00ff88;
    color: #00ff88 !important;
  }

  /* Chat bubbles */
  .bubble-user {
    background: linear-gradient(135deg, #00cc66, #00aa55);
    color: #fff;
    padding: 12px 16px;
    border-radius: 18px 18px 4px 18px;
    max-width: 78%;
    margin-left: auto;
    margin-bottom: 14px;
    font-size: 14px;
    line-height: 1.7;
    word-break: break-word;
    white-space: pre-wrap;
  }
  .bubble-ai {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(0,255,136,0.18);
    color: #eee;
    padding: 12px 16px;
    border-radius: 18px 18px 18px 4px;
    max-width: 78%;
    margin-right: auto;
    margin-bottom: 14px;
    font-size: 14px;
    line-height: 1.7;
    word-break: break-word;
    white-space: pre-wrap;
  }
  .bubble-row-user { display: flex; justify-content: flex-end; gap: 10px; align-items: flex-start; }
  .bubble-row-ai   { display: flex; justify-content: flex-start; gap: 10px; align-items: flex-start; }
  .avatar {
    width: 36px; height: 36px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; flex-shrink: 0; margin-top: 2px;
  }
  .avatar-ai  { background: linear-gradient(135deg, #00ff88, #00ccff); box-shadow: 0 0 12px rgba(0,255,136,0.4); }
  .avatar-usr { background: linear-gradient(135deg, #333, #555); }

  /* Quick question buttons */
  div[data-testid="stHorizontalBlock"] button {
    background: rgba(0,255,136,0.07) !important;
    border: 1px solid rgba(0,255,136,0.25) !important;
    color: #00cc77 !important;
    border-radius: 16px !important;
    font-size: 12px !important;
    font-family: 'Courier New', monospace !important;
    padding: 4px 12px !important;
  }
  div[data-testid="stHorizontalBlock"] button:hover {
    border-color: #00ff88 !important;
    color: #00ff88 !important;
  }

  /* Text input */
  textarea, [data-testid="stTextArea"] textarea {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(0,255,136,0.3) !important;
    color: #eee !important;
    border-radius: 16px !important;
    font-family: 'Courier New', monospace !important;
    font-size: 14px !important;
  }

  /* Send button */
  [data-testid="stFormSubmitButton"] button {
    background: linear-gradient(135deg, #00ff88, #00ccff) !important;
    color: #000 !important;
    border: none !important;
    border-radius: 50% !important;
    font-size: 18px !important;
    width: 46px !important;
    height: 46px !important;
  }

  /* Footer */
  .nexus-footer {
    text-align: center;
    font-size: 10px;
    color: #333;
    letter-spacing: 1px;
    padding: 8px 0;
  }

  /* Divider */
  hr { border-color: rgba(0,255,136,0.15) !important; }

  /* Scrollbar */
  ::-webkit-scrollbar { width: 4px; }
  ::-webkit-scrollbar-track { background: #0a0a0a; }
  ::-webkit-scrollbar-thumb { background: #333; border-radius: 2px; }
</style>
""", unsafe_allow_html=True)

# ── Session state init ─────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Assalam o Alaikum! 👋 Main Concrete Nexus AI hoon.\n\nI'm your unified assistant for the entire Concrete Protocol ecosystem — vaults, points, docs, and more.\n\nAsk me anything in English or Roman Urdu! 🏛️✨",
        }
    ]
if "lang" not in st.session_state:
    st.session_state.lang = "en"
if "pending_question" not in st.session_state:
    st.session_state.pending_question = None

# ── Header ─────────────────────────────────────────────────────────────────────
col_logo, col_title, col_lang = st.columns([1, 5, 2])
with col_logo:
    st.markdown("<div style='font-size:32px; margin-top:8px;'>🏛️</div>", unsafe_allow_html=True)
with col_title:
    st.markdown("""
      <div class='nexus-title'>CONCRETE NEXUS AI</div>
      <div class='nexus-sub'>UNIFIED ECOSYSTEM ASSISTANT</div>
    """, unsafe_allow_html=True)
with col_lang:
    lang_choice = st.radio("Lang", ["🇬🇧 EN", "🇵🇰 UR"], horizontal=True, label_visibility="collapsed")
    st.session_state.lang = "ur" if "UR" in lang_choice else "en"

st.markdown("<hr style='margin:6px 0 10px 0;'>", unsafe_allow_html=True)

# ── Quick Links ────────────────────────────────────────────────────────────────
links_html = '<div class="link-bar">' + "".join(
    f'<a href="{url}" target="_blank">{label}</a>' for label, url in LINKS
) + '</div>'
st.markdown(links_html, unsafe_allow_html=True)
st.markdown("<hr style='margin:10px 0;'>", unsafe_allow_html=True)

# ── Chat History ───────────────────────────────────────────────────────────────
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"""
        <div class="bubble-row-user">
          <div class="bubble-user">{msg['content']}</div>
          <div class="avatar avatar-usr">👤</div>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="bubble-row-ai">
          <div class="avatar avatar-ai">🏛️</div>
          <div class="bubble-ai">{msg['content']}</div>
        </div>""", unsafe_allow_html=True)

# ── Quick Questions ────────────────────────────────────────────────────────────
lang = st.session_state.lang
questions = QUICK_QUESTIONS[lang]

q_cols = st.columns(3)
for i, q in enumerate(questions):
    if q_cols[i % 3].button(q, key=f"qq_{i}", use_container_width=True):
        st.session_state.pending_question = q

st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)

# ── Input Form ─────────────────────────────────────────────────────────────────
placeholder = (
    "Koi bhi sawaal poochho Concrete ke baare mein..."
    if lang == "ur"
    else "Ask anything about Concrete Protocol..."
)

with st.form("chat_form", clear_on_submit=True):
    inp_col, btn_col = st.columns([9, 1])
    with inp_col:
        user_input = st.text_area(
            "Message",
            placeholder=placeholder,
            label_visibility="collapsed",
            height=68,
            key="user_input_box",
        )
    with btn_col:
        submitted = st.form_submit_button("➤")

# ── Send logic ─────────────────────────────────────────────────────────────────
def send_message(text: str):
    text = text.strip()
    if not text:
        return

    st.session_state.messages.append({"role": "user", "content": text})

    client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

    with st.spinner("Thinking... 🏛️"):
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
        )

    reply = "".join(b.text for b in response.content if hasattr(b, "text"))
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()


# Handle quick-question click
if st.session_state.pending_question:
    q = st.session_state.pending_question
    st.session_state.pending_question = None
    send_message(q)

# Handle form submit
if submitted and user_input and user_input.strip():
    send_message(user_input)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("<hr style='margin:12px 0 4px 0;'>", unsafe_allow_html=True)
st.markdown(
    "<div class='nexus-footer'>CONCRETE NEXUS AI • concrete.xyz • docs.concrete.xyz • points.concrete.xyz</div>",
    unsafe_allow_html=True,
)
