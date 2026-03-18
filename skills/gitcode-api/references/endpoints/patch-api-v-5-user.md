# Update Profile of Authorized User
Source: [https://docs.gitcode.com/en/docs/apis/patch-api-v-5-user](https://docs.gitcode.com/en/docs/apis/patch-api-v-5-user)
Category: Users
- Method: `PATCH`
- Path: `/api/v5/user`
- Operation ID: `patch_api_v5_user`
- Tags: `Users`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| access_token | query | true | string | User authorization code |
| Content-Type | header | false | string |  |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "avatar": {
      "description": "avatar",
      "type": "string"
    },
    "company": {
      "description": "company",
      "type": "string"
    },
    "description": {
      "description": "User biography",
      "type": "string"
    },
    "email": {
      "description": "Personal email (requires verification)",
      "type": "string"
    },
    "github_account": {
      "description": "GitHub account",
      "type": "string"
    },
    "location": {
      "description": "Location",
      "type": "string"
    },
    "nickname": {
      "description": "User nickname",
      "type": "string"
    },
    "website": {
      "description": "personal website",
      "type": "string"
    }
  },
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
    "avatar": {
      "type": "string"
    },
    "company": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "email": {
      "type": "string"
    },
    "github_account": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "location": {
      "type": "string"
    },
    "login": {
      "type": "string"
    },
    "nickname": {
      "type": "string"
    },
    "website": {
      "type": "string"
    }
  },
  "required": [
    "avatar",
    "nickname",
    "company",
    "description",
    "email",
    "github_account",
    "website",
    "location",
    "id",
    "login"
  ],
  "type": "object"
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "avatar": "https://avatars.githubusercontent.com/u/28579840",
      "company": "velit fugiat et labore qui",
      "description": "abcabcabc",
      "email": "",
      "github_account": "esse elit officia fugiat ad",
      "id": "6638af02bbeee41d0fe74c35",
      "location": "in magna laboris Excepteur",
      "login": "malongge5",
      "nickname": "Yu Yu",
      "website": "incididunt enim est"
    }
  }
}
```
## JSON Request Example
```json
{
  "avatar": "string",
  "company": "string",
  "description": "string",
  "email": "string",
  "github_account": "string",
  "location": "string",
  "nickname": "string",
  "website": "string"
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
    "avatar": "string",
    "company": "string",
    "description": "string",
    "email": "string",
    "github_account": "string",
    "location": "string",
    "nickname": "string",
    "website": "string"
  },
  "method": "patch",
  "operationId": "patch_api_v5_user",
  "parameters": [
    {
      "description": "User authorization code",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "",
      "example": "application/json",
      "in": "header",
      "name": "Content-Type",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/user",
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
    "name": "Update Profile of Authorized User",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "user"
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
      "variable": []
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "avatar": {
              "description": "avatar",
              "type": "string"
            },
            "company": {
              "description": "company",
              "type": "string"
            },
            "description": {
              "description": "User biography",
              "type": "string"
            },
            "email": {
              "description": "Personal email (requires verification)",
              "type": "string"
            },
            "github_account": {
              "description": "GitHub account",
              "type": "string"
            },
            "location": {
              "description": "Location",
              "type": "string"
            },
            "nickname": {
              "description": "User nickname",
              "type": "string"
            },
            "website": {
              "description": "personal website",
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
                "avatar": "https://avatars.githubusercontent.com/u/28579840",
                "company": "velit fugiat et labore qui",
                "description": "abcabcabc",
                "email": "",
                "github_account": "esse elit officia fugiat ad",
                "id": "6638af02bbeee41d0fe74c35",
                "location": "in magna laboris Excepteur",
                "login": "malongge5",
                "nickname": "Yu Yu",
                "website": "incididunt enim est"
              }
            }
          },
          "schema": {
            "properties": {
              "avatar": {
                "type": "string"
              },
              "company": {
                "type": "string"
              },
              "description": {
                "type": "string"
              },
              "email": {
                "type": "string"
              },
              "github_account": {
                "type": "string"
              },
              "id": {
                "type": "string"
              },
              "location": {
                "type": "string"
              },
              "login": {
                "type": "string"
              },
              "nickname": {
                "type": "string"
              },
              "website": {
                "type": "string"
              }
            },
            "required": [
              "avatar",
              "nickname",
              "company",
              "description",
              "email",
              "github_account",
              "website",
              "location",
              "id",
              "login"
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
    "Users"
  ]
}
```
