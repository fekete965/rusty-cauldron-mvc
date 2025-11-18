# 🍲 Rusty Cauldron

> A magical recipe sharing platform inspired by the wizarding world

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A multi-page web application built with Django that allows users to discover, share, and manage recipes. Perfect for food enthusiasts who want to explore culinary magic!

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Running the Application](#-running-the-application)
- [Usage](#-usage)
- [Development](#-development)
- [Project Status](#-project-status)

## ✨ Features

- 🔍 **Recipe Search** - Search recipes by title and ingredients
- 👤 **User Authentication** - Secure signup and login system
- 📝 **Recipe Management** - Create, read, update, and delete your recipes
- 🏷️ **Ingredient Tracking** - Detailed ingredient lists with measurements
- 📄 **Pagination** - Efficient browsing of recipe collections
- 🎨 **Modern UI** - Clean, responsive design with Tailwind CSS

## 🛠️ Tech Stack

### Core Framework
- **Django 4.2+** - High-level Python web framework
- **Python 3.10+** - Programming language

### Key Libraries
- **python-dateutil** - Advanced date/time parsing
- **StrEnum** - String enumeration support
- **SQLite** - Lightweight database

### Development Tools
- **Ruff** - Fast Python linter and formatter
- **Black** - Code formatter (via Ruff)

### Frontend
- **Tailwind CSS** - Utility-first CSS framework
- **Django Templates** - Server-side rendering

## 📁 Project Structure

```
rusty-cauldron-mvc/
├── source/                      # Main project directory
│   ├── app/                     # Django application configuration
│   │   ├── conf/                # Environment-specific settings
│   │   │   ├── development/     # Development settings
│   │   │   └── production/      # Production settings
│   │   ├── urls.py              # URL routing configuration
│   │   └── wsgi.py              # WSGI application entry point
│   ├── main/                    # Main Django app
│   │   ├── views.py             # View classes (controllers)
│   │   ├── context_processors.py # Template context processors
│   │   └── templatetags/        # Custom template tags and filters
│   ├── tables/                  # Django models (database schema)
│   │   ├── users.py             # User model
│   │   ├── recipes.py           # Recipe model
│   │   └── ingredients.py      # Ingredient model
│   ├── content/                # Static files and templates
│   │   ├── static/              # CSS, JavaScript, images
│   │   └── templates/           # HTML templates
│   ├── migrations/              # SQL migration files
│   ├── utils/                   # Utility functions
│   ├── constants.py             # Application constants
│   ├── recipe_service.py        # Recipe business logic
│   ├── user_service.py          # User business logic
│   ├── manage.py                # Django management script
│   └── rusty-cauldron.db        # SQLite database (generated)
└── README.md                    # This file
```

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package installer (usually comes with Python)
- **Git** - Version control system (optional)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd rusty-cauldron-mvc
```

### 2. Navigate to Source Directory

```bash
cd source
```

### 3. Create Virtual Environment (Recommended)

**Linux/macOS:**
```bash
python3 -m venv ../rusty-couldron-env
source ../rusty-couldron-env/bin/activate
```

**Windows:**
```bash
python -m venv ..\rusty-couldron-env
..\rusty-couldron-env\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install django python-dateutil strenum
```

## ⚙️ Configuration

### 1. Generate Secret Key

Generate a secure secret key for your application:

```bash
python -c 'import secrets; print(secrets.token_hex())'
```

**Save this key securely!** You'll need it in the next step.

### 2. Set Environment Variable

Set the `RUSTY_CAULDRON_KEY` environment variable with your generated secret.

#### Linux/macOS

Add to your shell configuration file (`~/.bashrc`, `~/.zshrc`, or `~/.profile`):

```bash
export RUSTY_CAULDRON_KEY="your_generated_secret_key_here"
```

Then reload your shell:
```bash
source ~/.zshrc  # or ~/.bashrc
```

#### Windows

**PowerShell:**
```powershell
$env:RUSTY_CAULDRON_KEY="your_generated_secret_key_here"
```

**Command Prompt:**
```cmd
set RUSTY_CAULDRON_KEY=your_generated_secret_key_here
```

**Permanent (Windows):**
1. Open System Properties → Environment Variables
2. Add new User Variable: `RUSTY_CAULDRON_KEY` = `your_generated_secret_key_here`

### 3. Database Setup

Create and apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

This will create the SQLite database file (`rusty-cauldron.db`) with all necessary tables.

## ▶️ Running the Application

### Development Mode

1. **Navigate to source directory:**
   ```bash
   cd source
   ```

2. **Activate virtual environment** (if using one):
   ```bash
   source ../rusty-couldron-env/bin/activate  # Linux/macOS
   # or
   ..\rusty-couldron-env\Scripts\activate     # Windows
   ```

3. **Ensure environment variable is set:**
   ```bash
   echo $RUSTY_CAULDRON_KEY  # Linux/macOS
   # or
   echo %RUSTY_CAULDRON_KEY% # Windows
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver 8080
   ```

5. **Open your browser:**
   Navigate to [http://localhost:8080](http://localhost:8080)

### Production Mode

Set the `IS_PRODUCTION` environment variable:

```bash
export IS_PRODUCTION=1  # Linux/macOS
# or
$env:IS_PRODUCTION="1"  # Windows PowerShell

python manage.py runserver 8080
```

> **Note:** For production deployments, use a proper WSGI server like Gunicorn or uWSGI instead of Django's development server.

## 📖 Usage

### Creating an Account

1. Click **"Sign up"** in the navigation bar
2. Fill in your first name, last name, email, and password
3. Password requirements:
   - Minimum 8 characters
   - At least one uppercase letter
   - At least one number
   - At least one special character
4. Click **"Sign up"** to create your account

### Logging In

Use the test accounts provided below, or use your newly created account.

### Adding a Recipe

1. Log in to your account
2. Click **"Add Recipe"** in the navigation bar
3. Fill in the recipe details:
   - Title (required)
   - Preparation time (optional, in minutes)
   - Cooking time (required, in minutes)
   - Ingredients with amounts and measurements
   - Description (required)
4. Click **"Add Recipe"** to save

### Searching Recipes

1. Navigate to **"Recipes"** page
2. Use the search form to filter by:
   - Recipe title
   - Ingredients (comma-separated)
   - Page size (10, 15, or 20 recipes per page)
3. Click **"Search"** to apply filters

### Managing Your Recipes

1. Click **"My Recipes"** to view all your recipes
2. Click on any recipe to view details
3. Edit or delete recipes you own

## 🧪 Test Accounts

The following test accounts are available for demonstration:

| Email                                | Password       | Has Recipes |
| ------------------------------------ | -------------- | ----------- |
| harry-potter@owl-postal.co.uk        | `Password123!` | ✅ Yes       |
| hermione-granger@owl-postal.co.uk   | `Password123!` | ✅ Yes       |
| albus-dumbledore@owl-postal.co.uk  | `Password123!` | ✅ Yes       |
| draco-malfoy@owl-postal.co.uk       | `Password123!` | ✅ Yes       |
| tom-riddle@owl-postal.co.uk         | `Password123!` | ✅ Yes       |
| ron-weasley@owl-postal.co.uk        | `Password123!` | ❌ No        |

> **⚠️ Important:** These are test accounts. In a production environment, change all default passwords!

## 🔧 Development

### Code Formatting and Linting

This project uses **Ruff** for linting and formatting. All code follows PEP 8 style guidelines.

#### Install Linting Tools

```bash
pip install ruff black
```

#### Format Code

```bash
# Format all Python files
cd source
ruff format .

# Or use the Makefile
make format
```

#### Lint Code

```bash
# Lint and auto-fix issues
cd source
ruff check --fix .

# Or use the Makefile
make lint
```

#### Run All Checks

```bash
# Format and lint in one command
make check
```

### Running Migrations

After making model changes:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating a Superuser

Access Django admin panel:

```bash
python manage.py createsuperuser
```

Then visit [http://localhost:8080/admin](http://localhost:8080/admin)

### Database Reset

To reset the database:

```bash
rm rusty-cauldron.db          # Delete database file
python manage.py migrate       # Recreate database
```

### Code Style

The project follows Django best practices and PEP 8 style guidelines. Configuration files:

- `pyproject.toml` - Ruff and Black configuration
- `.ruffignore` - Files to exclude from linting
- `.editorconfig` - Editor configuration for consistent formatting
- `Makefile` - Convenient commands for common tasks

## 📝 Project Status

This project was originally built as a **CS50 final project** and has been migrated from Flask to Django for improved structure and maintainability.

### Current Status
- ✅ User authentication
- ✅ Recipe CRUD operations
- ✅ Recipe search and filtering
- ✅ Pagination
- ✅ Responsive UI

### Future Enhancements
- [ ] Recipe ratings and reviews
- [ ] Recipe categories/tags
- [ ] Image uploads for recipes
- [ ] Social features (sharing, following)
- [ ] Recipe export (PDF, print)
- [ ] API endpoints for mobile apps

## ⚠️ Important Notes

### AI-Generated Content

**⚠️ WARNING:** The recipes in this application were generated by AI. **DO NOT attempt to cook these recipes** as the ingredients and methods may be incorrect or unsafe.

### Security

- Always use strong, unique passwords
- Never commit secret keys to version control
- Use environment variables for sensitive configuration
- Keep dependencies up to date

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Python Documentation](https://docs.python.org/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Bence Fekete**

- CS50 Final Project
- Video Demo: [Watch on Loom](https://www.loom.com/share/2bc603e03dc04ace857fb567ed81daac)

---

**Made with ❤️ and a touch of magic** ✨
