# Sentence Similarity
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-similarity](https://docs.gitcode.com/en/docs/apis/post-api-v-5-similarity)
Category: AI hub
- Method: `POST`
- Path: `/api/v5/similarity/`
- Operation ID: `post-api-v-5-similarity`
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
  "properties": {
    "inputs": {
      "properties": {
        "sentences": {
          "description": "[\"That is a happy dog\", \"That is a very happy person\"]",
          "items": {
            "type": "string"
          },
          "title": "Target text array for comparison",
          "type": "array"
        },
        "source_sentence": {
          "description": "\"That is a happy person\"",
          "title": "Comparative source text",
          "type": "string"
        }
      },
      "required": [
        "source_sentence",
        "sentences"
      ],
      "title": "Input parameters",
      "type": "object"
    },
    "model": {
      "title": "Model Name",
      "type": "string"
    }
  },
  "required": [
    "model",
    "inputs"
  ],
  "type": "object"
}
```
Example:
```json
{
  "inputs": {
    "sentences": [
      "That is a happy dog",
      "That is a very happy person"
    ],
    "source_sentence": "That is a happy person"
  },
  "model": "text2vec-base-chinese"
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
  "items": {
    "type": "number"
  },
  "type": "array"
}
```
Example:
```json
[
  0.8220268487930298,
  0.9805881381034851
]
```
## JSON Request Example
```json
{
  "inputs": {
    "sentences": [
      "string"
    ],
    "source_sentence": "string"
  },
  "model": "string"
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
  "jsonRequestBodyExample": {
    "inputs": {
      "sentences": [
        "string"
      ],
      "source_sentence": "string"
    },
    "model": "string"
  },
  "method": "post",
  "operationId": "post-api-v-5-similarity",
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
  "path": "/api/v5/similarity/",
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
      "content": "",
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
    "name": "Sentence Similarity",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "similarity",
        ""
      ],
      "query": [],
      "variable": []
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "example": {
          "inputs": {
            "sentences": [
              "That is a happy dog",
              "That is a very happy person"
            ],
            "source_sentence": "That is a happy person"
          },
          "model": "text2vec-base-chinese"
        },
        "schema": {
          "properties": {
            "inputs": {
              "properties": {
                "sentences": {
                  "description": "[\"That is a happy dog\", \"That is a very happy person\"]",
                  "items": {
                    "type": "string"
                  },
                  "title": "Target text array for comparison",
                  "type": "array"
                },
                "source_sentence": {
                  "description": "\"That is a happy person\"",
                  "title": "Comparative source text",
                  "type": "string"
                }
              },
              "required": [
                "source_sentence",
                "sentences"
              ],
              "title": "Input parameters",
              "type": "object"
            },
            "model": {
              "title": "Model Name",
              "type": "string"
            }
          },
          "required": [
            "model",
            "inputs"
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
          "example": [
            0.8220268487930298,
            0.9805881381034851
          ],
          "schema": {
            "items": {
              "type": "number"
            },
            "type": "array"
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
