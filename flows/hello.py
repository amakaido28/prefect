from prefect import flow, tags
from prefect.logging import get_run_logger
import os 
os.environ['PREFECT_API_URL'] = 'http://172.18.21.116:4200/api'
os.environ['PREFECT_SERVER_API_HOST'] = '172.18.21.116'
os.environ['PREFECT_SERVER_ALLOW_EPHEMERAL_MODE'] = 'False'

@flow
def hello(name: str = "Marvin"):
    logger = get_run_logger()
    logger.info(f"Hello, {name}!")

if __name__ == "__main__":
    hello.from_source(
        source="https://github.com/amakaido28/prefect.git",
        entrypoint="flows/hello.py:hello"
    ).deploy(
        name="deploy-prova-git",
        work_pool_name="test1",
        job_variables={"pip_packages": ["prefect", "prefect-docker", "prefect-kubernetes"], 
                        "env": {"PREFECT_API_URL": "172.18.21.116"},
                        "env": {"PREFECT_SERVER_ALLOW_EPHEMERAL_MODE": "False"},
                    }
    )