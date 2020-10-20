import os
from google.cloud.translate import TranslationServiceClient
from custom_types import Language

class TranslationService:
    
    def __init__(self):
        credential_file = os.getenv('GOOGLE_SERVICE_ACCOUNT_CREDENTIALS')
        self.project_id = os.getenv('GOOGLE_PROJECT_ID')
        self.location = os.getenv('GOOGLE_SERVICE_LOCATION')
        self.project_name = f'projects/{self.project_id}'
        self.project_resource = f'{self.project_name}/locations/{self.location}'

        self.google = TranslationServiceClient.from_service_account_json(
                credential_file)
        print("Google translation service initialised.")


    def translate(self, source:Language, target:Language, content:str) -> str:
        request = {
            'parent': self.project_resource,
            'contents': [content],
            'mime_type': 'text/plain',
            'source_language_code': source.code,
            'target_language_code': target.code
        }
        response = self.google.translate_text(request)
        result = response.translations[0].translated_text
        return result
        
    @staticmethod
    def get_monthly_quota() -> int:
        return 436511
