
from app import create_app
import os

app = create_app()

if __name__ == "__main__":
    # Only launch Tkinter when running manually, not in tests
    if os.environ.get("TESTING") != "1":
        import threading
        import tkinter as tk
        from ACEest_Fitness import FitnessTrackerApp

        def run_tkinter_app():
            root = tk.Tk()
            app_instance = FitnessTrackerApp(root)
            root.mainloop()

        threading.Thread(target=run_tkinter_app).start()

    app.run(debug=True)

