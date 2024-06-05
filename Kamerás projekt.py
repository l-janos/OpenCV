import cv2
import datetime
import tkinter as tk
from tkinter import messagebox
#White box documentation / tesztelés -> A kód működése, és a függvények működése     Hozzáférésünk van a kódhoz
#Black box documentation / tesztelés -> A kód lefuttatása, az összkép ellenőrzése    Nincs hozáférésünk a kódhoz
#Állapotváltozók (adattagok)
is_grayscale = False
fps = 10
show_instructions = True
def show_message(title, message):
    #Ez lesz nekünk a Python doc
    """
    Megjelenít egy Tkinter felugró ablakot egy üzenettel.
    :param title : Az üzenet címe.
    :param message : AZ üzenet szövege.
    """
    root = tk.Tk()
    root.withdraw() #Elrejti a fő ablakot
    messagebox.showinfo(title, message)
    root.destroy()
def capture_video(source = 0):
    """
    Képet rögzít as zámítógép kamerájáról, és alkalmazza a megadott képfeldolgozási lépéseket.
    Figyeli a billentyűleütéseket, és az állapotváltozásokat módosítja.
    :param source : A kamera forrása (alapértelmezett : 0).
    """
    global is_grayscale, fps, show_instructions
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        show_message("Hiba", "Nem sikerült megnyitni a kamerát.")
        print("Nem sikerült megnyitni a kamerát.")
        return
    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    while True:
        ret, frame = cap.read()
        #Hibakezelés
        if not ret:
            show_message("Hiba", "Nem sikerült beolvasni a képkockát.")
            print("Nem sikerült beolvasni a képkockát.")
            break
        #Kép feldolgozása
        if is_grayscale:
            frame = apply_grayscale(frame)
        #Billentyűkombinációk kiírása
        if show_instructions:
            overlay_text(frame)
        cv2.imshow("Video", frame)
        key = cv2.waitKey(1000 // fps) & 0xff
        if key == ord("q"):
            break
        elif key == ord("s"):
            save_frame(frame)
        elif key == ord("g"):
            is_grayscale = not is_grayscale
        elif key == ord("l"):
            fps = 5
        elif key == ord("h"):
            fps = 60
        elif key == ord("i"):
            show_instructions = not show_instructions
    cap.release()
    cv2.destroyAllWindows()
def overlay_text(frame):
    """
    Kírja a képernyőre a bilentyűkombinációkat, és azok jelentéseit.
    :param frame : A képkocka, amelyre kiírjuk a szövegeket.
    """
    instructions = [
        "Billentyukombinaciok : ",
        "Q - Kilepes",
        "S - Kep mentese",
        "G - Szurkearnyalatos ki/be",
        "L - Lassitas",
        "H - Gyorsitas",
        "I - Utasitasok ki/be"
    ]
    y0, dy = 30, 30
    for i, line in enumerate(instructions):
        y = y0 + i * dy
        cv2.putText(frame, line, (10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
def process_frame(frame, *args, **kwargs):
    """
    Képfeldolgozási lépések végrehajtása a képkockán.
    :param frame : A képkocka, amelyen a feldolgozás történik.
    :param args : Tetszőleges számú, pozícionális argumentum.
    :param kwargs : Tetszőleges számú kulcsszavas argumentum.
    """
    for func in args:
        frame = func(frame, **kwargs)
    return frame
def apply_grayscale(frame, **kwargs):
    """
    Képfeldolgozási függvény, ami a képkockát szürkeárnyalatossá alakítja.
    :param frame : Képkocka, amin a képfeldolgozás történik.
    :param kwargs : Tetszőleges számú, kulcsszavas argumentum.
    :return : A szürkeárnyalatos képkocka.
    """
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
def save_frame(frame):
    """
    Elmeni a képkockát a számítógépre.
    :param frame : A képkocka, amelyet elmentünk.
    """
    filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    cv2.imwrite(filename, frame)
    show_message("Kép mentve", f"A kép elmentve a következp néven : {filename}")
    print(f"A kép elmentve a következő néven : {filename}")
#Videó rögzítése
capture_video(0)