from pathlib import Path
from jeod_helpers import cli


def test_cli_version(capsys):
    assert cli.main(["version"]) == 0
    out = capsys.readouterr().out.strip()
    assert out


def test_cli_generate(tmp_path):
    out = tmp_path / "input.py"
    assert cli.main(["generate", str(out)]) == 0
    assert out.exists()
    text = out.read_text()
    assert "actions" in text
