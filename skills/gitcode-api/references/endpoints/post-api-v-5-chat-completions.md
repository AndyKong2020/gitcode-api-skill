# Text generation
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-chat-completions](https://docs.gitcode.com/en/docs/apis/post-api-v-5-chat-completions)
Category: AI hub
- Method: `POST`
- Path: `/api/v5/chat/completions`
- Operation ID: `post-api-v-5-chat-completions`
- Tags: `AI hub`
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
    "frequency_penalty": {
      "description": "Default 1.0",
      "type": "number"
    },
    "maxTokens": {
      "title": "Maximum Token Count",
      "type": "integer"
    },
    "messages": {
      "items": {
        "type": "string"
      },
      "title": "Message List",
      "type": "array"
    },
    "model": {
      "title": "Model",
      "type": "string"
    },
    "temperature": {
      "description": "Default 0.7",
      "title": "Temperature",
      "type": "number"
    },
    "top_k": {
      "description": "Default 50",
      "title": "top_k",
      "type": "integer"
    },
    "top_p": {
      "description": "Default 0.7",
      "title": "top_p",
      "type": "number"
    }
  },
  "required": [
    "messages",
    "model"
  ],
  "type": "object"
}
```
Example:
```json
{
  "frequency_penalty": 1,
  "max_tokens": 4096,
  "messages": [
    {
      "content": "Hello, what can you help me with?",
      "role": "user"
    }
  ],
  "model": "hf_mirrors/rohithsiddhartha/DeepSeek-R1-4bit",
  "temperature": 0.7,
  "top_k": 50,
  "top_p": 0.7
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
    "choices": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "ext": {
      "description": "Extended field, usually null",
      "type": "string"
    },
    "trace_id": {
      "description": "Unique identifier of the request",
      "title": "String",
      "type": "string"
    },
    "usage": {
      "properties": {
        "completion_tokens": {
          "description": "Token count required to complete the content",
          "title": "1",
          "type": "integer"
        },
        "prompt_tokens": {
          "description": "Token count for the prompt",
          "title": "1",
          "type": "integer"
        },
        "think_tokens": {
          "description": "The number of token consumed in the thinking process",
          "title": "1",
          "type": "integer"
        },
        "total_tokens": {
          "description": "Total token count",
          "title": "1",
          "type": "integer"
        }
      },
      "required": [
        "prompt_tokens",
        "completion_tokens",
        "total_tokens"
      ],
      "type": "object"
    }
  },
  "required": [
    "trace_id",
    "choices",
    "ext",
    "usage"
  ],
  "type": "object"
}
```
Example:
```json
{
  "choices": [
    {
      "delta": {
        "content": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation! This is a streaming content fragment."
      },
      "finish_reason": null,
      "index": 0
    }
  ],
  "ext": null,
  "trace_id": "045560649c7c483e80eb196e2bc95d38",
  "usage": {
    "completion_tokens": 146,
    "prompt_tokens": 11,
    "think_tokens": null,
    "total_tokens": 157
  }
}
```
## JSON Request Example
```json
{
  "frequency_penalty": 0,
  "maxTokens": 0,
  "messages": [
    "string"
  ],
  "model": "string",
  "temperature": 0,
  "top_k": 0,
  "top_p": 0
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
    "frequency_penalty": 0,
    "maxTokens": 0,
    "messages": [
      "string"
    ],
    "model": "string",
    "temperature": 0,
    "top_k": 0,
    "top_p": 0
  },
  "method": "post",
  "operationId": "post-api-v-5-chat-completions",
  "parameters": [
    {
      "description": "User Personal Token",
      "in": "header",
      "name": "Authorization",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/chat/completions",
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
    "name": "Text generation",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "chat",
        "completions"
      ],
      "query": [],
      "variable": []
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "example": {
          "frequency_penalty": 1,
          "max_tokens": 4096,
          "messages": [
            {
              "content": "Hello, what can you help me with?",
              "role": "user"
            }
          ],
          "model": "hf_mirrors/rohithsiddhartha/DeepSeek-R1-4bit",
          "temperature": 0.7,
          "top_k": 50,
          "top_p": 0.7
        },
        "schema": {
          "properties": {
            "frequency_penalty": {
              "description": "Default 1.0",
              "type": "number"
            },
            "maxTokens": {
              "title": "Maximum Token Count",
              "type": "integer"
            },
            "messages": {
              "items": {
                "type": "string"
              },
              "title": "Message List",
              "type": "array"
            },
            "model": {
              "title": "Model",
              "type": "string"
            },
            "temperature": {
              "description": "Default 0.7",
              "title": "Temperature",
              "type": "number"
            },
            "top_k": {
              "description": "Default 50",
              "title": "top_k",
              "type": "integer"
            },
            "top_p": {
              "description": "Default 0.7",
              "title": "top_p",
              "type": "number"
            }
          },
          "required": [
            "messages",
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
            "choices": [
              {
                "delta": {
                  "content": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation! This is a streaming content fragment."
                },
                "finish_reason": null,
                "index": 0
              }
            ],
            "ext": null,
            "trace_id": "045560649c7c483e80eb196e2bc95d38",
            "usage": {
              "completion_tokens": 146,
              "prompt_tokens": 11,
              "think_tokens": null,
              "total_tokens": 157
            }
          },
          "schema": {
            "properties": {
              "choices": {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              "ext": {
                "description": "Extended field, usually null",
                "type": "string"
              },
              "trace_id": {
                "description": "Unique identifier of the request",
                "title": "String",
                "type": "string"
              },
              "usage": {
                "properties": {
                  "completion_tokens": {
                    "description": "Token count required to complete the content",
                    "title": "1",
                    "type": "integer"
                  },
                  "prompt_tokens": {
                    "description": "Token count for the prompt",
                    "title": "1",
                    "type": "integer"
                  },
                  "think_tokens": {
                    "description": "The number of token consumed in the thinking process",
                    "title": "1",
                    "type": "integer"
                  },
                  "total_tokens": {
                    "description": "Total token count",
                    "title": "1",
                    "type": "integer"
                  }
                },
                "required": [
                  "prompt_tokens",
                  "completion_tokens",
                  "total_tokens"
                ],
                "type": "object"
              }
            },
            "required": [
              "trace_id",
              "choices",
              "ext",
              "usage"
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
  "tags": [
    "AI hub"
  ]
}
```
