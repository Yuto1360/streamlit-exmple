import os
import pandas as pd

DATA_DIR = "data"
CSV_PATH = os.path.join(DATA_DIR, "passes.csv")

def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def append_passes_csv(df: pd.DataFrame):
    """通過予定データをCSVに追記保存"""
    ensure_data_dir()
    # 文字化け防止にUTF-8
    header = not os.path.exists(CSV_PATH)
    df.to_csv(CSV_PATH, mode="a", header=header, index=False, encoding="utf-8")

def load_passes_csv() -> pd.DataFrame | None:
    """保存済み通過データを読み込み（あれば）"""
    if not os.path.exists(CSV_PATH):
        return None
    return pd.read_csv(CSV_PATH, encoding="utf-8")
