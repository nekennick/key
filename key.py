import tkinter as tk
import pyperclip
from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if pressed and button == button.left:
        selected_text = pyperclip.paste()
        selected_text_label.config(text=f'Văn bản được chọn: {selected_text}')
        compare_text(selected_text)

def compare_text(selected_text):
    found = False
    with open('text.txt', 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split('|')
            if len(parts) > 1 and selected_text.strip() == parts[0].strip():
                result_label.config(text=f'Kết quả: {parts[1].strip()}')
                found = True
                break
    if not found:
        result_label.config(text='Kết quả: Không tìm thấy')

app = tk.Tk()
app.title('Ứng dụng so sánh văn bản được chọn')

# Đặt kích thước giao diện
app.geometry('500x100')

# Đặt cửa sổ luôn xuất hiện trên cùng
app.attributes('-topmost', True)

selected_text_label = tk.Label(app, text='')
selected_text_label.pack()

result_label = tk.Label(app, text='')
result_label.pack()

# Bắt đầu theo dõi sự kiện chuột để lấy và so sánh văn bản
with Listener(on_click=on_click) as listener:
    app.mainloop()
