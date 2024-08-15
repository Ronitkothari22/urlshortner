# urlshortner
# URL Shortener API

## Project Overview

This project implements a basic URL shortener API using FastAPI and PostgreSQL. It allows users to submit long URLs and receive shortened versions, as well as use the shortened URLs to redirect to the original long URLs.

## Features

- Shorten long URLs to unique short codes
- Redirect from short codes to original URLs
- FastAPI for efficient API handling
- PostgreSQL database for persistent storage

## Technologies Used

- Python 3.7+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic



## API Usage

### Shorten a URL

- **Endpoint**: [POST /shorten](http://127.0.0.1:8000/shorten)
- **Request Body**:
```json
{
 "url": "https://example.com/very/long/url"
}

{
  "short_url":(http://127.0.0.1:8000/SMHJX)
}
