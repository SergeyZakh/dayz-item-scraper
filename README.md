# 🎮 DayZ Item Scraper

[![CI/CD Pipeline](https://github.com/SergeyZakh/dayz-item-scraper/workflows/DayZ%20Item%20Scraper%20CI%2FCD/badge.svg)](https://github.com/SergeyZakh/dayz-item-scraper/actions)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub release](https://img.shields.io/github/release/SergeyZakh/dayz-item-scraper.svg)](https://github.com/SergeyZakh/dayz-item-scraper/releases/)
[![Downloads](https://img.shields.io/github/downloads/SergeyZakh/dayz-item-scraper/total.svg)](https://github.com/SergeyZakh/dayz-item-scraper/releases)
[![Stars](https://img.shields.io/github/stars/SergeyZakh/dayz-item-scraper.svg?style=social&label=Star)](https://github.com/SergeyZakh/dayz-item-scraper)

A comprehensive Python web scraper that automatically downloads **ALL DayZ item icons** from the [DayZ Fandom Wiki](https://dayz.fandom.com). This professional-grade tool extracts high-quality item images and organizes them into a logical folder structure based on the wiki's own categorization system.

> 🎯 **Perfect for DayZ content creators, mod developers, and community projects!**

## ✨ Features

- **Complete Coverage**: Scrapes 37+ item categories covering weapons, equipment, clothing, food, medical supplies, and more
- **Intelligent Organization**: Automatically organizes downloaded images into hierarchical folders (e.g., `Weapons/Assault_Rifles/`, `Equipment/Backpacks/`)
- **High Quality Images**: Downloads images in highest available resolution with `/revision/latest` parameter
- **Smart Filtering**: Advanced filtering system eliminates UI elements, logos, and irrelevant images
- **Duplicate Prevention**: Automatically skips already downloaded files
- **Respectful Scraping**: Implements proper delays and browser headers to avoid server overload
- **Progress Tracking**: Real-time progress updates and detailed statistics
- **Error Handling**: Robust error handling with detailed logging
- **Wiki-Based Categorization**: Uses the wiki's own category system instead of error-prone name guessing

## Output Structure

The scraper creates a well-organized folder structure:

```
dayz_items/
├── Weapons/
│   ├── Assault_Rifles/
│   │   ├── AK-74.png
│   │   ├── M4-A1.png
│   │   └── ...
│   ├── Sniper_Rifles/
│   ├── Shotguns/
│   ├── Pistols/
│   ├── Melee/
│   ├── Ammunition/
│   ├── Magazines/
│   └── Attachments/
├── Equipment/
│   ├── Backpacks/
│   ├── Vests/
│   ├── Helmets/
│   ├── Tools/
│   └── Electronics/
├── Clothing/
│   ├── Tops/
│   ├── Bottoms/
│   ├── Shoes/
│   └── Gloves/
├── Food/
│   ├── Canned/
│   ├── Fresh/
│   ├── Drinks/
│   └── Seeds/
└── Medical/
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Internet connection
- ~500MB disk space (for all images)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/dayz-item-scraper.git
   cd dayz-item-scraper
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the scraper:**
   ```bash
   python dayz_item_scraper.py
   ```

### Alternative Installation (Direct Download)

1. Download `dayz_item_scraper.py` and `requirements.txt`
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python dayz_item_scraper.py`

## Expected Results

- **~600+ item images** from all DayZ categories
- **37+ categories** automatically discovered and scraped
- **Success rate**: Typically 85-95% depending on wiki availability
- **Runtime**: 15-30 minutes depending on internet speed
- **File size**: ~300-500MB total

## ⚙️ Configuration

You can modify these variables in the script to customize behavior:

```python
# Configuration options
BASE_URL = "https://dayz.fandom.com"    # Wiki base URL
OUTPUT_DIR = "dayz_items"               # Output directory name
HEADERS = {...}                         # Browser headers for requests
```

### Adding Custom Categories

To add additional categories, modify the `MAIN_CATEGORIES` list:

```python
MAIN_CATEGORIES = [
    # ... existing categories ...
    "https://dayz.fandom.com/wiki/Category:Your_Custom_Category",
]
```

## 🔧 How It Works

The scraper uses a sophisticated 3-phase approach:

### Phase 1: Category Discovery
- Scans predefined wiki category pages
- Automatically discovers additional categories
- Extracts all item page links
- Maps wiki categories to folder structures

### Phase 2: Image Extraction
- Visits each item's individual wiki page
- Uses multiple strategies to find item images:
  1. **Main image detection**: Finds the primary item icon
  2. **Gallery scanning**: Discovers variant images
  3. **Filename matching**: Fallback method for edge cases
- Filters out UI elements, logos, and irrelevant images

### Phase 3: Download & Organization
- Downloads all discovered images
- Creates organized folder structure
- Generates descriptive filenames
- Avoids duplicate downloads

## Ethical Considerations

This scraper is designed to be **respectful and ethical**:

- **Rate Limiting**: Implements delays between requests (0.3-0.8 seconds)
- **Browser Headers**: Uses proper User-Agent to identify requests
- **Error Handling**: Gracefully handles server errors without retry loops
- **Content Respect**: Only downloads publicly available wiki content
- **Fair Use**: Images are downloaded for personal/educational use

## Troubleshooting

### Common Issues

**"Connection Error" or "Timeout":**
- Check your internet connection
- The wiki might be temporarily unavailable
- Try running the script later

**"Permission Denied" when saving files:**
- Ensure you have write permissions in the script directory
- Try running with administrator/sudo privileges
- Check available disk space

**Missing images or low success rate:**
- Wiki structure might have changed
- Some item pages might be temporarily unavailable
- Check the console output for specific error messages

### Debug Mode

Add this to enable verbose logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📈 Performance

- **Memory Usage**: ~50-100MB RAM
- **Network Usage**: ~300-500MB download
- **CPU Usage**: Low (mostly I/O bound)
- **Disk Usage**: ~500MB for all images

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Add tests** if applicable
5. **Commit**: `git commit -m 'Add amazing feature'`
6. **Push**: `git push origin feature/amazing-feature`
7. **Create Pull Request**

### Areas for Contribution

- Additional image filtering improvements
- Better error handling and retry logic
- Performance optimizations
- Support for other game wikis
- GUI interface
- Docker containerization

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational and personal use only. The DayZ game and its assets are property of Bohemia Interactive. Wiki content is provided by the Fandom community under their respective licenses. Please respect the terms of service of both DayZ and Fandom.

## 🙏 Acknowledgments

- **DayZ Fandom Wiki** contributors for maintaining comprehensive item information
- **Bohemia Interactive** for creating DayZ
- **Python community** for excellent libraries (requests, BeautifulSoup)
- **Contributors** who help improve this tool

## 📞 Support

If you encounter issues or have questions:

1. Check the [Issues](https://github.com/your-username/dayz-item-scraper/issues) page
2. Create a new issue with:
   - Your Python version
   - Error messages (if any)
   - Steps to reproduce the problem
3. For general questions, use [Discussions](https://github.com/your-username/dayz-item-scraper/discussions)

---

**Star ⭐ this repository if you find it useful!**

Made with ❤️ by the DayZ community
