import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/Arijeetzz/Twitter-Sentiment_Analysis.mlflow')
dagshub.init(repo_owner='Arijeetzz', repo_name='Twitter-Sentiment_Analysis', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

