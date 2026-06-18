import os
import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Loads a CSV dataset from a given path, prints its dimensions,

    and returns it. Handles bad paths and format errors.
    """
    try:
        if not isinstance(path, str) or not path:
            print("Error: invalid path argument")
            return None
        if not os.path.exists(path):
            raise FileNotFoundError
        if os.path.isdir(path):
            raise IsADirectoryError(f"Error: {path} is not a file")
        if not path.lower().endswith(".csv"):
            print("Error: file must be an .csv file")
            return None
        df = pd.read_csv(path)
        if df.empty:
            raise pd.errors.EmptyDataError
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except PermissionError:
        print(f"Error: Permission denied to access {path}.")
        return None
    except pd.errors.ParserError:
        print(
            f"Error: The file {path} has an invalid or "
            "malformed CSV format."
        )
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: file {path} is empty")
        return None
    except FileNotFoundError:
        print(f"Error: file {path} not founded")
        return None
    except IsADirectoryError as e:
        print(e)
        return None
    except Exception:
        return None
