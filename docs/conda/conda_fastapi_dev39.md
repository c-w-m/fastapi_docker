## Create Environment

```shell
conda create --name fastapi_dev39
```

## Create Environment File

```shell
conda env export --name fastapi_dev39 --file fastapi_dev39_v1.yml
```

## To activate this environment, use

```shell
conda activate fastapi_dev39
```

## To deactivate an active environment, use

```shell
conda deactivate
```

## Install package and updating the yaml file

```shell
conda install -c conda-forge fastapi      # 8 new, 1 update, 2 superseded
conda env export --name fastapi_dev39 --file fastapi_dev39_v2.yml

conda install -c conda-forge uvicorn      # 4 new
conda env export --name fastapi_dev39 --file fastapi_dev39_v3.yml

conda install -c conda-forge httpx        # 6 new, h11 downgrade
conda env export --name fastapi_dev39 --file fastapi_dev39_v4.yml
```
