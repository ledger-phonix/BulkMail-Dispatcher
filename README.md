# 🚀 Bulk Email Dispatcher

A clean, self-hosted, and lightweight bulk email broadcasting tool built to give you absolute control over your subscriber lists and email campaigns. Skip the expensive, bloated third-party newsletter subscriptions—this app runs entirely locally from a single pane of glass.

---

## 💡 How It Works

The application splits your workspace into a highly responsive, side-by-side interface:

* **Left Column (Recipients Management):** Input subscriber emails. The app automatically sanitizes whitespaces, converts text to lowercase, and saves it to a local database. It enforces strict unique constraints so duplicates never slip in. You can view your active pool and instantly drop any email with a single click.
* **Right Column (Broadcast Box):** Set up your custom SMTP relay server details, compose a high-converting message, and upload an optional file attachment. Once you hit send, the backend handles the delivery process asynchronously.

---

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Python 3** | Core application logic and automation engine. |
| **Streamlit** | Powers the modern, clean, two-column web user interface. |
| **SQLite3** | Lightweight, zero-configuration local database for recipient storage. |
| **MIME / SMTP** | Multi-part mail protocols to handle inline HTML rendering and file attachments. |

---

## 📦 Getting Started (One-Click Setup)

This repository is completely plug-and-play. Anyone cloning this project does not need to worry about manual environment configurations or installing dependencies.

### Running the App:
1. Clone this repository to your local machine.
2. Double-click the **`run_app.bat`** script.

> **What happens under the hood?**
> * **First Run:** The batch file automatically creates an isolated local virtual environment (`.venv`), upgrades `pip`, and installs all necessary packages from `requirements.txt`.
> * **Subsequent Runs:** It skips configuration entirely, boots up the local environment, and launches the Streamlit dashboard directly in your default web browser.

---

## 👨‍💻 Developed By

**Talha Nadeem** *Python Developer & Data Analyst*

Specializing in full-stack Python web development, end-to-end automation workflows, and high-impact data analytics dashboards. I build clean, modular codebases designed to solve real-world operational bottlenecks.

🌐 **Connect with me:**
* **GitHub:** [github.com/ledger-phonix](https://github.com/ledger-phonix)
* **LinkedIn:** [linkedin.com/in/talha-nadeem-python-developer](https://linkedin.com/in/talha-nadeem-pyhton-developer)
* **Portfolio:** [Portfolio Website](https://talhanadeem.onrender.com/)