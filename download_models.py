import os
import urllib.request
import sys

HF_REPO = "px6/real-human-lora-ltx2.3"
MODELS_DIR = "models"
FILES = [
    "real_human.safetensors",
    "real_human_000000200.safetensors",
    "real_human_000000400.safetensors",
    "real_human_000000600.safetensors",
    "real_human_000000800.safetensors"
]

def reporthook(block_num, block_size, total_size):
    if total_size > 0:
        percent = min(100, int(block_num * block_size * 100 / total_size))
        sys.stdout.write(f"\rDownloading... {percent}%")
        sys.stdout.flush()

def main():
    print(f"Preparing to download {len(FILES)} model files from Hugging Face...")
    os.makedirs(MODELS_DIR, exist_ok=True)

    for file in FILES:
        url = f"https://huggingface.co/{HF_REPO}/resolve/main/models/{file}?download=true"
        dest = os.path.join(MODELS_DIR, file)
        
        print(f"\n--- {file} ---")
        if not os.path.exists(dest):
            try:
                urllib.request.urlretrieve(url, dest, reporthook)
                print(f"\nSuccessfully saved to {dest}")
            except Exception as e:
                print(f"\nError downloading {file}: {e}")
        else:
            print(f"File already exists, skipping.")
            
    print("\nAll downloads completed!")

if __name__ == "__main__":
    main()
