# 🎮 DayZ Item Scraper

A simple Python script that downloads **all item icons** from the [DayZ Fandom Wiki](https://dayz.fandom.com).

## 🚀 Quick Start

1. **Install Python 3.8+**
2. **Install dependencies:**
   ```bash
   pip install requests beautifulsoup4 lxml
   ```
3. **Run the scraper:**
   ```bash
   python dayz_item_scraper.py
   ```

Icons will be downloaded to `dayz_items/` folder, organized by category (Weapons, Equipment, etc.).

## ✨ Features

- Downloads **700+ item icons** from 37+ categories
- **Smart organization** into folders (Weapons/Rifles/, Equipment/Backpacks/, etc.)
- **Duplicate detection** - skips already downloaded files
- **Rate limiting** - respectful to the wiki servers
- **Cross-platform** - works on Windows, Linux, macOS

## 📁 Output Structure

```
dayz_items/
├── Weapons/
│   ├── Assault_Rifles/
│   ├── Sniper_Rifles/
│   └── ...
├── Equipment/
│   ├── Backpacks/
│   ├── Storage/
│   └── ...
└── Clothing/
    ├── Headgear/
    ├── Tops/
    └── ...
```

## 🔧 Requirements

- Python 3.8+
- Internet connection
- ~500MB free disk space

## 📝 License

MIT License - feel free to use for any purpose!

## 🐛 Issues?

- Check your internet connection
- Make sure you have write permissions
- Try running as administrator/sudo if needed

Perfect for **DayZ content creators** and **mod developers**! 🎯

If you want to support me - I would appreciate a Donation.

paypal.me/acasahar?country.x=DE&locale.x=de_DE
