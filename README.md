# Quick Setup Guide 🚀

## 1. Install Software

### Python (3.8+)
- Download: https://www.python.org/downloads/
- ✅ Check "Add Python to PATH" during install
- Verify: `python --version`

### MySQL
- Download: https://dev.mysql.com/downloads/installer/
- Set root password: `root`
- Port: `3306`
# MySQL Workbench Download & Setup

## Download MySQL Workbench

**Option 1: With MySQL Installer (Recommended)**
1. Download MySQL Installer: https://dev.mysql.com/downloads/installer/
2. Run installer
3. Choose **"Developer Default"** setup type
4. It will install:
   - MySQL Server
   - MySQL Workbench
   - MySQL Shell
   - Connectors


### First Time Setup:
1. **Open MySQL Workbench**
2. Click **"+"** next to "MySQL Connections"
3. Enter details:
   - **Connection Name:** Local MySQL
   - **Hostname:** `localhost`
   - **Port:** `3306`
   - **Username:** `root`
   - **Password:** Click "Store in Vault" → enter `root`
4. Click **"Test Connection"**
5. Click **"OK"**

### Run Your Database Files:

**Method 1: Execute SQL File**
1. Open MySQL Workbench
2. Click your connection (Local MySQL)
3. Go to **File → Open SQL Script**
4. Select `E:\Sem 7\new\database.sql`
5. Click **⚡ Execute** button (or Ctrl+Shift+Enter)
6. Repeat for `E:\Sem 7\new\ASS8\database.sql`

**Method 2: Copy-Paste**
1. Open your connection
2. Click **Query tab** (blank editor)
3. Copy SQL from your `.sql` files

### VS Code
- Download: https://code.visualstudio.com/
- ✅ Check "Add to PATH"

### Browser
- Chrome/Edge (best for DevTools)

---

## 2. VS Code Extensions

Press `Ctrl+Shift+X` and install:
- **Python** (by Microsoft)
- **Live Server** (by Ritwick Dey) - for HTML
- **HTML CSS Support**
- **Auto Rename Tag**
- **JavaScript (ES6) code snippets**
- **MySQL** (optional)

---

## 3. Setup Project

```powershell

# Install packages
pip install -r requirements.txt
```

---

## 4. Setup Database

```powershell
# Login to MySQL
mysql -u root -p

# Run database files
mysql -u root -p < database.sql
cd ASS8
mysql -u root -p < database.sql
```

---

## 5. Run Assignments

### HTML/CSS/JS (ASS1-4, ASS6a)
- Right-click HTML file → "Open with Live Server"
- OR just open in browser

### Flask Apps (ASS5-8)
```powershell
cd ASS5  # or ASS6, ASS7, ASS8
python app.py
```
Access: `http://127.0.0.1:5000`

**ASS6 Login:** username: `admin`, password: `admin`

---

## 6. JavaScript - No Setup Needed!
- Runs in browser automatically
- Press `F12` → Console tab to debug
- Use `console.log()` for testing
- Your ASS3 already has JS validation working ✅


---

**That's it! Your ASS3 registration.html with JS validation is ready to run - just open with Live Server or browser!** 🎉
