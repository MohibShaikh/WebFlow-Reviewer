# 🌐 WebFlow Reviewer

A lightning-fast, keyboard-driven tool for efficiently reviewing and categorizing websites. Perfect for content moderators, SEO specialists, and web researchers who need to quickly evaluate multiple websites.

## 🎯 Why WebFlow Reviewer?

- 🚄 **Speed-Optimized** - Review hundreds of websites with just single keystrokes
- 🎮 **Keyboard-Centric** - No mouse needed, everything at your fingertips
- 📊 **Progress Tracking** - Real-time statistics and progress monitoring
- 💾 **Auto-Save** - Results automatically saved with timestamps
- 🔄 **Resume-Friendly** - Skip websites and come back later

## 🚀 Installation

```bash
git clone https://github.com/MohibShaikh/WebFlow-Reviewer.git
cd website-reviewer
pip install -r requirements.txt
```

## 📝 Usage

1. Prepare a CSV file with a column named 'url' containing your websites
2. Run the script:
   ```bash
   python website_reviewer.py
   ```
3. Enter the path to your CSV file when prompted
4. Review each website using:
   - `y` - Mark as good
   - `n` - Mark as bad
   - `q` - Quit the process

## 📋 Input CSV Format

Your input CSV should look like this:
```csv
url
https://example.com
https://example.org
```

## 📊 Output

Results are saved in a new CSV file named `website_reviews_TIMESTAMP.csv` with the format:
```csv
url,review
https://example.com,good
https://example.org,bad
```

## 🛠️ Requirements

- Python 3.6+
- See `requirements.txt` for package dependencies

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
