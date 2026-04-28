import subprocess
import time
import random

# 🔹 Read links from file
def read_links(file):
    with open(file, "r") as f:
        return [line.strip() for line in f if line.strip()]

# 🔹 Split list into chunks
def chunk_list(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

# 🔹 Main logic
links = read_links("links.txt")

# Split into batches of 2
batches = list(chunk_list(links, 2))

for i, batch in enumerate(batches, start=1):
    print(f"\n🚀 Starting batch {i}: {batch}")

    subprocess.Popen(
        ["cmd", "/c", "start", "cmd", "/k", "python", "worker.py", *batch]
    )

    # 🔹 Random delay (5–15 seconds)
    delay = random.uniform(5, 15)
    print(f"⏳ Waiting {delay:.2f} seconds before next batch...")
    time.sleep(delay)

print("\n✅ All batches launched!")