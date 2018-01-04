import keras
import json
import requests
 
class PostToSlack(keras.callbacks.Callback):
    def __init__(self):
        self.webhook_url = 'https://hooks.slack.com/services/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'
    
    def formatText(self, epoch, loss):
        formattedText = """***********
        *Epoch*: {} of {}
        *Loss* : {}""".format(epoch, self.epochs, loss)
        return formattedText

    def on_train_begin(self, logs={}):
        self.aucs = []
        self.losses = []
        self.epochs = self.params["epochs"]
 
    def on_train_end(self, logs={}):
        return
 
    def on_epoch_begin(self, epoch, logs={}):
        return
 
    def on_epoch_end(self, epoch, logs={}):
        self.losses.append(logs.get('loss'))
        slack_data = {'text': self.formatText(epoch, logs.get("loss"))}
        response = requests.post(
            self.webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
            )
        return
 
    def on_batch_begin(self, batch, logs={}):
        return
 
    def on_batch_end(self, batch, logs={}):
        return