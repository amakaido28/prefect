from prefect import flow, tags
from prefect.logging import get_run_logger

@flow
def hello(name: str = "Marvin"):
    logger = get_run_logger()
    logger.info(f"Hello, {name}!")

if __name__ == "__main__":
    hello.source(
        source="https://github.com/username/repository.git",
        entrypoint="path/to/your/flow.py:your_flow_function"
    ).deploy(
        name="deploy-prova-s3",
        work_pool_name="test1"
    )