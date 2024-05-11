from django.conf import settings
import openai
import traceback

openai.api_key = settings.OPENAI_API_KEY

