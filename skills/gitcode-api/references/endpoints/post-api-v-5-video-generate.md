# Image Generation Video (Create Task)
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-video-generate](https://docs.gitcode.com/en/docs/apis/post-api-v-5-video-generate)
Category: AI hub
- Method: `POST`
- Path: `/api/v5/video/generate`
- Operation ID: `post-api-v-5-video-generate`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Authorization | header | true | string | User Personal Token |
## Request Body
#### `application/json`
Schema:
```json
{
  "description": "",
  "properties": {
    "img_url": {
      "description": "Supports input of Base64 or image URL",
      "example": "https://cdn-static.gitcode.com/_nuxtaihub/chatexample_67.png",
      "type": "string"
    },
    "model": {
      "description": "Model Name",
      "example": "Wan2.2-I2V-A14B",
      "type": "string"
    },
    "prompt": {
      "description": "Prompt words",
      "example": "The kitten is taking a walk.",
      "type": "string"
    },
    "seed": {
      "default": 0,
      "description": "Random seed, range 0-2147483648",
      "example": 0,
      "format": "int64",
      "type": "integer"
    }
  },
  "required": [
    "img_url",
    "model",
    "prompt"
  ],
  "type": "object"
}
```
Example:
```json
{
  "img_url": "https://cdn-static.gitcode.com/_nuxtaihub/chatexample_67.png",
  "model": "Wan2.2-I2V-A14B",
  "prompt": "The magician's hands release a shower of playing cards, with dazzling light bursting from his palm, followed by a cascade of colorful paper pieces and fireworks, dazzling and sparkling.",
  "seed": 0
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
    "error_message": {
      "description": "Error message (appears only when an exception occurs)",
      "type": "string"
    },
    "request_id": {
      "description": "Request ID",
      "type": "string"
    },
    "status": {
      "description": "Processing Status",
      "example": "running",
      "type": "string"
    }
  },
  "type": "object"
}
```
## JSON Request Example
```json
{
  "img_url": "https://cdn-static.gitcode.com/_nuxtaihub/chatexample_67.png",
  "model": "Wan2.2-I2V-A14B",
  "prompt": "The kitten is taking a walk.",
  "seed": 0
}
```
## Raw OpenAPI Operation
```json
{
  "deprecated": false,
  "description": "Call this interface to create a video generation task. If there is no exception, the asynchronous video result can be queried using the requestId.",
  "info": {
    "description": "",
    "title": "GicodeOpenAPI",
    "version": "1.0.0"
  },
  "jsonRequestBodyExample": {
    "img_url": "https://cdn-static.gitcode.com/_nuxtaihub/chatexample_67.png",
    "model": "Wan2.2-I2V-A14B",
    "prompt": "The kitten is taking a walk.",
    "seed": 0
  },
  "method": "post",
  "operationId": "post-api-v-5-video-generate",
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
  "path": "/api/v5/video/generate",
  "postman": {
    "body": {
      "mode": "raw",
      "options": {
        "raw": {
          "language": "json"
        }
      },
      "raw": ""
    },
    "description": {
      "content": "Call this interface to create a video generation task. If there is no exception, the asynchronous video result can be queried using the requestId.",
      "type": "text/plain"
    },
    "header": [
      {
        "key": "Content-Type",
        "value": "application/json"
      },
      {
        "key": "Accept",
        "value": "application/json"
      }
    ],
    "method": "POST",
    "name": "Image Generation Video (Create Task)",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "video",
        "generate"
      ],
      "query": [],
      "variable": []
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "example": {
          "img_url": "https://cdn-static.gitcode.com/_nuxtaihub/chatexample_67.png",
          "model": "Wan2.2-I2V-A14B",
          "prompt": "The magician's hands release a shower of playing cards, with dazzling light bursting from his palm, followed by a cascade of colorful paper pieces and fireworks, dazzling and sparkling.",
          "seed": 0
        },
        "schema": {
          "description": "",
          "properties": {
            "img_url": {
              "description": "Supports input of Base64 or image URL",
              "example": "https://cdn-static.gitcode.com/_nuxtaihub/chatexample_67.png",
              "type": "string"
            },
            "model": {
              "description": "Model Name",
              "example": "Wan2.2-I2V-A14B",
              "type": "string"
            },
            "prompt": {
              "description": "Prompt words",
              "example": "The kitten is taking a walk.",
              "type": "string"
            },
            "seed": {
              "default": 0,
              "description": "Random seed, range 0-2147483648",
              "example": 0,
              "format": "int64",
              "type": "integer"
            }
          },
          "required": [
            "img_url",
            "model",
            "prompt"
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
          "schema": {
            "properties": {
              "error_message": {
                "description": "Error message (appears only when an exception occurs)",
                "type": "string"
              },
              "request_id": {
                "description": "Request ID",
                "type": "string"
              },
              "status": {
                "description": "Processing Status",
                "example": "running",
                "type": "string"
              }
            },
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
