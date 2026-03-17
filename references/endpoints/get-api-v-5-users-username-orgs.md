# List Organizations the User Belongs To
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-users-username-orgs](https://docs.gitcode.com/en/docs/apis/get-api-v-5-users-username-orgs)
Category: Organizations
- Method: `GET`
- Path: `/api/v5/users/{username}/orgs`
- Operation ID: `get_api_v5_users_{username}_orgs`
- Tags: `Organizations`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| username | path | true | string | username (alias: login) |
| access_token | query | true | string | User authorization code |
| page | query | false | string | Current page number: defaults to 1 |
| per_page | query | false | string | The number of items per page, default is 20, with a maximum of 100. |
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
  "items": {
    "properties": {
      "avatar_url": {
        "type": "null"
      },
      "description": {
        "type": "string"
      },
      "events_url": {
        "type": "null"
      },
      "follow_count": {
        "type": "integer"
      },
      "id": {
        "type": "integer"
      },
      "login": {
        "type": "string"
      },
      "members_url": {
        "type": "null"
      },
      "name": {
        "type": "string"
      },
      "repos_url": {
        "type": "null"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "avatar_url": null,
      "description": "OpenHarmony is an open-source project incubated and operated by the OpenAtom Open Source Foundation. Its goal is to build an operating system framework and platform for the era of all-scenario, full-connectivity, and full-intelligence, promoting the prosperity and development of the万物互联industry.",
      "events_url": null,
      "follow_count": 3,
      "id": 133039,
      "login": "openharmony",
      "members_url": null,
      "name": "OpenHarmony",
      "repos_url": null
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
  "operationId": "get_api_v5_users_{username}_orgs",
  "parameters": [
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
    },
    {
      "description": "Current page number: defaults to 1",
      "in": "query",
      "name": "page",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "The number of items per page, default is 20, with a maximum of 100.",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/users/{username}/orgs",
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
    "name": "List Organizations the User Belongs To",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "users",
        ":username",
        "orgs"
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
        },
        {
          "description": {
            "content": "Current page number: defaults to 1",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "page",
          "value": ""
        },
        {
          "description": {
            "content": "The number of items per page, default is 20, with a maximum of 100.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "per_page",
          "value": ""
        }
      ],
      "variable": [
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
              "summary": "Successful Example",
              "value": {
                "avatar_url": null,
                "description": "OpenHarmony is an open-source project incubated and operated by the OpenAtom Open Source Foundation. Its goal is to build an operating system framework and platform for the era of all-scenario, full-connectivity, and full-intelligence, promoting the prosperity and development of the万物互联industry.",
                "events_url": null,
                "follow_count": 3,
                "id": 133039,
                "login": "openharmony",
                "members_url": null,
                "name": "OpenHarmony",
                "repos_url": null
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "avatar_url": {
                  "type": "null"
                },
                "description": {
                  "type": "string"
                },
                "events_url": {
                  "type": "null"
                },
                "follow_count": {
                  "type": "integer"
                },
                "id": {
                  "type": "integer"
                },
                "login": {
                  "type": "string"
                },
                "members_url": {
                  "type": "null"
                },
                "name": {
                  "type": "string"
                },
                "repos_url": {
                  "type": "null"
                }
              },
              "type": "object"
            },
            "type": "array"
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
