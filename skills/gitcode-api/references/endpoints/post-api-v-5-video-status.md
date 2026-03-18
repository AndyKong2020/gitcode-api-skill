# Image Generation Video (Query Status)
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-video-status](https://docs.gitcode.com/en/docs/apis/post-api-v-5-video-status)
Category: AI hub
- Method: `POST`
- Path: `/api/v5/video/status`
- Operation ID: `post-api-v-5-video-status`
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
    "request_id": {
      "description": "Request ID",
      "example": "009522a671394f3f5ac02c63b1a62662",
      "type": "string"
    }
  },
  "required": [
    "request_id"
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
    "error_message": {
      "description": "Error message (appears only when an exception occurs)",
      "type": "string"
    },
    "request_id": {
      "description": "Request ID (Valid for 24h, please get the result as soon as possible)",
      "type": "string"
    },
    "status": {
      "description": "Process Status (running, failed, succeeded)",
      "example": "succeeded",
      "type": "string"
    },
    "video_url": {
      "description": "Video URL (only returned successfully, and the valid duration is 10 minutes)",
      "type": "string"
    }
  },
  "type": "object"
}
```
Example:
```json
{
  "request_id": "2600c2714f184f9087060b014fb2f7a3",
  "status": "succeeded",
  "video_url": "https://ai-inference-cdn-static.gitcode.com/video-2600c2714f184f9087060b014fb2f7a3-output.mp4?auth_key=1765510460-86c58596bd5944b1af78aa3587cfb902-0-44a97eda8e44774e561eaced4dd124865c7855ca2e251f3099b3ec3aea77c62b"
}
```
## JSON Request Example
```json
{
  "request_id": "009522a671394f3f5ac02c63b1a62662"
}
```
## Raw OpenAPI Operation
```json
{
  "deprecated": false,
  "description": "Query the video generation status based on requestId.",
  "info": {
    "description": "",
    "title": "GicodeOpenAPI",
    "version": "1.0.0"
  },
  "jsonRequestBodyExample": {
    "request_id": "009522a671394f3f5ac02c63b1a62662"
  },
  "method": "post",
  "operationId": "post-api-v-5-video-status",
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
  "path": "/api/v5/video/status",
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
      "content": "Query the video generation status based on requestId.",
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
    "name": "Image Generation Video (Query Status)",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "video",
        "status"
      ],
      "query": [],
      "variable": []
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "description": "",
          "properties": {
            "request_id": {
              "description": "Request ID",
              "example": "009522a671394f3f5ac02c63b1a62662",
              "type": "string"
            }
          },
          "required": [
            "request_id"
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
            "request_id": "2600c2714f184f9087060b014fb2f7a3",
            "status": "succeeded",
            "video_url": "https://ai-inference-cdn-static.gitcode.com/video-2600c2714f184f9087060b014fb2f7a3-output.mp4?auth_key=1765510460-86c58596bd5944b1af78aa3587cfb902-0-44a97eda8e44774e561eaced4dd124865c7855ca2e251f3099b3ec3aea77c62b"
          },
          "schema": {
            "properties": {
              "error_message": {
                "description": "Error message (appears only when an exception occurs)",
                "type": "string"
              },
              "request_id": {
                "description": "Request ID (Valid for 24h, please get the result as soon as possible)",
                "type": "string"
              },
              "status": {
                "description": "Process Status (running, failed, succeeded)",
                "example": "succeeded",
                "type": "string"
              },
              "video_url": {
                "description": "Video URL (only returned successfully, and the valid duration is 10 minutes)",
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
