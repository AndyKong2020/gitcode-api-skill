# Upload File
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-file-upload](https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-file-upload)
Category: Repositories
- Method: `POST`
- Path: `/api/v5/repos/{owner}/{repo}/file/upload`
- Operation ID: `post_api_v5_repos_{owner}_{repo}_file_upload`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "file": {
      "description": "File (up to 20M)",
      "type": "file"
    }
  },
  "required": [
    "file"
  ],
  "type": "object"
}
```
Example:
```json
""
```
## Responses
### `200`
Successful Response
Headers:
```json
{}
```
#### `application/json`
Schema:
```json
{
  "properties": {
    "full_path": {
      "type": "string"
    },
    "path": {
      "type": "string"
    },
    "success": {
      "type": "integer"
    }
  },
  "type": "object"
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "full_path": "https://gitcode.com/xiaogang/test/attachment/uploads/4c98ad75-729f-49ce-82ab-b41c1f7ffc90/test3.txt",
      "path": "uploads/4c98ad75-729f-49ce-82ab-b41c1f7ffc90/test3.txt",
      "success": true
    }
  }
}
```
## JSON Request Example
```json
{}
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
  "jsonRequestBodyExample": {},
  "method": "post",
  "operationId": "post_api_v5_repos_{owner}_{repo}_file_upload",
  "parameters": [
    {
      "description": "Repository space address (address path of the enterprise, organization, or individual)",
      "example": "",
      "in": "path",
      "name": "owner",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Repository path (path)",
      "example": "",
      "in": "path",
      "name": "repo",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "User authorization code",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/file/upload",
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
    "name": "Upload File",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "repos",
        ":owner",
        ":repo",
        "file",
        "upload"
      ],
      "query": [
        {
          "description": {
            "content": "(Required) User authorization code",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "access_token",
          "value": ""
        }
      ],
      "variable": [
        {
          "description": {
            "content": "(Required) Repository space address (address path of the enterprise, organization, or individual)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "owner",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) Repository path (path)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "repo",
          "type": "any",
          "value": ""
        }
      ]
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "example": "",
        "schema": {
          "properties": {
            "file": {
              "description": "File (up to 20M)",
              "type": "file"
            }
          },
          "required": [
            "file"
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
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": {
                "full_path": "https://gitcode.com/xiaogang/test/attachment/uploads/4c98ad75-729f-49ce-82ab-b41c1f7ffc90/test3.txt",
                "path": "uploads/4c98ad75-729f-49ce-82ab-b41c1f7ffc90/test3.txt",
                "success": true
              }
            }
          },
          "schema": {
            "properties": {
              "full_path": {
                "type": "string"
              },
              "path": {
                "type": "string"
              },
              "success": {
                "type": "integer"
              }
            },
            "type": "object"
          }
        }
      },
      "description": "Successful Response",
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
    "Repositories"
  ]
}
```
