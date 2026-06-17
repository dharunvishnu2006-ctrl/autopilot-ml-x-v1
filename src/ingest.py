import asyncio, pandas as pd

async def load_one(path: str):
    """Load ONE file into a DataFrame based on its extension."""
    try:
        if path.endswith(".csv"):
            df = pd.read_csv(path)
        elif path.endswith(".json"):
            df = pd.read_json(path)
        elif path.endswith(".xlsx"):
            df = pd.read_excel(path)
        else:
            print(f"Unsupported file type: {path}")
            return None
        return df
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return None


async def ingest_all(paths: list) -> list:
    """Load MANY files concurrently and return all DataFrames."""
    return await asyncio.gather(*(load_one(p) for p in paths))