# Get or Refresh Authorization Token Interface
Source: [https://docs.gitcode.com/en/docs/apis/post-oauth-token-grant-type-authorization-code-code-code-client-id-client-id-client-secret-client-secret](https://docs.gitcode.com/en/docs/apis/post-oauth-token-grant-type-authorization-code-code-code-client-id-client-id-client-secret-client-secret)
Category: Oauth2.0
- Method: `POST`
- Path: `/oauth/token`
- Operation ID: `post_oauth_token?grant_type=authorization_code&code={code}&client_id={client_id}&client_secret={client_secret}`
- Tags: `Oauth2.0`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| grant_type | query | true | string | Authorization Code Mode |
| code | query | false | string | Authorization code |
| client_id | query | false | string | Registered client ID |
| client_secret | query | false | string | Registered client key |
| refresh_token | query | false | string | Refresh token, required only when grant_type is refresh_token. |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "client_secret": {
      "description": "Registered client key",
      "type": "string"
    }
  },
  "required": [
    "client_secret"
  ],
  "type": "object"
}
```
Example:
```json
{
  "client_secret": "string"
}
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
    "access_token": {
      "type": "string"
    },
    "created_at": {
      "type": "string"
    },
    "expires_in": {
      "type": "integer"
    },
    "refresh_token": {
      "type": "string"
    },
    "scope": {
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
      "access_token": "eyPZPVNfsibj9tap_ibj3t3p",
      "created_at": "2024-04-20T09:07:59.889Z",
      "expires_in": 1296000,
      "refresh_token": "b77ced3aee884348852160deab3697a1",
      "scope": "all_user all_key all_groups all_projects all_pr all_issue all_note all_hook all_repository"
    }
  }
}
```
## JSON Request Example
```json
{
  "client_secret": "string"
}
```
## Raw OpenAPI Operation
```json
{
  "deprecated": false,
  "description": "## Basic Information\n- Request Path: `/oauth/token`\n- Request Method: POST\n- Interface Description: A unified interface for obtaining or refreshing the access token (access_token)\n\n## Request Parameters\n\n### Query Parameters\n\n| Parameter Name | Required | Type | Description |\n|----------------|----------|------|-------------|\n| grant_type | Yes | string | Authorization type. Possible values:<br/>- `authorization_code`: Authorization code mode, used to obtain a new token<br/>- `refresh_token`: Refresh token mode, used to refresh an existing token |\n| code | Conditional Required | string | Authorization code. Required when grant_type=authorization_code |\n| client_id | Conditional Required | string | Registered client ID. Required when grant_type=authorization_code |\n| refresh_token | Conditional Required | string | Refresh token. Required when grant_type=refresh_token |\n\n### Body Parameters\n\n| Parameter Name | Required | Type | Description |\n|----------------|----------|------|-------------|\n| client_secret | Conditional Required | string | Registered client secret. Required when grant_type=authorization_code |\n\n## Usage Scenarios\n\n1. **Obtain a New Access Token**\n   - Set grant_type=authorization_code\n   - Provide code, client_id, and client_secret\n   \n2. **Refresh an Access Token**\n   - Set grant_type=refresh_token\n   - Provide refresh_token\n\n## Examples\n\n### Obtain a New Token\n```\nPOST /oauth/token?grant_type=authorization_code&code={code}&client_id={client_id}\nContent-Type: application/json\n\n{\n    \"client_secret\": \"{client_secret}\"\n}\n```\n\n### Refresh a Token\n```\nPOST /oauth/token?grant_type=refresh_token&refresh_token={refresh_token}\n```",
  "info": {
    "description": "",
    "title": "GicodeOpenAPI",
    "version": "1.0.0"
  },
  "jsonRequestBodyExample": {
    "client_secret": "string"
  },
  "method": "post",
  "operationId": "post_oauth_token?grant_type=authorization_code&code={code}&client_id={client_id}&client_secret={client_secret}",
  "parameters": [
    {
      "description": "Authorization Code Mode",
      "example": "",
      "in": "query",
      "name": "grant_type",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Authorization code",
      "example": "",
      "in": "query",
      "name": "code",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Registered client ID",
      "example": "",
      "in": "query",
      "name": "client_id",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Registered client key",
      "example": "",
      "in": "query",
      "name": "client_secret",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Refresh token, required only when grant_type is refresh_token.",
      "example": "",
      "in": "query",
      "name": "refresh_token",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/oauth/token",
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
      "content": "## Basic Information\n- Request Path: `/oauth/token`\n- Request Method: POST\n- Interface Description: A unified interface for obtaining or refreshing the access token (access_token)\n\n## Request Parameters\n\n### Query Parameters\n\n| Parameter Name | Required | Type | Description |\n|----------------|----------|------|-------------|\n| grant_type | Yes | string | Authorization type. Possible values:<br/>- `authorization_code`: Authorization code mode, used to obtain a new token<br/>- `refresh_token`: Refresh token mode, used to refresh an existing token |\n| code | Conditional Required | string | Authorization code. Required when grant_type=authorization_code |\n| client_id | Conditional Required | string | Registered client ID. Required when grant_type=authorization_code |\n| refresh_token | Conditional Required | string | Refresh token. Required when grant_type=refresh_token |\n\n### Body Parameters\n\n| Parameter Name | Required | Type | Description |\n|----------------|----------|------|-------------|\n| client_secret | Conditional Required | string | Registered client secret. Required when grant_type=authorization_code |\n\n## Usage Scenarios\n\n1. **Obtain a New Access Token**\n   - Set grant_type=authorization_code\n   - Provide code, client_id, and client_secret\n   \n2. **Refresh an Access Token**\n   - Set grant_type=refresh_token\n   - Provide refresh_token\n\n## Examples\n\n### Obtain a New Token\n```\nPOST /oauth/token?grant_type=authorization_code&code={code}&client_id={client_id}\nContent-Type: application/json\n\n{\n    \"client_secret\": \"{client_secret}\"\n}\n```\n\n### Refresh a Token\n```\nPOST /oauth/token?grant_type=refresh_token&refresh_token={refresh_token}\n```",
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
    "name": "Get or Refresh Authorization Token Interface",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "oauth",
        "token"
      ],
      "query": [
        {
          "description": {
            "content": "(Required) Authorization Code Mode",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "grant_type",
          "value": ""
        },
        {
          "description": {
            "content": "Authorization code",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "code",
          "value": ""
        },
        {
          "description": {
            "content": "Registered client ID",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "client_id",
          "value": ""
        },
        {
          "description": {
            "content": "Registered client key",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "client_secret",
          "value": ""
        },
        {
          "description": {
            "content": "Refresh token, required only when grant_type is refresh_token.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "refresh_token",
          "value": ""
        }
      ],
      "variable": []
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "example": {
          "client_secret": "string"
        },
        "schema": {
          "properties": {
            "client_secret": {
              "description": "Registered client key",
              "type": "string"
            }
          },
          "required": [
            "client_secret"
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
                "access_token": "eyPZPVNfsibj9tap_ibj3t3p",
                "created_at": "2024-04-20T09:07:59.889Z",
                "expires_in": 1296000,
                "refresh_token": "b77ced3aee884348852160deab3697a1",
                "scope": "all_user all_key all_groups all_projects all_pr all_issue all_note all_hook all_repository"
              }
            }
          },
          "schema": {
            "properties": {
              "access_token": {
                "type": "string"
              },
              "created_at": {
                "type": "string"
              },
              "expires_in": {
                "type": "integer"
              },
              "refresh_token": {
                "type": "string"
              },
              "scope": {
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
      "url": "https://gitcode.com"
    }
  ],
  "tags": [
    "Oauth2.0"
  ]
}
```
