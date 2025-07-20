# Contributing to DayZ Item Scraper

First off, thank you for considering contributing to DayZ Item Scraper! 

It's people like you that make this tool useful for the entire DayZ community.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Community](#community)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

### Our Standards

- **Be respectful** and inclusive
- **Be collaborative** and helpful
- **Be patient** with newcomers
- **Focus on what's best** for the community
- **Show empathy** towards other community members

## Getting Started

### Prerequisites

- Python 3.7+
- Git
- Basic understanding of web scraping concepts
- Familiarity with the DayZ game (helpful but not required)

### Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/dayz-item-scraper.git
   cd dayz-item-scraper
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates.

**When filing a bug report, include:**
- Clear, descriptive title
- Steps to reproduce the issue
- Expected vs actual behavior
- Your environment (OS, Python version)
- Screenshots (if applicable)
- Console output/error messages

### 💡 Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:
- Clear description of the enhancement
- Why this enhancement would be useful
- Any implementation ideas you might have

### 🔧 Code Contributions

#### Areas Where Help Is Needed

1. **Image Quality Improvements**
   - Better image resolution detection
   - Advanced duplicate detection
   - Image format optimization

2. **Performance Optimizations**
   - Concurrent downloads
   - Memory usage optimization
   - Faster category discovery

3. **Error Handling**
   - Better retry mechanisms
   - Network timeout handling
   - Graceful degradation

4. **New Features**
   - GUI interface
   - Configuration file support
   - Progress resumption
   - Other game wiki support

5. **Documentation**
   - Code comments
   - Usage examples
   - Troubleshooting guides

#### Getting Started with Code

1. Look for issues labeled `good first issue` or `help wanted`
2. Comment on the issue to let others know you're working on it
3. Fork the repository and create a feature branch
4. Make your changes with clear, commented code
5. Test your changes thoroughly
6. Submit a pull request

## 🛠️ Development Setup

### Running Tests

```bash
# Run the scraper in test mode (limit to 5 items)
python dayz_item_scraper.py --test

# Check code style
flake8 dayz_item_scraper.py

# Type checking (if using mypy)
mypy dayz_item_scraper.py
```

### Debug Mode

Enable debug logging for development:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📝 Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new functionality
3. **Follow the coding style** guidelines
4. **Update README.md** if you've added features
5. **Write a clear commit message**
6. **Create the pull request**

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tested locally
- [ ] Added tests for new functionality
- [ ] All existing tests pass

## Screenshots (if applicable)

## Additional Notes
```

## 🎨 Style Guidelines

### Python Code Style

- Follow **PEP 8** standards
- Use **type hints** where appropriate
- Write **clear, descriptive comments**
- Use **meaningful variable names**
- Keep functions **focused and small**

### Documentation Style

- Use **clear, concise language**
- Include **code examples** where helpful
- Keep **README.md updated**
- Comment **complex logic thoroughly**

### Commit Message Format

```
type(scope): brief description

Longer description if needed

Fixes #issue_number
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(scraper): add support for custom categories
fix(download): handle timeout errors gracefully
docs(readme): update installation instructions
```

## 🏗️ Project Structure

```
dayz-item-scraper/
├── dayz_item_scraper.py    # Main scraper script
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── CONTRIBUTING.md        # This file
├── LICENSE               # MIT license
├── .gitignore           # Git ignore rules
└── examples/            # Usage examples (future)
```

## 🧪 Testing Guidelines

### Manual Testing

1. **Test with different categories**
2. **Verify folder structure creation**
3. **Check image quality and naming**
4. **Test error handling** (disconnect internet, etc.)
5. **Verify duplicate detection**

### Automated Testing (Future)

We're working on adding automated tests. Areas that need testing:
- Category mapping functions
- Image URL extraction
- File naming and cleaning
- Error handling scenarios

## 📚 Learning Resources

New to web scraping or Python? Here are some helpful resources:

- [Python Requests Documentation](https://docs.python-requests.org/)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Web Scraping Ethics](https://blog.apify.com/web-scraping-ethics/)
- [Git Basics](https://git-scm.com/doc)

## 💬 Community

### Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For general questions and ideas
- **Discord**: Join our community server (link coming soon)

### Communication Guidelines

- Be respectful and professional
- Search existing issues before creating new ones
- Provide context and details in your communications
- Help others when you can

## 🎯 Roadmap

### Short Term Goals
- [ ] Add comprehensive test suite
- [ ] Improve error handling
- [ ] Add configuration file support
- [ ] Performance optimizations

### Long Term Goals
- [ ] GUI interface
- [ ] Support for other game wikis
- [ ] Docker containerization
- [ ] Multi-language support

## 🏆 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- GitHub contributors page

## ❓ Questions?

Don't hesitate to ask questions! You can:
- Open a GitHub issue
- Start a discussion
- Comment on existing issues

Remember, there are no stupid questions - we're all here to learn and improve together!

---

**Thank you for contributing to DayZ Item Scraper!** 🙏
