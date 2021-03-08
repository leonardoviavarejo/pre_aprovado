"""
Para fazer a instalacao de bibliotecas que estao no pypi utilizar:

dbutils.library.installPyPI('numpy', '1.18.1')
"""

dbutils.library.install('dbfs:/mnt/gen2ds/app/packages/yggdrasil/Yggdrasil-2.3.0b0-py3-none-any.whl')
dbutils.library.install('dbfs:/mnt/gen2ds/app/packages/vvml/VVML-1.5.0b0-py3-none-any.whl')

dbutils.library.restartPython()

PROJECT_NAME = 'pre_aprovado'
PROJECT_MODE = 'dev' # Preencher com dev ou prod
