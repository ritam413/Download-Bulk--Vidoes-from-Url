import subprocess
import sys

links = sys.argv[1:]  # receive links from main script

for url in links:
    print(f"⬇️ Downloading: {url}")

    process = subprocess.Popen(
        # ["yt-dlp", "--cookies", "hamster.txt", url ],
        ["yt-dlp",
            url,
            "--add-header", "Referer: https://embed.wilowitty.win/",
            "--add-header", "User-Agent: Mozilla/5.0"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    for line in process.stdout:
        print(line.strip())

    process.wait()

    if process.returncode == 0:
        print("✅ Done\n")
    else:
        print("❌ Failed\n")