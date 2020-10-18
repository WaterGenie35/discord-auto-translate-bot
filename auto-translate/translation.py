import os
from google.cloud.translate import TranslationServiceClient
from custom_types import Language

class TranslationService:
    
    def __init__(self):
        credential_file = os.getenv('GOOGLE_SERVICE_ACCOUNT_CREDENTIALS')
        self.google = TranslationServiceClient.from_service_account_json(
                credential_file
        )
        self.project_id = os.getenv('GOOGLE_PROJECT_ID')
        self.location = os.getenv('GOOGLE_SERVICE_LOCATION')
        print("Google translation service initialised.")

    def translate(self, source:Language, target:Language, content:str) -> str:
        resource = f'projects/{self.project_id}/locations/{self.location}'
        request = {
            'parent': resource,
            'contents': [content],
            'mime_type': 'text/plain',
            'source_language_code': source.code,
            'target_language_code': target.code
        }
        response = self.google.translate_text(request)
        result = response.translations[0].translated_text
        return result
        
