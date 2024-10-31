import subprocess

# Define the input and output parameters
input_url = 'https://stream.spicefmbd.com/stream.m3u8'
output_url = 'rtmp://live.restream.io/live/re_8739149_eventbf65f345abb74307bca2b595dbc53754'

# Construct the FFmpeg command
command = [
    'ffmpeg',
    '-re',
    '-i', input_url,
    '-c:v', 'libx264',
    '-f', 'flv',
    output_url
]

# Execute the command
try:
    subprocess.run(command, check=True)
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
