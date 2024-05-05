import json
import os
from openai import OpenAI

def hit_llm(event, context):
    # Get OpenAI API key from environment variables
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    # print("made it into function")
    
    # Check if API key is present
    if not openai_api_key:
        return {
            'statusCode': 400,
            'body': 'OpenAI API key not found in environment variables.'
        }
    
    # Initialize OpenAI client with API key
    client = OpenAI(api_key=openai_api_key)
    
    # Extract data from event argument
    model = event.get('model')
    prompt = event.get('prompt')
    stream = event.get('stream')
    max_tokens = event.get('max_tokens')
    
    # Check if all necessary data is present in the event
    if not model or not prompt:
        return {
            'statusCode': 400,
            'body': 'Missing required data in the event argument.'
        }
    
    # Generate completion using OpenAI client
    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                        messages=[{"role": "user", "content": prompt}],
                                        max_tokens=max_tokens,
                                        stream=stream)
    # Return the response
    # print(response)
    return {
        'statusCode': 200,
        'body': response.choices[0].message.content
    }