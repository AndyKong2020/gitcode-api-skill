# Get Organization Information
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-orgs-org](https://docs.gitcode.com/en/docs/apis/get-api-v-5-orgs-org)
Category: Organizations
- Method: `GET`
- Path: `/api/v5/orgs/{org}`
- Operation ID: `get_api_v5_orgs_{org}`
- Tags: `Organizations`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| org | path | true | string | Organization's path (path/login) |
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
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "enterprise": {
      "type": "string"
    },
    "events_url": {
      "type": "string"
    },
    "follow_count": {
      "type": "integer"
    },
    "gitee": {
      "properties": {
        "follows": {
          "type": "integer"
        }
      },
      "type": "object"
    },
    "id": {
      "type": "integer"
    },
    "login": {
      "type": "string"
    },
    "members_url": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "repos_url": {
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
      "avatar_url": "",
      "description": "OpenHarmony is an open-source project incubated and operated by the OpenAtom Open Source Foundation. Its aim is to build an operating system framework and platform for the era of full-scenario, full-connectivity, and full-intelligence, promoting the prosperity and development of the everything-connected industry.",
      "enterprise": "openharmony",
      "events_url": "https://api.gitcode.com/openharmony/events",
      "follow_count": 40819,
      "gitee": {
        "follows": 43454
      },
      "id": 6486504,
      "login": "openharmony",
      "members_url": "https://api.gitcode.com/openharmony/members{/member}",
      "name": "OpenHarmony",
      "repos_url": "https://api.gitcode.com/openharmony/repos"
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
  "operationId": "get_api_v5_orgs_{org}",
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
    "name": "Get Organization Information",
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
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": {
                "avatar_url": "",
                "description": "OpenHarmony is an open-source project incubated and operated by the OpenAtom Open Source Foundation. Its aim is to build an operating system framework and platform for the era of full-scenario, full-connectivity, and full-intelligence, promoting the prosperity and development of the everything-connected industry.",
                "enterprise": "openharmony",
                "events_url": "https://api.gitcode.com/openharmony/events",
                "follow_count": 40819,
                "gitee": {
                  "follows": 43454
                },
                "id": 6486504,
                "login": "openharmony",
                "members_url": "https://api.gitcode.com/openharmony/members{/member}",
                "name": "OpenHarmony",
                "repos_url": "https://api.gitcode.com/openharmony/repos"
              }
            }
          },
          "schema": {
            "properties": {
              "avatar_url": {
                "type": "string"
              },
              "description": {
                "type": "string"
              },
              "enterprise": {
                "type": "string"
              },
              "events_url": {
                "type": "string"
              },
              "follow_count": {
                "type": "integer"
              },
              "gitee": {
                "properties": {
                  "follows": {
                    "type": "integer"
                  }
                },
                "type": "object"
              },
              "id": {
                "type": "integer"
              },
              "login": {
                "type": "string"
              },
              "members_url": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "repos_url": {
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
