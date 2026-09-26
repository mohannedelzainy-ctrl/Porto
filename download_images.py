import urllib.request
import os

images = {
    "trapezoidal-rule.jpg": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Integration_num_trapezes_notation.svg/800px-Integration_num_trapezes_notation.svg.png",
        "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?auto=format&fit=crop&w=800&q=80"
    ],
    "automatic-light-sensor.jpg": [
        "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Photoresistor.jpg/800px-Photoresistor.jpg"
    ],
    "cpp-calculator.jpg": [
        "https://images.unsplash.com/photo-1587145820266-a5951ee6f620?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=800&q=80"
    ],
    "tic-tac-toe.jpg": [
        "https://images.unsplash.com/photo-1668901382969-8c73e450a1f5?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1611996575749-79a3a250f948?auto=format&fit=crop&w=800&q=80"
    ],
    "dinosaur-game.jpg": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/T-Rex_game.svg/800px-T-Rex_game.svg.png",
        "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=800&q=80"
    ]
}

dest_dir = "image"
os.makedirs(dest_dir, exist_ok=True)
os.makedirs("images", exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

for filename, urls in images.items():
    success = False
    for url in urls:
        try:
            print(f"Trying to download {filename} from {url}...")
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
                if len(data) > 1000:
                    with open(os.path.join(dest_dir, filename), "wb") as f:
                        f.write(data)
                    with open(os.path.join("images", filename), "wb") as f:
                        f.write(data)
                    print(f"Successfully saved {filename} ({len(data)} bytes)")
                    success = True
                    break
        except Exception as e:
            print(f"Failed {url}: {e}")
    if not success:
        print(f"ERROR: Could not download {filename}")
