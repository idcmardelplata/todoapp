import sys
import dagger
import anyio

async def main():
    config = dagger.Config(log_output=sys.stdout)
    async with dagger.Connection(config) as client:
        python = (
                client.container()
                .from_("python:3.11-slim")
                .with_directory("/src", client.host().directory("."), exclude=["ci/"])
                .with_workdir("/src")
                .with_exec(["pip3", "install", "poetry"])
                .with_exec(["poetry", "config", "virtualenvs.create", "false"])
                .with_exec(["poetry", "install"])               
                .with_exec(["poetry", "run", "pytest"])
                )

        await python.stderr()

anyio.run(main)
