import streamlit as st
import random
from pathlib import Path
from datetime import date
import base64

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Happy Birthday, My Love 💕",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Helper: encode image to base64 ────────────────────────────────────────────
def img_to_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ── Days together ──────────────────────────────────────────────────────────────
START_DATE = date(2026, 1, 11)
DAYS_TOGETHER = (date.today() - START_DATE).days

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lato:wght@300;400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Lato', sans-serif;
    background-color: #fff0f5;
    color: #5a2a3a;
}
.stApp {
    background: linear-gradient(135deg, #fff0f5 0%, #ffe4f0 50%, #ffd6e8 100%);
    min-height: 100vh;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 3rem; max-width: 680px; }

/* ── Floating hearts ── */
@keyframes floatUp {
    0%   { transform: translateY(0) scale(1) rotate(0deg); opacity: 0.9; }
    100% { transform: translateY(-105vh) scale(1.5) rotate(25deg); opacity: 0; }
}
.floating-heart {
    position: fixed; bottom: -60px; font-size: 1.8rem;
    animation: floatUp linear infinite;
    pointer-events: none; z-index: 0; user-select: none;
}

/* ── All buttons base ── */
.stButton > button {
    border-radius: 50px !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px !important;
    transition: transform 0.18s, box-shadow 0.18s !important;
    border: none !important;
}

/* ── Password page ── */
.pw-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.6rem, 6vw, 2.6rem);
    font-weight: 700; text-align: center; color: #c2185b;
    margin: 2.5rem 0 0.3rem; line-height: 1.3;
    text-shadow: 0 2px 10px rgba(194,24,91,0.15);
}
.pw-hint {
    text-align: center; font-style: italic;
    font-size: clamp(0.85rem, 3vw, 1rem);
    color: #e91e8c; margin-bottom: 1.5rem;
}
.pw-error {
    text-align: center; color: #c2185b;
    font-size: 0.9rem; margin-top: 0.5rem;
    font-style: italic;
}

/* ── Question page ── */
.question-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.55rem, 6.5vw, 2.8rem);
    font-weight: 700; text-align: center; color: #c2185b;
    margin: 2rem 0 0.4rem;
    text-shadow: 0 2px 10px rgba(194,24,91,0.18);
    line-height: 1.3;
}
.question-sub {
    text-align: center; font-size: clamp(0.88rem, 3.2vw, 1.1rem);
    color: #e91e8c; margin-bottom: 2rem; font-style: italic;
}

/* YES button — first col */
[data-testid="stHorizontalBlock"] > div:first-child .stButton > button {
    background: linear-gradient(135deg, #e91e8c, #f06292) !important;
    color: white !important;
    font-size: clamp(1rem, 4vw, 1.25rem) !important;
    padding: 0.82rem 1rem !important;
    box-shadow: 0 6px 22px rgba(233,30,140,0.42) !important;
    width: 100% !important;
}
[data-testid="stHorizontalBlock"] > div:first-child .stButton > button:hover {
    transform: scale(1.07) !important;
}
/* NO button — second col */
[data-testid="stHorizontalBlock"] > div:last-child .stButton > button {
    background: linear-gradient(135deg, #f8bbd9, #f48fb1) !important;
    color: #880e4f !important;
    font-size: clamp(1rem, 4vw, 1.25rem) !important;
    padding: 0.82rem 1rem !important;
    box-shadow: 0 4px 14px rgba(244,143,177,0.4) !important;
    width: 100% !important;
}

/* ── Days together badge ── */
.days-badge {
    background: linear-gradient(135deg, #e91e8c, #f06292);
    border-radius: 20px; padding: 1.1rem 1.5rem;
    text-align: center; margin: 1.2rem 0;
    box-shadow: 0 6px 20px rgba(233,30,140,0.3);
    position: relative; z-index: 1;
}
.days-num {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.8rem, 10vw, 4.5rem);
    font-weight: 700; color: white; line-height: 1;
    text-shadow: 0 2px 8px rgba(0,0,0,0.15);
}
.days-label {
    color: rgba(255,255,255,0.92);
    font-size: clamp(0.85rem, 3vw, 1rem);
    margin-top: 0.2rem; letter-spacing: 1px;
}
.days-sub {
    color: rgba(255,255,255,0.78);
    font-size: clamp(0.75rem, 2.5vw, 0.88rem);
    margin-top: 0.3rem; font-style: italic;
}

/* ── Birthday page ── */
.bday-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 7.5vw, 3.5rem);
    font-weight: 700; text-align: center; color: #ad1457;
    margin: 0.8rem 0 0.2rem;
    text-shadow: 0 3px 14px rgba(173,20,87,0.2);
    line-height: 1.25;
}
.bday-subtitle {
    font-family: 'Playfair Display', serif; font-style: italic;
    font-size: clamp(1rem, 3.8vw, 1.5rem);
    text-align: center; color: #e91e8c; margin-bottom: 1.2rem;
}
.love-note {
    background: linear-gradient(135deg, rgba(255,255,255,0.88), rgba(255,228,240,0.88));
    border-left: 4px solid #e91e8c; border-radius: 16px;
    padding: 1.1rem 1.4rem; margin: 0.75rem 0;
    font-size: clamp(0.92rem, 3.2vw, 1.08rem); line-height: 1.75;
    color: #5a2a3a; box-shadow: 0 4px 18px rgba(233,30,140,0.1);
    position: relative; z-index: 1;
}
.love-note::before { content: '💌'; font-size: 1.3rem; display: block; margin-bottom: 0.35rem; }

/* ── Reasons page button (on birthday page) ── */
.reasons-nav-btn .stButton > button {
    background: linear-gradient(135deg, #e91e8c, #f06292) !important;
    color: white !important; border: none !important;
    border-radius: 30px !important;
    padding: 0.55rem 1.1rem !important;
    font-size: clamp(0.7rem, 2.6vw, 0.85rem) !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 14px rgba(233,30,140,0.4) !important;
    white-space: nowrap !important;
}

/* ── Reasons PAGE ── */
.reasons-page-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.6rem, 6vw, 2.6rem);
    font-weight: 700; text-align: center; color: #ad1457;
    margin: 1rem 0 0.3rem; line-height: 1.3;
}
.reason-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.92), rgba(255,228,240,0.92));
    border-radius: 14px; padding: 0.95rem 1.2rem; margin: 0.5rem 0;
    font-size: clamp(0.88rem, 3vw, 1.03rem); color: #5a2a3a;
    box-shadow: 0 3px 12px rgba(233,30,140,0.12);
    border: 1px solid rgba(233,30,140,0.14);
    line-height: 1.65; position: relative; z-index: 1;
}
.reason-num {
    font-weight: 700; color: #e91e8c;
    font-size: 0.8rem; display: block; margin-bottom: 0.2rem;
}
.endless-love {
    font-family: 'Playfair Display', serif; font-style: italic;
    font-size: clamp(0.98rem, 3.5vw, 1.22rem); color: #c2185b;
    text-align: center; margin: 1.4rem 0 1.8rem;
    padding: 1rem 1.2rem; background: rgba(255,255,255,0.65);
    border-radius: 14px; line-height: 1.7;
}
.show-more-center { display: flex; justify-content: center; margin: 0.5rem 0; }
.show-more-center .stButton > button {
    background: linear-gradient(135deg, #fce4ec, #f8bbd9) !important;
    color: #880e4f !important; border: 2px solid #f06292 !important;
    border-radius: 30px !important; padding: 0.48rem 1.8rem !important;
    font-weight: 700 !important; font-size: clamp(0.83rem, 3vw, 0.95rem) !important;
}
.show-more-center .stButton > button:hover {
    background: linear-gradient(135deg, #f8bbd9, #f06292) !important;
    color: white !important; transform: scale(1.05) !important;
}
/* back button */
.back-btn .stButton > button {
    background: rgba(255,255,255,0.7) !important;
    color: #c2185b !important; border: 2px solid #f06292 !important;
    border-radius: 30px !important; padding: 0.45rem 1.2rem !important;
    font-size: 0.85rem !important; font-weight: 600 !important;
}

/* ── Photo swiper ── */
.gallery-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.45rem, 5.5vw, 2.3rem);
    text-align: center; color: #ad1457;
    margin: 2rem 0 0.4rem; font-weight: 700;
}
.gallery-sub {
    text-align: center; font-style: italic;
    font-size: clamp(0.88rem, 3vw, 1.02rem);
    color: #e91e8c; margin-bottom: 1.2rem;
}
.swiper-card {
    background: rgba(255,255,255,0.92);
    border-radius: 22px; padding: 1rem;
    box-shadow: 0 8px 28px rgba(233,30,140,0.18);
    border: 1px solid rgba(233,30,140,0.13);
    text-align: center; position: relative; z-index: 1;
}
.swiper-img {
    width: 100%; aspect-ratio: 1/1;
    object-fit: cover; border-radius: 14px;
    display: block;
}
.swiper-caption {
    font-family: 'Playfair Display', serif; font-style: italic;
    font-size: clamp(0.88rem, 3.2vw, 1.06rem);
    color: #880e4f; margin-top: 0.9rem; line-height: 1.6;
}
.swiper-dots {
    display: flex; justify-content: center; gap: 6px; margin-top: 0.7rem;
}
.dot {
    width: 8px; height: 8px; border-radius: 50%;
    display: inline-block;
}
.dot-active { background: #e91e8c; }
.dot-inactive { background: #f8bbd9; }
.swiper-nav { display: flex; align-items: center; justify-content: center; gap: 0.5rem; margin-top: 0.6rem; }
/* nav arrow buttons */
.swiper-prev .stButton > button,
.swiper-next .stButton > button {
    background: linear-gradient(135deg, #e91e8c, #f06292) !important;
    color: white !important; border: none !important;
    border-radius: 50% !important;
    width: 2.8rem !important; height: 2.8rem !important;
    padding: 0 !important; font-size: 1.2rem !important;
    box-shadow: 0 4px 14px rgba(233,30,140,0.35) !important;
    min-width: unset !important;
}

/* ── Divider ── */
.pink-divider {
    border: none; height: 2px;
    background: linear-gradient(90deg, transparent, #f06292, transparent);
    margin: 1.8rem 0;
}

/* ── Mobile ── */
@media (max-width: 480px) {
    .block-container { padding-left: 0.8rem; padding-right: 0.8rem; }
    .love-note, .reason-card { padding: 0.9rem 1rem; }
    .swiper-card { padding: 0.8rem; }
}
</style>
""", unsafe_allow_html=True)

# ── Helpers ───────────────────────────────────────────────────────────────────
def floating_hearts(count=18):
    hearts = ["💖","💕","💗","💓","💞","🌸","✨","💝","🌷","💫","🎀","🌹"]
    html = ""
    for i in range(count):
        left  = random.randint(0, 97)
        delay = round(random.uniform(0, 10), 2)
        dur   = round(random.uniform(5, 14), 2)
        size  = round(random.uniform(1.1, 2.6), 2)
        h     = random.choice(hearts)
        html += (
            f'<span class="floating-heart" style="left:{left}vw;'
            f'animation-delay:{delay}s;animation-duration:{dur}s;'
            f'font-size:{size}rem;">{h}</span>'
        )
    st.markdown(html, unsafe_allow_html=True)

# ── Session state ──────────────────────────────────────────────────────────────
defaults = {
    "page": "password",   # password → question → birthday → reasons
    "no_pos": 0,
    "reasons_shown": 10,
    "photo_idx": 0,
    "pw_error": False,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Data ──────────────────────────────────────────────────────────────────────
CORRECT_PASSWORD = "11012026"   # 11th Jan 2026  — hint: "the day we met"

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

PIC_DATA = [
    {
        "file": "images/photo1.jpeg",
        "caption": "You were literally brushing your teeth on a video call and I still thought you were the most beautiful person I'd ever seen. I would screenshot this a thousand times over. 💕"
    },
    {
        "file": "images/photo2.jpeg",
        "caption": "Excuse me?? The sunset, the Adidas fit, that smile, the thumbs up like you already know you've completely ruined my day just by existing. God, you are so unfairly attractive. 🌅💖"
    },
    {
        "file": "images/photo3.jpeg",
        "caption": "Face mask on, earring in, not a single care in the world — and I was already completely gone for you. Soft, silly, and entirely mine. This is my favourite version of you. 🌿🥺"
    },
    {
        "file": "images/photo4.jpeg",
        "caption": "That LAUGH. That full-face, eyes-squeezed-shut, completely unguarded laugh — that is the laugh I want to spend the rest of my life causing. You have no idea how much I love you. 🥹💗"
    },
]

# ═════════════════════════════════════════════════════════════════════════════
# PAGE: PASSWORD
# ═════════════════════════════════════════════════════════════════════════════
if st.session_state.page == "password":
    floating_hearts(8)

    st.markdown('<div style="text-align:center;font-size:3rem;margin-top:1rem;">🔒💕</div>', unsafe_allow_html=True)
    st.markdown("<p class='pw-title'>This is for someone<br>very special 🌸</p>", unsafe_allow_html=True)
    st.markdown("<p class='pw-hint'>Hint: enter the day we met (DDMMYYYY)</p>", unsafe_allow_html=True)

    pw_input = st.text_input(
        "", placeholder="Enter the password…",
        type="password", key="pw_field",
        label_visibility="collapsed"
    )

    _, btn_col, _ = st.columns([1, 2, 1])
    with btn_col:
        if st.button("Open 💖", key="pw_submit", use_container_width=True):
            if pw_input.strip() == CORRECT_PASSWORD:
                st.session_state.page = "question"
                st.session_state.pw_error = False
                st.rerun()
            else:
                st.session_state.pw_error = True
                st.rerun()

    if st.session_state.pw_error:
        st.markdown("<p class='pw-error'>Hmm, that's not quite right… think about when everything started 💕</p>", unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════════════════════
# PAGE: QUESTION
# ═════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "question":
    floating_hearts(12)

    st.markdown('<div style="text-align:center;font-size:3rem;margin-top:0.8rem;">💕</div>', unsafe_allow_html=True)
    st.markdown("<p class='question-title'>ARE YOU SAKSHI'S BOYFRIEND?</p>", unsafe_allow_html=True)
    st.markdown("<p class='question-sub'>Think very carefully before you answer… 🌸</p>", unsafe_allow_html=True)

    col_yes, col_no = st.columns(2, gap="medium")
    with col_yes:
        if st.button("YES 💖", key="yes_btn", use_container_width=True):
            st.session_state.page = "birthday"
            st.rerun()
    with col_no:
        if st.button("NO 💔", key="no_btn", use_container_width=True):
            st.session_state.no_pos += 1
            st.rerun()

    if st.session_state.no_pos > 0:
        messages = [
            "Hmm, are you sure about that? 🌸",
            "That button keeps slipping away… maybe it knows something 💕",
            "The universe is literally trying to tell you something 😭",
            "Okay at this point just click YES, babe 💖",
            "I'm not letting you go that easily 🌹",
        ]
        msg_idx = min(st.session_state.no_pos - 1, len(messages) - 1)
        offsets = ["flex-end", "flex-start", "center", "flex-end", "flex-start"]
        align = offsets[st.session_state.no_pos % len(offsets)]
        st.markdown(
            f'<div style="display:flex;justify-content:{align};margin-top:0.5rem;">'
            f'<span style="font-size:1.6rem;opacity:0.45;cursor:default;">💔</span></div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div style="text-align:center;margin-top:0.7rem;font-style:italic;'
            f'color:#e91e8c;font-size:0.93rem;line-height:1.6;">'
            f'{messages[msg_idx]}</div>',
            unsafe_allow_html=True,
        )

# ═════════════════════════════════════════════════════════════════════════════
# PAGE: BIRTHDAY
# ═════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "birthday":
    floating_hearts(24)

    # ── Reasons button — top right ─────────────────────────────────────────
    _, reasons_col = st.columns([1.2, 1])
    with reasons_col:
        st.markdown('<div class="reasons-nav-btn">', unsafe_allow_html=True)
        if st.button("💌 Reasons I Love You", key="go_reasons"):
            st.session_state.page = "reasons"
            st.session_state.reasons_shown = 10
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Header ──────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="text-align:center;font-size:clamp(2rem,7vw,3rem);
                letter-spacing:5px;margin:0.2rem 0 0.1rem;">
        💖 🌸 💖 🌸 💖
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='bday-title'>Happy Birthday,<br>My Love 🎂💕</h1>", unsafe_allow_html=True)
    st.markdown("<p class='bday-subtitle'>Today the world got a little more beautiful<br>because it's your day. 🌹</p>", unsafe_allow_html=True)

    # ── Days together badge ──────────────────────────────────────────────────
    st.markdown(f"""
    <div class="days-badge">
        <div class="days-num">{DAYS_TOGETHER}</div>
        <div class="days-label">DAYS TOGETHER 💕</div>
        <div class="days-sub">since 11th January 2026 — and counting forever 🌸</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="pink-divider">', unsafe_allow_html=True)

    # ── Romantic notes ───────────────────────────────────────────────────────
    for note in [
        "Every single day I get to know you is the best day of my life. Today just happens to be extra special because you came into this world — and I will forever be grateful for that. 🌸",
        "The distance between us is just a number. My heart has never once doubted that you are exactly where you're supposed to be — right here, in every thought, every smile, every quiet moment I save for you. 💕",
        "I don't have the words to explain what you mean to me. But I hope you feel it — in every 'good morning', every 'are you okay?', every late night we stay up just to be near each other. 💖",
        "You deserve a birthday as soft, as warm, and as completely overwhelmingly wonderful as you make me feel every single day. This is just the beginning. 🎂✨",
    ]:
        st.markdown(f'<div class="love-note">{note}</div>', unsafe_allow_html=True)

    st.markdown('<hr class="pink-divider">', unsafe_allow_html=True)

    # ── Photo swiper ─────────────────────────────────────────────────────────
    st.markdown('<h2 class="gallery-title">📸 My Favourite Pics of You 📸</h2>', unsafe_allow_html=True)
    st.markdown('<p class="gallery-sub">Swipe through the moments I\'ve saved in my heart 🌸</p>', unsafe_allow_html=True)

    idx = st.session_state.photo_idx
    pic = PIC_DATA[idx]
    img_path = Path(pic["file"])

    # Square image via HTML/CSS
    if img_path.exists():
        b64 = img_to_b64(img_path)
        img_html = f'<img class="swiper-img" src="data:image/jpeg;base64,{b64}" alt="photo {idx+1}">'
    else:
        img_html = '<div style="width:100%;aspect-ratio:1/1;background:linear-gradient(135deg,#fce4ec,#f8bbd9);border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:3rem;">📷</div>'

    # Dots
    dots_html = '<div class="swiper-dots">'
    for i in range(len(PIC_DATA)):
        cls = "dot dot-active" if i == idx else "dot dot-inactive"
        dots_html += f'<span class="{cls}"></span>'
    dots_html += '</div>'

    st.markdown(f'<div class="swiper-card">{img_html}<p class="swiper-caption">{pic["caption"]}</p>{dots_html}</div>', unsafe_allow_html=True)

    # Navigation arrows
    prev_col, counter_col, next_col = st.columns([1, 2, 1])
    with prev_col:
        st.markdown('<div class="swiper-prev">', unsafe_allow_html=True)
        if st.button("←", key="prev_photo", use_container_width=False):
            st.session_state.photo_idx = (idx - 1) % len(PIC_DATA)
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with counter_col:
        st.markdown(
            f'<div style="text-align:center;color:#e91e8c;font-size:0.88rem;'
            f'padding-top:0.6rem;font-weight:600;">{idx+1} / {len(PIC_DATA)}</div>',
            unsafe_allow_html=True
        )
    with next_col:
        st.markdown('<div class="swiper-next">', unsafe_allow_html=True)
        if st.button("→", key="next_photo", use_container_width=False):
            st.session_state.photo_idx = (idx + 1) % len(PIC_DATA)
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Footer ──────────────────────────────────────────────────────────────
    st.markdown('<hr class="pink-divider">', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center;padding:1.5rem 1rem 3.5rem;
                font-family:'Playfair Display',serif;line-height:2;">
        <div style="font-size:clamp(1.2rem,4.5vw,1.65rem);color:#ad1457;font-weight:700;">
            Happy Birthday, my love. 💖
        </div>
        <div style="font-size:clamp(0.88rem,3.2vw,1.08rem);color:#c2185b;
                    font-style:italic;margin-top:0.8rem;line-height:1.8;">
            You are my favourite part of every single day.<br>
            I love you more than words will ever, ever manage to say. 🌹
        </div>
        <div style="font-size:clamp(1.6rem,6vw,2.2rem);margin-top:1.2rem;letter-spacing:5px;">
            💕🌸💖🌸💕
        </div>
    </div>
    """, unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════════════════════
# PAGE: REASONS
# ═════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "reasons":
    floating_hearts(20)

    # Back button
    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("← Back", key="back_from_reasons"):
        st.session_state.page = "birthday"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;font-size:2.5rem;margin:0.5rem 0;">💕</div>
    """, unsafe_allow_html=True)
    st.markdown("<h1 class='reasons-page-title'>Reasons Why I Love You 💌</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center;font-style:italic;color:#e91e8c;
                font-size:clamp(0.85rem,3vw,1rem);margin-bottom:1.2rem;">
        Let me count the ways… 🌸
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="pink-divider">', unsafe_allow_html=True)

    for i, reason in enumerate(REASONS[: st.session_state.reasons_shown], 1):
        st.markdown(
            f'<div class="reason-card"><span class="reason-num">#{i}</span>{reason}</div>',
            unsafe_allow_html=True,
        )

    if st.session_state.reasons_shown < len(REASONS):
        st.markdown('<div class="show-more-center">', unsafe_allow_html=True)
        if st.button("Show More 💖", key="show_more"):
            st.session_state.reasons_shown = min(st.session_state.reasons_shown + 10, len(REASONS))
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            '<div class="endless-love">…and I could keep going on. 💕<br>'
            '<span style="font-size:0.93em;">There aren\'t enough reasons in the world '
            'to hold everything I feel for you.</span></div>',
            unsafe_allow_html=True,
        )

    st.markdown('<hr class="pink-divider">', unsafe_allow_html=True)

    # Back to birthday at the bottom too
    _, back_col, _ = st.columns([1, 2, 1])
    with back_col:
        st.markdown('<div class="back-btn">', unsafe_allow_html=True)
        if st.button("← Back to Birthday 💖", key="back_bottom", use_container_width=True):
            st.session_state.page = "birthday"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
