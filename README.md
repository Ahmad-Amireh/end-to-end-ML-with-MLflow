# end-to-end-ML-with-MLflow


##Workflows 

1. Update config.yaml
2. Update schema.yaml 
3. update param.yaml 
4. update the entity 
5. update configuration manager in src
6. update the components 
7. update the pipeline
8. update the main.py 
9. update the app.py


# How to run?

## STEPS: 

### STEP 01 Clone the repo: 

```bash 
https://github.com/Ahmad-Amireh/end-to-end-ML-with-MLflow/
``` 
### STEP 02 Create a conda environment (The base env has been used here)

```bash  
conda create -n env python=3.9.13 -y 
```

```bash
conda activate env
```

#### Note please if you don't have conda in your system please follow this link: 

[Documentiaon](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)


### STEP 03 Install the requirments 
```bash 
pip install -r requirments.txt 
```

```bash 
python app.py
```

```bash 
open up your local host and port
```

## MLflow 

[Documentaion](https://mlflow.org/docs/latest/index.html)


#### cmd 
- mflow uri 

### dagshub 
[dagshub](https://dagshub.com)

MLFOLOW_TRACKING_URI= https://dagshub.com/Ahmad97/my-first-repo.mlflow
DAGS_HUB_TOKEN = 4cefc6718b7a65548a8d20d5c9012fcff949fd23

``` bash
export MLFOLOW_TRACKING_URI= https://dagshub.com/Ahmad97/my-first-repo.mlflow #Linux
set MLFOLOW_TRACKING_URI= https://dagshub.com/Ahmad97/my-first-repo.mlflow # CMD
export DAGS_HUB_TOKEN=4cefc6718b7a65548a8d20d5c9012fcff949fd23 #Linux
'''
