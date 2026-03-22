from .asset_resolver import resolve_active_asset
from .paths import ensure_base_dirs


def validate_ready(context):
    resolved = resolve_active_asset(context)
    dirs = ensure_base_dirs(context)
    errors = []
    if not resolved.image_path.exists():
        errors.append(f"Image file does not exist: {resolved.image_path}")
    for key in ("job", "source", "export"):
        if not dirs[key].exists():
            errors.append(f"Missing directory: {dirs[key]}")
    return errors
