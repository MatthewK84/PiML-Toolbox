# -*- coding: utf-8 -*-
"""
GAMI-Net Classification (Taiwan Credit)
===============================================
"""

#%%
# Experiment initialization and data preparation
from piml import Experiment
from piml.models import GAMINetClassifier

exp = Experiment()
exp.data_loader(data="TaiwanCredit", silent=True)
exp.data_summary(feature_exclude=["LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE"], silent=True)
exp.data_prepare(target="FlagDefault", task_type="classification", silent=True)

#%%
# Train Model
exp.model_train(model=GAMINetClassifier(), name="GAMI-Net")

#%%
# Evaluate predictive performance
exp.model_diagnose(model="GAMI-Net", show='accuracy_table')

#%%
# Effect importance
exp.model_interpret(model="GAMI-Net", show="global_ei", figsize=(5, 4))

#%%
# Feature importance
exp.model_interpret(model="GAMI-Net", show="global_fi", figsize=(5, 4))

#%%
# Global effect plot for PAY_1
exp.model_interpret(model="GAMI-Net", show="global_effect_plot", uni_feature="PAY_1",
                    original_scale=True, figsize=(5, 4))

#%%
# Local interpretation by effect
exp.model_interpret(model="GAMI-Net", show="local_ei", sample_id=0, original_scale=True, figsize=(5, 4))

#%%
# Local interpretation by feature
exp.model_interpret(model="GAMI-Net", show="local_fi", sample_id=0, original_scale=True, figsize=(5, 4))
