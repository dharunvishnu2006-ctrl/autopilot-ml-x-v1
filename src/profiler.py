def profile(df) -> dict:
    """Return a dict report for any dataset."""

    report = {
        "rows": df.shape[0],
        "cols": df.shape[1],
        "column_names": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "numeric_summary": df.describe().to_dict()
    }

    return report