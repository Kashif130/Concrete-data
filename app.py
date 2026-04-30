import streamlit as st

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Concrete Nexus Guide",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════════════════════
# KNOWLEDGE BASE — scraped from concrete.xyz, docs.concrete.xyz,
# points.concrete.xyz, enterprise.concrete.xyz, businesswire, coinlaunch, etc.
# No AI agent used — all data is hardcoded from official sources.
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# ENGLISH CONTENT — Maps section heading → English body text
# ══════════════════════════════════════════════════════════════════════════════
EN_BODIES = {
    "Concrete Protocol Kya Hai?": (
        "**Concrete** (concrete.xyz) is an **institutional-grade, on-chain DeFi infrastructure** platform. "
        "It provides automated yield strategies through ERC-4626 vaults — users deposit once "
        "and Concrete automatically allocates, rebalances, and compounds across top protocols with zero manual action.\n\n"
        "Concrete is developed by **Blueprint Finance** — a multi-chain DeFi infrastructure company. "
        "It operates on Ethereum, with **Glow Finance** as its sister protocol on Solana."
    ),
    "Core Philosophy": (
        "> \"Yield isn't discovered. It's Engineered.\"\n\n"
        "Concrete converts DeFi complexity into a simple **Deposit → Earn** experience. "
        "Users need no trading skills, quant modeling, or multi-chain expertise. "
        "One click and you access institutional-grade yield."
    ),
    "Yield Strategies Inside Each Vault": (
        "Each vault deploys capital across multiple DeFi strategies:\n\n"
        "- 📈 **Lending** — Aave, Compound, Morpho\n"
        "- 💧 **Liquidity Provisioning** — Curve, Pendle\n"
        "- 🔄 **Restaking** — EigenLayer\n"
        "- 📊 **Delta-Neutral Hedging** — Market-neutral strategies\n"
        "- 🎯 **Incentive Farming** — Protocol reward capture\n"
        "- 🔗 **Cross-Chain Yield Routing** — Best opportunity across chains\n"
        "- 🔁 **Automated Compounding** — Continuous reinvestment"
    ),
    "ct[Asset] Tokens — Vault Shares": (
        "When you deposit into a Concrete vault, you receive **ct[asset]** tokens:\n\n"
        "- They are yield-bearing vault shares\n"
        "- Their value automatically increases as the vault earns yield\n"
        "- They can be used elsewhere in DeFi:\n"
        "  - **Pendle** — Yield tokenization\n"
        "  - **Morpho** — Collateral for borrowing\n"
        "  - **Euler** — Lending base\n"
        "- Turns a passive position into an active financial primitive\n\n"
        "**Examples:** ctUSDT · ctWBTC · ctWeETH"
    ),
    "Probability Engine — Risk Management": (
        "Concrete's internal quantitative risk system:\n\n"
        "- Analyzes asset distribution and concentration\n"
        "- Projects price movements (e.g. ETH 8% drop probability)\n"
        "- Uses multiple oracle feeds — on-chain + off-chain\n"
        "- Tracks asset correlations across the portfolio\n"
        "- Automatically shifts into protective strategies during downturns\n"
        "- Liquidation risk forecasting and mitigation"
    ),
    "Concrete Example Scenario (Earn V2)": (
        "1. **Partner** launches a USDC vault via Concrete Enterprise Factory (Pendle + Curve strategies)\n"
        "2. **User** deposits USDC → receives vault shares (ctUSDC)\n"
        "3. **Allocator** deploys capital: 50% Pendle, 50% Curve\n"
        "4. **Daily:** automated accounting updates NAV, calculates yield\n"
        "5. **Withdrawal:** user requests → USDC returned (instant or next epoch)\n"
        "6. **Everything** is recorded on subgraph — full on-chain transparency"
    ),
    "USDT Vault — Details": (
        "- **Asset:** Tether USDT\n"
        "- **TVL:** $62.4M\n"
        "- **Target APY:** 8.5%\n"
        "- **Strategies:** Lending (Morpho Aave), Liquidity Mining, Algorithmic Arbitrage\n"
        "- **Reward:** Concrete Points + APY\n"
        "- **Best for:** Stablecoin holders seeking risk-adjusted returns"
    ),
    "WBTC Vault — Details": (
        "- **Asset:** Wrapped Bitcoin\n"
        "- **TVL:** $4.31M\n"
        "- **Target APY:** 7%\n"
        "- **Key Feature:** BTC productive without cross-chain bridge exposure\n"
        "- **Best for:** BTC holders who want yield without bridge risk"
    ),
    "Supported Assets": "**WBTC · USDe · USDT · WeETH · EIGEN · USDC · ETH** — and growing",
    "Step 1: Wallet Connect Karo": (
        "1. Open [app.concrete.xyz/earn](https://app.concrete.xyz/earn)\n"
        "2. Click **Connect Wallet** in the top-right\n"
        "3. Select your wallet:\n"
        "   - MetaMask ✅\n"
        "   - Rainbow ✅\n"
        "   - WalletConnect ✅\n"
        "   - Coinbase Wallet ✅\n"
        "   - Any EVM-compatible wallet ✅"
    ),
    "Step 2: Vault Select Karo": (
        "- Browse available vaults (USDT · WBTC · WeETH)\n"
        "- Review TVL, APY, and strategy details\n"
        "- Choose a vault based on your risk appetite and goals\n"
        "- Check restricted jurisdictions first"
    ),
    "Step 3: Deposit Karo": (
        "1. Enter amount\n"
        "2. Approve in your wallet\n"
        "3. Receive **ct[asset] tokens** — your vault ownership proof\n"
        "4. ✅ Done! Your capital is now earning yield"
    ),
    "Step 4: Yield Track Karo": (
        "- Concrete automatically allocates and rebalances\n"
        "- Daily NAV updates occur automatically\n"
        "- No manual action required\n"
        "- Your ct[asset] token value grows over time"
    ),
    "Step 5: Withdraw Karo": (
        "- **Standard Vault:** Instant withdrawal available\n"
        "- **Async Vault:** Request joins queue, processed at next epoch\n"
        "- ❌ No withdrawal fees\n"
        "- Receive USDC/USDT/WBTC back"
    ),
    "⚠️ Important Disclaimers": (
        "- Yields are **NOT guaranteed** — market risk always exists\n"
        "- **Smart contract risk** exists despite audits\n"
        "- **Past performance** does not guarantee future results\n"
        "- Check restricted jurisdictions: [docs.concrete.xyz/restrictions](https://docs.concrete.xyz/restrictions/)\n"
        "- Only invest according to your own risk tolerance"
    ),
    "Bags Kya Hain?": (
        "**'Bags'** is Concrete's reward currency earned by completing social tasks. "
        "They will later convert into **Concrete Points**, which qualify for a potential future **token airdrop**.\n\n"
        "> Token not yet launched (April 2026). But $17M funding + active points campaign = strong airdrop signal.\n\n"
        "**Dashboard:** [points.concrete.xyz/home](https://points.concrete.xyz/home)\n"
        "**Registered Participants:** 100,000+"
    ),
    "Article of the Week — Content Creation": (
        "- Every Monday a **rubric is posted** in Discord\n"
        "- Write your article according to that rubric\n"
        "- Submit for review\n"
        "- **Accepted article: +400 Bags/Points** per week\n"
        "- Max 1 submission per week\n"
        "- Requirements: Clarity · Research depth · Value-add · Accuracy · Originality\n"
        "- Top articles: Bonus points + featured in community"
    ),
    "Step-by-Step: Bags Earn Karna Shuru Karo": (
        "1. Open [points.concrete.xyz/home](https://points.concrete.xyz/home)\n"
        "2. Click **Connect Wallet** — top-right (EVM wallet required)\n"
        "3. Go to **Linked Accounts** → connect X and Discord\n"
        "4. Browse **Quests tab** and complete tasks\n"
        "5. Complete earlier tasks to unlock locked ones\n"
        "6. Share your **referral link** for extra bags\n"
        "7. Check the **Leaderboard** tab for your rank"
    ),
    "Airdrop Strategy Tips": (
        "- **Early participation** matters — historically early users get larger allocations\n"
        "- Previous DeFi airdrops gave early users **2-5x larger allocation**\n"
        "- Bags → Concrete Points conversion ratio is currently **TBA**\n"
        "- **Phase 2** (coming soon): Bags will also be earned from platform usage (on-chain leaderboard)\n"
        "- Consistency beats intensity — don't miss daily tasks"
    ),
    "Smart Contract Risk": (
        "- All vaults are governed by smart contracts\n"
        "- Audited but no system is 100% safe\n\n"
        "**How Concrete mitigates:**\n"
        "- ✅ Regular audits by Halborn, Zellic, Cantina, Code4rena\n"
        "- ✅ Open-source contracts with community review\n"
        "- ✅ Bug bounty programs\n"
        "- ✅ Ongoing security testing"
    ),
    "Impermanent Loss (IL)": (
        "IL occurs in LP pools when token prices diverge.\n\n"
        "**More likely when:**\n"
        "- Non-stablecoin pairs (ETH/BTC)\n"
        "- Volatile markets\n"
        "- New chain pre-deposit campaigns\n\n"
        "**Mitigation:**\n"
        "- Diversified vault strategies\n"
        "- Dynamic reallocation during volatility"
    ),
    "Slippage Risk": (
        "The difference between expected and actual trade execution price.\n\n"
        "**More likely when:**\n"
        "- Volatile or thinly traded tokens\n"
        "- High market activity\n"
        "- Large trades relative to pool size\n\n"
        "**Mitigation:**\n"
        "- 1inch aggregator integration (optimal routing)\n"
        "- Built-in slippage protection\n"
        "- UI warnings when slippage exceeds threshold"
    ),
    "Strategy-Specific & Market Risk": (
        "- Underlying protocols (Aave, Pendle, Morpho) carry their own risks\n"
        "- Market volatility can reduce asset value\n"
        "- Yields are not guaranteed — they are variable\n\n"
        "**Mitigation:**\n"
        "- Protocol vetting and monitoring\n"
        "- Capped exposures for experimental strategies\n"
        "- Transparent allocation disclosures"
    ),
    "Restricted Jurisdictions": (
        "Concrete is not available in certain countries.\n\n"
        "Full list: [docs.concrete.xyz/restrictions](https://docs.concrete.xyz/restrictions/)"
    ),
    "Concrete Enterprise": (
        "Dedicated solutions for institutional and large capital allocators.\n\n"
        "**Link:** [enterprise.concrete.xyz](https://enterprise.concrete.xyz)"
    ),
    "AssetCX — Flagship Enterprise Product": (
        "AssetCX bridges CeFi custody and DeFi yield:\n\n"
        "> **\"Custody assets in CeFi while earning DeFi yield\"**\n\n"
        "- Institutional clients can keep assets with traditional custodians\n"
        "- Simultaneously earn DeFi yield through Concrete\n"
        "- Best of both worlds: CeFi security + DeFi returns\n\n"
        "**Audit:** January 09, 2026 by Halborn"
    ),
    "Binance Wallet Integration (March 2026)": (
        "Latest major partnership (March 12, 2026):\n\n"
        "- Binance Wallet users can now directly access USDT yield strategies\n"
        "- No need to leave the Binance Wallet app\n"
        "- Institutional-grade vault infrastructure now available to retail Binance users\n"
        "- Concrete vault technology integrated into one of the world's largest wallet ecosystems"
    ),
    "Figment Partnership (Nov 2025)": (
        "- Concrete + Figment expanding institutional access to BTC and XRP yield\n"
        "- Figment is a leading independent staking infrastructure provider\n"
        "- Concrete yield solutions now available to Figment's institutional clients"
    ),
    "Ecosystem Link": "[concrete.xyz/ecosystem](https://concrete.xyz/ecosystem) — All partner protocols and integrations",
    "Blueprint Finance — Parent Company": (
        "- **Concrete** (Ethereum) — Institutional DeFi vaults\n"
        "- **Glow Finance** (Solana) — Yield, trading & lending on Solana\n\n"
        "Blueprint Finance is building cross-chain DeFi infrastructure for the next generation of institutional capital."
    ),
    "Protocol Basics": (
        "**Q: What is Concrete Protocol?**\n"
        "A: An institutional-grade DeFi platform that optimizes yield through automated vault strategies. Deposit — Concrete handles the rest.\n\n"
        "**Q: What wallet do I need?**\n"
        "A: Any EVM-compatible wallet — MetaMask, Rainbow, WalletConnect, Coinbase Wallet.\n\n"
        "**Q: What is the minimum deposit?**\n"
        "A: No specific minimum in official docs. Be mindful of gas fees.\n\n"
        "**Q: Are deposits safe?**\n"
        "A: Vaults are thoroughly audited (Halborn, Zellic, Cantina), but DeFi always carries risk. Concrete has not suffered any major exploit to date."
    ),
    "Fees & Yield": (
        "**Q: What are the fees?**\n"
        "A: Deposit, withdrawal, maintenance — all zero. Only a 1.5% annual vault fee (AUM-based).\n\n"
        "**Q: Is APY guaranteed?**\n"
        "A: No. Yields are variable and depend on market conditions. Target APY is indicative only.\n\n"
        "**Q: When will I receive my withdrawal?**\n"
        "A: Standard vaults: instant. Async vaults: next epoch (no withdrawal fee)."
    ),
    "Points & Airdrop": (
        "**Q: What is the difference between Bags and Points?**\n"
        "A: Bags are earned now through social tasks. They will later convert into Concrete Points. Points count toward future token allocation.\n\n"
        "**Q: When will the token launch?**\n"
        "A: No official announcement as of April 2026. The active points campaign is a strong indicator.\n\n"
        "**Q: How many points per referral?**\n"
        "A: Bonus bags per successful referral. Exact amount is dynamic.\n\n"
        "**Q: Can I use it from Pakistan?**\n"
        "A: Check [docs.concrete.xyz/restrictions](https://docs.concrete.xyz/restrictions/) — Pakistan is generally accessible."
    ),
    "Technical Questions": (
        "**Q: Why is the WeETH vault so large ($705M)?**\n"
        "A: Institutional demand for WeETH (Wrapped EigenLayer ETH) is very high — it's Concrete's largest vault.\n\n"
        "**Q: Where can ct[asset] tokens be used?**\n"
        "A: Pendle (yield tokenization), Morpho (collateral), Euler (borrowing base).\n\n"
        "**Q: What is the difference between Earn V1 and V2?**\n"
        "A: V2 is fully automated — daily NAV updates, role-based automation, async withdrawals. V1 was manual.\n\n"
        "**Q: Where can I get support?**\n"
        "A: Discord: [discord.gg/concretexyz](https://discord.gg/concretexyz) or the Docs Support page."
    ),
    "XP System Kya Hai?": (
        "Concrete Discord rewards **XP (Experience Points)** for chatting and engaging. "
        "The more you engage, the more XP, the higher your level!\n\n"
        "Certain levels unlock **special roles + BAGS milestone rewards**.\n\n"
        "**Join Discord:** [discord.gg/concretexyz](https://discord.gg/concretexyz)"
    ),
    "XP Fast Earn Tips": (
        "- 💬 **Daily Chat:** Message in Discord every day — quality over quantity\n"
        "- 📝 **Articles:** Publish community articles on Mirror/Paragraph → extra XP + pts\n"
        "- 🤝 **Referrals:** Invite friends to Discord — referrals = XP\n"
        "- 🎯 **Events:** Participate in AMAs, Twitter Spaces, community events\n"
        "- ❓ **Q&A:** Helpful answers and thoughtful questions count toward engagement"
    ),
    "KEY Kya Hai?": (
        "**KEY** is a special access/role in the Concrete community. "
        "It is awarded to those who consistently add value — through support, content creation, "
        "and platform engagement.\n\n"
        "KEY holders receive exclusive community recognition."
    ),
    "4 Conditions to Get KEY": (
        "**1. 🤝 Friendly Support**\n"
        "Help new members, answer questions, be welcoming in Discord. "
        "Your attitude matters — make people feel at home in the community.\n\n"
        "**2. 😂 Daily Memes**\n"
        "Create Concrete-related memes daily. Post in the memes channel. "
        "Creative, funny, and on-topic content gets noticed. "
        "Tools: DALL-E, Canva, CapCut, or manual design.\n\n"
        "**3. 🤖 Server Moderation Help**\n"
        "Report spam, assist with moderation tasks, keep channels clean and organized. "
        "Be a responsible community member.\n\n"
        "**4. 📱 X (Twitter) = 2-3 Posts/Day**\n"
        "Post about Concrete on X/Twitter 2-3 times daily. "
        "Use #ConcreteDeFi. Share updates, vault experiences, educational content. "
        "Consistent Twitter presence is key!"
    ),
    "MOAI — Elite Tier": (
        "**🗿 MOAI** is the highest community role:\n\n"
        "- Awarded at season end\n"
        "- Only top contributors receive it\n"
        "- Must use the Concrete DeFi tag\n"
        "- Check #announcements channel for more info\n\n"
        "> Rare and prestigious — reserved for the most dedicated builders only!"
    ),
    "Community Vault Intelligence Tool": (
        "A community-built vault tracker with real-time data:\n\n"
        "**🔗 [concrete-vault.streamlit.app](https://concrete-vault.streamlit.app/)**\n\n"
        "Features:\n"
        "- Live APY tracking (app.concrete.xyz → DeFiLlama → ETH RPC → Simulated)\n"
        "- Health Factor monitoring\n"
        "- Yield Calculator (deposit amount → projected earnings)\n"
        "- Portfolio Rebalancer\n"
        "- Smart Alerts\n"
        "- Vault DNA Fingerprint\n\n"
        "*Built by @mkashifalikcp — community contributor. Not affiliated with Concrete Protocol.*"
    ),
    "Efficiency Index — Kya Hai?": (
        "Concrete's internal performance scoring system:\n\n"
        "```\n"
        "Efficiency Index = (Avg APY / (1 + APY Volatility)) × Util Stability × 100\n"
        "```\n\n"
        "More reliable than raw APY — compares consistent yield vs. volatile yield.\n\n"
        "**6 Vault DNA Dimensions:**\n"
        "- Yield Consistency — How stable the APY is\n"
        "- Liquidity Depth — Liquidity available for withdrawals\n"
        "- Strategy Diversity — Number of protocols used\n"
        "- Protocol Maturity — Age/reliability of underlying protocols\n"
        "- Util Stability — Utilization rate stability\n"
        "- Efficiency Index — Overall composite score"
    ),
}

EN_HEADINGS = {
    "Concrete Protocol Kya Hai?": "What is Concrete Protocol?",
    "Vaults Kaise Kaam Karte Hain": "How Vaults Work",
    "Bags Kya Hain?": "What Are Bags?",
    "Step-by-Step: Bags Earn Karna Shuru Karo": "Step-by-Step: Start Earning Bags",
    "Airdrop Strategy Tips": "Airdrop Strategy Tips",
    "Step 1: Wallet Connect Karo": "Step 1: Connect Wallet",
    "Step 2: Vault Select Karo": "Step 2: Select Vault",
    "Step 3: Deposit Karo": "Step 3: Deposit",
    "Step 4: Yield Track Karo": "Step 4: Track Yield",
    "Step 5: Withdraw Karo": "Step 5: Withdraw",
    "XP System Kya Hai?": "What is the XP System?",
    "KEY Kya Hai?": "What is KEY Role?",
    "Efficiency Index — Kya Hai?": "What is the Efficiency Index?",
    "FAQ — Aksar Pooche Jane Wale Sawal": "FAQ — Frequently Asked Questions",
}


KB = {
    "overview": {
        "title": "Concrete Protocol — Overview",
        "icon": "🏛️",
        "sections": [
            {
                "heading": "Concrete Protocol Kya Hai?",
                "body": (
                    "**Concrete** (concrete.xyz) ek **institutional-grade, on-chain DeFi infrastructure** platform hai. "
                    "Yeh automated yield strategies through ERC-4626 vaults provide karta hai — users ek baar deposit karte hain "
                    "aur Concrete automatically best protocols pe allocate, rebalance, aur compound karta rehta hai bina kisi manual action ke.\n\n"
                    "Concrete ko **Blueprint Finance** ne develop kiya hai — ek multi-chain DeFi infrastructure company. "
                    "Ethereum pe Concrete operate karta hai, aur Solana pe uska sister protocol **Glow Finance** hai."
                ),
            },
            {
                "heading": "Key Stats (April 2026)",
                "body": (
                    "| Metric | Value |\n"
                    "|--------|-------|\n"
                    "| 💰 Assets on Platform | ~$902.3M |\n"
                    "| 📦 Assets Processed (Lifetime) | ~$11.25B |\n"
                    "| 💼 Total Funding Raised | $17M |\n"
                    "| 🐦 Twitter Followers | 138K+ |\n"
                    "| 👥 Discord Community | Active & Growing |\n"
                    "| 🔐 Security Audits Completed | 4 |\n"
                    "| 📋 Live Vaults | USDT · WeETH · WBTC |\n"
                ),
            },
            {
                "heading": "Investors / Backers",
                "body": (
                    "| Round | Amount | Lead Investors |\n"
                    "|-------|--------|----------------|\n"
                    "| Seed (Feb 2024) | $7.5M | Hashed & Tribe Capital |\n"
                    "| Series A (Jun 2025) | $9.5M | Polychain Capital |\n\n"
                    "**Other Backers:** YZi Labs (prev. Binance Labs) · VanEck · Portal Ventures · "
                    "Avalanche Foundation · Hypersphere · Sam Kazemian (HDF)"
                ),
            },
            {
                "heading": "Core Team Background",
                "body": (
                    "- **@nic_builds** — CEO\n"
                    "- **@dill_sl** — Core Team\n"
                    "- **@crypttoji** — Core Team\n\n"
                    "Team has roots in: **EigenLayer, Coinbase, Morgan Stanley, Point72, ConsenSys**"
                ),
            },
            {
                "heading": "Core Philosophy",
                "body": (
                    "> \"Yield isn't discovered. It's Engineered.\"\n\n"
                    "Concrete DeFi ki complexity ko ek simple **Deposit → Earn** experience mein convert karta hai. "
                    "Users ko trading skills, quant modeling, ya multi-chain knowledge ki zarurat nahi. "
                    "Ek click, aur institutional-grade yield milta hai."
                ),
            },
        ],
    },

    "how_it_works": {
        "title": "Vaults Kaise Kaam Karte Hain",
        "icon": "⚙️",
        "sections": [
            {
                "heading": "Basic Flow",
                "body": (
                    "```\n"
                    "User deposits asset (USDC / WBTC / WeETH / etc.)\n"
                    "        ↓\n"
                    "Vault mints ERC-20 shares → ct[asset] tokens\n"
                    "        ↓\n"
                    "Allocator role capital ko strategies mein deploy karta hai\n"
                    "        ↓\n"
                    "Automated yield accrual — daily NAV updates\n"
                    "        ↓\n"
                    "User withdraws anytime (instant OR epoch-based)\n"
                    "```"
                ),
            },
            {
                "heading": "Earn V1 vs Earn V2",
                "body": (
                    "| Feature | Earn V1 | Earn V2 (Current) |\n"
                    "|---------|---------|-------------------|\n"
                    "| Accounting | Manual | Fully Automated |\n"
                    "| Rebalancing | Curator + Multi-sig | Role-Based Automation |\n"
                    "| Withdrawals | Manual approval | Instant OR Async Epochs |\n"
                    "| NAV Updates | Manual | Daily automated |\n"
                    "| Transparency | Basic | Full subgraph indexing |\n"
                    "| Speed | Limited | Market speed |\n\n"
                    "**Earn V2 Roles:** Vault Manager · Allocator · Strategy Manager · Hook Manager · Withdrawal Manager"
                ),
            },
            {
                "heading": "Yield Strategies Inside Each Vault",
                "body": (
                    "Har vault multiple strategies across DeFi pe deploy karta hai:\n\n"
                    "- 📈 **Lending** — Aave, Compound, Morpho\n"
                    "- 💧 **Liquidity Provisioning** — Curve, Pendle\n"
                    "- 🔄 **Restaking** — EigenLayer\n"
                    "- 📊 **Delta-Neutral Hedging** — Market-neutral strategies\n"
                    "- 🎯 **Incentive Farming** — Protocol rewards\n"
                    "- 🔗 **Cross-Chain Yield Routing** — Best opportunity across chains\n"
                    "- 🔁 **Automated Compounding** — Continuous reinvestment"
                ),
            },
            {
                "heading": "ct[Asset] Tokens — Vault Shares",
                "body": (
                    "Jab aap Concrete vault mein deposit karte hain, aapko **ct[asset]** tokens milte hain:\n\n"
                    "- Yield-bearing vault shares hain\n"
                    "- Value automatically badhti rehti hai as vault earns yield\n"
                    "- DeFi mein kahin aur bhi use kar sakte hain:\n"
                    "  - **Pendle** — Yield tokenization\n"
                    "  - **Morpho** — Collateral for borrowing\n"
                    "  - **Euler** — Lending base\n"
                    "- Passive position ko active financial primitive banata hai\n\n"
                    "**Examples:** ctUSDT · ctWBTC · ctWeETH"
                ),
            },
            {
                "heading": "Probability Engine — Risk Management",
                "body": (
                    "Concrete ka internal quantitative risk system:\n\n"
                    "- Asset distribution aur concentration analyze karta hai\n"
                    "- Price movements project karta hai (e.g. ETH 8% drop probability)\n"
                    "- Multiple Oracle feeds use karta hai — on-chain + off-chain\n"
                    "- Asset correlations track karta hai across portfolio\n"
                    "- Automatically protection strategies mein shift karta hai downturn mein\n"
                    "- Liquidation risk forecasting aur mitigation"
                ),
            },
            {
                "heading": "Concrete Example Scenario (Earn V2)",
                "body": (
                    "1. **Partner** Concrete Enterprise Factory se USDC vault launch karta hai (Pendle + Curve strategies)\n"
                    "2. **User** USDC deposit karta hai → vault shares (ctUSDC) milte hain\n"
                    "3. **Allocator** capital deploy karta hai: 50% Pendle, 50% Curve\n"
                    "4. **Har roz:** automated accounting NAV update karta hai, yield calculate hoti hai\n"
                    "5. **Withdrawal:** User request karta hai → USDC wapas milti hai (instant ya next epoch)\n"
                    "6. **Sab kuch** subgraph pe record hota hai — full on-chain transparency"
                ),
            },
        ],
    },

    "vaults": {
        "title": "Live Vaults & Products",
        "icon": "💎",
        "sections": [
            {
                "heading": "Current Live Vaults (April 2026)",
                "body": (
                    "| Vault | TVL | Target APY | Type |\n"
                    "|-------|-----|-----------|------|\n"
                    "| 🟢 DeFi USDT | $62.4M | 8.5% | Stablecoin yield |\n"
                    "| 🔵 WeETH (Institutional) | $705M | Institutional | Wrapped ETH restaking |\n"
                    "| 🟠 WBTC | $4.31M | 7% | Bitcoin yield |\n\n"
                    "**Link:** [app.concrete.xyz/earn](https://app.concrete.xyz/earn)"
                ),
            },
            {
                "heading": "USDT Vault — Details",
                "body": (
                    "- **Asset:** Tether USDT\n"
                    "- **TVL:** $62.4M\n"
                    "- **Target APY:** 8.5%\n"
                    "- **Strategies:** Lending (Morpho Aave), Liquidity Mining, Algorithmic Arbitrage\n"
                    "- **Reward:** Concrete Points + APY\n"
                    "- **Best for:** Stablecoin holders jo risk-adjusted returns chahte hain"
                ),
            },
            {
                "heading": "WeETH Vault — Details",
                "body": (
                    "- **Asset:** Wrapped EigenLayer ETH\n"
                    "- **TVL:** $705M (Concrete ka largest vault)\n"
                    "- **APY:** Institutional (contact required)\n"
                    "- **Access:** Institutional clients only\n"
                    "- **Use case:** ETH restaking without complexity"
                ),
            },
            {
                "heading": "WBTC Vault — Details",
                "body": (
                    "- **Asset:** Wrapped Bitcoin\n"
                    "- **TVL:** $4.31M\n"
                    "- **Target APY:** 7%\n"
                    "- **Key Feature:** BTC productive without cross-chain bridge exposure\n"
                    "- **Best for:** BTC holders jo yield chahte hain bina bridge risk ke"
                ),
            },
            {
                "heading": "Past / Completed Campaigns",
                "body": (
                    "- **sEIGEN Vault** — EigenLayer restaking pre-deposit (completed)\n"
                    "- **Stable Pre-Deposit Vault** — Stable Chain rewards access (completed)"
                ),
            },
            {
                "heading": "Vault Feature Summary",
                "body": (
                    "| Feature | Details |\n"
                    "|---------|--------|\n"
                    "| Standard | Single base asset per vault |\n"
                    "| ERC-4626 | Industry standard, interoperable |\n"
                    "| Auto-Rebalancing | Market conditions ke saath |\n"
                    "| Deposit Fee | ❌ None |\n"
                    "| Withdrawal Fee | ❌ None |\n"
                    "| Vault Fee | ✅ 1.5% AUM annually |\n"
                    "| Sentora/Lombard Fee | ✅ 1.25% AUM annually |\n"
                    "| Withdrawal Mode | Instant ya Async Epoch |\n"
                ),
            },
            {
                "heading": "Supported Assets",
                "body": "**WBTC · USDe · USDT · WeETH · EIGEN · USDC · ETH** — aur aage badh raha hai",
            },
        ],
    },

    "earn_guide": {
        "title": "Deposit Guide — Step by Step",
        "icon": "📥",
        "sections": [
            {
                "heading": "Step 1: Wallet Connect Karo",
                "body": (
                    "1. [app.concrete.xyz/earn](https://app.concrete.xyz/earn) open karo\n"
                    "2. Top-right mein **Connect Wallet** dabao\n"
                    "3. Apna wallet select karo:\n"
                    "   - MetaMask ✅\n"
                    "   - Rainbow ✅\n"
                    "   - WalletConnect ✅\n"
                    "   - Coinbase Wallet ✅\n"
                    "   - Koi bhi EVM-compatible ✅"
                ),
            },
            {
                "heading": "Step 2: Vault Select Karo",
                "body": (
                    "- Available vaults browse karo (USDT · WBTC · WeETH)\n"
                    "- TVL, APY, aur strategy details review karo\n"
                    "- Apne risk appetite aur goals ke hisab se vault chunao\n"
                    "- Restricted jurisdictions check karo pehle"
                ),
            },
            {
                "heading": "Step 3: Deposit Karo",
                "body": (
                    "1. Amount enter karo\n"
                    "2. Wallet mein approve karo\n"
                    "3. **ct[asset] tokens** receive karo — ye aapki vault ownership hai\n"
                    "4. ✅ Done! Aapka capital ab earn kar raha hai"
                ),
            },
            {
                "heading": "Step 4: Yield Track Karo",
                "body": (
                    "- Concrete automatically allocate aur rebalance karta hai\n"
                    "- Daily NAV updates hoti hain\n"
                    "- Koi manual action required nahi\n"
                    "- ct[asset] token value waqt ke saath badhti hai"
                ),
            },
            {
                "heading": "Step 5: Withdraw Karo",
                "body": (
                    "- **Standard Vault:** Instant withdrawal available\n"
                    "- **Async Vault:** Request queue mein jati hai, next epoch pe process\n"
                    "- ❌ No withdrawal fees\n"
                    "- USDC/USDT/WBTC wapas milti hai"
                ),
            },
            {
                "heading": "Manual DeFi vs Concrete — Comparison",
                "body": (
                    "| Problem (Manual DeFi) | Solution (Concrete) |\n"
                    "|----------------------|---------------------|\n"
                    "| 50+ protocols monitor karo | Ek vault mein sab |\n"
                    "| Gas fees har rebalancing pe | Automated, fees minimize |\n"
                    "| APY manually hunt karo | Quant engine auto-finds best |\n"
                    "| Timing miss karo | 24/7 auto-rebalancing |\n"
                    "| Multi-chain complexity | Fully abstracted |\n"
                    "| Liquidation risk | Risk-managed strategies |\n"
                    "| Compounding manually | Auto-compounding built-in |"
                ),
            },
            {
                "heading": "⚠️ Important Disclaimers",
                "body": (
                    "- Yields are **NOT guaranteed** — market risk hota hai\n"
                    "- **Smart contract risk** exists despite audits\n"
                    "- **Past performance** future results guarantee nahi karta\n"
                    "- Check restricted jurisdictions: [docs.concrete.xyz/restrictions](https://docs.concrete.xyz/restrictions/)\n"
                    "- Apni risk tolerance ke mutabiq invest karo"
                ),
            },
        ],
    },

    "points": {
        "title": "Points & Bags System",
        "icon": "🎯",
        "sections": [
            {
                "heading": "Bags Kya Hain?",
                "body": (
                    "**'Bags'** Concrete ki reward currency hai jo social tasks complete karne se milti hai. "
                    "Yeh baad mein **Concrete Points** mein convert honge, jo potential future **token airdrop** ke liye qualify karte hain.\n\n"
                    "> Token abhi launch nahi hua (April 2026). Lekin $17M funding + active points campaign = strong airdrop signal.\n\n"
                    "**Dashboard:** [points.concrete.xyz/home](https://points.concrete.xyz/home)\n"
                    "**Registered Participants:** 100,000+"
                ),
            },
            {
                "heading": "Twitter/X Tasks — Points Table",
                "body": (
                    "| Task | Points |\n"
                    "|------|--------|\n"
                    "| Follow @ConcreteXYZ | 50 pts |\n"
                    "| Follow @nic_builds (CEO) | 25 pts |\n"
                    "| Follow @dill_sl | 25 pts |\n"
                    "| Follow @crypttoji | 10 pts |\n"
                    "| Daily post likes | Variable |\n"
                    "| Quality tweets/threads | 200–400 pts |\n"
                    "| Educational posts | 200–400 pts |\n"
                    "| Comparative analysis posts | 250–400 pts |"
                ),
            },
            {
                "heading": "Discord Tasks — Points Table",
                "body": (
                    "| Task | Points |\n"
                    "|------|--------|\n"
                    "| Join Concrete Discord | 50 pts |\n"
                    "| Participate & level up | Variable |\n"
                    "| Reach Contributor role | Major bonus |\n"
                    "| Reach **Moai** role (top tier) | Largest bonus |\n\n"
                    "Discord link: [discord.gg/concretexyz](https://discord.gg/concretexyz)"
                ),
            },
            {
                "heading": "Article of the Week — Content Creation",
                "body": (
                    "- Every Monday Discord mein **rubric post** hota hai\n"
                    "- Apna article us rubric ke mutabiq likho\n"
                    "- Submit karo review ke liye\n"
                    "- **Accepted article: +400 Bags/Points** per week\n"
                    "- Max 1 submission per week\n"
                    "- Requirements: Clarity · Research depth · Value-add · Accuracy · Originality\n"
                    "- Top articles: Bonus points + featured in community"
                ),
            },
            {
                "heading": "Platform Tasks",
                "body": (
                    "| Task | Points |\n"
                    "|------|--------|\n"
                    "| Daily check-ins | Variable |\n"
                    "| Profile completion | Variable |\n"
                    "| Identity verification | Variable |\n"
                    "| Referral (per successful referral) | Bonus bags |"
                ),
            },
            {
                "heading": "Step-by-Step: Bags Earn Karna Shuru Karo",
                "body": (
                    "1. [points.concrete.xyz/home](https://points.concrete.xyz/home) kholo\n"
                    "2. **Connect Wallet** — top-right (EVM wallet chahiye)\n"
                    "3. **Linked Accounts** pe jao → X aur Discord connect karo\n"
                    "4. **Quests tab** mein tasks dekho aur complete karo\n"
                    "5. Locked tasks unlock karne ke liye pehle wala task complete karo\n"
                    "6. Apna **referral link** share karo extra bags ke liye\n"
                    "7. **Leaderboard** tab pe apni rank dekho"
                ),
            },
            {
                "heading": "Airdrop Strategy Tips",
                "body": (
                    "- **Early participation** matters — jo pehle aate hain unhe zyada allocation milti hai historically\n"
                    "- Previous DeFi airdrops mein early users ko **2-5x larger allocation** mila\n"
                    "- Bags → Concrete Points conversion ratio abhi **TBA** hai\n"
                    "- **Phase 2** (coming soon): Platform usage se bhi bags milenge (on-chain leaderboard)\n"
                    "- Consistency zyada important hai — daily tasks miss mat karo"
                ),
            },
        ],
    },

    "fees_risks": {
        "title": "Fees & Risks",
        "icon": "⚖️",
        "sections": [
            {
                "heading": "Fee Structure — Complete Table",
                "body": (
                    "| Fee Type | Amount | Details |\n"
                    "|----------|--------|---------|\n"
                    "| Deposit Fee | ❌ None | Free entry into vaults |\n"
                    "| Withdrawal Fee | ❌ None | Free exit anytime |\n"
                    "| Maintenance Fee | ❌ None | Protocol bears operational cost |\n"
                    "| Performance Fee | ❌ None | No profit-sharing charge |\n"
                    "| **Vault Fee (AUM)** | ✅ **1.5% annualized** | On deposited capital |\n"
                    "| **Sentora/Lombard Vault Fee** | ✅ **1.25% annualized** | Reduced rate |\n\n"
                    "**Example:** $10,000 deposit mein ~$150/year vault fee lagti hai."
                ),
            },
            {
                "heading": "Smart Contract Risk",
                "body": (
                    "- Sab vaults smart contracts se governed hain\n"
                    "- Audited hain lekin 100% safe kabhi bhi nahi hota\n\n"
                    "**How Concrete mitigates:**\n"
                    "- ✅ Regular audits by Halborn, Zellic, Cantina, Code4rena\n"
                    "- ✅ Open-source contracts with community review\n"
                    "- ✅ Bug bounty programs\n"
                    "- ✅ Ongoing security testing"
                ),
            },
            {
                "heading": "Impermanent Loss (IL)",
                "body": (
                    "LP pools mein token prices diverge hone se IL hoti hai.\n\n"
                    "**Zyada likely when:**\n"
                    "- Non-stablecoin pairs (ETH/BTC)\n"
                    "- Volatile markets\n"
                    "- New chain pre-deposit campaigns\n\n"
                    "**Mitigation:**\n"
                    "- Diversified vault strategies\n"
                    "- Dynamic reallocation during volatility"
                ),
            },
            {
                "heading": "Slippage Risk",
                "body": (
                    "Expected aur actual trade execution price mein difference.\n\n"
                    "**Zyada likely when:**\n"
                    "- Volatile ya thinly traded tokens\n"
                    "- High market activity\n"
                    "- Large trades relative to pool size\n\n"
                    "**Mitigation:**\n"
                    "- 1inch aggregator integration (optimal routing)\n"
                    "- Built-in slippage protection\n"
                    "- UI warnings when slippage exceeds threshold"
                ),
            },
            {
                "heading": "Strategy-Specific & Market Risk",
                "body": (
                    "- Underlying protocols (Aave, Pendle, Morpho) ke apne risks\n"
                    "- Market volatility se asset value ghat sakti hai\n"
                    "- Yields guaranteed nahi hain — variable hain\n\n"
                    "**Mitigation:**\n"
                    "- Protocol vetting aur monitoring\n"
                    "- Capped exposures for experimental strategies\n"
                    "- Transparent allocation disclosures"
                ),
            },
            {
                "heading": "Safety Infrastructure",
                "body": (
                    "| System | Role |\n"
                    "|--------|------|\n"
                    "| **TRES Finance** | Independent accounting verification |\n"
                    "| **Hypernative** | Real-time on-chain threat monitoring |\n"
                    "| **ZeroShadow** | On-chain security monitoring |\n"
                    "| **Role-Based Access** | No single point of failure |\n"
                    "| **Subgraph Indexing** | Full on-chain transparency |\n"
                    "| **Open Source** | Community review enabled |"
                ),
            },
            {
                "heading": "Restricted Jurisdictions",
                "body": (
                    "Kuch countries mein Concrete use karna allowed nahi.\n\n"
                    "Full list dekho: [docs.concrete.xyz/restrictions](https://docs.concrete.xyz/restrictions/)"
                ),
            },
        ],
    },

    "audits": {
        "title": "Security Audits — Complete List",
        "icon": "🔐",
        "sections": [
            {
                "heading": "Audit Firms",
                "body": (
                    "| Firm | Specialty |\n"
                    "|------|-----------|\n"
                    "| **Cantina** | Smart contract deep review |\n"
                    "| **Halborn** | Blockchain security |\n"
                    "| **Zellic** | Code vulnerability assessment |\n"
                    "| **Code4rena** | Community-based competitive audit |\n\n"
                    "**Ongoing Monitoring:**\n"
                    "- **Hypernative** — Real-time threat detection\n"
                    "- **ZeroShadow** — On-chain security monitoring\n"
                    "- **TRES Finance** — Independent accounting"
                ),
            },
            {
                "heading": "Audit History (2025-2026)",
                "body": (
                    "| Date | Contract/Module | Auditor |\n"
                    "|------|-----------------|--------|\n"
                    "| Feb 20, 2026 | Earn V2 Core | Cantina |\n"
                    "| Feb 13, 2026 | Looping Strategy Swapper | Halborn |\n"
                    "| Jan 09, 2026 | AssetCX | Halborn |\n"
                    "| Dec 18, 2025 | Earn V2 Whitelisting Hook | Halborn |\n"
                    "| Oct 23, 2025 | Earn V2 Predeposit Vault | Halborn |\n"
                    "| Oct 10, 2025 | Earn V2 Core - Async | Halborn |\n"
                    "| Oct 10, 2025 | Earn V2 Core - Standard | Halborn |\n"
                    "| Sep 29, 2025 | Upgradable Multisig & Queue | Halborn |\n"
                    "| Jul 19, 2025 | Earn V1 | Halborn |\n"
                    "| Jun 06, 2025 | Earn V1 | Zellic |\n"
                    "| May 16, 2025 | Withdrawal Queue Toggle | Halborn |\n"
                    "| Mar 28, 2025 | Morpho Strategy Auto-Compounding | Halborn |\n"
                    "| Mar 24, 2025 | Curve/Pendle Strategy | Halborn |"
                ),
            },
            {
                "heading": "Audit Approach",
                "body": (
                    "1. **Initial Development Review** — In-house + third-party during dev phase\n"
                    "2. **External Audit Partnerships** — Detailed code review + vulnerability assessment\n"
                    "3. **Ongoing Monitoring** — Post-deployment continuous security checks\n"
                    "4. **Public Transparency** — All reports publicly accessible\n\n"
                    "📄 All reports: [docs.concrete.xyz/audits](https://docs.concrete.xyz/audits/)"
                ),
            },
        ],
    },

    "enterprise": {
        "title": "Enterprise & Institutional",
        "icon": "🏢",
        "sections": [
            {
                "heading": "Concrete Enterprise",
                "body": (
                    "Institutional aur large capital allocators ke liye dedicated solutions.\n\n"
                    "**Link:** [enterprise.concrete.xyz](https://enterprise.concrete.xyz)"
                ),
            },
            {
                "heading": "AssetCX — Flagship Enterprise Product",
                "body": (
                    "AssetCX CeFi custody aur DeFi yield ko bridge karta hai:\n\n"
                    "> **\"Custody assets in CeFi while earning DeFi yield\"**\n\n"
                    "- Institutional clients assets traditional custodians ke paas rakh sakte hain\n"
                    "- Simultaneously Concrete ke through DeFi yield earn karte hain\n"
                    "- Best of both worlds: CeFi ki security + DeFi ke returns\n\n"
                    "**Audit:** January 09, 2026 by Halborn"
                ),
            },
            {
                "heading": "Enterprise Partners",
                "body": (
                    "| Partner | Role |\n"
                    "|---------|------|\n"
                    "| **BitGo** | Institutional custody |\n"
                    "| **Fireblocks** | Asset security & transfer |\n"
                    "| **Binance Wallet** | USDT yield for Binance users |\n"
                    "| **Coinbase** | Custodian integration |\n"
                    "| **Figment** | BTC & XRP institutional staking |\n"
                    "| **Theo (thUSD)** | Genesis vault for yield-bearing stablecoin |"
                ),
            },
            {
                "heading": "Binance Wallet Integration (March 2026)",
                "body": (
                    "Latest major partnership (March 12, 2026):\n\n"
                    "- Binance Wallet users ab directly USDT yield strategies access kar sakte hain\n"
                    "- Binance Wallet app se bahar jane ki zarurat nahi\n"
                    "- Institutional-grade vault infrastructure retail Binance users ke liye bhi available\n"
                    "- Concrete ki vault technology world ke largest wallet ecosystems mein se ek mein integrate"
                ),
            },
            {
                "heading": "Figment Partnership (Nov 2025)",
                "body": (
                    "- Concrete + Figment milke BTC aur XRP pe institutional access expand kar rahe hain\n"
                    "- Figment leading independent staking infrastructure provider hai\n"
                    "- Figment ke institutional clients ke liye Concrete yield solutions available"
                ),
            },
            {
                "heading": "Enterprise Features",
                "body": (
                    "- ✅ Factory-deployed custom vaults for partners\n"
                    "- ✅ Role-based operational controls (Vault Manager, Allocator, etc.)\n"
                    "- ✅ Independent accounting (TRES Finance)\n"
                    "- ✅ Real-time monitoring (Hypernative)\n"
                    "- ✅ Regulatory-friendly architecture\n"
                    "- ✅ Segregation of duties (strategy vs. custody)\n"
                    "- ✅ On-chain curator identity & verification\n"
                    "- ✅ Auditable vault contracts (Halborn, Cantina)"
                ),
            },
        ],
    },

    "ecosystem": {
        "title": "Ecosystem & Roadmap",
        "icon": "🌐",
        "sections": [
            {
                "heading": "DeFi Protocol Integrations",
                "body": (
                    "| Protocol | Role in Concrete |\n"
                    "|----------|------------------|\n"
                    "| **Pendle** | Yield tokenization strategies |\n"
                    "| **Morpho** | Lending optimization |\n"
                    "| **Euler** | Money market |\n"
                    "| **Aave** | Lending market |\n"
                    "| **Compound** | Lending market |\n"
                    "| **Curve** | Stable pool liquidity |\n"
                    "| **EigenLayer** | ETH restaking |\n"
                    "| **1inch** | Swap aggregation (slippage protection) |"
                ),
            },
            {
                "heading": "Ecosystem Link",
                "body": "[concrete.xyz/ecosystem](https://concrete.xyz/ecosystem) — All partner protocols aur integrations",
            },
            {
                "heading": "Blueprint Finance — Parent Company",
                "body": (
                    "- **Concrete** (Ethereum) — Institutional DeFi vaults\n"
                    "- **Glow Finance** (Solana) — Yield, trading & lending on Solana\n\n"
                    "Dono milke complete multi-chain DeFi infrastructure banate hain."
                ),
            },
            {
                "heading": "Community Tools (Community-Built)",
                "body": (
                    "| Tool | URL |\n"
                    "|------|-----|\n"
                    "| 📊 Vault Tracker | [concrete-vault--mkashifali130.replit.app](https://concrete-vault--mkashifali130.replit.app/) |\n"
                    "| 📖 Community Guide | [concrete-guide.streamlit.app](https://concrete-guide.streamlit.app/) |"
                ),
            },
            {
                "heading": "Future Roadmap",
                "body": (
                    "| Product | Description | Status |\n"
                    "|---------|-------------|--------|\n"
                    "| **Concrete Borrow** | Borrow against deposits — no liquidation risk | Coming Soon |\n"
                    "| **Concrete Protect** | Multi-layered liquidation protection | Coming Soon |\n"
                    "| **Stablecoin Borrowing** | Borrow stables against vault deposits | Planned |\n"
                    "| **Cross-Chain Swaps** | Asset swap within platform | Planned |\n"
                    "| **Community Vaults** | Users create own yield strategies | Planned |\n"
                    "| **Ecosystem ETFs** | Diversified cross-protocol portfolios | Planned |\n"
                    "| **Phase 2 Points** | On-chain leaderboard (platform usage) | Coming Soon |"
                ),
            },
        ],
    },

    "links": {
        "title": "All Official Links",
        "icon": "🔗",
        "sections": [
            {
                "heading": "Main Products",
                "body": (
                    "| Platform | URL |\n"
                    "|----------|-----|\n"
                    "| 🌐 Main Website | [concrete.xyz](https://concrete.xyz) |\n"
                    "| 💎 Earn App | [app.concrete.xyz/earn](https://app.concrete.xyz/earn) |\n"
                    "| 🎯 Points Dashboard | [points.concrete.xyz/home](https://points.concrete.xyz/home) |\n"
                    "| 📚 Documentation | [docs.concrete.xyz](https://docs.concrete.xyz) |\n"
                    "| 🌐 Ecosystem | [concrete.xyz/ecosystem](https://concrete.xyz/ecosystem) |\n"
                    "| 🏢 Enterprise | [enterprise.concrete.xyz](https://enterprise.concrete.xyz) |"
                ),
            },
            {
                "heading": "Documentation Pages",
                "body": (
                    "| Page | URL |\n"
                    "|------|-----|\n"
                    "| Welcome | [docs.concrete.xyz/Overview/welcome](https://docs.concrete.xyz/Overview/welcome/) |\n"
                    "| How It Works | [docs.concrete.xyz/Overview/how-it-works](https://docs.concrete.xyz/Overview/how-it-works/) |\n"
                    "| Our Solution | [docs.concrete.xyz/Overview/our-solution](https://docs.concrete.xyz/Overview/our-solution/) |\n"
                    "| Earn V2 | [docs.concrete.xyz/Earn-V2/overview](https://docs.concrete.xyz/Earn-V2/overview/) |\n"
                    "| Vaults | [docs.concrete.xyz/Vaults/yield-vaults](https://docs.concrete.xyz/Vaults/yield-vaults/) |\n"
                    "| Fees | [docs.concrete.xyz/fees](https://docs.concrete.xyz/fees/) |\n"
                    "| Risks | [docs.concrete.xyz/risks](https://docs.concrete.xyz/risks/) |\n"
                    "| Audits | [docs.concrete.xyz/audits](https://docs.concrete.xyz/audits/) |\n"
                    "| Restrictions | [docs.concrete.xyz/restrictions](https://docs.concrete.xyz/restrictions/) |\n"
                    "| Support | [docs.concrete.xyz/support](https://docs.concrete.xyz/support/) |"
                ),
            },
            {
                "heading": "Community & Social",
                "body": (
                    "| Platform | URL |\n"
                    "|----------|-----|\n"
                    "| 🐦 Twitter/X | [x.com/ConcreteXYZ](https://x.com/ConcreteXYZ) |\n"
                    "| 💬 Discord | [discord.gg/concretexyz](https://discord.gg/concretexyz) |\n"
                    "| 📝 Blog | [concrete.xyz/blog](https://concrete.xyz/blog) |\n"
                    "| 🪞 Mirror | [mirror.xyz/concretexyz.eth](https://mirror.xyz/concretexyz.eth) |\n\n"
                    "**Team Twitter:**\n"
                    "- CEO: [@nic_builds](https://x.com/nic_builds)\n"
                    "- [@dill_sl](https://x.com/dill_sl)\n"
                    "- [@crypttoji](https://x.com/crypttoji)"
                ),
            },
            {
                "heading": "Community-Built Tools",
                "body": (
                    "| Tool | URL |\n"
                    "|------|-----|\n"
                    "| 📊 Vault Tracker | [concrete-vault--mkashifali130.replit.app](https://concrete-vault--mkashifali130.replit.app/) |\n"
                    "| 📖 Community Guide | [concrete-guide.streamlit.app](https://concrete-guide.streamlit.app/) |"
                ),
            },
            {
                "heading": "Legal",
                "body": (
                    "| Document | URL |\n"
                    "|----------|-----|\n"
                    "| Terms of Use | [concrete.xyz/terms](https://concrete.xyz/terms) |\n"
                    "| Privacy Policy | [concrete.xyz/privacy-policy](https://concrete.xyz/privacy-policy) |\n"
                    "| Disclaimers | [concrete.xyz/disclaimers](https://concrete.xyz/disclaimers) |"
                ),
            },
        ],
    },

    "faq": {
        "title": "FAQ — Aksar Pooche Jane Wale Sawal",
        "icon": "❓",
        "sections": [
            {
                "heading": "Protocol Basics",
                "body": (
                    "**Q: Concrete Protocol kya hai?**\n"
                    "A: Ek institutional-grade DeFi platform jo automated vault strategies se yield optimize karta hai. Deposit karo — baki sab Concrete handle karta hai.\n\n"
                    "**Q: Mujhe kya wallet chahiye?**\n"
                    "A: Koi bhi EVM-compatible — MetaMask, Rainbow, WalletConnect, Coinbase Wallet.\n\n"
                    "**Q: Minimum deposit kitna hai?**\n"
                    "A: Official docs mein specific minimum nahi. Gas fees ka dhyan rakhein.\n\n"
                    "**Q: Kya deposits safe hain?**\n"
                    "A: Vaults thoroughly audited hain (Halborn, Zellic, Cantina), lekin DeFi mein risk hamesha hota hai. Concrete ne abhi tak koi major exploit face nahi kiya."
                ),
            },
            {
                "heading": "Fees & Yield",
                "body": (
                    "**Q: Fees kya hain?**\n"
                    "A: Deposit, withdrawal, maintenance — sab zero. Sirf 1.5% annual vault fee (AUM-based).\n\n"
                    "**Q: APY guaranteed hai?**\n"
                    "A: Nahi. Yields variable hain aur market conditions pe depend karte hain. Target APY sirf indicative hai.\n\n"
                    "**Q: Withdrawal kab milegi?**\n"
                    "A: Standard vaults: instant. Async vaults: next epoch (no withdrawal fee)."
                ),
            },
            {
                "heading": "Points & Airdrop",
                "body": (
                    "**Q: Bags aur Points mein kya fark hai?**\n"
                    "A: Bags abhi earn hoti hain social tasks se. Yeh baad mein Concrete Points mein convert hongi. Points future token allocation mein count honge.\n\n"
                    "**Q: Token kab launch hoga?**\n"
                    "A: April 2026 tak koi official announcement nahi. Points campaign strong indicator hai.\n\n"
                    "**Q: Referral se kitne points?**\n"
                    "A: Har successful referral pe bonus bags. Exact amount dynamic hai.\n\n"
                    "**Q: Kya Pakistan se use kar sakte hain?**\n"
                    "A: [docs.concrete.xyz/restrictions](https://docs.concrete.xyz/restrictions/) check karo — Pakistan generally accessible hai."
                ),
            },
            {
                "heading": "Technical Questions",
                "body": (
                    "**Q: WeETH vault itna bada kyun hai ($705M)?**\n"
                    "A: WeETH (Wrapped EigenLayer ETH) pe institutional demand bahut zyada hai — Concrete ka largest vault hai.\n\n"
                    "**Q: ct[asset] tokens kahan use ho sakte hain?**\n"
                    "A: Pendle (yield tokenization), Morpho (collateral), Euler (borrowing base).\n\n"
                    "**Q: Earn V1 aur V2 mein kya fark hai?**\n"
                    "A: V2 fully automated hai — daily NAV updates, role-based automation, async withdrawals. V1 manual tha.\n\n"
                    "**Q: Support kahan milega?**\n"
                    "A: Discord: [discord.gg/concretexyz](https://discord.gg/concretexyz) ya Docs Support page."
                ),
            },
        ],
    },

    # ── NEW: Discord Roles & XP Levels ──────────────────────────────────────
    "discord_roles": {
        "title": "Discord Roles, XP & Levels",
        "icon": "🎮",
        "sections": [
            {
                "heading": "XP System Kya Hai?",
                "body": (
                    "Concrete Discord pe chatting karne se **XP (Experience Points)** milte hain. "
                    "Jitna zyada engage karo, utna zyada XP, utna zyada level up!\n\n"
                    "Kuch specific levels pe **special roles + BAGS milestone rewards** unlock hote hain.\n\n"
                    "**Discord Join Karo:** [discord.gg/concretexyz](https://discord.gg/concretexyz)"
                ),
            },
            {
                "heading": "Complete Level Table (Lv.1 – Lv.25)",
                "body": (
                    "| Level | XP Needed | Role Unlocked | Reward |\n"
                    "|-------|-----------|---------------|--------|\n"
                    "| Lv.1  | 100 XP    | —             | —      |\n"
                    "| Lv.2  | 155 XP    | —             | —      |\n"
                    "| Lv.3  | 220 XP    | —             | —      |\n"
                    "| Lv.4  | 295 XP    | —             | —      |\n"
                    "| **Lv.5**  | **380 XP**  | **🗿 NEWBIE ROLE**       | **+50 BAGS**  |\n"
                    "| Lv.6  | 475 XP    | —             | —      |\n"
                    "| Lv.7  | 580 XP    | —             | —      |\n"
                    "| Lv.8  | 695 XP    | —             | —      |\n"
                    "| Lv.9  | 820 XP    | —             | —      |\n"
                    "| **Lv.10** | **955 XP**  | **🧭 VAULT NAVIGATOR**   | **+150 BAGS** |\n"
                    "| Lv.11 | 1,100 XP  | —             | —      |\n"
                    "| Lv.12 | 1,250 XP  | —             | —      |\n"
                    "| Lv.13 | 1,420 XP  | —             | —      |\n"
                    "| Lv.14 | 1,590 XP  | —             | —      |\n"
                    "| Lv.15 | 1,780 XP  | —             | —      |\n"
                    "| Lv.16 | 1,980 XP  | —             | —      |\n"
                    "| **Lv.17** | **2,180 XP** | **☘️ LUCKY 17 ROLE**    | **+250 pts**  |\n"
                    "| Lv.18 | 2,400 XP  | —             | —      |\n"
                    "| Lv.19 | 2,620 XP  | —             | —      |\n"
                    "| Lv.20 | 2,850 XP  | —             | —      |\n"
                    "| Lv.21 | 3,620 XP  | —             | —      |\n"
                    "| Lv.22 | 3,900 XP  | —             | —      |\n"
                    "| Lv.23 | 3,620 XP  | —             | —      |\n"
                    "| Lv.24 | 3,900 XP  | —             | —      |\n"
                    "| **Lv.25** | **4,180 XP** | **🏆 GRINDOOR ROLE**    | **+1000 pts** |\n"
                ),
            },
            {
                "heading": "Roles & Their Perks",
                "body": (
                    "| Role | Unlock | Perks |\n"
                    "|------|--------|-------|\n"
                    "| 👶 **Newcomer** | Discord join karte hi | Basic channels, community chat, XP start |\n"
                    "| 🗿 **Newbie** | Lv.5 — 380 XP | +50 BAGS, more channels, recognized member |\n"
                    "| 🧭 **Vault Navigator** | Lv.10 — 955 XP | +150 BAGS, vault discussions, early protocol updates |\n"
                    "| ☘️ **Lucky 17** | Lv.17 — 2,180 XP | +250 pts, exclusive events, special channels |\n"
                    "| 🏆 **Grindoor** | Lv.25 — 4,180 XP | +1000 pts, top community member, max perks |\n"
                    "| 📝 **Writer / Contributor** | Quality article submit karo | Writer badge, extra XP, community visibility |\n"
                    "| 🗿 **MOAI (Elite)** | Season end — top contributors | Awarded to top community builders — rare! |"
                ),
            },
            {
                "heading": "XP Fast Earn Tips",
                "body": (
                    "- 💬 **Daily Chat:** Har roz Discord pe messages karo — quality over quantity\n"
                    "- 📝 **Articles:** Mirror/Paragraph pe community articles → extra XP + pts\n"
                    "- 🤝 **Referrals:** Dosto ko Discord invite karo — referrals = XP\n"
                    "- 🎯 **Events:** AMAs, Twitter Spaces, community events mein participate karo\n"
                    "- ❓ **Q&A:** Helpful answers aur questions bhi engagement mein count hote hain"
                ),
            },
        ],
    },

    # ── NEW: KEY Conditions ──────────────────────────────────────────────────
    "key_conditions": {
        "title": "KEY Role — 4 Conditions",
        "icon": "🗝️",
        "sections": [
            {
                "heading": "KEY Kya Hai?",
                "body": (
                    "**KEY** Concrete community mein ek special access/role hai. "
                    "Yeh unhe milti hai jo consistently value add karte hain — support, content creation, "
                    "aur platform engagement ke zariye.\n\n"
                    "KEY holders ko exclusive community recognition milti hai."
                ),
            },
            {
                "heading": "4 Conditions to Get KEY",
                "body": (
                    "**1. 🤝 Friendly Support**\n"
                    "Naye members ki help karo, sawalo ke jawab do, Discord mein welcoming raho. "
                    "Aapka attitude matter karta hai — kisi ko community mein ghar jaisa feel karao.\n\n"
                    "**2. 😂 Daily Memes**\n"
                    "Har roz Concrete-related memes banao. Memes channel mein post karo. "
                    "Creative, funny aur on-topic content notice hoti hai. "
                    "Tools: DALL-E, Canva, CapCut, ya manual design.\n\n"
                    "**3. 🤖 Server Moderation Help**\n"
                    "Spam report karo, moderation tasks mein help karo, channels ko clean aur organized rakho. "
                    "Responsible community member bano.\n\n"
                    "**4. 📱 X (Twitter) = 2-3 Posts/Day**\n"
                    "X/Twitter pe roz 2-3 baar Concrete ke baare mein post karo. "
                    "#ConcreteDeFi tag use karo. Updates, vault experience, educational content share karo. "
                    "Consistent Twitter presence key hai!"
                ),
            },
            {
                "heading": "MOAI — Elite Tier",
                "body": (
                    "**🗿 MOAI** sabse bada community role hai:\n\n"
                    "- Season end pe diya jata hai\n"
                    "- Sirf top contributors ko milta hai\n"
                    "- Concrete DeFi tag use karna zaruri hai\n"
                    "- #announcements channel dekho zyada info ke liye\n\n"
                    "> Rare aur prestigious — sirf sabse dedicated builders ke liye!"
                ),
            },
        ],
    },

    # ── NEW: Vault Technical Data ────────────────────────────────────────────
    "vault_tech": {
        "title": "Vault Technical Data & Addresses",
        "icon": "🔬",
        "sections": [
            {
                "heading": "On-Chain Vault Addresses (Ethereum Mainnet)",
                "body": (
                    "| Vault | Asset | Contract Address |\n"
                    "|-------|-------|------------------|\n"
                    "| 🏦 WeETH (Institutional) | WETH | `0xB9DC54c8261745CB97070CeFBE3D3d815aee8f20` |\n"
                    "| ₿ ctWBTC | WBTC | `0xacce65B9dB4810125adDEa9797BaAaaaD2B73788` |\n"
                    "| 💵 ctUSD (Stable) | USDC | `0x0E609b710da5e0AA476224b6c0e5445cCc21251E` |\n"
                    "| ⚡ frxUSD+ | FRAX | `0xCF9ceAcf5c7d6D2FE6e8650D81FbE4240c72443f` |\n\n"
                    "**Verify on Etherscan:** [etherscan.io](https://etherscan.io)"
                ),
            },
            {
                "heading": "Vault Health Factor Guide",
                "body": (
                    "Health Factor (HF) vault ki safety measure karta hai (Aave V3 se read hota hai):\n\n"
                    "| HF Range | Status | Color |\n"
                    "|----------|--------|-------|\n"
                    "| HF > 3.0 | 🟢 SAFE | Green |\n"
                    "| HF 2.0–3.0 | 🟡 LOW RISK | Yellow |\n"
                    "| HF 1.5–2.0 | 🟠 MEDIUM RISK | Orange |\n"
                    "| HF 1.1–1.5 | 🔴 HIGH RISK | Red-Orange |\n"
                    "| HF < 1.0 | ⚫ LIQUIDATABLE | Critical |\n\n"
                    "**Formula:** `getUserAccountData(vaultAddress)` pe Aave V3 Pool se milta hai, 1e18 se scale hota hai."
                ),
            },
            {
                "heading": "Vault Risk & Performance Snapshot",
                "body": (
                    "| Vault | APY | Health Factor | Risk | Strategy |\n"
                    "|-------|-----|---------------|------|----------|\n"
                    "| WeETH (Institutional) | 7.84% | 3.82 (SAFE) | LOW | Aave V3 + Silo Restaking |\n"
                    "| ctWBTC | 5.21% | 2.14 (LOW) | MEDIUM | Morpho + Radiant Delta-Neutral |\n"
                    "| ctUSD (Stable) | 9.12% | 4.51 (SAFE) | LOW | Morpho + Silo + Aave V3 |\n"
                    "| frxUSD+ | 18.44% | 1.38 (HIGH) | HIGH | EigenLayer + Morpho + Silo |"
                ),
            },
            {
                "heading": "Efficiency Index — Kya Hai?",
                "body": (
                    "Concrete ka internal performance scoring system:\n\n"
                    "```\n"
                    "Efficiency Index = (Avg APY / (1 + APY Volatility)) × Util Stability × 100\n"
                    "```\n\n"
                    "Raw APY se zyada reliable metric hai — consistent yield vs. volatile yield compare karta hai.\n\n"
                    "**6 Vault DNA Dimensions:**\n"
                    "- Yield Consistency — Kitna stable rehta hai APY\n"
                    "- Liquidity Depth — Withdrawal ke liye liquidity\n"
                    "- Strategy Diversity — Kitne protocols use\n"
                    "- Protocol Maturity — Underlying protocols ki age/reliability\n"
                    "- Util Stability — Utilization rate stability\n"
                    "- Efficiency Index — Overall composite score"
                ),
            },
            {
                "heading": "Community Vault Intelligence Tool",
                "body": (
                    "Community-built vault tracker jo real-time data fetch karta hai:\n\n"
                    "**🔗 [concrete-vault.streamlit.app](https://concrete-vault.streamlit.app/)**\n\n"
                    "Features:\n"
                    "- Live APY tracking (app.concrete.xyz → DeFiLlama → ETH RPC → Simulated)\n"
                    "- Health Factor monitoring\n"
                    "- Yield Calculator (deposit amount → projected earnings)\n"
                    "- Portfolio Rebalancer\n"
                    "- Smart Alerts\n"
                    "- Vault DNA Fingerprint\n\n"
                    "*Built by @mkashifalikcp — community contributor. Not affiliated with Concrete Protocol.*"
                ),
            },
        ],
    },
}

# ══════════════════════════════════════════════════════════════════════════════
# LINK MAP — Topic ke hisab se relevant links suggest karta hai
# ══════════════════════════════════════════════════════════════════════════════
LINK_MAP = {
    "overview":      [("💎 Earn App", "https://app.concrete.xyz/earn"),
                      ("📚 Docs Overview", "https://docs.concrete.xyz/Overview/welcome/"),
                      ("🌐 concrete.xyz", "https://concrete.xyz"),
                      ("🐦 Twitter/X", "https://x.com/ConcreteXYZ")],
    "how_it_works":  [("📖 How It Works (Docs)", "https://docs.concrete.xyz/Overview/how-it-works/"),
                      ("🔧 Earn V2 Overview", "https://docs.concrete.xyz/Earn-V2/overview/"),
                      ("💎 Earn App", "https://app.concrete.xyz/earn")],
    "vaults":        [("💎 Earn App — Live Vaults", "https://app.concrete.xyz/earn"),
                      ("📖 Vaults Docs", "https://docs.concrete.xyz/Vaults/yield-vaults/"),
                      ("📊 Vault Intelligence Tool", "https://concrete-vault.streamlit.app/")],
    "earn_guide":    [("💎 Earn App", "https://app.concrete.xyz/earn"),
                      ("📖 Our Solution (Docs)", "https://docs.concrete.xyz/Overview/our-solution/"),
                      ("⚠️ Restrictions", "https://docs.concrete.xyz/restrictions/")],
    "points":        [("🎯 Points Dashboard", "https://points.concrete.xyz/home"),
                      ("💬 Discord", "https://discord.gg/concretexyz"),
                      ("📖 Concrete 101 Guide", "https://concrete-guide.streamlit.app/")],
    "fees_risks":    [("📖 Fees Docs", "https://docs.concrete.xyz/fees/"),
                      ("📖 Risks Docs", "https://docs.concrete.xyz/risks/"),
                      ("⚠️ Restrictions", "https://docs.concrete.xyz/restrictions/")],
    "audits":        [("🔐 Audits Docs", "https://docs.concrete.xyz/audits/"),
                      ("🌐 Halborn Security", "https://halborn.com"),
                      ("🌐 Cantina Audit", "https://cantina.xyz")],
    "enterprise":    [("🏢 Enterprise Site", "https://enterprise.concrete.xyz"),
                      ("📖 Docs", "https://docs.concrete.xyz"),
                      ("🌐 concrete.xyz", "https://concrete.xyz")],
    "ecosystem":     [("🌐 Ecosystem Page", "https://concrete.xyz/ecosystem"),
                      ("🌿 Glow Finance (Solana)", "https://glowfinance.xyz"),
                      ("📖 Docs", "https://docs.concrete.xyz")],
    "faq":           [("💬 Discord Support", "https://discord.gg/concretexyz"),
                      ("📖 Support Docs", "https://docs.concrete.xyz/support/"),
                      ("🎯 Points Dashboard", "https://points.concrete.xyz/home")],
    "discord_roles": [("💬 Discord", "https://discord.gg/concretexyz"),
                      ("🎯 Points Dashboard", "https://points.concrete.xyz/home"),
                      ("📖 Concrete 101 Guide", "https://concrete-guide.streamlit.app/")],
    "key_conditions":[("💬 Discord", "https://discord.gg/concretexyz"),
                      ("🐦 Twitter/X @ConcreteXYZ", "https://x.com/ConcreteXYZ"),
                      ("🎯 Points Dashboard", "https://points.concrete.xyz/home")],
    "vault_tech":    [("📊 Vault Intelligence Tool", "https://concrete-vault.streamlit.app/"),
                      ("🔍 Etherscan", "https://etherscan.io"),
                      ("💎 Earn App", "https://app.concrete.xyz/earn"),
                      ("📖 Earn V2 Docs", "https://docs.concrete.xyz/Earn-V2/overview/")],
    "links":         [("🌐 concrete.xyz", "https://concrete.xyz"),
                      ("📚 docs.concrete.xyz", "https://docs.concrete.xyz"),
                      ("💬 discord.gg/concretexyz", "https://discord.gg/concretexyz")],
}

# Search karo to LINK_MAP mein relevant links keywords se match karo
KEYWORD_LINKS = {
    "vault":        ("vaults", LINK_MAP["vaults"]),
    "earn":         ("earn_guide", LINK_MAP["earn_guide"]),
    "apy":          ("vaults", LINK_MAP["vaults"]),
    "deposit":      ("earn_guide", LINK_MAP["earn_guide"]),
    "withdraw":     ("earn_guide", LINK_MAP["earn_guide"]),
    "fees":         ("fees_risks", LINK_MAP["fees_risks"]),
    "risk":         ("fees_risks", LINK_MAP["fees_risks"]),
    "audit":        ("audits", LINK_MAP["audits"]),
    "points":       ("points", LINK_MAP["points"]),
    "bags":         ("points", LINK_MAP["points"]),
    "airdrop":      ("points", LINK_MAP["points"]),
    "discord":      ("discord_roles", LINK_MAP["discord_roles"]),
    "xp":           ("discord_roles", LINK_MAP["discord_roles"]),
    "level":        ("discord_roles", LINK_MAP["discord_roles"]),
    "role":         ("discord_roles", LINK_MAP["discord_roles"]),
    "key":          ("key_conditions", LINK_MAP["key_conditions"]),
    "meme":         ("key_conditions", LINK_MAP["key_conditions"]),
    "twitter":      ("key_conditions", LINK_MAP["key_conditions"]),
    "moai":         ("key_conditions", LINK_MAP["key_conditions"]),
    "enterprise":   ("enterprise", LINK_MAP["enterprise"]),
    "assetcx":      ("enterprise", LINK_MAP["enterprise"]),
    "binance":      ("enterprise", LINK_MAP["enterprise"]),
    "health":       ("vault_tech", LINK_MAP["vault_tech"]),
    "address":      ("vault_tech", LINK_MAP["vault_tech"]),
    "contract":     ("vault_tech", LINK_MAP["vault_tech"]),
    "erc":          ("how_it_works", LINK_MAP["how_it_works"]),
    "cterc":        ("how_it_works", LINK_MAP["how_it_works"]),
    "ct[":          ("how_it_works", LINK_MAP["how_it_works"]),
}

# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #050a0a !important;
    color: #eeeeee !important;
    font-family: 'Courier New', monospace !important;
  }
  [data-testid="stHeader"] { background: transparent !important; }
  [data-testid="stSidebar"] {
    background-color: #080f0f !important;
    border-right: 1px solid rgba(0,255,136,0.12) !important;
  }
  #MainMenu, footer { visibility: hidden; }

  .stat-box {
    background: rgba(0,255,136,0.06);
    border: 1px solid rgba(0,255,136,0.2);
    border-radius: 10px;
    padding: 14px 10px;
    text-align: center;
  }
  .stat-num { font-size: 20px; font-weight: bold; color: #00ff88; }
  .stat-lbl { font-size: 10px; color: #555; letter-spacing: 1px; margin-top: 4px; }

  /* Section card */
  .section-card {
    background: rgba(0,255,136,0.025);
    border: 1px solid rgba(0,255,136,0.1);
    border-radius: 10px;
    padding: 18px 22px 10px 22px;
    margin-bottom: 14px;
  }
  .section-heading {
    font-size: 14px;
    color: #00cc77;
    font-weight: bold;
    letter-spacing: 1px;
    border-bottom: 1px solid rgba(0,255,136,0.1);
    padding-bottom: 6px;
    margin-bottom: 10px;
  }

  h1, h3 { color: #eee !important; }
  h2 { color: #00cc77 !important; }
  a { color: #00cc77 !important; }
  a:hover { color: #00ff88 !important; }

  table { border-collapse: collapse; width: 100%; margin: 6px 0; }
  th { background: rgba(0,255,136,0.1); color: #00ff88; padding: 7px 12px;
       font-size: 12px; border: 1px solid rgba(0,255,136,0.2); }
  td { padding: 6px 12px; font-size: 13px;
       border: 1px solid rgba(255,255,255,0.04); color: #ccc; }
  tr:nth-child(even) td { background: rgba(255,255,255,0.02); }

  code { background: rgba(0,255,136,0.08) !important;
         border: 1px solid rgba(0,255,136,0.2) !important;
         border-radius: 4px; padding: 2px 6px;
         color: #00ff88 !important; font-size: 12px; }
  pre { background: rgba(0,0,0,0.5) !important;
        border: 1px solid rgba(0,255,136,0.15) !important;
        border-radius: 8px; padding: 12px !important; color: #00cc77 !important; }

  blockquote { border-left: 3px solid #00ff88 !important;
               padding-left: 14px; color: #999; font-style: italic; margin: 10px 0; }

  hr { border-color: rgba(0,255,136,0.1) !important; margin: 16px 0; }

  [data-testid="stTextInput"] input {
    background: rgba(0,255,136,0.04) !important;
    border: 1px solid rgba(0,255,136,0.25) !important;
    color: #eee !important; border-radius: 8px !important;
    font-family: 'Courier New', monospace !important;
  }

  ::-webkit-scrollbar { width: 4px; height: 4px; }
  ::-webkit-scrollbar-track { background: #050a0a; }
  ::-webkit-scrollbar-thumb { background: #1a2a1a; border-radius: 2px; }

  .footer-bar {
    text-align: center; font-size: 10px; color: #2a2a2a;
    letter-spacing: 1px; padding: 14px 0;
    border-top: 1px solid rgba(0,255,136,0.06);
    margin-top: 30px;
  }
  .link-box {
    background: rgba(0,204,255,0.04);
    border: 1px solid rgba(0,204,255,0.15);
    border-left: 3px solid #00ccff;
    border-radius: 8px;
    padding: 12px 16px;
    margin-top: 20px;
    margin-bottom: 4px;
  }
  .link-box-title { font-size:10px; color:#00ccff; letter-spacing:2px; font-weight:bold; margin-bottom:8px; }
  .link-pill {
    display:inline-block; background:rgba(0,204,255,0.07);
    border:1px solid rgba(0,204,255,0.2); border-radius:4px;
    padding:3px 10px; margin:3px 4px 3px 0; font-size:11px;
    color:#00ccff !important; text-decoration:none !important;
  }
</style>
""", unsafe_allow_html=True)

# ── Related Links Helpers ──────────────────────────────────────────────────────
def render_links(section_key, extra_links=None):
    links = list(LINK_MAP.get(section_key, []))
    if extra_links:
        for el in extra_links:
            if el not in links:
                links.append(el)
    if not links:
        return
    pills = "".join(
        f"<a href='{url}' target='_blank' class='link-pill'>{lbl}</a>"
        for lbl, url in links
    )
    st.markdown(
        f"<div class='link-box'><div class='link-box-title'>🔗 RELATED LINKS</div>{pills}</div>",
        unsafe_allow_html=True,
    )

def get_links_for_query(q):
    seen, result = set(), []
    for kw, (_, links) in KEYWORD_LINKS.items():
        if kw in q:
            for item in links:
                if item[1] not in seen:
                    seen.add(item[1])
                    result.append(item)
    return result[:6]

# ══════════════════════════════════════════════════════════════════════════════
# LANGUAGE SYSTEM — English / Roman Urdu toggle
# ══════════════════════════════════════════════════════════════════════════════
if "lang" not in st.session_state:
    st.session_state.lang = "en"
if "selected" not in st.session_state:
    st.session_state.selected = "overview"
if "search_q" not in st.session_state:
    st.session_state.search_q = ""

def T(en_text, ur_text):
    """Return English or Roman Urdu text based on language toggle."""
    return ur_text if st.session_state.lang == "ur" else en_text

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div style='text-align:center; padding:10px 0 4px;'>
      <div style='font-size:34px;'>🏛️</div>
      <div style='font-size:14px; font-weight:bold; background:linear-gradient(90deg,#00ff88,#00ccff);
           -webkit-background-clip:text; -webkit-text-fill-color:transparent; letter-spacing:2px;'>
        CONCRETE NEXUS
      </div>
      <div style='font-size:9px; color:#333; letter-spacing:2px; margin-top:2px;'>
        {T("COMPLETE ECOSYSTEM GUIDE", "MUKAMMAL GUIDE")}
      </div>
    </div>
    <hr style='margin:10px 0 12px;'>
    """, unsafe_allow_html=True)

    # ── Language Toggle ──
    st.markdown(f"<div style='font-size:9px;color:#333;letter-spacing:2px;margin-bottom:6px;'>🌐 {T('LANGUAGE','ZABAN')}</div>", unsafe_allow_html=True)
    lc1, lc2 = st.columns(2)
    with lc1:
        en_active = "background:rgba(0,255,136,0.15);border:1px solid #00ff88;color:#00ff88;" if st.session_state.lang == "en" else "background:transparent;border:1px solid #1a2a1a;color:#444;"
        if st.button("🇬🇧 English", use_container_width=True, key="lang_en"):
            st.session_state.lang = "en"; st.rerun()
    with lc2:
        ur_active = "background:rgba(0,255,136,0.15);border:1px solid #00ff88;color:#00ff88;" if st.session_state.lang == "ur" else "background:transparent;border:1px solid #1a2a1a;color:#444;"
        if st.button("🇵🇰 Roman Urdu", use_container_width=True, key="lang_ur"):
            st.session_state.lang = "ur"; st.rerun()

    st.markdown("<hr style='margin:12px 0 10px;'>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size:9px;color:#333;letter-spacing:2px;margin-bottom:7px;'>{T('NAVIGATION','NAVIGATION')}</div>", unsafe_allow_html=True)

    NAV_LABELS_EN = {
        "overview":      "🏛️  Overview",
        "how_it_works":  "⚙️  How It Works",
        "vaults":        "💎  Live Vaults",
        "earn_guide":    "📥  Deposit Guide",
        "points":        "🎯  Points & Bags",
        "fees_risks":    "⚖️  Fees & Risks",
        "audits":        "🔐  Security Audits",
        "enterprise":    "🏢  Enterprise",
        "ecosystem":     "🌐  Ecosystem",
        "discord_roles": "🎮  Discord & XP",
        "key_conditions":"🗝️  KEY Role",
        "vault_tech":    "🔬  Vault Tech",
        "faq":           "❓  FAQ",
        "links":         "🔗  All Links",
    }
    NAV_LABELS_UR = {
        "overview":      "🏛️  Overview",
        "how_it_works":  "⚙️  Kaam Kaise Karta Hai",
        "vaults":        "💎  Live Vaults",
        "earn_guide":    "📥  Deposit Guide",
        "points":        "🎯  Points aur Bags",
        "fees_risks":    "⚖️  Fees aur Risk",
        "audits":        "🔐  Security Audits",
        "enterprise":    "🏢  Enterprise",
        "ecosystem":     "🌐  Ecosystem",
        "discord_roles": "🎮  Discord aur XP",
        "key_conditions":"🗝️  KEY Role",
        "vault_tech":    "🔬  Vault Tech",
        "faq":           "❓  Sawal Jawab",
        "links":         "🔗  Tamam Links",
    }
    nav_labels = NAV_LABELS_UR if st.session_state.lang == "ur" else NAV_LABELS_EN

    selected = st.radio(
        "Navigation",
        options=list(nav_labels.keys()),
        format_func=lambda k: nav_labels[k],
        label_visibility="collapsed",
        key="nav_radio",
    )

    st.markdown("<hr style='margin:12px 0 10px;'>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size:9px;color:#333;letter-spacing:2px;margin-bottom:7px;'>{T('QUICK ACCESS','QUICK LINKS')}</div>", unsafe_allow_html=True)
    for lbl, url in [
        ("💎 Earn App", "https://app.concrete.xyz/earn"),
        ("🎯 Points", "https://points.concrete.xyz/home"),
        ("📚 Docs", "https://docs.concrete.xyz"),
        ("💬 Discord", "https://discord.gg/concretexyz"),
        ("🐦 Twitter/X", "https://x.com/ConcreteXYZ"),
        ("🏢 Enterprise", "https://enterprise.concrete.xyz"),
    ]:
        st.markdown(
            f"<a href='{url}' target='_blank' style='display:block;padding:5px 8px;"
            f"font-size:12px;color:#666;text-decoration:none;border-radius:5px;"
            f"margin-bottom:2px;'>{lbl}</a>",
            unsafe_allow_html=True,
        )
    st.markdown(f"""
    <div style='font-size:9px;color:#222;letter-spacing:1px;margin-top:14px;line-height:1.8;text-align:center;'>
    ⚠ {T("NOT FINANCIAL ADVICE · DYOR", "MAALIYATI MASHWARA NAHI · DYOR")}
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# MAIN PAGE — Header + Language Toggle Button + Search Bar (HOMEPAGE)
# ══════════════════════════════════════════════════════════════════════════════

# ── Header with Language Toggle ───────────────────────────────────────────────
hdr_col, btn_col = st.columns([5, 1])
with hdr_col:
    st.markdown(f"""
    <div style='background:rgba(0,0,0,0.55); border:1px solid rgba(0,255,136,0.13);
         border-radius:10px; padding:14px 20px; display:flex; align-items:center;
         gap:14px; margin-bottom:6px;'>
      <div style='font-size:26px;'>🏛️</div>
      <div>
        <div style='font-size:17px; font-weight:bold; background:linear-gradient(90deg,#00ff88,#00ccff);
             -webkit-background-clip:text; -webkit-text-fill-color:transparent; letter-spacing:2px;'>
          CONCRETE NEXUS — {T("COMPLETE GUIDE", "MUKAMMAL GUIDE")}
        </div>
        <div style='font-size:9px; color:#444; letter-spacing:2px; margin-top:2px;'>
          {T("Data sourced from:", "Data source:")} concrete.xyz • docs.concrete.xyz • points.concrete.xyz • enterprise.concrete.xyz
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
with btn_col:
    st.markdown("<div style='padding-top:6px;'></div>", unsafe_allow_html=True)
    btn_label = "🇵🇰 Roman Urdu" if st.session_state.lang == "en" else "🇬🇧 English"
    if st.button(btn_label, use_container_width=True, key="lang_top_toggle"):
        st.session_state.lang = "ur" if st.session_state.lang == "en" else "en"
        st.rerun()

# ── HOMEPAGE SEARCH BAR ───────────────────────────────────────────────────────
st.markdown(f"""
<div style='margin:10px 0 4px; font-size:9px; color:#2a3a2a; letter-spacing:2px;'>
🔍 {T("SEARCH ANYTHING ABOUT CONCRETE PROTOCOL", "CONCRETE PROTOCOL KE BAARE MEIN KUCH BHI SEARCH KARO")}
</div>
""", unsafe_allow_html=True)

search_q = st.text_input(
    "search_main",
    placeholder=T("e.g. vault, apy, bags, discord, key, audit, enterprise...",
                  "misaal: vault, apy, bags, discord, key, audit..."),
    label_visibility="collapsed",
    key="search_main_input",
)

# ── Search Mode ────────────────────────────────────────────────────────────────
if search_q and len(search_q.strip()) > 1:
    q = search_q.lower().strip()
    st.markdown(f"### 🔍 {T('Results for','Nataij:')}: `{search_q}`")
    st.markdown("---")
    found = False
    for key, sec in KB.items():
        hits = []
        for sub in sec["sections"]:
            if q in sub["heading"].lower() or q in sub["body"].lower():
                hits.append(sub)
        if hits:
            found = True
            st.markdown(f"**{sec['icon']} {sec['title']}**")
            for h in hits[:2]:
                st.markdown(f"*{h['heading']}*")
                lines = [l.strip() for l in h["body"].split("\n") if q in l.lower() and l.strip() and len(l.strip()) > 4]
                for ln in lines[:3]:
                    clean = ln.lstrip("#|>*-").strip()
                    if clean:
                        st.markdown(f"> {clean}")
            st.markdown("")
    if not found:
        st.markdown(f"<span style='color:#555;'>'{search_q}' {T('ke liye results nahi mile. Sidebar se section browse karo.','ke liye kuch nahi mila. Sidebar se section choose karo.')}</span>", unsafe_allow_html=True)

    # Relevant links for search
    q_links = get_links_for_query(q)
    pills_html = "".join(
        f"<a href='{url}' target='_blank' class='link-pill'>{lbl}</a>"
        for lbl, url in q_links
    ) if q_links else "".join(
        f"<a href='{url}' target='_blank' class='link-pill'>{lbl}</a>"
        for lbl, url in LINK_MAP["overview"]
    )
    st.markdown(
        f"<div class='link-box'><div class='link-box-title'>🔗 {T('RELATED LINKS','MUTALIQA LINKS')}</div>{pills_html}</div>",
        unsafe_allow_html=True,
    )

# ── Normal Mode ────────────────────────────────────────────────────────────────
else:
    page = KB[selected]

    # Stats bar on overview
    if selected == "overview":
        st.markdown("<br>", unsafe_allow_html=True)
        cols = st.columns(5)
        stat_labels = (
            [("~$902M", "PLATFORM PE"), ("~$11.25B", "PROCESS HUA"), ("$17M", "FUNDING"), ("138K+", "FOLLOWERS"), ("4", "AUDITS")]
            if st.session_state.lang == "ur" else
            [("~$902M", "ON PLATFORM"), ("~$11.25B", "PROCESSED"), ("$17M", "RAISED"), ("138K+", "FOLLOWERS"), ("4", "AUDITS")]
        )
        for col, (num, lbl) in zip(cols, stat_labels):
            col.markdown(f"<div class='stat-box'><div class='stat-num'>{num}</div><div class='stat-lbl'>{lbl}</div></div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

    # Page title
    pg_title = EN_HEADINGS.get(page["title"], page["title"]) if st.session_state.lang == "en" else page["title"]
    st.markdown(f"## {page['icon']} {pg_title}")
    st.markdown("---")

    # Render each sub-section with bilingual headings
    for sub in page["sections"]:
        sh = EN_HEADINGS.get(sub["heading"], sub["heading"]) if st.session_state.lang == "en" else sub["heading"]
        st.markdown(f"<div class='section-card'><div class='section-heading'>▸ {sh}</div></div>", unsafe_allow_html=True)
        body_text = EN_BODIES.get(sub["heading"], sub.get("body_en", sub["body"])) if st.session_state.lang == "en" else sub["body"]
        st.markdown(body_text)
        st.markdown("")

    # Relevant links for this section
    render_links(selected)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class='footer-bar'>
  CONCRETE NEXUS GUIDE • concrete.xyz • docs.concrete.xyz • points.concrete.xyz • enterprise.concrete.xyz<br>
  ⚠️ {T("Educational purposes only — Not financial advice. DeFi involves significant risk. Always DYOR.",
        "Sirf taalimi maqsad — Maaliyati mashwara nahi. DeFi mein nuksaan ka khatra hai. Pehle research karo.")}
</div>
""", unsafe_allow_html=True)
