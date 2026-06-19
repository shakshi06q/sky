import streamlit as st
import random
from pathlib import Path
from datetime import date
import base64

st.set_page_config(
    page_title="Happy Birthday, My Love 💕",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

def img_to_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

START_DATE = date(2026, 1, 11)
DAYS_TOGETHER = (date.today() - START_DATE).days

# ─── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Lato:wght@300;400;700&display=swap');

/* ══ GLOBAL ══════════════════════════════════════════════════════════════════ */
html, body, [class*="css"], .stApp {
    font-family: 'Lato', sans-serif;
    background: #1a0a12 !important;
    color: #ffd6e8;
}
.stApp {
    background:
        radial-gradient(ellipse at 20% 10%, rgba(180,20,80,0.18) 0%, transparent 55%),
        radial-gradient(ellipse at 80% 80%, rgba(140,10,60,0.15) 0%, transparent 55%),
        radial-gradient(ellipse at 50% 50%, rgba(100,5,40,0.1) 0%, transparent 70%),
        #1a0a12 !important;
    min-height: 100vh;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 1.2rem !important;
    padding-bottom: 4rem !important;
    max-width: 520px !important;
    padding-left: 1.2rem !important;
    padding-right: 1.2rem !important;
}

/* remove ALL white/grey streamlit element backgrounds */
.stTextInput > div > div,
.stTextInput input,
[data-baseweb="input"],
[data-baseweb="base-input"] {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(240,98,146,0.35) !important;
    border-radius: 14px !important;
    color: #ffd6e8 !important;
    caret-color: #f06292;
}
.stTextInput input::placeholder { color: rgba(255,180,210,0.4) !important; }
.stTextInput input:focus { border-color: rgba(240,98,146,0.7) !important; box-shadow: 0 0 0 2px rgba(240,98,146,0.15) !important; }
div[data-testid="stColumn"], section[data-testid="stSidebar"] { background: transparent !important; }
[data-testid="stVerticalBlock"] > div { background: transparent !important; }

/* ══ FLOATING HEARTS ════════════════════════════════════════════════════════ */
@keyframes floatUp {
    0%   { transform: translateY(0) scale(1) rotate(-5deg); opacity: 1; }
    100% { transform: translateY(-110vh) scale(1.6) rotate(20deg); opacity: 0; }
}
.fh {
    position: fixed; bottom: -70px; pointer-events: none;
    z-index: 0; user-select: none; animation: floatUp linear infinite;
}

/* ══ BUTTONS BASE ═══════════════════════════════════════════════════════════ */
.stButton > button {
    border-radius: 50px !important;
    font-family: 'Lato', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px !important;
    transition: transform 0.15s, box-shadow 0.15s, opacity 0.15s !important;
    border: none !important;
    cursor: pointer !important;
}
.stButton > button:active { transform: scale(0.96) !important; }

/* ══ PASSWORD PAGE ══════════════════════════════════════════════════════════ */
.pw-wrap {
    text-align: center;
    padding: 2rem 0 1rem;
}
.pw-lock { font-size: 3.5rem; margin-bottom: 0.8rem; }
.pw-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.7rem, 7vw, 2.6rem);
    font-weight: 700; color: #ffb3d1;
    text-shadow: 0 0 30px rgba(255,100,160,0.5);
    line-height: 1.3; margin-bottom: 0.3rem;
}
.pw-hint {
    font-style: italic; font-size: clamp(0.82rem, 3vw, 0.95rem);
    color: rgba(255,180,210,0.6); margin-bottom: 1.6rem;
}
.pw-error {
    text-align: center; margin-top: 0.6rem;
    font-style: italic; font-size: 0.88rem;
    color: rgba(255,130,170,0.85);
}

/* open button */
.open-btn .stButton > button {
    background: linear-gradient(135deg, #c2185b, #e91e8c, #f06292) !important;
    color: white !important;
    padding: 0.75rem 2.5rem !important;
    font-size: 1rem !important;
    box-shadow: 0 6px 24px rgba(233,30,140,0.45), 0 0 0 1px rgba(255,180,210,0.15) !important;
    width: 100% !important;
}
.open-btn .stButton > button:hover { transform: scale(1.04) !important; box-shadow: 0 8px 30px rgba(233,30,140,0.6) !important; }

/* ══ QUESTION PAGE ══════════════════════════════════════════════════════════ */
.q-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.7rem, 7vw, 2.8rem);
    font-weight: 700; color: #ffb3d1;
    text-align: center;
    text-shadow: 0 0 30px rgba(255,100,160,0.45);
    line-height: 1.3; margin: 1.5rem 0 0.4rem;
}
.q-sub {
    text-align: center; font-style: italic;
    font-size: clamp(0.85rem, 3vw, 1rem);
    color: rgba(255,180,210,0.6); margin-bottom: 2rem;
}

/* YES */
[data-testid="stHorizontalBlock"] > div:first-child .stButton > button {
    background: linear-gradient(135deg, #c2185b, #e91e8c) !important;
    color: white !important;
    font-size: clamp(1rem, 4vw, 1.2rem) !important;
    padding: 0.8rem 1rem !important;
    box-shadow: 0 6px 24px rgba(194,24,91,0.5) !important;
    width: 100% !important;
}
[data-testid="stHorizontalBlock"] > div:first-child .stButton > button:hover { transform: scale(1.06) !important; }
/* NO */
[data-testid="stHorizontalBlock"] > div:last-child .stButton > button {
    background: rgba(240,98,146,0.15) !important;
    color: rgba(255,180,210,0.8) !important;
    font-size: clamp(1rem, 4vw, 1.2rem) !important;
    padding: 0.8rem 1rem !important;
    border: 1.5px solid rgba(240,98,146,0.3) !important;
    width: 100% !important;
}

/* ══ BIRTHDAY PAGE ══════════════════════════════════════════════════════════ */
.bday-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2.2rem, 9vw, 3.8rem);
    font-weight: 700; color: #ffb3d1;
    text-align: center; line-height: 1.2;
    text-shadow: 0 0 40px rgba(255,100,160,0.5);
    margin: 0.4rem 0 0.2rem;
}
.bday-sub {
    font-family: 'Cormorant Garamond', serif; font-style: italic;
    font-size: clamp(1rem, 4vw, 1.45rem);
    color: rgba(255,180,210,0.75);
    text-align: center; margin-bottom: 0.5rem;
}

/* reasons pill — top right */
.r-pill .stButton > button {
    background: linear-gradient(135deg, #c2185b, #e91e8c) !important;
    color: white !important;
    padding: 0.42rem 0.9rem !important;
    font-size: clamp(0.66rem, 2.4vw, 0.8rem) !important;
    box-shadow: 0 4px 16px rgba(194,24,91,0.4) !important;
    white-space: nowrap !important;
}
.r-pill .stButton > button:hover { transform: scale(1.05) !important; }

/* days badge */
.days-badge {
    background: linear-gradient(135deg, rgba(194,24,91,0.7), rgba(233,30,140,0.7));
    border-radius: 20px; padding: 1.3rem 1rem;
    text-align: center; margin: 1rem 0;
    border: 1px solid rgba(255,150,190,0.2);
    box-shadow: 0 8px 32px rgba(194,24,91,0.4), inset 0 1px 0 rgba(255,200,220,0.15);
    position: relative; z-index: 1;
}
.days-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(3.2rem, 13vw, 5.5rem);
    font-weight: 700; color: #fff; line-height: 1;
    text-shadow: 0 2px 16px rgba(0,0,0,0.3);
}
.days-label {
    color: rgba(255,255,255,0.88); font-size: clamp(0.78rem, 2.8vw, 0.95rem);
    letter-spacing: 2.5px; margin-top: 0.1rem; font-weight: 600;
}
.days-sub {
    color: rgba(255,255,255,0.6); font-size: clamp(0.7rem, 2.4vw, 0.82rem);
    margin-top: 0.3rem; font-style: italic;
}

/* love notes */
.love-note {
    background: rgba(255,255,255,0.04);
    border-left: 2.5px solid rgba(240,98,146,0.6);
    border-radius: 0 14px 14px 0;
    padding: 0.9rem 1.1rem; margin: 0.6rem 0;
    font-size: clamp(0.86rem, 3vw, 0.98rem); line-height: 1.82;
    color: rgba(255,210,228,0.92);
    border-top: 1px solid rgba(255,150,190,0.07);
    border-right: 1px solid rgba(255,150,190,0.07);
    border-bottom: 1px solid rgba(255,150,190,0.07);
    position: relative; z-index: 1;
}

/* divider */
.divider {
    border: none; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(240,98,146,0.35), transparent);
    margin: 1.4rem 0;
}

/* ══ PHOTO SWIPER ═══════════════════════════════════════════════════════════ */
.gallery-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.35rem, 5.5vw, 2rem);
    font-weight: 700; text-align: center; color: #ffb3d1;
    margin: 0.4rem 0 0.2rem;
    text-shadow: 0 0 20px rgba(255,100,160,0.3);
}
.gallery-sub {
    text-align: center; font-style: italic;
    font-size: clamp(0.78rem, 2.8vw, 0.9rem);
    color: rgba(255,180,210,0.5); margin-bottom: 0.9rem;
}

/* photo — circle, smaller, NO background card */
.photo-wrap { text-align: center; position: relative; z-index: 1; }
.photo-img {
    width: min(52vw, 200px);
    height: min(52vw, 200px);
    object-fit: cover;
    border-radius: 50%;
    display: block;
    margin: 0 auto;
    border: 2.5px solid rgba(240,98,146,0.55);
    box-shadow:
        0 0 0 5px rgba(240,98,146,0.1),
        0 0 0 10px rgba(240,98,146,0.05),
        0 14px 40px rgba(0,0,0,0.55);
}
.photo-caption {
    font-family: 'Cormorant Garamond', serif; font-style: italic;
    font-size: clamp(0.88rem, 3.2vw, 1.05rem);
    color: rgba(255,210,228,0.88);
    margin-top: 0.85rem; line-height: 1.65;
    padding: 0 0.3rem;
}
.photo-dots {
    display: flex; justify-content: center;
    gap: 6px; margin-top: 0.75rem;
}
.da { width:8px;height:8px;border-radius:50%;background:#f06292;display:inline-block; }
.di { width:8px;height:8px;border-radius:50%;background:rgba(240,98,146,0.25);display:inline-block; }

/* swipe arrows — inline, tight */
.swipe-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    margin-top: 0.65rem;
}
.swipe-row .arr .stButton > button {
    background: rgba(240,98,146,0.18) !important;
    color: #ffb3d1 !important;
    border: 1.5px solid rgba(240,98,146,0.35) !important;
    border-radius: 50% !important;
    width: 2.4rem !important; height: 2.4rem !important;
    padding: 0 !important; font-size: 1rem !important;
    box-shadow: 0 3px 12px rgba(0,0,0,0.35) !important;
    min-width: unset !important; line-height: 1 !important;
}
.swipe-row .arr .stButton > button:hover {
    background: rgba(240,98,146,0.38) !important;
    transform: scale(1.1) !important;
}
.swipe-counter {
    color: rgba(255,180,210,0.55);
    font-size: 0.8rem; font-weight: 600;
    min-width: 2rem; text-align: center;
}

/* ══ FOOTER ═════════════════════════════════════════════════════════════════ */
.footer { text-align: center; padding: 1.8rem 1rem 3.5rem; font-family: 'Cormorant Garamond', serif; }
.footer-main { font-size: clamp(1.3rem, 5.5vw, 1.8rem); color: #ffb3d1; font-weight: 700; text-shadow: 0 0 20px rgba(255,100,160,0.35); }
.footer-sub { font-size: clamp(0.85rem, 3.2vw, 1rem); color: rgba(255,180,210,0.68); font-style: italic; margin-top: 0.7rem; line-height: 1.85; }
.footer-hearts { font-size: clamp(1.5rem, 5vw, 2rem); margin-top: 1rem; letter-spacing: 5px; }

/* ══ REASONS PAGE ═══════════════════════════════════════════════════════════ */
.reasons-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.7rem, 7vw, 2.6rem);
    font-weight: 700; text-align: center; color: #ffb3d1;
    text-shadow: 0 0 30px rgba(255,100,160,0.4);
    margin: 0.5rem 0 0.2rem; line-height: 1.25;
}
.reason-card {
    background: rgba(255,255,255,0.04);
    border-radius: 14px; padding: 0.85rem 1.05rem; margin: 0.45rem 0;
    font-size: clamp(0.84rem, 3vw, 0.97rem); color: rgba(255,210,228,0.93);
    border: 1px solid rgba(255,140,185,0.12);
    line-height: 1.68; position: relative; z-index: 1;
    transition: background 0.2s, border-color 0.2s;
}
.reason-card:hover { background: rgba(255,255,255,0.08); border-color: rgba(240,98,146,0.25); }
.reason-num {
    font-weight: 700; color: #f06292;
    font-size: 0.72rem; display: block; margin-bottom: 0.12rem; letter-spacing: 1px;
}
.endless {
    font-family: 'Cormorant Garamond', serif; font-style: italic;
    font-size: clamp(1rem, 3.8vw, 1.2rem); color: #ffb3d1;
    text-align: center; margin: 1.4rem 0 2rem;
    padding: 1rem 1.2rem;
    background: rgba(194,24,91,0.1);
    border-radius: 16px; border: 1px solid rgba(255,140,185,0.18);
    line-height: 1.72;
}
.sm-wrap { display: flex; justify-content: center; margin: 0.7rem 0; }
.sm-wrap .stButton > button {
    background: rgba(194,24,91,0.18) !important;
    color: #ffb3d1 !important;
    border: 1.5px solid rgba(240,98,146,0.35) !important;
    border-radius: 50px !important;
    padding: 0.48rem 2rem !important;
    font-weight: 700 !important; font-size: 0.88rem !important;
}
.sm-wrap .stButton > button:hover { background: rgba(194,24,91,0.35) !important; transform: scale(1.04) !important; }

/* back btn */
.back-btn .stButton > button {
    background: rgba(255,255,255,0.06) !important;
    color: rgba(255,180,210,0.8) !important;
    border: 1px solid rgba(255,140,185,0.22) !important;
    border-radius: 50px !important;
    padding: 0.4rem 1rem !important;
    font-size: 0.8rem !important; font-weight: 600 !important;
}
.back-btn .stButton > button:hover { background: rgba(255,255,255,0.12) !important; }

/* mobile */
@media (max-width: 430px) {
    .block-container { padding-left: 0.8rem !important; padding-right: 0.8rem !important; }
    .love-note { padding: 0.8rem 0.9rem; }
    .reason-card { padding: 0.75rem 0.9rem; }
}
</style>
""", unsafe_allow_html=True)

# ─── Helpers ───────────────────────────────────────────────────────────────────
def floating_hearts(n=18):
    emojis = ["💖","💕","💗","💓","💞","🌸","✨","💝","🌷","💫","🎀","🌹","💘"]
    html = ""
    for _ in range(n):
        left  = random.randint(0, 97)
        delay = round(random.uniform(0, 11), 2)
        dur   = round(random.uniform(6, 15), 2)
        size  = round(random.uniform(1, 2.4), 2)
        e     = random.choice(emojis)
        html += (f'<span class="fh" style="left:{left}vw;font-size:{size}rem;'
                 f'animation-delay:{delay}s;animation-duration:{dur}s;">{e}</span>')
    st.markdown(html, unsafe_allow_html=True)

# ─── Session state ─────────────────────────────────────────────────────────────
for k, v in [("page","password"),("no_pos",0),("reasons_shown",10),
              ("photo_idx",0),("pw_error",False)]:
    if k not in st.session_state:
        st.session_state[k] = v

# ─── Data ──────────────────────────────────────────────────────────────────────
PASSWORD = "11012026"

REASONS = [
    "The way you make me laugh through a screen.",
    "Your voice is my favorite comfort sound.",
    "You always know exactly how to cheer me up.",
    "You make the distance feel so small.",
    "How you make time for me, no matter what.",
    "You always make me feel so safe and secure.",
    "The butterflies I still get when you call.",
    "Just sitting in silence with you on video.",
    "You are my favorite distraction.",
    "You are my safest, happiest space.",
    "How much I trust you with my whole heart.",
    "I can completely be my weird self with you.",
    "You love me on my good days and bad days.",
    "How amazing you look on camera when you first wake up.",
    "Thinking about what we'll do the minute the door finally closes.",
    "How easily you can make me blush from thousands of miles away.",
    "The way you look at me when you're feeling playful.",
    "Our late-night conversations that get a little too distracting.",
    "Your hands—and thinking about exactly where they'll be when I see you.",
    "The way you make me crave your touch just by using your words.",
    "Sending you photos that I know will absolutely ruin your concentration for the rest of the day.",
    "How hot you look when you get protective or a little bit possessive.",
    "The quiet, unspoken comfort of knowing I've found my forever person in you.",
    "Hearing you talk about the little details of your day just to keep me included.",
    "The way you make me feel so close to you, even when the distance feels heavy.",
    "How gently you love me, despite the heavy things you've had to carry from your past.",
    "I love that you've seen my worst angles on Video Calls and you're still here.",
    "Your willingness to talk to me even when I'm looking like a complete potato.",
    "How you manage to tell me I smell through a phone screen.",
    "Knowing with absolute certainty that I will spend the rest of my life making sure you never regret choosing me.",
    "How I promise to always protect your peace, your trust, and everything we've built together.",
    "The fact that you never have to worry about where we stand — I am entirely, completely, and only yours.",
    "How I promise to love you gently, honor your trust, and never give you a reason to doubt us.",
    "You've given me your heart, and my biggest promise in life is to never, ever break it.",
]

PICS = [
    ("images/photo1.jpeg", "You were literally brushing your teeth on a video call and I still thought you were the most beautiful person I'd ever seen. I would screenshot this a thousand times over. 💕"),
    ("images/photo2.jpeg", "The sunset, the Adidas fit, that smile, the thumbs up — like you already know you've completely ruined my day just by existing. God, you are so unfairly attractive. 🌅💖"),
    ("images/photo3.jpeg", "Face mask on, earring in, not a single care in the world — and I was already completely gone for you. Soft, silly, and entirely mine. 🌿🥺"),
    ("images/photo4.jpeg", "That LAUGH. Full-face, eyes-squeezed-shut, completely unguarded — that is the laugh I want to spend the rest of my life causing. You have no idea how much I love you. 🥹💗"),
]

# ══════════════════════════════════════════════════════════════════════════════
# PASSWORD
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.page == "password":
    floating_hearts(8)
    st.markdown("""
    <div class="pw-wrap">
        <div class="pw-lock">🔒</div>
        <div class="pw-title">This is for someone<br>very special 🌸</div>
        <div class="pw-hint">Hint: the day we met — DDMMYYYY</div>
    </div>
    """, unsafe_allow_html=True)

    pw = st.text_input("", placeholder="Enter password…", type="password",
                       key="pw_field", label_visibility="collapsed")
    _, c, _ = st.columns([1, 3, 1])
    with c:
        st.markdown('<div class="open-btn">', unsafe_allow_html=True)
        if st.button("Open 💖", key="pw_submit", use_container_width=True):
            if pw.strip() == PASSWORD:
                st.session_state.page = "question"
                st.session_state.pw_error = False
                st.rerun()
            else:
                st.session_state.pw_error = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.pw_error:
        st.markdown('<p class="pw-error">Hmm, that\'s not right… think about when everything started 💕</p>',
                    unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# QUESTION
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "question":
    floating_hearts(12)
    st.markdown('<div style="text-align:center;font-size:3rem;margin-top:1.2rem;">💕</div>',
                unsafe_allow_html=True)
    st.markdown("<p class='q-title'>ARE YOU<br>SHAKSHI'S BOYFRIEND?</p>", unsafe_allow_html=True)
    st.markdown("<p class='q-sub'>Think very carefully before you answer… 🌸</p>",
                unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        if st.button("YES 💖", key="yes_btn", use_container_width=True):
            st.session_state.page = "birthday"
            st.rerun()
    with c2:
        if st.button("NO 💔", key="no_btn", use_container_width=True):
            st.session_state.no_pos += 1
            st.rerun()

    if st.session_state.no_pos > 0:
        msgs = [
            "Are you sure about that? 🌸",
            "That button keeps running away… 💕",
            "The universe is literally telling you something 😭",
            "Just click YES, babe, come on 💖",
            "I'm not letting you go that easily 🌹",
            "Come On Daddy",
            "Don't You Loveeee Me??????"
              ]
        aligns = ["flex-end","flex-start","center","flex-end","flex-start"]
        m = min(st.session_state.no_pos - 1, len(msgs)-1)
        a = aligns[st.session_state.no_pos % len(aligns)]
        st.markdown(
            f'<div style="display:flex;justify-content:{a};margin-top:0.4rem;">'
            f'<span style="font-size:1.5rem;opacity:0.4;">💔</span></div>'
            f'<div style="text-align:center;margin-top:0.6rem;font-style:italic;'
            f'color:rgba(255,180,210,0.6);font-size:0.9rem;">{msgs[m]}</div>',
            unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# BIRTHDAY
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "birthday":
    floating_hearts(22)

    # reasons pill — top right
    _, rp = st.columns([1.3, 1])
    with rp:
        st.markdown('<div class="r-pill">', unsafe_allow_html=True)
        if st.button("💌 Reasons I Love You", key="go_reasons"):
            st.session_state.page = "reasons"
            st.session_state.reasons_shown = 10
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # header
    st.markdown("""
    <div style="text-align:center;font-size:clamp(1.6rem,6vw,2.2rem);
                letter-spacing:6px;margin:0.1rem 0;">💖 🌸 💖 🌸 💖</div>
    """, unsafe_allow_html=True)
    st.markdown("<h1 class='bday-title'>Happy Birthday,<br>My Love 🎂</h1>",
                unsafe_allow_html=True)
    st.markdown("<p class='bday-sub'>Today the world got a little more beautiful<br>because it's your day. 🌹</p>",
                unsafe_allow_html=True)

    # days badge
    st.markdown(f"""
    <div class="days-badge">
        <div class="days-num">{DAYS_TOGETHER}</div>
        <div class="days-label">DAYS TOGETHER 💕</div>
        <div class="days-sub">since 11th January 2026 — and counting forever 🌸</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # love notes
    for icon, note in [
        ("🌸", "Every single day I get to know you is the best day of my life. Today just happens to be extra special because you came into this world — and I will forever be grateful for that."),
        ("💕", "The distance between us is just a number. My heart has never once doubted that you are exactly where you're supposed to be — right here, in every thought, every smile, every quiet moment I save for you."),
        ("💖", "I don't have the words to explain what you mean to me. But I hope you feel it — in every 'good morning', every 'are you okay?', every late night we stay up just to be near each other."),
        ("🎂", "You deserve a birthday as soft, as warm, and as completely overwhelmingly wonderful as you make me feel every single day. This is just the beginning. ✨"),
    ]:
        st.markdown(f'<div class="love-note"><span style="font-size:1.05rem;">{icon}</span><br>{note}</div>',
                    unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # ── PHOTO SWIPER ──────────────────────────────────────────────────────────
    st.markdown("<h2 class='gallery-title'>📸 My Favourite Pics of You</h2>",
                unsafe_allow_html=True)
    st.markdown("<p class='gallery-sub'>moments I've saved in my heart 🌸</p>",
                unsafe_allow_html=True)

    idx = st.session_state.photo_idx
    img_path, caption = PICS[idx]

    if Path(img_path).exists():
        b64 = img_to_b64(img_path)
        img_tag = f'<img class="photo-img" src="data:image/jpeg;base64,{b64}" alt="photo">'
    else:
        img_tag = '<div style="width:min(52vw,200px);height:min(52vw,200px);border-radius:50%;background:rgba(240,98,146,0.15);display:flex;align-items:center;justify-content:center;font-size:3rem;margin:0 auto;border:2.5px solid rgba(240,98,146,0.4);">📷</div>'

    dots = "".join(f'<span class="{"da" if i==idx else "di"}"></span>' for i in range(len(PICS)))

    st.markdown(f"""
    <div class="photo-wrap">
        {img_tag}
        <p class="photo-caption">{caption}</p>
        <div class="photo-dots">{dots}</div>
    </div>
    """, unsafe_allow_html=True)

    # tight arrow row — use 5 columns, arrows in cols 1 and 3, counter in col 2
    _, ac1, cc, ac2, _ = st.columns([2, 1, 1, 1, 2])
    with ac1:
        st.markdown('<div class="swipe-row"><div class="arr">', unsafe_allow_html=True)
        if st.button("←", key="prev_p"):
            st.session_state.photo_idx = (idx - 1) % len(PICS)
            st.rerun()
        st.markdown('</div></div>', unsafe_allow_html=True)
    with cc:
        st.markdown(f'<div class="swipe-counter">{idx+1}/{len(PICS)}</div>',
                    unsafe_allow_html=True)
    with ac2:
        st.markdown('<div class="swipe-row"><div class="arr">', unsafe_allow_html=True)
        if st.button("→", key="next_p"):
            st.session_state.photo_idx = (idx + 1) % len(PICS)
            st.rerun()
        st.markdown('</div></div>', unsafe_allow_html=True)

    # footer
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown("""
    <div class="footer">
        <div class="footer-main">Happy Birthday, my love. 💖</div>
        <div class="footer-sub">
            You are my favourite part of every single day.<br>
            I love you more than words will ever, ever manage to say. 🌹
        </div>
        <div class="footer-hearts">💕🌸💖🌸💕</div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# REASONS
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "reasons":
    floating_hearts(18)

    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("← Back", key="back_top"):
        st.session_state.page = "birthday"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="text-align:center;font-size:2.4rem;margin:0.4rem 0;">💕</div>',
                unsafe_allow_html=True)
    st.markdown("<h1 class='reasons-title'>Reasons Why<br>I Love You 💌</h1>",
                unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-style:italic;color:rgba(255,180,210,0.5);font-size:0.88rem;margin-bottom:1rem;">let me count the ways… 🌸</div>',
                unsafe_allow_html=True)
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    for i, r in enumerate(REASONS[:st.session_state.reasons_shown], 1):
        st.markdown(
            f'<div class="reason-card"><span class="reason-num">#{i}</span>{r}</div>',
            unsafe_allow_html=True)

    if st.session_state.reasons_shown < len(REASONS):
        st.markdown('<div class="sm-wrap">', unsafe_allow_html=True)
        if st.button("Show More 💖", key="show_more"):
            st.session_state.reasons_shown = min(st.session_state.reasons_shown + 10, len(REASONS))
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            '<div class="endless">…and I could keep going on. 💕<br>'
            '<span style="font-size:0.9em;">There aren\'t enough reasons in the world '
            'to hold everything I feel for you.</span></div>',
            unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    _, bc, _ = st.columns([1, 2, 1])
    with bc:
        st.markdown('<div class="back-btn">', unsafe_allow_html=True)
        if st.button("← Back to Birthday 💖", key="back_bot", use_container_width=True):
            st.session_state.page = "birthday"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)