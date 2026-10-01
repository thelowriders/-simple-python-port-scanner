# multithreaded Python Port Scanner

A fast, multithreaded TCP port scanner built from scratch in python.designed for foundational computer science and cybersecurity reconnaissance practice

## features
- multi threading: built using Python's `threading` and `Queue` libraries to scan up to 50 ports concurrently
- automated logging: saves discovered open ports dynamically to a local `scan_results.log` file with timestamps
- safe testing defaults: configured out of the box to safely target localhost (`127.0.0.1`)

## how to Run It
1. download the `scanner.py` file.
2. open your terminal or command prompt in that folder.
3. run the script using python:
   ```bash
   python scanner.py
   ```

##⚠️ Disclaimer
this tool is intended strictly for educational purposes and authorized penetration testing within private lab environments. unauthorized port scanning can be flagged as malicious network behavior. always obtain explicit permission before scanning external targets
