Final work for Beetroot Python course

# Django Blog App
A blog project built with Django.
UI templates were provided; the main focus was on implementing backend logic, working with models, authentication, and media handling.

## Technologies
- Python 3.13+
- Django 5.2+
- PostgreSQL (via psycopg)
- Pillow (image processing)
- python-dotenv (environment variable management)
- bandit (security static analysis)
- pre-commit (git hooks for code quality)
- ruff (Python linter, dev dependency)

## Features
- User registration and authentication
- Custom user model (`AUTH_USER_MODEL`)
- User profile with avatar upload
- Blog post management via Django admin
- Post categories and tags
- Comment system
- Image gallery for posts
- Context processors for recent posts and navigation menu
- Avatar upload via frontend; post images managed through Django admin
- Automatic unique slug generation for posts (with trimming and transliteration)

## Project Structure
- `users` – user accounts, registration, profile
- `blog` – posts, categories, comments, images
- `templates/`, `media/`, `static/` – layout, uploads, static files

## Status
Core functionality is implemented and working (MVP).
Further development is in progress to enhance features, fix known issues, and expand capabilities.
