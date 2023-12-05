# Tratamiento de datos
# ==============================================================================
import pandas as pd
import numpy as np

# Gráficos
# ==============================================================================
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

# Preprocesado y modelado
# ==============================================================================
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.weightstats import ttest_ind

# Configuración matplotlib
# ==============================================================================
plt.rcParams['image.cmap'] = "bwr"
#plt.rcParams['figure.dpi'] = "100"
plt.rcParams['savefig.bbox'] = "tight"
style.use('ggplot') or plt.style.use('ggplot')

# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')


data_frame = pd.read_csv('./home/amuoz23/Escritorio/probabilidad/data.csv')
data_frame.head(475)

#array de SEMESTRE ACTUAL
semAct = data_frame['SEMESTRE ACTUAL'].values

#array de ESTRATO
estrato = data_frame['ESTRATO'].values

#array de PROMEDIO CARRERA
promCarr = data_frame['PROMEDIO CARRERA'].values

#array de PROMEDIO SEMESTRE
promSeme = data_frame['PROMEDIO SEMESTRE'].values

#array de RESUTADO
resultados = data_frame['RESULTADO'].values

print(resultados)