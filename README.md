Hack Camera Script

Disclaimer: This tool is for educational purposes only. The author is not responsible for misuse. Do not access or manipulate devices without explicit permission.


---

⚡ Description

Hack Camera Script is a Python tool to quickly gather publicly accessible camera IPs from Insecam by country. It supports:

Multithreaded scraping for maximum speed

Saving collected IPs to a country-specific .txt file

Thread-safe operations to avoid duplicates

Graceful CTRL+C exit to save all collected links


This tool is intended for learning, testing, and educational research.


---

🛠 Requirements

Python 3.8+

termux,linux installation:


pkg install python pip install requests colorama


---

📋 Usage

1. Clone or download the repository:



git clone <repository_url>
cd <repository_folder>

2. Run the script:



python3 hack_camera.py

3. The script shows a country menu:



Countries List:
1) UNITED STATES
2) JAPAN
3) ITALY
...
OPTIONS :

4. Select a country by typing its number. Example:



OPTIONS : 10

5. The script will start scraping all camera IPs for the selected country:



http://123.45.67.89:8080
http://98.76.54.32:8080
...

6. To stop at any time, press CTRL+C. All collected IPs are saved automatically to a file:



<CountryCode>.txt

e.g., US.txt


---

📂 Output

Saves IPs in the current working directory.

Each IP is on a separate line.

Thread-safe collection avoids duplicates.



---

🚀 Features

Multithreaded scraping → faster results

Automatic saving on interrupt

Supports 90+ countries

Simple, terminal-based interface



---

⚠ Warnings

Only access publicly available cameras.

Avoid scanning aggressively to prevent being blocked.

Use responsibly and only for educational purposes.



---

📝 License

Educational use only. The author takes no responsibility for illegal usage.

