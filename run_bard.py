from model_implementations.BardModel import BardModel

token = "<token>"

bard = BardModel("Bard", token, use_survey_data=True)
bard.run()
bard.close_logfile()