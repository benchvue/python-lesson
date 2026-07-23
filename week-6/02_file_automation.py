from pathlib import Path

reports_dir = Path("reports")
reports_dir.mkdir(exist_ok=True)

for month in ["January", "February", "March"]:
    file_path = reports_dir / f"{month}_report.txt"
    file_path.write_text(f"{month} accounting report\n", encoding="utf-8")

print("Report files created in reports folder.")
