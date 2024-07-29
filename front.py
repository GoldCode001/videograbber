import streamlit as st
import requests

def main():
    st.title('Download Vid')

    # Create a text input field for the video URL
    video_url = st.text_input('Enter the video URL')

    # Create a button to trigger the video processing
    if st.button('Process Video'):
        # Display a spinner while waiting for the response
        with st.spinner('Processing...'):
            backend_url = 'https://video-download-9jmu.onrender.com/download'
            response = requests.post(backend_url, data={'url': video_url})

            if response.status_code == 200:
                download_info = response.json()
                download_url = download_info.get('download_url')
                title = download_info.get('title')

                if download_url:
                    # Use the filename to download the processed video
                    download_file_url = f'https://video-download-9jmu.onrender.com/download-file/{title}.avi'
                    
                    try:
                        file_response = requests.get(download_file_url)
                        if file_response.status_code == 200:
                            st.write('Download successful!')
                            st.download_button(
                                label=f'Download {title}',
                                data=file_response.content,
                                file_name=f'{title}.avi',
                                key='download_button'
                            )
                        else:
                            st.error(f'Error fetching file: Status Code {file_response.status_code}')
                    except requests.RequestException as e:
                        st.error(f'Request failed: {e}')
                else:
                    st.error('Download URL not found in response.')
            else:
                st.error(f'Error processing video: Status Code {response.status_code}')

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

if __name__ == '__main__':
    main()
