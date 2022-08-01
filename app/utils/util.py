from app.config.settings import setting


def init_config_env_db(env=None):
    if env:
        setting.env = env
        env_yml = setting.get_config_env()
        return env_yml
    env_yml = setting.get_config_env()
    return env_yml
