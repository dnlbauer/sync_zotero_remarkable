import yaml
from pathlib import Path
from os.path import join

CONFIG_FILE = join(str(Path.home()), ".zotero_remarkable.yaml")

def _read_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return yaml.safe_load(f)
    except:
        return None

def _write_config(cfg):
    with open(CONFIG_FILE, "w", encoding="utf8") as f:
        yaml.dump(cfg, f, default_flow_style=False, allow_unicode=True)

def _check_config(cfg):
    if not isinstance(cfg, dict):
        return False
    valid = True
    for i in [
        "zot_api_key",
        "zot_user_id",
        "zot_collection",
        "webdav_url",
        "webdav_user",
        "webdav_password",
        "rm_folder"]:
        if i not in cfg:
            valid = False
    return valid

def _create_config():
    cfg = {}
    for i in [
        "zot_api_key",
        "zot_user_id",
        "zot_collection",
        "webdav_url",
        "webdav_user",
        "webdav_password",
        "rm_folder"]:
        answer = input(i + ": ")
        cfg[i] = answer.strip()
    _write_config(cfg)
    return cfg

def get_config():
    cfg = _read_config()
    if not _check_config(cfg):
        return _create_config()
    else:
        return cfg



