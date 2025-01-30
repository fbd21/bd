import streamlit as st
from PIL import Image
import base64
import random

def set_custom_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:wght@400;600&display=swap');
        
        .main {
            background: linear-gradient(135deg, #fff5f5 0%, #fff0f6 100%);
            padding: 2rem;
        }
        
        .title-container {
            text-align: center;
            margin: 2rem 0;
            animation: fadeIn 2s ease-in;
        }
        
        .title-text {
            font-family: 'Dancing Script', cursive;
            background: linear-gradient(45deg, #FF1493, #FF69B4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 4rem;
            text-align: center;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
            animation: sparkle 2s infinite;
        }
        
        .subtitle-text {
            font-family: 'Playfair Display', serif;
            color: #FF69B4;
            font-size: 2rem;
            text-align: center;
            margin: 2rem 0;
            animation: slideIn 1s ease-out;
        }
        
        .message-card {
            background: linear-gradient(45deg, #FFE6F2 0%, #FFF0F5 100%);
            border-radius: 20px;
            padding: 2.5rem;
            box-shadow: 0 15px 30px rgba(0,0,0,0.1);
            margin: 2.5rem 0;
            border: 3px solid #FFB6C1;
            transition: transform 0.3s ease;
            animation: fadeIn 1.5s ease-in;
        }
        
        .message-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        }
        
        .love-quote {
            font-family: 'Dancing Script', cursive;
            color: #D63384;
            font-size: 1.8rem;
            text-align: center;
            margin: 1.5rem 0;
            line-height: 1.6;
        }
        
        .signature {
            font-family: 'Dancing Script', cursive;
            background: linear-gradient(45deg, #FF1493, #FF69B4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem;
            text-align: right;
            margin-top: 3rem;
            animation: fadeIn 2s ease-in;
        }
        
        .image-caption {
            font-family: 'Dancing Script', cursive;
            color: #FF69B4;
            font-size: 1.4rem;
            text-align: center;
            margin-top: 1rem;
            padding: 1rem;
            background: rgba(255, 240, 245, 0.95);
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        
        .image-caption:hover {
            transform: scale(1.05);
        }
        
        .photo-frame {
            border: 12px solid #FFF;
            border-radius: 20px;
            box-shadow: 0 12px 24px rgba(0,0,0,0.15);
            transition: all 0.3s ease;
            animation: fadeIn 1.5s ease-in;
        }
        
        .photo-frame:hover {
            transform: scale(1.03);
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }
        
        .special-button {
            background: linear-gradient(45deg, #FF1493, #FF69B4);
            color: white;
            padding: 1rem 2rem;
            border-radius: 50px;
            border: none;
            font-size: 1.2rem;
            margin: 2rem auto;
            display: block;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        .special-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        }
        
        @keyframes sparkle {
            0% { opacity: 1; }
            50% { opacity: 0.8; }
            100% { opacity: 1; }
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes slideIn {
            from { transform: translateX(-50px); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        
        .floating-hearts {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 100;
        }
        
        .heart {
            position: absolute;
            font-size: 1.5rem;
            animation: floatHeart 4s ease-in infinite;
            opacity: 0;
        }
        
        @keyframes floatHeart {
            0% { transform: translateY(100vh) scale(0); opacity: 0; }
            50% { opacity: 0.8; }
            100% { transform: translateY(-100px) scale(1); opacity: 0; }
        }
        </style>
    """, unsafe_allow_html=True)

def create_floating_hearts():
    return """
        <div class="floating-hearts">
            <div class="heart" style="left: 10%; animation-delay: 0s;">💝</div>
            <div class="heart" style="left: 30%; animation-delay: 2s;">💖</div>
            <div class="heart" style="left: 50%; animation-delay: 4s;">💗</div>
            <div class="heart" style="left: 70%; animation-delay: 1s;">💓</div>
            <div class="heart" style="left: 90%; animation-delay: 3s;">💕</div>
        </div>
    """

def get_romantic_quote():
    quotes = [
        "Your beauty outshines the stars in the night sky ✨",
        "Every moment with you feels like a beautiful dream come true 💫",
        "Your smile holds the power to make my world perfect 🌟",
        "You are the poetry I never knew how to write 📝",
        "In your eyes, I found my favorite place to get lost 👀"
    ]
    return random.choice(quotes)

def main():
    set_custom_style()
    
    # Floating Hearts Animation
    st.markdown(create_floating_hearts(), unsafe_allow_html=True)
    
    # Title Section with Gradient and Animation
    st.markdown("""
        <div class="title-container">
            <div class="title-text">✨ To My Beloved Bhawana ✨</div>
            <div style="font-size: 2rem; color: #FF69B4;">💝 Forever & Always 💝</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Introduction Message
    st.markdown("""
        <div class="message-card">
            <p style="font-size: 1.4rem; text-align: center; color: #D63384; line-height: 1.8;">
                My Precious Bhawana, <br><br>
                Every time I look at you, I'm reminded of how blessed I am to have 
                someone as beautiful, kind, and amazing as you in my life. Your presence 
                makes my world complete. 💖
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Photo Gallery
    st.markdown('<div class="subtitle-text">✨ Capturing Heaven\'s Most Beautiful Angel ✨</div>', 
                unsafe_allow_html=True)
    
    photo_captions = [
        "Your smile melts my heart every single time 💫",
        "Beauty personified in every way ✨",
        "A glimpse of paradise in your eyes 🌹",
        "Radiant like the morning sun 💖",
        "The embodiment of pure grace ⭐"
    ]
    
    # Create elegant photo grid
    # [Previous imports and style definitions remain the same until the image display part]

    # Create elegant photo grid
    cols = st.columns(3)
    for i in range(5):
        with cols[i % 3]:
            try:
                img = Image.open(f"pic{i+1}.jpg")
                st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
                st.image(img, use_container_width=True)  # Updated parameter here
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown(f'<p class="image-caption">{photo_captions[i]}</p>', 
                          unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Please add pic{i+1}.jpg to your project directory")

# [Rest of the code remains the same]
    
    # Romantic Quote
    st.markdown(f"""
        <div class="message-card">
            <p class="love-quote">"{get_romantic_quote()}"</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Special Message Section
    st.markdown('<div class="subtitle-text">💌 Words From My Heart 💌</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="message-card">
            <p style="font-size: 1.5rem; text-align: center; color: #D63384; line-height: 2;">
                Bhawana, my love for you grows deeper with each passing moment. ✨<br>
                Your beauty radiates from within, touching everyone around you,<br>
                but your heart... oh your beautiful heart, that's what makes you truly special. 🌹<br><br>
                You are my dream come true, my answered prayer,<br>
                my favorite reason to smile every single day. 💫<br><br>
                You are and will always be my greatest blessing. 💝
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Interactive Elements
    if st.button("💝 Tap Here For Magic 💝", key="magic_button"):
        st.balloons()
        st.snow()
        st.markdown("""
            <div class="message-card" style="background: linear-gradient(45deg, #FFD700, #FFC0CB);">
                <p style="font-size: 2rem; text-align: center; color: #D63384;">
                    I Love You to Infinity and Beyond! 💖
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    # Signature
    st.markdown("""
        <div class="signature">
            Forever Yours,<br>
            Susanta Baidya 💕
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
