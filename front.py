import streamlit as st
import requests
import yt_dlp
import urllib.parse

# --- PAGE CONFIG ---
st.set_page_config(
    page_title='Online Video Downloader',
    page_icon=":smiley:",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Define the account details
account_name = "Alice Goldman"
account_number = "40630168569188462"
bank_name = "WELLS FARGO BANK, N.A."

# CSS to hide Streamlit's default menu and footer
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

def check_internet_connection():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def main():
    st.title('Download Vid')

    # Create a text input field for the video URL
    video_url = st.text_input('Enter the video URL')

    # Create a button to trigger the download
    if st.button('Process Video'):
        # Display a spinner while waiting for the response
        with st.spinner('Processing...'):
            # Send a POST request to your Flask backend
            backend_url = 'https://video-download-9jmu.onrender.com'  # Update to your actual backend URL
            response = requests.post(backend_url, data={'url': video_url})

            if response.status_code == 200:
                try:
                    download_links = response.json()
                    st.write('Download Links:')
                    for i, link in enumerate(download_links, start=1):
                        # Fetch the video information from yt-dlp
                        decoded_url = urllib.parse.unquote(video_url)
                        ydl_opts = {
                            'format': 'best',  # You can adjust the format based on your requirements
                            'quiet': True,
                        }
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            info = ydl.extract_info(decoded_url, download=False)
                            title = info.get('title', f'downloaded_video_{i}')
                            thumbnail_url = info.get('thumbnail')

                        # Display video title and preview
                        st.subheader(f'Video Title:')
                        st.write(f'Video Name: {title}')

                        # Fetch the video content from the provided link
                        video_content = requests.get(link).content

                        # Create a download button with the video content and the video title as the filename
                        st.download_button(f'Download Video {i}', data=video_content, file_name=f'{title}.mp4', key=f'download_button_{i}')
                except Exception as e:
                    st.error(f'Error processing the video: {str(e)}')
            else:
                st.error(f'Error fetching download links: Status Code {response.status_code}')

    # Introduction
    st.write("""Please consider donating any amount you have, this free tool was built with Python by Goldman Precious, and any donation you make will be very much appreciated 💚🌍. With love from Nigeria.""")

    # Display donation information
    st.header('Donations:')
    st.markdown('If you are donating from Nigeria, [Click here](https://paystack.com/pay/donate-nigeria)')
    
    st.subheader("If you are donating from other parts of the world, kindly transfer to the account details below")
    st.write(
        f'<div style="border: 2px solid #999; color:yellow; padding: 20px; border-radius: 10px;">'
        f'<h3>Bank Account Details</h3>'
        f'<p><b>Account name:</b> {account_name} </p>'
        f'<p><b>Bank name:</b> {bank_name} </p>'
        f'<p><b>Account number:</b> {account_number} </p>'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        """
        Welcome to the Online Video Downloader! This tool allows you to easily download videos from various websites.
        Simply enter the video URL, click the "Download" button, and get ready to save your favorite videos for offline viewing.
        """
    )

    # How to Use
    st.header('How to Use:')
    st.markdown(
        """
        1. Enter the URL of the video you want to download in the provided text input field.

        2. Click the "Download" button to start the download process.

        3. Once the download links are available, you can preview the video, see its name, and download it to your device.
        """
    )

    # Platforms
    st.header('Platforms you can download from:')
    st.markdown(
        """
        1. Instagram
        2. Facebook
        3. TikTok
        4. YouTube
        5. X (formerly known as Twitter)
        """
    )

    # Write-up and Copyright
    st.markdown(
        """
        ---
        © 2023 Online Video Downloader. All Rights Reserved.
        """
    )

if check_internet_connection():
    main()
else:
    st.error("No internet connection. Please check your internet connectivity and try again.")
