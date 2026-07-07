@echo off
echo Downloading final LoRA weights...
mkdir models 2>nul
curl -L -o models\real_human.safetensors https://huggingface.co/px6/real-human-lora-ltx2.3/resolve/main/models/real_human.safetensors?download=true
echo.
echo Download complete! The model is in the models folder.
pause
