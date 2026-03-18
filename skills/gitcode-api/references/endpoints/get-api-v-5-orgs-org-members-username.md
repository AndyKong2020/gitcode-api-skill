# Get Organization Member Details
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-orgs-org-members-username](https://docs.gitcode.com/en/docs/apis/get-api-v-5-orgs-org-members-username)
Category: Organizations
- Method: `GET`
- Path: `/api/v5/orgs/{org}/members/{username}`
- Operation ID: `get_api_v5_orgs_{org}_members_{username}`
- Tags: `Organizations`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| org | path | true | string | Organization's path (path/login) |
| username | path | true | string | username (alias: login) |
| access_token | query | true | string | User authorization code |
## Request Body
No request body.
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
    "avatar_url": {
      "type": "null"
    },
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "path": {
      "type": "string"
    },
    "url": {
      "type": "string"
    },
    "user": {
      "properties": {
        "avatar_url": {
          "type": "null"
        },
        "html_url": {
          "type": "string"
        },
        "id": {
          "type": "string"
        },
        "login": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "object_id": {
          "type": "string"
        },
        "user_id": {
          "type": "string"
        }
      },
      "type": "object"
    }
  },
  "type": "object"
}
```
Examples:
```json
{
  "1": {
    "description": "",
    "summary": "Successful Example",
    "value": {
      "avatar_url": null,
      "id": 133039,
      "name": "",
      "path": "openharmony",
      "url": "",
      "user": {
        "avatar_url": null,
        "html_url": "https://gitcode.com/theo6789",
        "id": "64dc3b13b8b9504cec223ab1",
        "login": "theo6789",
        "name": "TheoCui"
      }
    }
  }
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
  "method": "get",
  "operationId": "get_api_v5_orgs_{org}_members_{username}",
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
      "description": "username (alias: login)",
      "example": "",
      "in": "path",
      "name": "username",
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
  "path": "/api/v5/orgs/{org}/members/{username}",
  "postman": {
    "description": {
      "content": "",
      "type": "text/plain"
    },
    "header": [
      {
        "key": "Accept",
        "value": "application/json"
      }
    ],
    "method": "GET",
    "name": "Get Organization Member Details",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "orgs",
        ":org",
        "members",
        ":username"
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
        },
        {
          "description": {
            "content": "(Required) username (alias: login)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "username",
          "type": "any",
          "value": ""
        }
      ]
    }
  },
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "examples": {
            "1": {
              "description": "",
              "summary": "Successful Example",
              "value": {
                "avatar_url": null,
                "id": 133039,
                "name": "",
                "path": "openharmony",
                "url": "",
                "user": {
                  "avatar_url": null,
                  "html_url": "https://gitcode.com/theo6789",
                  "id": "64dc3b13b8b9504cec223ab1",
                  "login": "theo6789",
                  "name": "TheoCui"
                }
              }
            }
          },
          "schema": {
            "properties": {
              "avatar_url": {
                "type": "null"
              },
              "id": {
                "type": "integer"
              },
              "name": {
                "type": "string"
              },
              "path": {
                "type": "string"
              },
              "url": {
                "type": "string"
              },
              "user": {
                "properties": {
                  "avatar_url": {
                    "type": "null"
                  },
                  "html_url": {
                    "type": "string"
                  },
                  "id": {
                    "type": "string"
                  },
                  "login": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  },
                  "object_id": {
                    "type": "string"
                  },
                  "user_id": {
                    "type": "string"
                  }
                },
                "type": "object"
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
