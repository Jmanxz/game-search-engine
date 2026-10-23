# game-search-engine

## Issues
1. Had to swap interpreter to get dotenv to work correctly 
2. need to include ?q= after path for params (Kept trying to use ?Q=)

## To-Do
1. Add GUI via web app
2. finish recommendation engine 
3. clean up files
4. add css to web app

## Setup


### Requirements
- Python 3.12 or newer
- A RAWG API key from [RAWG](https://rawg.io/apidocs)
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Jmanxz/game-search-engine.git
   cd game-search-engine
   ```

2. Create and activate a virtual environment:

   **Windows (PowerShell):**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **Linux/macOS:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your RAWG API key:

   ```dotenv
   RAWG_API_KEY=your_api_key_here
   ```

   Replace `your_api_key_here` with your actual API key. Do not commit the `.env` file to GitHub.

### Running the Application

Start the FastAPI server from the project root:

```bash
python -m uvicorn app.main:app --reload
```

Open the interactive API documentation in your browser:

http://127.0.0.1:8000/docs

### Testing Game Search

Use the `GET /games/search` endpoint and enter a search term in the required `q` parameter. For example, search for `Elden Ring` to retrieve matching games from RAWG.

