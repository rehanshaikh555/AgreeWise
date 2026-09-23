from pathlib import Path


def extract_txt(source: str | Path | bytes) -> str:
    if isinstance(source, bytes):
        return source.decode("utf-8", errors="replace")

    return Path(source).read_text(
        encoding="utf-8",
        errors="replace",
    )
