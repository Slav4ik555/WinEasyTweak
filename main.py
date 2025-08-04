import subprocess
import customtkinter
import threading
import os
import requests

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
    
        # Program settings
        self.geometry("250x200")
        self.resizable(False, False)
        self.title("WinEasyTweak")
        padx = 10
        pady = 5
        button_width = 9999

        # Widgets
        self.button1 = customtkinter.CTkButton(self, text="Debloat Windows", command=self.button_debloat_event, width=button_width)
        self.button1.grid(row=0,column=0,padx=padx, pady=pady)

        self.button2 = customtkinter.CTkButton(self, text="Activate Windows/Office", command=self.button_activate_event, width=button_width)
        self.button2.grid(row=1,column=0,padx=padx, pady=pady)

        self.button3 = customtkinter.CTkButton(self, text="Install All Redistributable Runtimes", command=self.check_and_download_vcpp, width=button_width)
        self.button3.grid(row=2,column=0,padx=padx, pady=pady)

        self.label1 = customtkinter.CTkLabel(self, text="")
        self.label1.grid(row=3,column=0,padx=padx, pady=pady)

        self.label2 = customtkinter.CTkLabel(self, text="by SL1X")
        self.label2.grid(row=4,column=0,padx=padx, pady=pady, sticky="sw")

        self.label3 = customtkinter.CTkLabel(self, text="v1.0.0")
        self.label3.grid(row=4,column=0,padx=padx, pady=pady, sticky="se")

        # Grid configuration for stretching
        self.grid_columnconfigure(0, weight=1)  # First column stretches
        self.grid_rowconfigure(4, weight=1)  # Fourth row stretches

    def button_debloat_event(self):
        def run_debloat():
            self.label1.configure(text="Debloating Windows...")
            command = "& ([scriptblock]::Create((irm \"https://win11debloat.raphi.re/\"))) -RunDefaults -Silent"
            ps_command = f"powershell.exe -Command \"{command}\""
            try:
                subprocess.run(ps_command)
            except Exception as e:
                print(f"An error occurred: {e}")
            self.label1.configure(text="")
        threading.Thread(target=run_debloat).start()

    def button_activate_event(self):
        self.label1.configure(text="Activating...")
        def run_activate():
            command = "& ([ScriptBlock]::Create((irm https://get.activated.win)))"
            ps_command = f"powershell.exe -Command \"{command}\""
            try:
                subprocess.run(ps_command)
            except Exception as e:
                print(f"An error occurred: {e}")
            self.label1.configure(text="")
        threading.Thread(target=run_activate).start()

    def download_file(self, url, filename):
        self.label1.configure(text="Downloading...")
        """Function to download a file from URL."""
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Error checking
            with open(filename, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"File {filename} downloaded successfully.")
            return True
        except Exception as e:
            print(f"Error downloading file: {e}")
            return False
        self.label1.configure(text="")
    
    def check_and_download_vcpp(self):
        def run_vcc_install(): 
            """Checks for file existence and downloads if missing."""
            filename = "VisualCppRedist_AIO_x86_x64.exe"
            if not os.path.exists(filename):  # File existence check
                print(f"File {filename} not found. Starting download...")
                url = "https://kutt.it/vcpp"  # Download URL
                if self.download_file(url, filename):
                    print("Download completed. Running file...")
                    self.label1.configure(text="Installing...")
                    subprocess.run([filename], shell=True)  # Run file
                else:
                    print("Failed to download file.")
            else:
                print(f"File {filename} already exists. Running...")
                self.label1.configure(text="Installing...")
                subprocess.run([filename], shell=True)  # Run file
            self.label1.configure(text="")
        threading.Thread(target=run_vcc_install).start()

app = App()
app.mainloop()