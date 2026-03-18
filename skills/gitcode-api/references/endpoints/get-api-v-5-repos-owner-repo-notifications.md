# List Notifications In A Repository
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-notifications](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-notifications)
Category: Users
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/notifications`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_notifications`
- Tags: `Users`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string |  |
| repo | path | true | string |  |
| access_token | query | true | string | User authorization code |
| unread | query | false | boolean | Whether unread, default true |
| type | query | false | string | Filter specified types of notifications, all: all, event: event notification, referer: @notification |
| since | query | false | string | Retrieve only the messages updated before the given time, with the time format required to be in ISO 8601. |
| before | query | false | string | Retrieve only the messages updated before the given time, with the time format required to be in ISO 8601. |
| ids | query | false | string | Specify a group of notification IDs, separated by commas. |
## Request Body
No request body.
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
    "list": {
      "items": {
        "properties": {
          "actor": {
            "properties": {
              "id": {
                "type": "integer"
              },
              "login": {
                "type": "string"
              },
              "name": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "login",
              "name"
            ],
            "title": "message_sender",
            "type": "object"
          },
          "content": {
            "title": "Notification content",
            "type": "string"
          },
          "html_url": {
            "title": "The resource access URL that triggered the message.",
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "repository": {
            "properties": {
              "full_name": {
                "type": "string"
              },
              "human_name": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "url": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "full_name",
              "human_name",
              "url"
            ],
            "title": "warehouse information",
            "type": "object"
          },
          "type": {
            "title": "notification type",
            "type": "string"
          },
          "unread": {
            "title": "unread",
            "type": "boolean"
          },
          "update_at": {
            "title": "Update time",
            "type": "string"
          }
        },
        "required": [
          "id",
          "content",
          "type",
          "unread",
          "update_at",
          "html_url",
          "actor",
          "repository"
        ],
        "type": "object"
      },
      "type": "array"
    }
  },
  "required": [
    "list"
  ],
  "type": "object"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_notifications",
  "parameters": [
    {
      "description": "",
      "example": "",
      "in": "path",
      "name": "owner",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "",
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
      "example": "",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Whether unread, default true",
      "example": "",
      "in": "query",
      "name": "unread",
      "required": false,
      "schema": {
        "type": "boolean"
      }
    },
    {
      "description": "Filter specified types of notifications, all: all, event: event notification, referer: @notification",
      "in": "query",
      "name": "type",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Retrieve only the messages updated before the given time, with the time format required to be in ISO 8601.",
      "example": "",
      "in": "query",
      "name": "since",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Retrieve only the messages updated before the given time, with the time format required to be in ISO 8601.",
      "in": "query",
      "name": "before",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Specify a group of notification IDs, separated by commas.",
      "in": "query",
      "name": "ids",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/notifications",
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
    "name": "List Notifications In A Repository",
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
        "notifications"
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
            "content": "Whether unread, default true",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "unread",
          "value": ""
        },
        {
          "description": {
            "content": "Filter specified types of notifications, all: all, event: event notification, referer: @notification",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "type",
          "value": ""
        },
        {
          "description": {
            "content": "Retrieve only the messages updated before the given time, with the time format required to be in ISO 8601.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "since",
          "value": ""
        },
        {
          "description": {
            "content": "Retrieve only the messages updated before the given time, with the time format required to be in ISO 8601.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "before",
          "value": ""
        },
        {
          "description": {
            "content": "Specify a group of notification IDs, separated by commas.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "ids",
          "value": ""
        }
      ],
      "variable": [
        {
          "description": {
            "content": "(Required) ",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "owner",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) ",
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
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "schema": {
            "properties": {
              "list": {
                "items": {
                  "properties": {
                    "actor": {
                      "properties": {
                        "id": {
                          "type": "integer"
                        },
                        "login": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "login",
                        "name"
                      ],
                      "title": "message_sender",
                      "type": "object"
                    },
                    "content": {
                      "title": "Notification content",
                      "type": "string"
                    },
                    "html_url": {
                      "title": "The resource access URL that triggered the message.",
                      "type": "string"
                    },
                    "id": {
                      "type": "string"
                    },
                    "repository": {
                      "properties": {
                        "full_name": {
                          "type": "string"
                        },
                        "human_name": {
                          "type": "string"
                        },
                        "id": {
                          "type": "integer"
                        },
                        "url": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "full_name",
                        "human_name",
                        "url"
                      ],
                      "title": "warehouse information",
                      "type": "object"
                    },
                    "type": {
                      "title": "notification type",
                      "type": "string"
                    },
                    "unread": {
                      "title": "unread",
                      "type": "boolean"
                    },
                    "update_at": {
                      "title": "Update time",
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "content",
                    "type",
                    "unread",
                    "update_at",
                    "html_url",
                    "actor",
                    "repository"
                  ],
                  "type": "object"
                },
                "type": "array"
              }
            },
            "required": [
              "list"
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
