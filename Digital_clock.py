import tkinter as tk 
import time

try :
    # GUI interface for the digital clock
    root = tk.Tk()
    root.title("Digital Clock")
    root.geometry("700x450")
    root.minsize(300, 300)

    themes = {
        "Cyberpunk": {"bg": "black", "fg": "cyan"},
        "Classic": {"bg": "black", "fg": "white"},
        "Matrix": {"bg": "black", "fg": "#39ff14"},      
        "Dracula": {"bg": "#282a36", "fg": "#ff79c6"},    
        "Ocean": {"bg": "#001f3f", "fg": "#7fdbff"},      
        "Sunset": {"bg": "#4a1c40", "fg": "#ff7a59"},    
        "Forest": {"bg": "#0b3d0b", "fg": "#7cfc00"},         
        "Royal": {"bg": "#2e003e", "fg": "#ffd700"},      
        "Retro": {"bg": "#2e211b", "fg": "#ff9800"}       
    }

    fonts = ["Helvetica", "Times New Roman", "Impact", "Comic Sans MS", "Arial Black","Verdana", "Georgia"]

    theme_names = list(themes.keys())
    current_theme_index = 0  
    current_font_index = 0
    current_font = fonts[current_font_index]
    current_format = "24H"

    # Change theme function
    def change_theme():
        global current_theme_index
        current_theme_index = (current_theme_index + 1) % len(theme_names)
        theme_name = theme_names[current_theme_index]
        new_background = themes[theme_name]["bg"]
        new_font_color = themes[theme_name]["fg"]

        root.config(bg=new_background)
        text_frame.config(bg=new_background)
        clock_label.config(bg=new_background, fg=new_font_color)
        date_label.config(bg=new_background, fg=new_font_color)
        button_frame.config(bg=new_background)


        btn_theme.config(text=f"Theme: {theme_name}", fg=new_font_color)
        btn_font.config(fg=new_font_color)
        btn_12h.config(fg=new_font_color)
        btn_24h.config(fg=new_font_color)
    
    def change_font():
        global current_font_index, current_font
        current_font_index = (current_font_index + 1) % len(fonts)
        current_font = fonts[current_font_index]
        current_width = root.winfo_width()
        clock_size = int(current_width / 12)
        clock_size = max(30, min(clock_size, 150))
        date_size = int(current_width / 25)
        date_size = max(12, min(date_size, 50))
        
        clock_label.config(font=(current_font, clock_size, "bold"))
        date_label.config(font=(current_font, date_size))
        btn_font.config(text=f"Font: {current_font}")
    # Set time format functions
    def set_12h():
        global current_format
        current_format = "12H"

    def set_24h():
        global current_format
        current_format = "24H"
    
    # Update the time displayed on the clock every second 
    def update_time():
        if current_format == "12H":
            time_string = time.strftime("%I:%M:%S %p")
        elif current_format == "24H":
            time_string = time.strftime("%H:%M:%S")
        
        clock_label.config(text=time_string)
        clock_label.after(1000, update_time)

        date_string = time.strftime("%A, %B %d, %Y")
        date_label.config(text=date_string)

    # Resize the text size based on the window size
    def resize_text(event):
        if event.widget == root:
            new_size = int(event.width / 15)
            new_size = max(20, min(new_size, 100))
            clock_label.config(font=(current_font, new_size, "bold"))

            date_size = int(event.width / 25)
            date_size = max(12, min(date_size, 50))
            date_label.config(font=(current_font, date_size))

    initial_bg = themes["Cyberpunk"]["bg"]
    initial_fg = themes["Cyberpunk"]["fg"]
    root.config(bg=initial_bg)    

    text_frame = tk.Frame(root, bg=initial_bg)
    text_frame.pack(expand=True)
        
    clock_label = tk.Label(text_frame, font=("Helvetica", 48, "bold"), bg=initial_bg, fg=initial_fg)
    clock_label.pack(expand=True, pady=20)

    date_label = tk.Label(text_frame, font=("Helvetica", 20), bg=initial_bg, fg=initial_fg)
    date_label.pack(pady=10)

    button_frame = tk.Frame(root, bg=initial_bg)
    button_frame.pack(side="bottom", pady=30)

    btn_style = {
        "font": ("times new roman", 11, "bold"),
        "bg": "#222222", 
        "fg": initial_fg,
        "relief": "flat",
        "bd": 0,
        "highlightthickness": 0,
        "cursor": "hand2",
        "activebackground": "#444444",
        "activeforeground": "white",
        "padx": 15,
        "pady": 8,
        
    }

    btn_12h = tk.Button(button_frame, text="12-Hour Format", command=set_12h, **btn_style)
    btn_24h = tk.Button(button_frame, text="24-Hour Format", command=set_24h, **btn_style)
    btn_font = tk.Button(button_frame, text=f"Font: {current_font}", command=change_font, **btn_style)
    btn_theme = tk.Button(button_frame, text="Theme: Cyberpunk", command=change_theme, **btn_style)

    btn_12h.grid(row=0, column=0, padx=10)
    btn_24h.grid(row=0, column=1, padx=10)
    btn_font.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
    btn_theme.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    root.bind("<Configure>", resize_text)
                
    update_time()
    root.mainloop()

except Exception as e:
    print("Unexpected Error:", e)