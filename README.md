# Cryptocurrency Portfolio Tracker

A Django-based web application that tracks cryptocurrency prices using data from the CoinGecko API. The application stores cryptocurrency data in the database and exposes REST API endpoints to fetch and retrieve the data. JWT authentication is used to secure the APIs.

## Features

- Fetch cryptocurrency data from the CoinGecko API.
- Store cryptocurrency data (name, symbol, price, market cap, etc.) in a database.
- Provide a REST API to expose cryptocurrency data.
- Secure the APIs using JWT (JSON Web Token) authentication.

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript (Bootstrap for styling)
- **Authentication**: JWT (via Django REST Framework SimpleJWT)
- **Database**: SQLite 

## API Endpoints

1. **Fetch and Store Cryptocurrency Data**:
   - **Endpoint**: `/api/fetch/`
   - **Method**: `GET`
   - **Description**: Fetches the latest cryptocurrency data from the CoinGecko API and stores it in the database.
   - **Authentication**: Requires JWT authentication.
   
2. **List Stored Cryptocurrency Data**:
   - **Endpoint**: `/api/cryptocurrencies/`
   - **Method**: `GET`
   - **Description**: Retrieves all stored cryptocurrency data from the database in JSON format.
   - **Authentication**: Requires JWT authentication.

3. **Get JWT Access and Refresh Tokens**:
   - **Endpoint**: `/api/token/`
   - **Method**: `POST`
   - **Description**: Obtain access and refresh tokens for authentication.
   
4. **Refresh JWT Access Token**:
   - **Endpoint**: `/api/token/refresh/`
   - **Method**: `POST`
   - **Description**: Obtain a new access token using the refresh token.

## Installation

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- Django REST Framework SimpleJWT

### Clone the Repository

```bash
git clone https://github.com/yourusername/Crypto-Portfolio-Tracker.git
cd Crypto-Portfolio-Tracker
