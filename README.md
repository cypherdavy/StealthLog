
# STEALTHLOG 



StealthLog is a simple keylogger tool built using Python and the pynput library. It is designed for educational purposes, and should not be used for malicious purposes. The tool captures keystrokes and displays them in real-time in a graphical user interface (GUI) built using the tkinter library. The captured data can also be saved to a log file for later analysis.
## Authors

- [@cypherdavy](https://github.com/cypherdavy)


![Logo](https://i.ibb.co/zn52Bpj/stealthlog-logo.png)


## Badges



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## License

[MIT](https://choosealicense.com/licenses/mit/)

[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)

[GPL v3 License](https://choosealicense.com/licenses/gpl-3.0/)

[BSD 3-Clause License](https://gptcall.net/%3Chttps://choosealicense.com/licenses/bsd-3-clause/%3E)




# Installation


**Parrot Linux / Kali Linux / Termux**


## Clone the repository:
```bash
git clone https://github.com/cypherdavy/StealthLog.git
```
```bash
cd StealthLog
```
## Install the required packages:
```bash
pip3 install -r requirements.txt
```
## Run the tool:
```bash
python3 stealthlog.py
```
**Windows**

Download the repository as a ZIP file:
```bash
https://github.com/cypherdavy/StealthLog.git
```
Extract the ZIP file.

Open a command prompt in the extracted directory.

Install the required packages:
```bash
pip install -r requirements.txt
```
Run the tool:
```bash
python stealthlog.py
```
## Demo


https://www.instagram.com/p/C6JpX8bPS_B/

# Appendix
 StealthLog should only be used for ethical purposes and with proper authorization. Misuse of this tool can have serious legal consequences.

Additional Features:

StealthLog includes the ability to set a custom log file name by modifying the LOG_FILE_NAME variable in the stealthlog.py file.

StealthLog includes the ability to set a custom interval between log saves by modifying the TIME_BETWEEN_LOGS variable in the stealthlog.py file.

## Troubleshooting:

If you encounter any issues or errors while using StealthLog, refer to the official documentation or contact the StealthLog support team.

Be sure to read the error messages carefully and provide as much information as possible when reporting an issue.

## Conclusion:
StealthLog is a powerful and useful tool for developers, testers, and researchers. By following the instructions in this appendix, you can install, configure, and use StealthLog to gain valuable insights into user behavior and patterns. Remember to always use StealthLog ethically and with proper authorization.

Hashtags:
#keylogger
#sealthlog
#developertools
#python
#gpl
#openSource
#cybersecurity 
## FAQ

#### Question 1                                               Can StealthLog detect and log keyloggers or other monitoring tools? 

Answer 1 No, StealthLog is not designed to detect or log other monitoring tools. It is a keylogger only.

#### Question 2  Can StealthLog be used for penetration testing or ethical hacking?

Answer 2 Yes, StealthLog can be used for ethical hacking or penetration testing with proper authorization. It is important to use the tool responsibly and ethically.

#### Question 3  Can StealthLog log keypresses on virtual machines or remote desktops?

Answer 3 Yes, StealthLog can log keypresses on virtual machines or remote desktops, as long as it is installed and running on the machine where the keypresses are taking place.

#### Question 4 Can StealthLog log keypresses in real-time or near real-time?

Answer 4  Yes, StealthLog can log keypresses in real-time or near real-time, depending on the TIME_BETWEEN_LOGS setting.


## Lessons Learned

While building StealthLog, I learned about the `pynput` library in Python, which allows for the creation of keyloggers and other user input monitoring tools. I also learned about the importance of ethical considerations when building and using such tools.

One challenge I faced when building StealthLog was ensuring that the tool was as stealthy as possible, while still being easy to use and configure. I overcame this challenge by implementing a simple graphical user interface with buttons to start and stop the keylogger, as well as a label to display the contents of the log file. I also set the tool to save the log file every `TIME_BETWEEN_LOGS` seconds, which can be customized in the `stealthlog.py` file.

Another challenge I faced was ensuring that the tool was easy to install and use. I overcame this challenge by including a `requirements.txt` file with the required packages for StealthLog, and by providing detailed instructions for installation, configuration, and usage in the Appendix and FAQ.

Overall, the most important lesson I learned while building StealthLog was the importance of ethical considerations when building and using monitoring tools. It is essential to use such tools responsibly and with proper authorization, and to ensure that they do not violate user privacy or security.



## Roadmap

- Near-Term Goals
Add support for additional browsers (e.g. Firefox, Safari, Edge)
Add integration with popular productivity tools (e.g. Trello, Slack, Asana)
Implement a real-time dashboard for monitoring keypresses and log file contents
Add customizable themes and branding options for the user interface
- Mid-Term Goals
Implement machine learning algorithms to detect and flag suspicious user activity
Add support for mobile platforms (e.g. Android, iOS)
Implement a command-line interface for advanced users
Add support for cloud storage and syncing of log files
- Long-Term Goals
Add support for custom plugins and extensions
Implement a RESTful API for integration with other tools and applications
Implement a distributed architecture for large-scale deployments
Develop a professional version of StealthLog for use in enterprise environments

# Run Locally 

 Clone the StealthLog repository:
 ```bash
git clone https://github.com/cypherdavy/StealthLog.git
```
Change into the StealthLog directory:
```bash
cd StealthLog
```
## Install the required packages:
```bash
pip install -r requirements.txt
```
Run StealthLog:
```bash
python stealthlog.py
```
This will start the StealthLog keylogger and display the user interface. From here, you can start and stop the keylogger, and view the contents of the log file.
## Support

For support, email davycypher@gmail.com or join our Slack channel.


## Feedback

If you have any feedback, please reach out to us at davycypher@gmail.com


## Usage/Examples

```python
import pynput
from pynput.keyboard import Key, Listener

def on_press(key):
    with open("log.txt", "a") as f:
        f.write(str(key))
        f.write("\n")

with Listener(on_press=on_press) as listener:
    listener.join()
```


## 🛠 Skills
- Python programming
- Tkinter GUI development
- Keylogger design and implementation
- Cross-platform development
- Ethical hacking and cybersecurity
- Git and version control
- Responsible and ethical use of technology

