import hashlib
from PIL import Image
import os

REFERENCE_IMAGE_PATH = 'static/image1.jpg'
REFERENCE_HASH = None

def init_reference_hash():
    """Вычисляет хеш эталонного изображения один раз при старте приложения."""
    global REFERENCE_HASH
    if os.path.exists(REFERENCE_IMAGE_PATH):
        try:
            with Image.open(REFERENCE_IMAGE_PATH) as img:
                # Используем SHA-256 вместо MD5 для безопасности
                REFERENCE_HASH = hashlib.sha256(img.tobytes()).hexdigest()
                print(f"[INFO] Reference coconut hash calculated: {REFERENCE_HASH[:10]}...")
        except Exception as e:
            print(f"[ERROR] Could not load reference image: {e}")
            REFERENCE_HASH = None
    else:
        print(f"[WARNING] Reference image not found at {REFERENCE_IMAGE_PATH}")
        REFERENCE_HASH = None

def verify_coconut_image(file_storage):
    """Сравнивает хеш загруженного файла с эталоном."""
    if REFERENCE_HASH is None:
        return False
    
    try:
        user_image = Image.open(file_storage)
        # Важно: то же самое преобразование байтов, что и у эталона
        user_hash = hashlib.sha256(user_image.tobytes()).hexdigest()
        return user_hash == REFERENCE_HASH
    except Exception:
        return False