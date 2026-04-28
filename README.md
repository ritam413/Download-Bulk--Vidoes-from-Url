give in markdown format 
# 📥 Multi-Terminal Video Downloader (yt-dlp + Python)

A simple Python-based tool to **download multiple videos in parallel**, using **yt-dlp**, with each batch running in a **separate terminal window**.

---

## 🚀 Features

* 📂 Reads video links from a file (`links.txt`)
* ⚡ Downloads in **parallel batches**
* 🖥 Opens **multiple terminal windows** (Windows)
* 🔄 Uses a **worker script** for each batch
* ⏳ Adds **random delay (5–15s)** to avoid rate limiting
* 📡 Supports **custom headers** (Referer, User-Agent)

---

## 📁 Project Structure

```
project/
│
├── main.py        # Launches multiple terminals with batches
├── worker.py      # Handles downloading for each batch
├── links.txt      # List of video URLs (one per line)
└── README.md
```

---

## ⚙️ Requirements

* Python 3.x
* yt-dlp installed

Install yt-dlp:

```bash
pip install yt-dlp
```

---

## 📌 How It Works

### Step 1: Add Links

Create a file named `links.txt`:

```
https://example.com/video1
https://example.com/video2
https://example.com/video3
...
```

---

### Step 2: Run Main Script

```bash
python main.py
```

---

### Step 3: What Happens Internally

* Links are split into **batches of 2**
* Each batch opens in a **new CMD window**
* Each window runs:

```bash
python worker.py <link1> <link2>
```

* Worker downloads videos **sequentially inside that terminal**

---

## 🧠 Code Breakdown

### 🔹 `main.py`

* Reads links from file
* Splits into batches
* Launches separate terminals using:

```python
subprocess.Popen(
    ["cmd", "/c", "start", "cmd", "/k", "python", "worker.py", *batch]
)
```

* Adds random delay:

```python
delay = random.uniform(5, 15)
time.sleep(delay)
```

---

### 🔹 `worker.py`

* Receives links via command-line arguments:

```python
links = sys.argv[1:]
```

* Runs `yt-dlp` using subprocess:

```python
["yt-dlp",
 url,
 "--add-header", "Referer: https://embed.wilowitty.win/",
 "--add-header", "User-Agent: Mozilla/5.0"]
```

* Streams logs in real-time
* Prints:

  * ✅ Done (success)
  * ❌ Failed (error)

---

## 🛡️ Why Random Delay?

To avoid:

* Rate limiting 🚫
* Temporary bans ⚠️
* Server overload

---

## ⚠️ Notes

* Works on **Windows only** (uses `cmd`)
* Make sure `yt-dlp` is in PATH
* Some sites may require cookies (download cookies from browser using "getcookieslocally" extension )

---

## 🧪 Example Output

```
🚀 Starting batch 1: [link1, link2]
⏳ Waiting 8.23 seconds before next batch...

⬇️ Downloading: link1
[download] 100% of 10.00MiB
✅ Done

⬇️ Downloading: link2
❌ Failed
```

---




## ✅ Summary

* Uses **batching + multiprocessing (terminals)**
* Separates logic cleanly (`main` + `worker`)
* Helps avoid rate limiting using **delays + headers**

