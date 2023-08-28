import customtkinter as ctk
import tkinter as tk
import time
from app import settings
from tkinter import filedialog
from app.utility.process_emails import update_template, send_ses
from app.utility.read_files import read_template, read_csv
from app.utility.database import get_nickname


class App:
    def __init__(self) -> None:
        ctk.set_appearance_mode(settings.APP_APPEARANCE_MODE)
        self.root = ctk.CTk()
        self.root.geometry(settings.APP_GEOMETRY)
        self.root.title(settings.APP_TITLE)

        self.title = ctk.CTkLabel(self.root, text="Email Sender", font=ctk.CTkFont(size=30, weight="bold"))
        self.title.pack(padx=10, pady=(20, 20))

        template_label = ctk.CTkLabel(self.root, text="Template", font=ctk.CTkFont(size=15))
        template_label.pack(pady=(10, 0))

        template_path = ctk.CTkTextbox(self.root, height=20, width=350, wrap="none", state="disabled")
        template_path.pack(pady=(0, 5))

        template_button = ctk.CTkButton(self.root, height=30, width=60, text="Open", command=lambda: self.openFile(template_path))
        template_button.pack(pady=(0, 20))

        data_label = ctk.CTkLabel(self.root, text="Data", font=ctk.CTkFont(size=15))
        data_label.pack(pady=(10, 0))

        data_path = ctk.CTkTextbox(self.root, height=20, width=350, wrap="none", state="disabled")
        data_path.pack(pady=(0, 5))

        data_button = ctk.CTkButton(self.root, height=30, width=60, text="Open", command=lambda: self.openFile(data_path))
        data_button.pack(pady=(0, 10))

        ctk.CTkButton(self.root, height=30, width=100, text="Submit", command=lambda: self.submit(template_path, data_path)).pack(
            pady=(30, 0)
        )

        self.root.resizable(False, False)
        self.root.mainloop()

    def openFile(self, text_box):
        text_box.configure(state="normal")
        file_path = filedialog.askopenfilename()
        if file_path:
            text_box.delete("0.0", tk.END)
            text_box.insert("0.0", file_path)
        text_box.configure(state="disabled")

    def submit(self, template_path, data_path):
        # Get data of both text_boxes
        template_path = template_path.get("0.0", tk.END).strip()
        data_path = data_path.get("0.0", tk.END).strip()

        # Parse content of files
        template = read_template(template_path)
        data = read_csv(data_path)

        # Do the logic for email sending
        for record in data:
            if record.get("NICKNAME", "") == "":
                record["NICKNAME"] = get_nickname(record["EMAIL"])
            print(f"Processing {record['NICKNAME']}...")
            update_template(template, record["SUBJECT"])
            send_ses(record)
            print(f"Processing Done!")
            time.sleep(0.1)
        print("Done")

        # Show a popup that the logic is done
        popup = ctk.CTkToplevel(self.root)
        popup_label = ctk.CTkLabel(popup, text="Emails are successfully sent!")
        popup_label.pack(padx=20, pady=20)
        popup.after(10, popup.focus)
