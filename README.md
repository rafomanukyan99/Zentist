## Prerequisites

- Python 3.11+
- pip

## How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/rafomanukyan99/Zentist.git
   cd YOUR_REPO
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv .venv
   ```

   - Windows (PowerShell):
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**

   ```bash
   playwright install chromium
   ```

5. **Run tests**

   ```bash
   pytest
   ```

## Test Scenarios

| # | Scenario | File |
|---|----------|------|
| 1 | Main Page — title, Fork me element, 44 links | `test_main_page.py` |
| 2 | Login Page — 15 invalid credentials test cases | `test_login_page.py` |
| 3 | Login/Logout — full authentication flow | `test_login_logout.py` |