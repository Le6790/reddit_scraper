import boto3
import config


class Amazon_Polly:
    def __init__(self, voiceId="Matthew", outputFormat="mp3"):
        self.polly_client = boto3.Session(
            aws_access_key_id=config.CONFIG["AWSAccessKeyId"],
            aws_secret_access_key=config.CONFIG["AWSSecretKey"], region_name='us-west-2').client('polly')
        self.voiceId = voiceId
        self.outputFormat = outputFormat

    def create_audio(self, text, filename):
        response = self.polly_client.synthesize_speech(
            VoiceId=self.voiceId, OutputFormat=self.outputFormat, Text=text, Engine='neural')

        with open(filename, 'wb') as fout:
            fout.write(response['AudioStream'].read())

        print(f"Completed creating audio file - {filename}")
