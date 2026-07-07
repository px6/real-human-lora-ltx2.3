import os
import urllib.request
import sys
import argparse

HF_REPO = "px6/real-human-lora-ltx2.3"
MODELS_DIR = "models"

def reporthook(block_num, block_size, total_size):
    if total_size > 0:
        percent = min(100, int(block_num * block_size * 100 / total_size))
        sys.stdout.write(f"\rDownloading... {percent}%")
        sys.stdout.flush()

def download_file(filename):
    url = f"https://huggingface.co/{HF_REPO}/resolve/main/models/{filename}?download=true"
    dest = os.path.join(MODELS_DIR, filename)
    print(f"\n--- {filename} ---")
    if not os.path.exists(dest):
        try:
            urllib.request.urlretrieve(url, dest, reporthook)
            print(f"\nSuccessfully saved to {dest}")
        except Exception as e:
            print(f"\nError downloading {filename}: {e}")
    else:
        print(f"File already exists, skipping.")

def main():
    parser = argparse.ArgumentParser(description="Download LoRA weights from Hugging Face.")
    parser.add_argument("--all", action="store_true", help="Download all checkpoints")
    parser.add_argument("--step", type=int, choices=[200, 400, 600, 800, 1000], help="Download a specific checkpoint step (e.g., 200, 400). 1000 is the final model.")
    
    args = parser.parse_args()
    os.makedirs(MODELS_DIR, exist_ok=True)
    
    if args.all:
        files = [
            "real_human.safetensors",
            "real_human_000000200.safetensors",
            "real_human_000000400.safetensors",
            "real_human_000000600.safetensors",
            "real_human_000000800.safetensors"
        ]
    elif args.step:
        if args.step == 1000:
            files = ["real_human.safetensors"]
        else:
            files = [f"real_human_000000{args.step}.safetensors"]
    else:
        # Default behavior: just the final model
        files = ["real_human.safetensors"]
        
    print(f"Preparing to download {len(files)} model file(s) from Hugging Face...")
    for f in files:
        download_file(f)
        
    print("\nAll requested downloads completed!")

if __name__ == "__main__":
    main()
