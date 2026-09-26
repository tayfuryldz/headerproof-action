from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
action = (root / "action.yml").read_text()
workflow = (root / ".github" / "workflows" / "e2e.yml").read_text()
installer = (root / "install.sh").read_text()
readme = (root / "README.md").read_text().lower()

assert "raw.githubusercontent.com/TayfurYldz/headerproof/main/install.sh" not in action
assert '"$GITHUB_ACTION_PATH/install.sh"' in action
assert "HEADERPROOF_VERSION: ${{ inputs.version }}" in action
assert "checksums.txt" in installer
assert "checksum verification failed" in installer
assert "verified finding" not in readme

for ref in re.findall(r"uses:\\s+([^\\s#]+)", workflow):
    if ref.startswith("./"):
        continue
    assert re.fullmatch(r"[^/@]+/[^/@]+@[0-9a-f]{40}", ref), ref
