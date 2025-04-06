from dynaconf import Dynaconf
from pathlib import Path
import sys


BASE_DIR = Path(__file__).resolve().parent.parent
resolved_path = Path("api/settings/default.application.yaml").resolve()
if not resolved_path.exists():
    print(f"❌ Config path not found: {resolved_path}")
    sys.exit(1)
else:
    print(f"✅ Config file found: {resolved_path}")

# Загрузка настроек
settings = Dynaconf(
    settings_files=["api/settings/default.application.yaml"],
    environments=True,
    envvar_prefix="",
    dotenv_path=BASE_DIR.parent / ".env",
    load_dotenv=True,
)

# Отладочная инфа
print("🔍 Active environment:", settings.current_env)
print("📦 All settings loaded:")
print(settings.to_dict())