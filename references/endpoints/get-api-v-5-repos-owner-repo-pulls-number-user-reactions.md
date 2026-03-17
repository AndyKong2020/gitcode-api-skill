# Get the list of reactions for a Pull Request
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-number-user-reactions](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-number-user-reactions)
Category: Pull Requests
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}/user_reactions`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_pulls_{number}_user_reactions`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| number | path | true | string | Pull Request Number (case-sensitive, no need to add # sign) |
| access_token | query | true | string | User authorization code |
| page | query | false | string | Current page number |
| per_page | query | false | string | Number of items per page |
| emoji_name | query | false | string | Emoji expressions, optional: like, dislike, smile, confused, love, rocket, eyes, party |
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
  "items": {
    "properties": {
      "emoji": {
        "title": "Emoji expressions",
        "type": "string"
      },
      "emoji_name": {
        "title": "Enumeration value of Emoji expressions",
        "type": "string"
      },
      "id": {
        "type": "string"
      },
      "user": {
        "properties": {
          "avatar_url": {
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
          }
        },
        "required": [
          "login",
          "name",
          "avatar_url",
          "object_id"
        ],
        "title": "User Information",
        "type": "object"
      }
    },
    "required": [
      "id",
      "emoji",
      "emoji_name",
      "user"
    ],
    "type": "object"
  },
  "type": "array"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_pulls_{number}_user_reactions",
  "parameters": [
    {
      "description": "Repository space address (address path of the enterprise, organization, or individual)",
      "in": "path",
      "name": "owner",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Repository path (path)",
      "in": "path",
      "name": "repo",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Pull Request Number (case-sensitive, no need to add # sign)",
      "in": "path",
      "name": "number",
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
      "description": "Current page number",
      "in": "query",
      "name": "page",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Number of items per page",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Emoji expressions, optional: like, dislike, smile, confused, love, rocket, eyes, party",
      "in": "query",
      "name": "emoji_name",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}/user_reactions",
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
    "name": "Get the list of reactions for a Pull Request",
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
        "pulls",
        ":number",
        "user_reactions"
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
            "content": "Current page number",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "page",
          "value": ""
        },
        {
          "description": {
            "content": "Number of items per page",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "per_page",
          "value": ""
        },
        {
          "description": {
            "content": "Emoji expressions, optional: like, dislike, smile, confused, love, rocket, eyes, party",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "emoji_name",
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
        },
        {
          "description": {
            "content": "(Required) Pull Request Number (case-sensitive, no need to add # sign)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "number",
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
            "items": {
              "properties": {
                "emoji": {
                  "title": "Emoji expressions",
                  "type": "string"
                },
                "emoji_name": {
                  "title": "Enumeration value of Emoji expressions",
                  "type": "string"
                },
                "id": {
                  "type": "string"
                },
                "user": {
                  "properties": {
                    "avatar_url": {
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
                    }
                  },
                  "required": [
                    "login",
                    "name",
                    "avatar_url",
                    "object_id"
                  ],
                  "title": "User Information",
                  "type": "object"
                }
              },
              "required": [
                "id",
                "emoji",
                "emoji_name",
                "user"
              ],
              "type": "object"
            },
            "type": "array"
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
