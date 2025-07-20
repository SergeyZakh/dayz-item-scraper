#!/usr/bin/env python3
"""
DayZ Item Icon Scraper

A comprehensive web scraper that automatically downloads all item icons from the DayZ Fandom Wiki.
This script extracts high-quality item images and organizes them into a proper folder structure
based on their wiki categories.

Author: Community Project
License: MIT
Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "Community Project"
__license__ = "MIT"

import requests
from bs4 import BeautifulSoup
import os
import time
import re
from typing import List, Tuple, Set, Dict

# =============================================================================
# CONFIGURATION SECTION
# =============================================================================

# Base configuration for the DayZ Fandom Wiki
BASE_URL = "https://dayz.fandom.com"
OUTPUT_DIR = "dayz_items"

# HTTP headers to mimic a real browser and avoid bot detection
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =============================================================================
# WIKI CATEGORIES TO SCRAPE
# =============================================================================
# 
# Strategy: We target specific wiki categories to ensure comprehensive coverage
# of all DayZ items. Each category corresponds to a different type of game item.
# This approach is more reliable than trying to guess item types from names.

MAIN_CATEGORIES = [
    # Primary categories - broad item classifications
    "https://dayz.fandom.com/wiki/Category:Weapons",
    "https://dayz.fandom.com/wiki/Category:Equipment", 
    "https://dayz.fandom.com/wiki/Category:Food",
    "https://dayz.fandom.com/wiki/Category:Medical_Items",
    "https://dayz.fandom.com/wiki/Category:Clothing",
    
    # Detailed weapon subcategories for better organization
    "https://dayz.fandom.com/wiki/Category:Assault_Rifles",
    "https://dayz.fandom.com/wiki/Category:Sniper_Rifles",
    "https://dayz.fandom.com/wiki/Category:Shotguns",
    "https://dayz.fandom.com/wiki/Category:Submachine_Guns",
    "https://dayz.fandom.com/wiki/Category:Pistols",
    "https://dayz.fandom.com/wiki/Category:Melee_Weapons",
    "https://dayz.fandom.com/wiki/Category:Ammunition",
    "https://dayz.fandom.com/wiki/Category:Magazines",
    "https://dayz.fandom.com/wiki/Category:Weapon_Attachments",
    
    # Equipment subcategories for precise classification
    "https://dayz.fandom.com/wiki/Category:Backpacks",
    "https://dayz.fandom.com/wiki/Category:Vests",
    "https://dayz.fandom.com/wiki/Category:Helmets",
    "https://dayz.fandom.com/wiki/Category:Eyewear",
    "https://dayz.fandom.com/wiki/Category:Masks",
    "https://dayz.fandom.com/wiki/Category:Hats",
    "https://dayz.fandom.com/wiki/Category:Tools",
    "https://dayz.fandom.com/wiki/Category:Electronics",
    "https://dayz.fandom.com/wiki/Category:Base_Building",
    
    # Clothing subcategories
    "https://dayz.fandom.com/wiki/Category:Tops",
    "https://dayz.fandom.com/wiki/Category:Bottoms",
    "https://dayz.fandom.com/wiki/Category:Shoes",
    "https://dayz.fandom.com/wiki/Category:Gloves",
    "https://dayz.fandom.com/wiki/Category:Bags",
    
    # Food and consumables
    "https://dayz.fandom.com/wiki/Category:Canned_Food",
    "https://dayz.fandom.com/wiki/Category:Fresh_Food",
    "https://dayz.fandom.com/wiki/Category:Drinks",
    "https://dayz.fandom.com/wiki/Category:Cooking",
    
    # Miscellaneous categories
    "https://dayz.fandom.com/wiki/Category:Containers",
    "https://dayz.fandom.com/wiki/Category:Resources",
    "https://dayz.fandom.com/wiki/Category:Books",
    "https://dayz.fandom.com/wiki/Category:Key_Cards",
    "https://dayz.fandom.com/wiki/Category:Vehicle_Parts",
    "https://dayz.fandom.com/wiki/Category:Seeds"
]


# =============================================================================
# CATEGORY MAPPING FUNCTIONS
# =============================================================================

def map_wiki_category_to_folder(wiki_category_name: str) -> str:
    """
    Maps wiki category names to proper folder structures.
    
    This function is crucial for organizing downloaded images into a logical
    folder hierarchy. Instead of guessing item types from names (which is
    error-prone), we use the wiki's own categorization system.
    
    Args:
        wiki_category_name: The category name from the wiki URL
        
    Returns:
        A folder path string (e.g., 'Weapons/Assault_Rifles')
        
    Design rationale:
    - Uses explicit mapping to avoid classification errors
    - Creates hierarchical structure for better organization
    - Has fallback logic for unknown categories
    """
    category_lower = wiki_category_name.lower()
    
    # Direct mappings for specific wiki categories
    # This is the most reliable method as it's based on the wiki's own structure
    category_mappings = {
        # Weapon categories
        'weapons': 'Weapons',
        'assault_rifles': 'Weapons/Assault_Rifles',
        'sniper_rifles': 'Weapons/Sniper_Rifles', 
        'shotguns': 'Weapons/Shotguns',
        'submachine_guns': 'Weapons/Submachine_Guns',
        'pistols': 'Weapons/Pistols',
        'melee_weapons': 'Weapons/Melee',
        'ammunition': 'Weapons/Ammunition',
        'magazines': 'Weapons/Magazines',
        'weapon_attachments': 'Weapons/Attachments',
        
        # Equipment categories
        'equipment': 'Equipment',
        'backpacks': 'Equipment/Backpacks',
        'vests': 'Equipment/Vests',
        'helmets': 'Equipment/Helmets',
        'eyewear': 'Equipment/Eyewear',
        'masks': 'Equipment/Masks',
        'hats': 'Equipment/Hats',
        'tools': 'Equipment/Tools',
        'electronics': 'Equipment/Electronics',
        'base_building': 'Equipment/Base_Building',
        'containers': 'Equipment/Containers',
        'resources': 'Equipment/Resources',
        'books': 'Equipment/Books',
        'key_cards': 'Equipment/Key_Cards',
        'vehicle_parts': 'Equipment/Vehicle_Parts',
        
        # Clothing categories
        'clothing': 'Clothing',
        'tops': 'Clothing/Tops',
        'bottoms': 'Clothing/Bottoms', 
        'shoes': 'Clothing/Shoes',
        'gloves': 'Clothing/Gloves',
        'bags': 'Clothing/Bags',
        
        # Food and medical categories
        'food': 'Food',
        'canned_food': 'Food/Canned',
        'fresh_food': 'Food/Fresh',
        'drinks': 'Food/Drinks',
        'cooking': 'Food/Cooking',
        'seeds': 'Food/Seeds',
        'medical_items': 'Medical',
    }
    
    # Try direct mapping first (most reliable)
    if category_lower in category_mappings:
        return category_mappings[category_lower]
    
    # Fallback logic for unknown categories
    # This catches edge cases where new categories might be added to the wiki
    if any(word in category_lower for word in ['weapon', 'gun', 'rifle', 'pistol']):
        return 'Weapons'
    elif any(word in category_lower for word in ['clothing', 'apparel', 'wear']):
        return 'Clothing' 
    elif any(word in category_lower for word in ['food', 'eat', 'drink', 'consumable']):
        return 'Food'
    elif any(word in category_lower for word in ['medical', 'health', 'medicine']):
        return 'Medical'
    else:
        return 'Equipment/Misc'


# =============================================================================
# WEB SCRAPING FUNCTIONS
# =============================================================================

def extract_item_links_from_category(url: str) -> List[Tuple[str, str, str]]:
    """
    Extracts all item links from a wiki category page.
    
    This function implements a multi-strategy approach to find item links:
    1. Look for category member lists (primary method)
    2. Search in lists and tables (backup method)
    3. Scan entire page (fallback method)
    
    Args:
        url: The wiki category URL to scrape
        
    Returns:
        List of tuples: (item_url, item_name, target_category)
        
    Design decisions:
    - Multiple strategies ensure we don't miss items due to HTML structure variations
    - Extensive filtering prevents non-item pages from being included
    - Category mapping happens here to maintain consistency
    """
    print(f"🔎 Analyzing category: {url}")
    
    # Extract category name from URL and determine target folder
    category_name = url.split('/')[-1].replace('Category:', '')
    target_category = map_wiki_category_to_folder(category_name)
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        item_links = set()
        
        # STRATEGY 1: Look for category member lists (most reliable)
        # Wiki category pages typically have dedicated sections for members
        category_members = soup.find('div', {'id': 'mw-pages'})
        if not category_members:
            category_members = soup.find('div', {'class': 'mw-category'})
        if not category_members:
            category_members = soup.find('div', {'class': 'category-page__members'})
        
        # STRATEGY 2: Search in lists and tables (backup)
        # Some categories might use different HTML structures
        additional_containers = soup.find_all(['ul', 'ol', 'table', 'div'], 
                                            class_=lambda x: x and ('mw-' in x or 'category' in x.lower()))
        
        # Combine all potential containers
        all_containers = []
        if category_members:
            all_containers.append(category_members)
        all_containers.extend(additional_containers)
        
        # STRATEGY 3: Fallback - search entire page if no specific containers found
        if not all_containers:
            all_containers = [soup]
        
        # Extract links from all identified containers
        for container in all_containers:
            links = container.find_all('a', href=True)
            
            for link in links:
                href = link['href']
                
                # Filter 1: Only internal wiki article links
                if not href.startswith('/wiki/'):
                    continue
                
                # Filter 2: Exclude special namespaces and meta pages
                # These are wiki maintenance pages, not game items
                if any(ignore in href.lower() for ignore in [
                    'category:', 'file:', 'image:', 'template:', 'help:', 'user:',
                    'talk:', 'special:', 'media:', '#', 'edit', 'history', 'action=',
                    'list_of', 'changelog', 'unused', 'legacy', 'cut_content',
                    'removed', 'obsolete', 'deprecated', 'beta', 'alpha'
                ]):
                    continue
                
                # Filter 3: Exclude meta pages by page name
                page_name = href.split('/')[-1].lower()
                if any(meta in page_name for meta in [
                    'main_page', 'community', 'admin', 'policy', 'rules',
                    'guidelines', 'portal', 'project', 'server', 'update',
                    'patch', 'version', 'changelog', 'news', 'disambiguation'
                ]):
                    continue
                    
                link_text = link.get_text().strip()
                
                # Filter 4: Reasonable text length (avoid empty or overly long links)
                if len(link_text) < 1 or len(link_text) > 60:
                    continue
                    
                # Filter 5: Exclude obvious non-items by link text
                if any(ignore in link_text.lower() for ignore in [
                    'list of', 'category', 'template', 'unused', 'legacy',
                    'removed', 'cut', 'beta', 'alpha', 'dev', 'developer',
                    'disambiguation', 'redirect'
                ]):
                    continue
                
                # Filter 6: Exclude navigation and meta content
                exclusion_patterns = [
                    'main page', 'home', 'index', 'portal',
                    'edit', 'talk', 'discussion', 'history',
                    'list of', 'category of', 'overview of',
                    'development', 'roadmap', 'changelog'
                ]
                
                exclude_this_link = any(pattern in link_text.lower() for pattern in exclusion_patterns)
                
                if not exclude_this_link:
                    full_url = BASE_URL + href
                    # Store item with its determined category
                    item_links.add((full_url, link_text, target_category))
                    print(f"   🔗 Found item: {link_text} -> {target_category}")
        
        print(f"   📊 Found {len(item_links)} items in this category")
        return list(item_links)
        
    except Exception as e:
        print(f"   ❌ Error loading {url}: {e}")
        return []


def extract_item_images_from_page(url: str, item_name: str) -> List[Tuple[str, str]]:
    """
    Extracts item images from an individual item's wiki page.
    
    This function implements a sophisticated image detection strategy:
    1. Find the main item icon (usually the first large image)
    2. Look for gallery images (additional variants)
    3. Search for images with item name in filename (fallback)
    
    Args:
        url: The item's wiki page URL
        item_name: Name of the item
        
    Returns:
        List of tuples: (image_url, variant_name)
        
    Key design decisions:
    - Multiple strategies ensure we find images regardless of page structure
    - Extensive filtering removes UI elements, logos, and irrelevant images
    - Limits results to avoid downloading too many variants per item
    - Prioritizes main item icon over secondary images
    """
    print(f"🎯 Loading item page: {item_name}")
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        images = []
        found_main_image = False
        
        # STRATEGY 1: Find the main item image (highest priority)
        # The first large image in the main content is typically the item icon
        main_content = soup.find('div', {'class': ['mw-parser-output', 'WikiaArticle']})
        if main_content:
            first_img = main_content.find('img')
            if first_img and first_img.get('src'):
                src = first_img.get('src')
                
                # Validate image source
                if ("static.wikia.nocookie.net" in src and 
                    any(ext in src.lower() for ext in ['.png', '.jpg', '.jpeg']) and
                    not any(ignore in src.lower() for ignore in ['logo', 'banner', 'nav', 'header'])):
                    
                    # Ensure full URL
                    if not src.startswith('http'):
                        src = "https:" + src if src.startswith('//') else BASE_URL + src
                    
                    # Use highest quality version
                    if "/revision/" not in src:
                        src = src + "/revision/latest"
                    
                    # Extract clean filename
                    filename = src.split('/')[-1].split('.')[0].split('?')[0]
                    variant_name = filename.replace('_', ' ').replace('%20', ' ')
                    
                    images.append((src, variant_name))
                    found_main_image = True
                    print(f"   📷 Found main icon: {variant_name}")
        
        # STRATEGY 2: Search gallery section for additional variants
        # Many item pages have gallery sections with different color variants
        gallery_section = soup.find('span', {'id': 'Gallery'})
        if gallery_section:
            gallery_parent = gallery_section.parent
            # Find all images in the gallery section
            gallery_imgs = gallery_parent.find_next_siblings()
            for section in gallery_imgs:
                # Stop at next major section
                if section.name in ['h2', 'h3'] and section != gallery_parent:
                    break
                
                # Extract images from this section
                for img in section.find_all('img') if hasattr(section, 'find_all') else []:
                    src = img.get('src', '')
                    if ("static.wikia.nocookie.net" in src and 
                        any(ext in src.lower() for ext in ['.png', '.jpg', '.jpeg']) and
                        not any(ignore in src.lower() for ignore in ['logo', 'banner', 'nav', 'header', 'fandom'])):
                        
                        # Ensure full URL
                        if not src.startswith('http'):
                            src = "https:" + src if src.startswith('//') else BASE_URL + src
                        
                        # Use highest quality
                        if "/revision/" not in src:
                            src = src + "/revision/latest"
                        
                        filename = src.split('/')[-1].split('.')[0].split('?')[0]
                        variant_name = filename.replace('_', ' ').replace('%20', ' ')
                        
                        # Avoid duplicates
                        if not any(existing_src == src for existing_src, _ in images):
                            images.append((src, variant_name))
                            print(f"   📷 Found gallery image: {variant_name}")
        
        # STRATEGY 3: Filename-based search (fallback for pages without clear main image)
        # Look for images where filename contains words from the item name
        if not found_main_image:
            item_words = [word.lower() for word in item_name.lower().replace('-', ' ').split() if len(word) > 2]
            
            all_imgs = soup.find_all('img')
            for img in all_imgs[:10]:  # Limit to first 10 images for performance
                src = img.get('src', '')
                if not src or "static.wikia.nocookie.net" not in src:
                    continue
                
                if not any(ext in src.lower() for ext in ['.png', '.jpg', '.jpeg']):
                    continue
                
                # Filter out UI elements and logos
                if any(ignore in src.lower() for ignore in [
                    'logo', 'banner', 'nav', 'header', 'footer', 'fandom',
                    'discord', 'reddit', 'steam', 'cursor', 'edit', 'view'
                ]):
                    continue
                
                # Filter out small UI images
                if any(size in src for size in ['/16px-', '/20px-', '/24px-', '/32px-', '/40px-']):
                    continue
                
                filename = src.split('/')[-1].split('.')[0].split('?')[0].lower()
                
                # Check if filename contains item-relevant words
                name_matches = 0
                for word in item_words:
                    if word in filename:
                        name_matches += 1
                
                if name_matches > 0:  # At least one word must match
                    if not src.startswith('http'):
                        src = "https:" + src if src.startswith('//') else BASE_URL + src
                    
                    if "/revision/" not in src:
                        src = src + "/revision/latest"
                    
                    variant_name = filename.replace('_', ' ').replace('%20', ' ')
                    
                    # Avoid duplicates
                    if not any(existing_src == src for existing_src, _ in images):
                        images.append((src, variant_name))
                        print(f"   📷 Found filename match: {variant_name}")
        
        # Limit to maximum 3 images per item to avoid clutter
        images = images[:3]
        
        print(f"   🖼️  Extracted {len(images)} relevant images")
        return images
        
    except Exception as e:
        print(f"   ❌ Error loading item page {url}: {e}")
        return []


# =============================================================================
# FILE SYSTEM UTILITIES
# =============================================================================

def create_category_folder(base_dir: str, category: str) -> str:
    """
    Creates folder structure for item categories.
    
    Args:
        base_dir: Base directory for all downloads
        category: Category path (e.g., 'Weapons/Assault_Rifles')
        
    Returns:
        Full path to the created folder
    """
    folder_path = os.path.join(base_dir, category)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path


def clean_filename(filename: str) -> str:
    """
    Cleans filenames to be filesystem-safe.
    
    This function handles common filename issues:
    - Removes or replaces invalid characters
    - Normalizes whitespace and underscores
    - Ensures proper file extension
    
    Args:
        filename: Original filename
        
    Returns:
        Cleaned, filesystem-safe filename
    """
    # Remove/replace invalid characters
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    # Normalize multiple underscores and spaces
    filename = re.sub(r'[_\s]+', '_', filename)
    filename = filename.strip('_')
    
    # Ensure file extension
    if '.' not in filename:
        filename += '.png'
    
    return filename


# =============================================================================
# DOWNLOAD FUNCTIONS
# =============================================================================

def download_image(url: str, item_name: str, image_variant: str, category: str, base_folder: str) -> bool:
    """
    Downloads a single image and saves it to the appropriate category folder.
    
    This function handles:
    - Creating proper folder structure
    - Generating descriptive filenames
    - Avoiding duplicate downloads
    - Handling download errors gracefully
    
    Args:
        url: Image URL to download
        item_name: Name of the item
        image_variant: Variant description (e.g., 'Green', 'With_Attachments')
        category: Target category folder
        base_folder: Base download directory
        
    Returns:
        True if download succeeded, False otherwise
    """
    try:
        # Create category folder structure
        category_folder = create_category_folder(base_folder, category)
        
        # Generate descriptive filename
        if image_variant and image_variant.lower() != item_name.lower():
            filename = clean_filename(f"{item_name}_{image_variant}")
        else:
            filename = clean_filename(f"{item_name}")
        
        # Ensure correct file extension
        if not any(filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
            # Extract extension from URL
            url_ext = url.split('.')[-1].split('?')[0].split('/')[0]
            if url_ext.lower() in ['png', 'jpg', 'jpeg']:
                filename = filename.rsplit('.', 1)[0] + '.' + url_ext
            else:
                filename = filename.rsplit('.', 1)[0] + '.png'
        
        # Check if file already exists (avoid re-downloading)
        file_path = os.path.join(category_folder, filename)
        if os.path.exists(file_path):
            print(f"   ⏭️  Skipped (already exists): {category}/{filename}")
            return True
        
        # Download image
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        
        # Save to file
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
        print(f"   ✅ Saved: {category}/{filename}")
        return True
        
    except Exception as e:
        print(f"   ❌ Download error for {url}: {e}")
        return False


# =============================================================================
# CATEGORY DISCOVERY
# =============================================================================

def discover_additional_categories() -> List[str]:
    """
    Automatically discovers additional item categories from the wiki.
    
    This function searches the main Items category page for subcategories
    that might not be in our predefined list. This ensures we don't miss
    any item types if the wiki structure changes.
    
    Returns:
        List of additional category URLs found
    """
    print("🕵️ Searching for additional item categories...")
    
    additional_categories = []
    base_category_url = "https://dayz.fandom.com/wiki/Category:Items"
    
    try:
        response = requests.get(base_category_url, headers=HEADERS)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Search for subcategories
            subcategories = soup.find_all('a', href=True)
            for link in subcategories:
                href = link['href']
                if '/wiki/Category:' in href and 'item' in href.lower():
                    full_url = BASE_URL + href if not href.startswith('http') else href
                    if full_url not in MAIN_CATEGORIES:
                        additional_categories.append(full_url)
                        print(f"   📂 Additional category found: {href}")
    
    except Exception as e:
        print(f"   ⚠️ Error searching for additional categories: {e}")
    
    print(f"   ➕ Discovered {len(additional_categories)} additional categories")
    return additional_categories


# =============================================================================
# MAIN EXECUTION FUNCTION
# =============================================================================

def main():
    """
    Main execution function that orchestrates the entire scraping process.
    
    The scraping process consists of three phases:
    1. PHASE 1: Discover and collect all item links from category pages
    2. PHASE 2: Visit each item page and extract image URLs
    3. PHASE 3: Download all discovered images
    
    This phased approach allows for better error handling and progress tracking.
    """
    print("🚀 Starting COMPLETE DayZ Item Icon Scraper...")
    print(f"📁 Saving all images to: {OUTPUT_DIR}/")
    
    # Expand category list automatically to catch any new categories
    all_categories = MAIN_CATEGORIES.copy()
    additional_cats = discover_additional_categories()
    all_categories.extend(additional_cats)
    
    print(f"\n📋 Searching {len(all_categories)} categories for items...")
    
    all_item_links = []
    
    # =============================================================================
    # PHASE 1: COLLECT ITEM LINKS FROM ALL CATEGORY PAGES
    # =============================================================================
    
    print("\n🔍 PHASE 1: Collecting item links from ALL category pages...")
    for i, category_url in enumerate(all_categories, 1):
        print(f"\n[{i}/{len(all_categories)}] Category: {category_url.split('/')[-1]}")
        item_links = extract_item_links_from_category(category_url)
        all_item_links.extend(item_links)
        time.sleep(0.8)  # Respectful delay between requests
    
    # Remove duplicates while preserving category information
    # Some items might appear in multiple categories - we keep the first occurrence
    unique_items = {}
    for item_url, item_name, category in all_item_links:
        key = (item_url, item_name)
        if key not in unique_items:
            unique_items[key] = category
    
    unique_item_links = [(url, name, cat) for (url, name), cat in unique_items.items()]
    print(f"\n📊 Found {len(unique_item_links)} unique item links total")
    print(f"📊 Removed {len(all_item_links) - len(unique_item_links)} duplicates")
    
    all_images = []
    
    # =============================================================================
    # PHASE 2: EXTRACT IMAGES FROM ALL ITEM PAGES
    # =============================================================================
    
    print("\n🎯 PHASE 2: Extracting images from ALL item pages...")
    total_items = len(unique_item_links)
    successful_extractions = 0
    
    for i, (item_url, item_name, wiki_category) in enumerate(unique_item_links, 1):
        print(f"\n[{i}/{total_items}] Item: {item_name} -> {wiki_category}")
        images = extract_item_images_from_page(item_url, item_name)
        
        if images:
            successful_extractions += 1
            
        for image_url, image_name in images:
            # Use wiki-determined category instead of name-based guessing
            all_images.append((image_url, item_name, image_name, wiki_category))
        
        # Respectful delay between page requests
        time.sleep(0.3)
        
        # Progress updates every 50 items
        if i % 50 == 0:
            print(f"   📈 Progress: {i}/{total_items} items processed, {len(all_images)} images collected")
    
    print(f"\n📦 Collected {len(all_images)} images from {successful_extractions}/{total_items} items")
    print(f"📈 Success rate: {(successful_extractions/total_items)*100:.1f}%")
    
    # Display statistics by category
    category_counts = {}
    for _, _, _, category in all_images:
        category_counts[category] = category_counts.get(category, 0) + 1
    
    print("\n📊 Images by category:")
    for category, count in sorted(category_counts.items()):
        print(f"   {category}: {count} images")
    
    # =============================================================================
    # PHASE 3: DOWNLOAD ALL DISCOVERED IMAGES
    # =============================================================================
    
    print(f"\n📥 PHASE 3: Starting download of all {len(all_images)} images...")
    successful_downloads = 0
    total_images = len(all_images)
    
    for i, (image_url, item_name, image_variant, category) in enumerate(all_images, 1):
        print(f"⬇️  [{i}/{total_images}] Downloading: {item_name} - {image_variant}")
        
        if download_image(image_url, item_name, image_variant, category, OUTPUT_DIR):
            successful_downloads += 1
        
        # Short delay between downloads to be respectful
        time.sleep(0.1)
        
        # Progress updates every 100 downloads
        if i % 100 == 0:
            print(f"   📈 Download progress: {i}/{total_images} ({(i/total_images)*100:.1f}%)")
    
    # =============================================================================
    # FINAL SUMMARY
    # =============================================================================
    
    print(f"\n🎉 COMPLETED! DayZ Item Scraper finished successfully!")
    print(f"✅ {successful_downloads}/{total_images} images downloaded successfully")
    print(f"📈 Download success rate: {(successful_downloads/total_images)*100:.1f}%")
    print(f"📁 All files saved to: '{OUTPUT_DIR}/'")
    print(f"📋 {len(all_categories)} categories searched")
    print(f"🔗 {len(unique_item_links)} unique items found")


if __name__ == "__main__":
    main()
