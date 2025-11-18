import os

IS_PRODUCTION = os.environ.get("IS_PRODUCTION")

if IS_PRODUCTION:
    from .conf.production.settings import *  # noqa: F403
else:
    from .conf.development.settings import *  # noqa: F403
