import yaml
from pathlib import Path
from os.path import join

CONFIG_FILE = join(str(Path.home()), ".zotero_remarkable.yaml")
CONFIG_OPTIONS = dict(
        zot_api_key = "Zotero api key",
        zot_user_id = "zotero user id",
        zot_collection = "zotero collection name",
        webdav_url = "webdav URL",
        webdav_user = "webdav user name",
        webdav_password = "webdav password",
        rm_folder = "Remarkable folder")

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
    for i in CONFIG_OPTIONS.keys():
        if i not in cfg:
            valid = False
    return valid

def _create_config():
    cfg = {}
    for key in CONFIG_OPTIONS:
        answer = input(CONFIG_OPTIONS[key] + ": ")
        cfg[key] = answer.strip()
    _write_config(cfg)
    return cfg

def get_config():
    cfg = _read_config()
    if not _check_config(cfg):
        return _create_config()
    else:
        return cfg



