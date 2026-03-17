# Update Authorized User's Managed Organization Profile
Source: [https://docs.gitcode.com/en/docs/apis/patch-api-v-5-orgs-org](https://docs.gitcode.com/en/docs/apis/patch-api-v-5-orgs-org)
Category: Organizations
- Method: `PATCH`
- Path: `/api/v5/orgs/{org}`
- Operation ID: `patch_api_v5_orgs_{org}`
- Tags: `Organizations`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| org | path | true | string | Organization's path (path/login) |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "description": {
      "description": "Organization Profile 或 Organization Description",
      "type": "string"
    },
    "email": {
      "description": "Organization's Public Email Address",
      "type": "string"
    },
    "html_url": {
      "description": "Organization Website",
      "type": "string"
    },
    "location": {
      "description": "Organization Location",
      "type": "string"
    },
    "name": {
      "description": "Organization Name",
      "type": "string"
    }
  },
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
    "description": {
      "type": "string"
    },
    "email": {
      "type": "string"
    },
    "html_url": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "path": {
      "type": "string"
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
      "description": "233333",
      "email": "123@qq.com",
      "html_url": "www.baidu.com",
      "id": 138108,
      "name": "organization",
      "path": "xiaogang444"
    }
  }
}
```
## JSON Request Example
```json
{
  "description": "string",
  "email": "string",
  "html_url": "string",
  "location": "string",
  "name": "string"
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
    "description": "string",
    "email": "string",
    "html_url": "string",
    "location": "string",
    "name": "string"
  },
  "method": "patch",
  "operationId": "patch_api_v5_orgs_{org}",
  "parameters": [
    {
      "description": "Organization's path (path/login)",
      "example": "",
      "in": "path",
      "name": "org",
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
  "path": "/api/v5/orgs/{org}",
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
    "method": "PATCH",
    "name": "Update Authorized User's Managed Organization Profile",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "orgs",
        ":org"
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
            "content": "(Required) Organization's path (path/login)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "org",
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
            "description": {
              "description": "Organization Profile 或 Organization Description",
              "type": "string"
            },
            "email": {
              "description": "Organization's Public Email Address",
              "type": "string"
            },
            "html_url": {
              "description": "Organization Website",
              "type": "string"
            },
            "location": {
              "description": "Organization Location",
              "type": "string"
            },
            "name": {
              "description": "Organization Name",
              "type": "string"
            }
          },
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
                "description": "233333",
                "email": "123@qq.com",
                "html_url": "www.baidu.com",
                "id": 138108,
                "name": "organization",
                "path": "xiaogang444"
              }
            }
          },
          "schema": {
            "properties": {
              "description": {
                "type": "string"
              },
              "email": {
                "type": "string"
              },
              "html_url": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "name": {
                "type": "string"
              },
              "path": {
                "type": "string"
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
    "Organizations"
  ]
}
```
