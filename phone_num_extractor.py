from pathlib import Path
import pandas as pd
import re

# File Paths
INPUT_FILE = Path("./data/test_input.csv")
GROUND_TRUTH_FILE = Path("./data/ground_truth.csv")

def load_csv(filepath: Path) -> pd.DataFrame:
    """
    Loads data from a CSV file into a pandas DataFrame, replacing all NaNs
    with empty strings.
    """
    return pd.read_csv(filepath).fillna('')

def preprocess_text_column(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Lowercase text in the specified column (modifies in place)."""
    df[column_name] = df[column_name].str.lower()
    return df

def extract_phone_number(text: str) -> str:
    """
    Extracts the first phone number matching the pattern '###-###-####'
    from the given text using regex. Returns empty string if none found.
    """
    phone_number_pattern = r"\d{3}-\d{3}-\d{4}"
    match = re.search(phone_number_pattern, text)
    return match.group(0) if match else "" 

def evaluate_predictions(predicted: pd.Series, actual: pd.Series) -> float:
    """Evaluate accuracy of predictions."""
    return (predicted == actual).mean()

def main():
    """
    Run the phone number extraction pipeline and evaluate its accuracy.

    Steps:
    1. Load input and ground truth data.
    2. Preprocess text data.
    3. Extract phone numbers.
    4. Merge predictions with ground truth.
    5. Calculate and print accuracy.
    """

    # Load data
    input_data = load_csv(INPUT_FILE)
    ground_truth = load_csv(GROUND_TRUTH_FILE)

    # Preprocess and predict
    input_data = preprocess_text_column(input_data, "text")
    input_data["predicted_phone_number"] = input_data["text"].apply(extract_phone_number)

    # Evaluate
    combined = input_data.merge(ground_truth, on="id", how="left")
    accuracy = evaluate_predictions(combined["predicted_phone_number"], combined["phone_number"])
    print(f"Accuracy: {accuracy:.2%}")
    print("")
    print("Predictions:\n", combined[["id", "text", "predicted_phone_number", "phone_number"]])

if __name__ == "__main__":
    main()
