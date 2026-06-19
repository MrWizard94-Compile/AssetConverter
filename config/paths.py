import os

# Repo root (parent of config/)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Override via environment for other machines
PROJECT_ROOT = os.environ.get("ASSETCONVERTER_ROOT", PROJECT_ROOT)

SOURCES_DIR = os.path.join(PROJECT_ROOT, "sources")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")
OUTPUT_ASSETS_DIR = os.path.join(OUTPUT_DIR, "assets")
RESOURCEPACK_DIR = os.path.join(OUTPUT_DIR, "resourcepack")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
CACHE_DIR = os.path.join(PROJECT_ROOT, "local", "cache")
JARS_DIR = os.path.join(PROJECT_ROOT, "local", "jars")

PACK_NAME = "Base-Wars_32x"
PACK_FORMAT = 15  # Minecraft 1.20.1

# CurseForge instance — override with ASSETCONVERTER_INSTANCE env
DEFAULT_INSTANCE = r"C:\Users\Bulkl\curseforge\minecraft\Instances\Base-Wars_Stripped"
INSTANCE_DIR = os.environ.get("ASSETCONVERTER_INSTANCE", DEFAULT_INSTANCE)
MODS_DIR = os.path.join(INSTANCE_DIR, "mods")
DEPLOY_DIR = os.path.join(INSTANCE_DIR, "resourcepacks")