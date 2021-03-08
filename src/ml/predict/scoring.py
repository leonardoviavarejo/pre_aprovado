"""
Para fazer a instalacao de bibliotecas que estao no pypi utilizar:

dbutils.library.installPyPI('numpy', '1.18.1')
"""

dbutils.library.install('dbfs:/mnt/gen2ds/app/packages/yggdrasil/Yggdrasil-2.3.0b0-py3-none-any.whl')
dbutils.library.install('dbfs:/mnt/gen2ds/app/packages/vvml/VVML-1.5.0b0-py3-none-any.whl')

dbutils.library.restartPython()

PROJECT_NAME = 'pre_aprovado'
PROJECT_MODE = 'dev' # Preencher com dev ou prod


import numpy as np
import pandas as pd

from vvml.core.node import Node
from vvml.core.project import Project


def predict():
	predict_df = pd.DataFrame()
	return dict(output=predict_df)

project = Project.get(PROJECT_NAME)
project.set_mode(PROJECT_MODE)
project.run_predict(predict, "Production predict of {project_name}".format(project_name=PROJECT_NAME))
