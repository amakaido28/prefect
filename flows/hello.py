from prefect import flow, tags
from prefect.logging import get_run_logger
import torch


@flow
def hello(name: str = "Marvin"):
    print("!*!*!*!*!* Hello *!*!**!*!*!*!")
    gpu_stats = torch.cuda.get_device_properties(0)
    start_gpu_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
    max_memory = round(gpu_stats.total_memory / 1024 / 1024 / 1024, 3)
    print(f"GPU = {gpu_stats.name}. Max memory = {max_memory} GB.")
    print(f"{start_gpu_memory} GB of memory reserved.")
    print("!*!*!*!*!* End *!*!**!*!*!*!")


if __name__ == "__main__":
    hello.from_source(
        source="https://github.com/amakaido28/prefect.git",
        entrypoint="flows/hello.py:hello"
    ).deploy(
        name="deploy-prova-git",
        work_pool_name="test1",
        job_variables={"pip_packages": ["prefect", "prefect-docker", "prefect-kubernetes", "torch"], 
                        "env": {
                            "PREFECT_API_URL": "http://172.18.21.116:4200/api",
                            "PREFECT_SERVER_ALLOW_EPHEMERAL_MODE": "False",
                            "PREFECT_SERVER_API_HOST": "172.18.21.116"
                        }
                    }
    )