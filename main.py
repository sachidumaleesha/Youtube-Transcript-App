import youtube
import json

# Ask user for video link
youtube_link = input("Enter YouTube link: ")

isValid = youtube.is_youtube(youtube_link)

if isValid:
    if "v=" in youtube_link:
        video_id = youtube_link.split("v=")[1]
    elif "shorts/" in youtube_link:
        video_id = youtube_link.split("shorts/")[1]
    else:
        video_id = youtube_link.split("be/")[1].split("?")[0]

    if youtube.is_playable(video_id):
        video_title = youtube.get_title(video_id)
        transcript = youtube.get_transcript(video_id)

        output_json = {
            "title": video_title,
            "transcript": transcript
        }

        json_output = json.dumps(output_json, indent=2, ensure_ascii=False)
        print(json_output)
    else:
        output_json = {
            "error": "Video is not playable."
        }
        json_output = json.dumps(output_json, indent=2, ensure_ascii=False)
        print(json_output)
else:
    output_json = {
        "error": "Provide a valid YouTube link 🤖"
    }
    json_output = json.dumps(output_json, indent=2, ensure_ascii=False)
    print(json_output)
