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

# Hide Streamlit branding and footer
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

# Function to check internet connection
def check_internet_connection():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

if check_internet_connection():

    # Function to display the webpage content
    def main():
        st.title('Download Vid')

        # Create a text input field for the video URL
        video_url = st.text_input('Enter the video URL')

        # Create a button to trigger the download
        if st.button('Process Video'):
            # Display a spinner while waiting for the response
            with st.spinner('Processing...'):
                # Send a POST request to your Flask backend to get the download URL
                backend_url = 'https://video-download-9jmu.onrender.com'
                response = requests.post(backend_url, data={'url': video_url})

                if response.status_code == 200:
                    data = response.json()
                    download_url = data.get('download_url')
                    title = data.get('title', 'video')

                    if download_url:
                        st.write('Download Links:')
                        # Create a download button with the video content
                        st.button(f'Download Video', on_click=download_video, args=(download_url, title))
                else:
                    st.error(f'Error fetching download links: Status Code {response.status_code}')

        # Introduction and donation section
        st.write("""Please consider donating any amount you have, this free tool was built with python by Goldman precious, and any donation you make will be very much appreciated💚🌍. With love from nigeria""")
        st.header('Donations:')
        st.markdown('If you are donating from Nigeria, [Click here](https://paystack.com/pay/donate-nigeria)')
        st.subheader("If you are donating from other parts of the world kindly transfer to the account details below")
        st.write(
            f'<div style="border: 2px solid #999;color:yellow; padding: 20px; border-radius: 10px;">'
            f'<h3>Bank Account Details</h3>'
            f'<p><b>Account name:</b> Alice Goldman </p>'
            f'<p><b>Bank name:</b> WELLS FARGO BANK, N.A. </p>'
            f'<p><b>Account number:</b> 40630168569188462 </p>'
            '</div>',
            unsafe_allow_html=True
        )
        st.write("""








        """)
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

        # Platforms section
        st.header('Platforms you can download from:')
        st.markdown(
            """
            1. Instagram
            2. Facebook
            3. Tiktok
            4. Youtube
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

    def download_video(download_url, title):
        try:
            response = requests.get(download_url)
            if response.status_code == 200:
                st.write('Download successful!')
                st.download_button(label=f'Download {title}', data=response.content, file_name=f'{title}.mp4')
            else:
                st.error(f'Error fetching file: Status Code {response.status_code}')
        except requests.RequestException as e:
            st.error(f'Request failed: {e}')

    if __name__ == '__main__':
        main()

else:
    st.error("No internet connection. Please check your internet connectivity and try again.")
