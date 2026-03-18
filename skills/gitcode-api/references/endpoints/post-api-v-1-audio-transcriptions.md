# Automatic Speech Recognition
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-1-audio-transcriptions](https://docs.gitcode.com/en/docs/apis/post-api-v-1-audio-transcriptions)
Category: AI hub
- Method: `POST`
- Path: `/api/v5/audio/transcriptions`
- Operation ID: `post-api-v-1-audio-transcriptions`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Authorization | header | true | string | User Personal Token |
## Request Body
#### `multipart/form-data`
Schema:
```json
{
  "properties": {
    "file": {
      "description": "Audio File (supports mp3, wav, m4a, flac, webm)",
      "format": "binary",
      "type": "string"
    },
    "model": {
      "description": "Model Name, default is openai/whisper-large-v3",
      "type": "string"
    },
    "temperature": {
      "description": "Sample Temperature (0.0-1.0), default is 0.6",
      "type": "string"
    }
  },
  "required": [
    "file",
    "model"
  ],
  "type": "object"
}
```
## Responses
### `200`
Headers:
```json
{}
```
#### `application/json`
Schema:
```json
{
  "properties": {
    "text": {
      "title": "Text",
      "type": "string"
    }
  },
  "required": [
    "text"
  ],
  "type": "object"
}
```
Example:
```json
{
  "text": "Good morning, the weather is very good today, sunny and bright. I plan to take a walk in the park, then have a cup of coffee, and start my work for the day."
}
```
## Raw OpenAPI Operation
```json
{
  "deprecated": false,
  "description": "",
  "info": {
    "description": "",
    "title": "GicodeOpenAPI",
    "version": "1.0.0"
  },
  "method": "post",
  "operationId": "post-api-v-1-audio-transcriptions",
  "parameters": [
    {
      "description": "User Personal Token",
      "example": "",
      "in": "header",
      "name": "Authorization",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/audio/transcriptions",
  "postman": {
    "body": {
      "formdata": [],
      "mode": "formdata"
    },
    "description": {
      "content": "",
      "type": "text/plain"
    },
    "header": [
      {
        "key": "Content-Type",
        "value": "multipart/form-data"
      },
      {
        "key": "Accept",
        "value": "application/json"
      }
    ],
    "method": "POST",
    "name": "Automatic Speech Recognition",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "audio",
        "transcriptions"
      ],
      "query": [],
      "variable": []
    }
  },
  "requestBody": {
    "content": {
      "multipart/form-data": {
        "schema": {
          "properties": {
            "file": {
              "description": "Audio File (supports mp3, wav, m4a, flac, webm)",
              "format": "binary",
              "type": "string"
            },
            "model": {
              "description": "Model Name, default is openai/whisper-large-v3",
              "type": "string"
            },
            "temperature": {
              "description": "Sample Temperature (0.0-1.0), default is 0.6",
              "type": "string"
            }
          },
          "required": [
            "file",
            "model"
          ],
          "type": "object"
        }
      }
    }
  },
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "example": {
            "text": "Good morning, the weather is very good today, sunny and bright. I plan to take a walk in the park, then have a cup of coffee, and start my work for the day."
          },
          "schema": {
            "properties": {
              "text": {
                "title": "Text",
                "type": "string"
              }
            },
            "required": [
              "text"
            ],
            "type": "object"
          }
        }
      },
      "description": "",
      "headers": {}
    }
  },
  "security": [],
  "securitySchemes": {},
  "servers": [
    {
      "description": "正式环境",
      "url": "https://api.gitcode.com"
    }
  ],
  "tags": []
}
```
