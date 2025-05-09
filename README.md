# Web Scraping Tool (Streamlit App)

This is a simple and beginner-friendly web scraping tool built using **Python**, **BeautifulSoup**, **Pandas**, and **Streamlit**. It allows users to extract specific HTML elements (like `p`, `h1`, `a`, `img`, etc.) from any publicly available website URL.

---

## Features

- Input any website URL
- Choose an HTML tag to extract (like `p`, `a`, `img`)
- View results directly in the browser
- Download the extracted data as a CSV file
- Error handling for invalid URLs or missing elements
- Simple and clean Streamlit interface

---

## Requirements

- Python 3.7 or higher
- pip (Python package installer)

---

## Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AditiS-2/web_scraping_tool.git
   cd web-scraping-tool
   ```
2. **Install dependencies:**
   ```bash
   pip install streamlit requests beautifulsoup4 pandas
   ```
3. **Run the app**
   ```bash
   streamlit run app.py
   ```

  ## Future Improvements
  - Select tag from dropdown instead of typing

  - Handle multiple tags at once

  - Scrape paginated websites

  - Deploy online using Streamlit Cloud
