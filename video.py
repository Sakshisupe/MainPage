import base64
import streamlit as st

# Function to encode an image to base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Function to encode a video to base64
def encode_video_to_base64(video_path):
    with open(video_path, "rb") as video_file:
        return base64.b64encode(video_file.read()).decode()

# Path to your video
video_path = 'V1080.mp4'

# Encode the video
encoded_video = encode_video_to_base64(video_path)

# Path to your icon images
icon_image_path = 'cropped.png'
grass_icon_image_path = 'te.png'
new_icon_image_path = 'green2.png'

# Encode the icon images
encoded_icon = encode_image_to_base64(icon_image_path)
encoded_grass_icon = encode_image_to_base64(grass_icon_image_path)
encoded_new_icon = encode_image_to_base64(new_icon_image_path)

def add_corner_gif(gif_path):
    with open(gif_path, "rb") as gif_file:
        encoded_string = base64.b64encode(gif_file.read()).decode()
        return encoded_string

# Add the corner GIF
encoded_string = add_corner_gif('chat_icon2.gif')

# Set page config for wide layout
st.set_page_config(layout="wide")

# Display the header
st.markdown(
    f"""
    <style>
    body {{
        overflow: hidden;
    }}
    
    .block-container {{
        padding:0;
    }}
    
    .header {{       
        padding: 10px 20px;
        position: fixed;
        width: 86%;
        top: 0;
        z-index: 1000;
        margin-left: 70px;
    }}
    
    .video-wrapper {{
        position: fixed;
        width: 100%;
        height: 100vh; /* Full viewport height */
        overflow: hidden; /* Hide overflow to prevent scroll bars */
    }}

    .video-bg {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover; /* Ensures video covers the entire area */
        z-index: -1;
    }}
    
    

    
    .content {{
        padding-top: 60px; /* Ensure content is not hidden behind fixed header */
        text-align: center;
        margin-top:100px;
        margin-left: 30px;
    }}
    
    .icon-container {{
        position:relative;
        z-index: 1000;
    }}
    
    .corner-icon {{
        position:relative;
        top: 5px;
        left: 22px;
        z-index: 1000;
    }}
    
    .corner-icon img {{
        width: 80px;
        height: 55px;
    }}
    
    .grass-icon {{
        position: absolute;
        top: 55px;
        left: 17px;
        z-index: 1000;
    }}
    
    .grass-icon img {{
        width: 190px;
        height: 62px;
    }}
    
    .new-icon {{
        position: absolute;
        top: 50px;
        left: 15px;
        z-index: 1000;
    }}
    
    .new-icon img {{
        width: 190px;
        height: 90px;
    }}
    
    .main-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        position: relative;
    }}
    
    
    
    .learn-more-button {{
        margin-top: 20px; /* Adjust space from the text */
        margin-left: -50px;
        padding: 8px 16px;
        font-size: 18px;
        font-weight: bold;
        color: white;
        background-color: #4CAF50;
        border: none;
        border-radius: 12px;
        height: 50px;
        width: 160px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.3s ease;
    }}

    .learn-more-button:hover {{
        background-color: #45a049;
        transform: scale(1.05);
    }}
    
    .fade-in-text {{
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
        opacity: 1;
        text-align: right;
        line-height: 1.5; /* Spacing between lines */
        display: flex;
        flex-direction: column;
        align-items: flex-end; /* Align text to the right */
        margin-top: -150px;
        margin-left: 600px;
    }}

    .fade-in-text h1 {{
        font-size: 50px;
        color: green; /* Color for the first heading */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2); /* Adds a shadow effect */
        margin-top: -100px;
    }}

    .fade-in-text h3 {{
        font-size: 30px;
        color: green; /* Color for the subheading */
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2); /* Adds a shadow effect */
        margin-top: -15px;
        margin-right: 40px;
    }}

    .more-content {{
        display: none; /* Initially hidden */
        margin-top: 20px;
        text-align: right;
        font-size: 20px;
        color: #333;
        max-width: 500px; /* Optional: Limit the width of the content */
    }}

    .show {{
        display: block; /* Show when triggered */
    }}
    .corner-gif-container {{
        position: fixed;
        bottom: 10px;
        right: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 1000;
        
    }}
    .corner-gif {{
        width: 40px;
        height: 40px;
        margin-bottom: 20px;
        margin-right: 30px;
        border-radius: 45%;
        background: #FFD700;
        box-shadow: 0 0 0 10px rgba(255, 255, 255, 0.5);
    }}
    
    .left-icon {{
        width: 150px;
        height: 150px;
        border-radius: 50%;
        background: #FFD700;
        box-shadow: 0 0 0 10px rgba(255, 165, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        transition: background 0.3s, transform 0.3s;
        position: absolute;
        text-align: center;
    }}
    .left-icon img {{
        width: 90px;
        height: 90px;
    }}
    .left-icon p {{
        position: absolute;
        bottom: -30px;
        width: 100%;
        text-align: center;
        font-size: 14px;
        color: white;
        font-weight: bold;
    }}
    .left-icon:hover {{
        transform: scale(1.1);
    }}
    .right-icons {{
        position: relative;
        width: 500px;
        height: 500px;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    .right-icons .menu-item {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        transition: background 0.3s, transform 0.3s;
        position: absolute;
        background: linear-gradient(145deg, #f0f0f0, #dcdcdc);
        box-shadow: 0 0 0 10px rgba(255, 255, 255, 0.5);
        text-align: center;
    }}
    .right-icons .menu-item:hover {{
        background: linear-gradient(145deg, #e6e6e6, #cccccc);
        transform: scale(1.1);
    }}
    .right-icons .menu-item img {{
        width: 40px;
        height: 40px;
    }}
    .right-icons .menu-item p {{
        margin-top: 5px;
        font-size: 12px;
        color: black;
        font-weight: bold;
        width: 115px;
        text-align: center;
        overflow: hidden;
        text-overflow: ellipsis;
    }}
    </style>

    
    """,
    unsafe_allow_html=True
)

# Add some space below the header
st.write("<div style='padding-top: 60px'></div>", unsafe_allow_html=True)

# Embed the video with autoplay
video_html = f"""
    <div class="video-wrapper">
        <video class="video-bg" autoplay muted loop>
            <source src="data:video/mp4;base64,{encoded_video}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    
    <div class="corner-icon">
        <img src="data:image/png;base64,{encoded_icon}" alt="Cropped Icon">
    </div>
    <div class="grass-icon">
        <img src="data:image/png;base64,{encoded_grass_icon}" alt="Grass Icon">
    </div>
    <div class="new-icon">
        <img src="data:image/png;base64,{encoded_new_icon}" alt="New Icon">
    </div>
    
    
    <div class="main-container" style="margin-left: -1230px;margin-top:10px;">
        <div class="corner-gif-container" >
            <a href="https://chatbot-eeypqzuingcwio573pbmdn.streamlit.app/" target="_blank">
                <img src="data:image/gif;base64,{encoded_string}" class="corner-gif" style="background-color: #2E8B57;">
            </a>
            <div class="main-container" style="margin-bottom:-40px;margin-right:30px;">
        <div class="corner-gif-container">
            <a href="https://chatbot-eeypqzuingcwio573pbmdn.streamlit.app/" target="_blank">
                <img src="data:image/gif;base64,{encoded_string}" class="corner-gif" style="background-color: #2E8B57;">
            </a>
        </div>
        <div class="left-icon">
            <img src="https://img.icons8.com/?size=100&id=15937&format=png" alt="KisanGPT"/>
        </div>
        <div class="right-icons">
            <a href="https://weatherprediction-int5n6cd2cb99lwd82e8nl.streamlit.app/" target="_blank" class="menu-item" style="background-color: #2E8B57; transform: rotate(0deg) translate(200px) rotate(0deg);">
                <img src="https://img.icons8.com/?size=100&id=9247&format=png" alt="Weather Prediction and Alerts"/>
                <p>Weather Prediction and Alerts</p>
            </a>
            <a href="https://kisangpt-yz2xwrpgek2dpyejmdkv6x.streamlit.app/" target="_blank" class="menu-item" style="background-color: #87CEEB; transform: rotate(45deg) translate(200px) rotate(-45deg);">
                <img src="https://img.icons8.com/ios-filled/50/000000/soil.png" alt="Crop and Soil Management"/>
                <p>Crop and Soil Management</p>
            </a>
            <a href="https://kisangpt-cznnfkrrppvenh6uosf783.streamlit.app/" target="_blank" class="menu-item" style="background-color: #8B4513; transform: rotate(90deg) translate(200px) rotate(-90deg);">
                <img src="https://img.icons8.com/?size=100&id=54383&format=png" alt="Smart Farming Practices"/>
                <p>Smart Farming Practices</p>
            </a>
            <a href="https://stackoverflow.com/questions/60866205/python-streamlit-run-issue" class="menu-item" style="background-color: #FFFACD; transform: rotate(135deg) translate(200px) rotate(-135deg);">
                <img src="https://img.icons8.com/?size=100&id=HmUJDT2vb7mU&format=png" alt="Pest and Disease Control"/>
                <p>Pest and Disease Control</p>
            </a>
            <a href="https://kisan-gpt-ad4ugvdjy46icmg3uxqcsa.streamlit.app/" target="_blank" class="menu-item" style="background-color: #A52A2A; transform: rotate(180deg) translate(200px) rotate(-180deg);">
                <img src="https://img.icons8.com/?size=100&id=rS0iQ61DOzEQ&format=png" alt="Market and Financial Insights"/>
                <p>Market and Financial Insights</p>
            </a>
            <a href="https://cropyeildpredictor-fboxyicx7mpdsb5eansryr.streamlit.app/" target="_blank" class="menu-item" style="background-color: #DAA520; transform: rotate(225deg) translate(200px) rotate(-225deg);">
                <img src="https://img.icons8.com/?size=100&id=10117&format=png" alt="Resource Management"/>
                <p>Crop Yield Predictor</p>
            </a>
            <a href="https://discuss.streamlit.io/t/getting-an-error-streamlit-is-not-recognized-as-an-internal-or-external-command-operable-program-or-batch-file/361" alt="Sustainability and Environmental Impact" target="_blank" class="menu-item" style="background-color: #808000; transform: rotate(270deg) translate(200px) rotate(-270deg);">
                <img src="https://img.icons8.com/?size=100&id=25852&format=png" alt="Sustainability and Environmental Impact"/>
                <p>Supply Chain Management</p>
            </a>
            <a href="https://kisangpt-k3cxjmfypg5jb8wtkgzov9.streamlit.app/" target="_blank" class="menu-item" style="background-color: #F5F5DC; transform: rotate(315deg) translate(200px) rotate(-315deg);">
                <img src="https://img.icons8.com/ios-filled/50/000000/education.png" alt="Educational Resources"/>
                <p>Educational Resources</p>
            </a>
        </div>
    </div>
        </div>
        <div class="block-container">
            <div class="fade-in-text">
                <div><h1>Welcome to KisanGPT!</h1></div>
                <div><h3>Where Farming meets Excellence</h3></div>
            </div>
            <div class="learn-more-container" style="margin-left: 800px;margin-top:-17px;">
                <button class="learn-more-button" onclick="window.location.href='#learn-more'">Discover More</button>
            </div>
        </div>
    </div>
    
    </div>
"""

# Render the video in the Streamlit app
st.markdown(video_html, unsafe_allow_html=True)


