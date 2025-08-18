import cv2
import os
import time
import random
import string
import asyncio
import pygame
import edge_tts

VOICE = "id-ID-GadisNeural"  # suara wanita Indonesia

# ---------- Fungsi bantu ----------
def random_filename():
    return "tts_" + "".join(random.choices(string.ascii_letters + string.digits, k=6)) + ".mp3"

async def tts_and_play(text):
    print(f"[TTS] {text}")
    filename = random_filename()
    communicate = edge_tts.Communicate(text, voice=VOICE)
    await communicate.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.unload()
    pygame.mixer.quit()
    os.remove(filename)

# ---------- Main Program ----------
async def main():
    await tts_and_play("Selamat datang di Speech Foto. Tekan 5 untuk hitungan 5 detik atau 0 untuk hitungan 10 detik")

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cv2.namedWindow("Preview", cv2.WINDOW_NORMAL)

    durasi = 0
    while durasi not in [5, 10]:
        ret, frame = cap.read()
        if ret:
            cv2.putText(frame, "Tekan 5 atau 0 untuk pilih durasi",
                        (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 2, cv2.LINE_AA)   
            cv2.imshow("Preview", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('5'):
            durasi = 5
        elif key == ord('0'):
            durasi = 10

    await tts_and_play(f"Durasi {durasi} detik dipilih")

    folder = "hasil foto"
    os.makedirs(folder, exist_ok=True)

    for i in range(1, 4):  # 3 kali jepretan
        await tts_and_play(f"Pengambilan gambar dalam {durasi} detik")
        for t in range(durasi, 0, -1):
            ret, frame = cap.read()
            if ret:
                h, w = frame.shape[:2]
                cv2.putText(frame, str(t),
                            (w//2 - 50, h//2), cv2.FONT_HERSHEY_SIMPLEX,
                            5, (0, 0, 255), 10, cv2.LINE_AA)
                cv2.imshow("Preview", frame)
            if cv2.waitKey(1000) & 0xFF == ord("q"):
                break

        ret, frame = cap.read()
        if ret:
            existing = [int(f.split(".")[0]) for f in os.listdir(folder)
                        if f.endswith(".jpg") and f.split(".")[0].isdigit()]
            next_num = max(existing, default=0) + 1
            filename = os.path.join(folder, f"{next_num}.jpg")
            cv2.imwrite(filename, frame)
            print(f"Foto tersimpan: {filename}")

            cv2.imshow("Preview", frame)
            cv2.waitKey(1000)

    cap.release()
    cv2.destroyAllWindows()
    await tts_and_play("Pemotretan selesai. Foto disimpan dalam folder hasil foto")

if __name__ == "__main__":
    asyncio.run(main())
