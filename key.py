import tkinter as tk
import pyperclip
from pynput.mouse import Listener
import keyboard

def on_click(x, y, button, pressed):
    if pressed and button == button.left:
        selected_text = pyperclip.paste()
        selected_text_label.config(text=f'Selected: {truncate_text(selected_text)}')
        compare_text(selected_text)

def truncate_text(text, max_length=30):
    if len(text) > max_length:
        return text[:max_length] + '...'
    return text

def compare_text(selected_text):
    found = False
    with open('text.txt', 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split('|')
            if len(parts) > 1 and selected_text.strip() == parts[0].strip():
                result_var.set(f'KQ: {parts[1].strip()}')
                found = True
                break
    if not found:
        result_var.set('KQ: không thấy')

def close_app():
    app.destroy()

app = tk.Tk()
app.title('Bypass Elearning')

# Đặt cửa sổ luôn xuất hiện trên cùng
app.attributes('-topmost', True)

# Ẩn nút close, minimize và maximize
app.overrideredirect(True)

# Đặt kích thước giao diện và vị trí góc dưới bên trái
app.geometry('150x50+0+{}' .format(app.winfo_screenheight() - 60))

frame = tk.Frame(app)
frame.pack(expand=True, fill="both")

selected_text_label = tk.Label(frame, text='')
selected_text_label.pack()

result_var = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_var, font=('Helvetica', 14), justify="center")
result_label.pack(expand=True)

# Bắt đầu theo dõi sự kiện chuột để lấy và so sánh văn bản
with Listener(on_click=on_click) as listener:
    # Thêm sự kiện theo dõi phím Ctrl + E để đóng cửa sổ
    keyboard.add_hotkey('ctrl+e', close_app)
    app.protocol("WM_DELETE_WINDOW", close_app)  # Gắn sự kiện đóng cửa sổ

    app.mainloop()
