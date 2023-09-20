import tkinter as tk
import pyperclip
from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if pressed and button == button.left:
        selected_text = pyperclip.paste()
        selected_text_label.config(text=f'Văn bản được chọn: {selected_text}')
        app.update()  # Cập nhật giao diện

app = tk.Tk()
app.title('Ứng dụng hiển thị văn bản được chọn')

# Đặt kích thước giao diện
app.geometry('500x50')

# Đặt cửa sổ luôn xuất hiện trên cùng
app.attributes('-topmost', True)

selected_text_label = tk.Label(app, text='')
selected_text_label.pack()

# Bắt đầu theo dõi sự kiện chuột để lấy văn bản đã chọn
with Listener(on_click=on_click) as listener:
    app.mainloop()
