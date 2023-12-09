# Import necessary libraries
import streamlit as st
import youtube
import json

st.set_page_config(page_title="Get Youtube Video Transcript", page_icon="🤟")

# Title of the web app
st.title("Get YouTube Video Transcript 🤟")

# Get user input for YouTube link using a text input box
youtube_link = st.text_input("Enter YouTube link:")

# Check if the "Get Transcript" button is clicked
if st.button("Get Transcript"):
    # Check if the provided link is a valid YouTube link
    isValid = youtube.is_youtube(youtube_link)

    # Display appropriate messages based on the validity of the link
    if isValid:
        if "v=" in youtube_link:
            video_id = youtube_link.split("v=")[1]
        elif "shorts/" in youtube_link:
            video_id = youtube_link.split("shorts/")[1]
        else:
            video_id = youtube_link.split("be/")[1].split("?")[0]
        
        # Check if the video is playable
        if youtube.is_playable(video_id):
            video_title = youtube.get_title(video_id)
            transcript = youtube.get_transcript(video_id)

            # Save the output as JSON
            output_json = {
                "title": video_title,
                "transcript": transcript
            }
            json_output = json.dumps(output_json, indent=2, ensure_ascii=False)

            # Display video information using Streamlit components
            st.subheader("Video Information:")
            st.write(f"Title: {video_title}")
            st.write("Transcript:")
            st.text_area("", transcript, height=300)
            st.download_button(
                label="Download Transcript",
                data=transcript,
                file_name="transcript.txt",
                key="download_button",
            )
        else:
            st.error("Error: Video is not playable 🥲")
    else:
        st.error("Error: Provide a valid YouTube link 🤖")


