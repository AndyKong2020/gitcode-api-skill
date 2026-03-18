# Get Issue Extended Configuration
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-orgs-org-issue-extend-settings](https://docs.gitcode.com/en/docs/apis/get-api-v-5-orgs-org-issue-extend-settings)
Category: Organizations
- Method: `GET`
- Path: `/api/v5/orgs/{org}/issue/extend/settings`
- Operation ID: `get_api_v5_orgs_{org}_issue_extend_settings`
- Tags: `Organizations`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| org | path | true | string | Repository space address (enterprise or organization path) |
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
  "items": {
    "properties": {
      "status": {
        "items": {
          "properties": {
            "gitcode_issue_status": {
              "type": "integer"
            },
            "status_desc": {
              "type": "string"
            },
            "status_id": {
              "type": "integer"
            },
            "status_name": {
              "type": "string"
            }
          },
          "type": "object"
        },
        "type": "array"
      },
      "type_desc": {
        "type": "string"
      },
      "type_id": {
        "type": "integer"
      },
      "type_name": {
        "type": "string"
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
      "status": [
        {
          "gitcode_issue_status": 0,
          "status_desc": "The requirement has not been formally submitted and is still in the conceptual or discussion phase, and has not entered the system management process.",
          "status_id": 11,
          "status_name": "Undelivered"
        },
        {
          "gitcode_issue_status": 0,
          "status_desc": "The solution to the requirement encountered issues during implementation and is currently being fixed.",
          "status_id": 20,
          "status_name": "Repairing"
        }
      ],
      "type_desc": "Define and describe new features or improvements to be implemented in the product or project.",
      "type_id": 4,
      "type_name": "requirement"
    }
  },
  "2": {
    "summary": "Successful Example",
    "value": {
      "status": [
        {
          "gitcode_issue_status": 0,
          "status_desc": "The requirement has not been formally submitted and is still in the conceptual or discussion phase, and has not entered the system management process.",
          "status_id": 11,
          "status_name": "Undelivered"
        },
        {
          "gitcode_issue_status": 1,
          "status_desc": "All related work for the requirement has been completed, deliverables have been handed over, and it has entered the archival status.",
          "status_id": 14,
          "status_name": "Completed"
        }
      ],
      "type_desc": "",
      "type_id": 36138,
      "type_name": "consultation"
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
  "operationId": "get_api_v5_orgs_{org}_issue_extend_settings",
  "parameters": [
    {
      "description": "Repository space address (enterprise or organization path)",
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
  "path": "/api/v5/orgs/{org}/issue/extend/settings",
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
    "name": "Get Issue Extended Configuration",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "orgs",
        ":org",
        "issue",
        "extend",
        "settings"
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
            "content": "(Required) Repository space address (enterprise or organization path)",
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
                "status": [
                  {
                    "gitcode_issue_status": 0,
                    "status_desc": "The requirement has not been formally submitted and is still in the conceptual or discussion phase, and has not entered the system management process.",
                    "status_id": 11,
                    "status_name": "Undelivered"
                  },
                  {
                    "gitcode_issue_status": 0,
                    "status_desc": "The solution to the requirement encountered issues during implementation and is currently being fixed.",
                    "status_id": 20,
                    "status_name": "Repairing"
                  }
                ],
                "type_desc": "Define and describe new features or improvements to be implemented in the product or project.",
                "type_id": 4,
                "type_name": "requirement"
              }
            },
            "2": {
              "summary": "Successful Example",
              "value": {
                "status": [
                  {
                    "gitcode_issue_status": 0,
                    "status_desc": "The requirement has not been formally submitted and is still in the conceptual or discussion phase, and has not entered the system management process.",
                    "status_id": 11,
                    "status_name": "Undelivered"
                  },
                  {
                    "gitcode_issue_status": 1,
                    "status_desc": "All related work for the requirement has been completed, deliverables have been handed over, and it has entered the archival status.",
                    "status_id": 14,
                    "status_name": "Completed"
                  }
                ],
                "type_desc": "",
                "type_id": 36138,
                "type_name": "consultation"
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "status": {
                  "items": {
                    "properties": {
                      "gitcode_issue_status": {
                        "type": "integer"
                      },
                      "status_desc": {
                        "type": "string"
                      },
                      "status_id": {
                        "type": "integer"
                      },
                      "status_name": {
                        "type": "string"
                      }
                    },
                    "type": "object"
                  },
                  "type": "array"
                },
                "type_desc": {
                  "type": "string"
                },
                "type_id": {
                  "type": "integer"
                },
                "type_name": {
                  "type": "string"
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
