# Get the list of kanban contents
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-org-owner-kanban-kanban-id-item-list](https://docs.gitcode.com/en/docs/apis/get-api-v-5-org-owner-kanban-kanban-id-item-list)
Category: Dashboard
- Method: `GET`
- Path: `/api/v5/org/{owner}/kanban/{kanban_id}/item_list`
- Operation ID: `get_api_v5_org_{owner}_kanban_{kanban_id}_item_list`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Organization's path |
| kanban_id | path | true | string | kanban_id |
| access_token | query | false | string | User authorization code |
| repo | query | false | string | Repository path |
| source_type | query | false | string | Source type: issue/merge_request |
| source_status | query | false | string | Source state: opened/closed/merged |
| title | query | false | string | Title |
| source_iids | query | false | string | Use the iid parameter to query pr or issue, and the repo parameter must be filled in when using this parameter, otherwise it will not take effect. |
| page | query | false | string | Pagination parameters, page number |
| per_page | query | false | string | Page parameters, number of entries per page |
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
      "assignees": {
        "items": {
          "properties": {
            "avatar_url": {
              "type": "string"
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
            "url": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "login",
            "name",
            "avatar_url",
            "html_url",
            "url"
          ],
          "type": "object"
        },
        "type": "array"
      },
      "html_url": {
        "type": "string"
      },
      "id": {
        "type": "integer"
      },
      "labels": {
        "items": {
          "properties": {
            "color": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "name",
            "color"
          ],
          "type": "object"
        },
        "type": "array"
      },
      "linked_pull_requests": {
        "items": {
          "properties": {
            "html_url": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "number": {
              "type": "integer"
            },
            "repo": {
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
                "name": {
                  "type": "string"
                },
                "url": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "full_name",
                "human_name",
                "url",
                "name"
              ],
              "type": "object"
            },
            "state": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "type": "object"
        },
        "type": "array"
      },
      "milestone_resp": {
        "properties": {
          "html_url": {
            "type": "string"
          },
          "id": {
            "type": "integer"
          },
          "title": {
            "type": "string"
          },
          "url": {
            "type": "string"
          }
        },
        "required": [
          "html_url",
          "id",
          "title",
          "url"
        ],
        "type": "object"
      },
      "number": {
        "type": "integer"
      },
      "repo": {
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
          "name": {
            "type": "string"
          },
          "url": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "full_name",
          "human_name",
          "url",
          "name"
        ],
        "type": "object"
      },
      "reviewers": {
        "items": {
          "properties": {
            "avatar_url": {
              "type": "string"
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
            "url": {
              "type": "string"
            }
          },
          "type": "object"
        },
        "type": "array"
      },
      "source_type": {
        "type": "string"
      },
      "status": {
        "type": "string"
      },
      "title": {
        "type": "string"
      },
      "url": {
        "type": "string"
      },
      "values": {
        "items": {
          "properties": {
            "field_name": {
              "type": "string"
            },
            "field_type": {
              "type": "string"
            },
            "value": {
              "properties": {
                "color": {
                  "type": "string"
                },
                "description": {
                  "type": "string"
                },
                "position": {
                  "type": "integer"
                },
                "value": {
                  "type": "string"
                }
              },
              "required": [
                "color",
                "value",
                "position"
              ],
              "type": "object"
            }
          },
          "required": [
            "field_name",
            "field_type",
            "value"
          ],
          "type": "object"
        },
        "type": "array"
      }
    },
    "required": [
      "id",
      "number",
      "title",
      "source_type",
      "status",
      "html_url",
      "url",
      "repo",
      "labels",
      "values",
      "assignees"
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
  "operationId": "get_api_v5_org_{owner}_kanban_{kanban_id}_item_list",
  "parameters": [
    {
      "description": "Organization's path",
      "example": "",
      "in": "path",
      "name": "owner",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "kanban_id",
      "example": "",
      "in": "path",
      "name": "kanban_id",
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
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Repository path",
      "in": "query",
      "name": "repo",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Source type: issue/merge_request",
      "in": "query",
      "name": "source_type",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Source state: opened/closed/merged",
      "in": "query",
      "name": "source_status",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Title",
      "in": "query",
      "name": "title",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Use the iid parameter to query pr or issue, and the repo parameter must be filled in when using this parameter, otherwise it will not take effect.",
      "in": "query",
      "name": "source_iids",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Pagination parameters, page number",
      "in": "query",
      "name": "page",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Page parameters, number of entries per page",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/org/{owner}/kanban/{kanban_id}/item_list",
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
    "name": "Get the list of kanban contents",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "org",
        ":owner",
        "kanban",
        ":kanban_id",
        "item_list"
      ],
      "query": [
        {
          "description": {
            "content": "User authorization code",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "access_token",
          "value": ""
        },
        {
          "description": {
            "content": "Repository path",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "repo",
          "value": ""
        },
        {
          "description": {
            "content": "Source type: issue/merge_request",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "source_type",
          "value": ""
        },
        {
          "description": {
            "content": "Source state: opened/closed/merged",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "source_status",
          "value": ""
        },
        {
          "description": {
            "content": "Title",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "title",
          "value": ""
        },
        {
          "description": {
            "content": "Use the iid parameter to query pr or issue, and the repo parameter must be filled in when using this parameter, otherwise it will not take effect.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "source_iids",
          "value": ""
        },
        {
          "description": {
            "content": "Pagination parameters, page number",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "page",
          "value": ""
        },
        {
          "description": {
            "content": "Page parameters, number of entries per page",
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
            "content": "(Required) Organization's path",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "owner",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) kanban_id",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "kanban_id",
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
                "assignees": {
                  "items": {
                    "properties": {
                      "avatar_url": {
                        "type": "string"
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
                      "url": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "id",
                      "login",
                      "name",
                      "avatar_url",
                      "html_url",
                      "url"
                    ],
                    "type": "object"
                  },
                  "type": "array"
                },
                "html_url": {
                  "type": "string"
                },
                "id": {
                  "type": "integer"
                },
                "labels": {
                  "items": {
                    "properties": {
                      "color": {
                        "type": "string"
                      },
                      "id": {
                        "type": "integer"
                      },
                      "name": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "id",
                      "name",
                      "color"
                    ],
                    "type": "object"
                  },
                  "type": "array"
                },
                "linked_pull_requests": {
                  "items": {
                    "properties": {
                      "html_url": {
                        "type": "string"
                      },
                      "id": {
                        "type": "integer"
                      },
                      "number": {
                        "type": "integer"
                      },
                      "repo": {
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
                          "name": {
                            "type": "string"
                          },
                          "url": {
                            "type": "string"
                          }
                        },
                        "required": [
                          "id",
                          "full_name",
                          "human_name",
                          "url",
                          "name"
                        ],
                        "type": "object"
                      },
                      "state": {
                        "type": "string"
                      },
                      "url": {
                        "type": "string"
                      }
                    },
                    "type": "object"
                  },
                  "type": "array"
                },
                "milestone_resp": {
                  "properties": {
                    "html_url": {
                      "type": "string"
                    },
                    "id": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    },
                    "url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "html_url",
                    "id",
                    "title",
                    "url"
                  ],
                  "type": "object"
                },
                "number": {
                  "type": "integer"
                },
                "repo": {
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
                    "name": {
                      "type": "string"
                    },
                    "url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "full_name",
                    "human_name",
                    "url",
                    "name"
                  ],
                  "type": "object"
                },
                "reviewers": {
                  "items": {
                    "properties": {
                      "avatar_url": {
                        "type": "string"
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
                      "url": {
                        "type": "string"
                      }
                    },
                    "type": "object"
                  },
                  "type": "array"
                },
                "source_type": {
                  "type": "string"
                },
                "status": {
                  "type": "string"
                },
                "title": {
                  "type": "string"
                },
                "url": {
                  "type": "string"
                },
                "values": {
                  "items": {
                    "properties": {
                      "field_name": {
                        "type": "string"
                      },
                      "field_type": {
                        "type": "string"
                      },
                      "value": {
                        "properties": {
                          "color": {
                            "type": "string"
                          },
                          "description": {
                            "type": "string"
                          },
                          "position": {
                            "type": "integer"
                          },
                          "value": {
                            "type": "string"
                          }
                        },
                        "required": [
                          "color",
                          "value",
                          "position"
                        ],
                        "type": "object"
                      }
                    },
                    "required": [
                      "field_name",
                      "field_type",
                      "value"
                    ],
                    "type": "object"
                  },
                  "type": "array"
                }
              },
              "required": [
                "id",
                "number",
                "title",
                "source_type",
                "status",
                "html_url",
                "url",
                "repo",
                "labels",
                "values",
                "assignees"
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
