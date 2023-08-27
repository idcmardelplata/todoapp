import sys
import dagger
import anyio

async def main():
    config = dagger.Config(log_output=sys.stdout)
    async with dagger.Connection(config) as client:
        cache = client.cache_volume("pip")
        python = (
                client.container()
                .from_("idcmardelplata/poetry:v02")
                .with_directory("/src", client.host().directory("."), exclude=["ci/"])
                .with_workdir("/src")
                .with_exec(["poetry", "config", "cache-dir", "/src/.cache/"])
                .with_mounted_cache("/src/.cache", cache)
                .with_exec(["poetry", "install"])               
                .with_mounted_cache("/src/.cache", cache)
                .with_exec(["poetry", "run", "pytest"])
                )

        await python.stderr()

anyio.run(main)
