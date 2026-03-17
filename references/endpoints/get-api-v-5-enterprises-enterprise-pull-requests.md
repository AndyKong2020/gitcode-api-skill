# Enterprise Pull Request List
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-enterprises-enterprise-pull-requests](https://docs.gitcode.com/en/docs/apis/get-api-v-5-enterprises-enterprise-pull-requests)
Category: Pull Requests
- Method: `GET`
- Path: `/api/v5/enterprises/{enterprise}/pull_requests`
- Operation ID: `get_api_v5_enterprises_{enterprise}_pull_requests`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| enterprise | path | true | string | The path of the enterprise (path/login) |
| access_token | query | true | string | User authorization code |
| state | query | false | string | Pull Request status, all, all, open: open, closed: closed, merged: merged |
| issue_number | query | false | integer | issue global ID |
| sort | query | false | string | None   Sort field, creation time: created, update time: updated. Default by creation time |
| direction | query | false | string | Ascending: asc, Descending: desc |
| page | query | false | integer | Current page number: defaults to 1 |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
| base | query | false | string | Target branch |
| author | query | false | string | Pull Request Author |
| search | query | false | string | Search by title and description with fuzzy query |
| created_after | query | false | string | Create merge requests created after the specified time, time format is ISO 8601 for example: 2024-11-20T13:00:21+08:00 |
| created_before | query | false | string | Merge requests created before the specified time, time format is ISO 8601 for example: 2024-11-20T13:00:21+08:00 |
| updated_before | query | false | string | Merge requests updated before the specified time, time format is ISO 8601, for example: 2024-11-20T13:00:21+08:00 |
| updated_after | query | false | string | Merge requests updated after the specified time, time format is ISO 8601 for example: 2024-11-20T13:00:21+08:00 |
| labels | query | false | string | Filter by the specified label name, multiple ones separated by English commas |
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
      "assignees": {
        "items": {
          "type": "string"
        },
        "type": "array"
      },
      "assignees_number": {
        "type": "integer"
      },
      "base": {
        "properties": {
          "ref": {
            "type": "string"
          },
          "repo": {
            "properties": {
              "namespace": {
                "properties": {
                  "path": {
                    "type": "string"
                  }
                },
                "required": [
                  "path"
                ],
                "type": "object"
              },
              "path": {
                "type": "string"
              }
            },
            "required": [
              "path",
              "namespace"
            ],
            "type": "object"
          },
          "sha": {
            "type": "string"
          }
        },
        "required": [
          "ref",
          "sha",
          "repo"
        ],
        "type": "object"
      },
      "created_at": {
        "type": "string"
      },
      "head": {
        "properties": {
          "ref": {
            "type": "string"
          },
          "repo": {
            "properties": {
              "assigner": {
                "properties": {
                  "id": {
                    "type": "string"
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
                "type": "object"
              },
              "namespace": {
                "properties": {
                  "path": {
                    "type": "string"
                  }
                },
                "required": [
                  "path"
                ],
                "type": "object"
              },
              "path": {
                "type": "string"
              }
            },
            "required": [
              "path",
              "namespace",
              "assigner"
            ],
            "type": "object"
          },
          "sha": {
            "type": "string"
          }
        },
        "required": [
          "ref",
          "sha",
          "repo"
        ],
        "type": "object"
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
            "created_at": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "updated_at": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "name",
            "color",
            "created_at",
            "updated_at"
          ],
          "type": "object"
        },
        "type": "array"
      },
      "merged_at": {
        "type": "string"
      },
      "merged_by": {
        "description": "Merged Person",
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
          }
        },
        "required": [
          "id",
          "login",
          "name",
          "avatar_url",
          "html_url"
        ],
        "type": "object"
      },
      "number": {
        "type": "integer"
      },
      "state": {
        "type": "string"
      },
      "testers_number": {
        "type": "integer"
      },
      "title": {
        "type": "string"
      },
      "updated_at": {
        "type": "string"
      },
      "url": {
        "type": "string"
      },
      "visibility_reason": {
        "description": "Visibility, public: Publicly visible, other: Visible to project members only",
        "type": "string"
      }
    },
    "required": [
      "id",
      "title",
      "url",
      "html_url",
      "number",
      "state",
      "assignees_number",
      "testers_number",
      "assignees",
      "head",
      "base",
      "created_at",
      "updated_at",
      "labels",
      "merged_at"
    ],
    "type": "object"
  },
  "type": "array"
}
```
Example:
```json
{
  "assignees": [],
  "assignees_number": 0,
  "base": {
    "ref": null,
    "repo": {
      "name_space": {
        "path": "repo-dev"
      },
      "path": "test"
    },
    "sha": null
  },
  "can_merge_check": true,
  "head": {
    "ref": "main",
    "repo": {
      "assigner": {
        "id": "uuid",
        "login": "Lzm_0916",
        "name": "Lzm_0916"
      },
      "name_space": {
        "path": "repo-dev"
      },
      "path": "test"
    },
    "sha": "d874402d259744a00121c2cff0febc8554339aef"
  },
  "html_url": "https://test.gitcode.net/test/test/1",
  "id": 71020,
  "mergeable": null,
  "milestone": {
    "created_at": "2024-04-15T18:33:01+08:00",
    "description": "1",
    "due_on": "2024-04-29",
    "number": 73008,
    "repository_id": 249609,
    "state": "active",
    "title": "the second milestone",
    "updated_at": "2024-04-15T18:33:01+08:00",
    "url": "https://test.gitcode.net/xiaogang_test/test222/milestones/2"
  },
  "number": 1,
  "state": "merged",
  "testers": [],
  "testers_number": 0,
  "url": "https://test.gitcode.net/api/v5/repos/test/test/1"
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
  "operationId": "get_api_v5_enterprises_{enterprise}_pull_requests",
  "parameters": [
    {
      "description": "The path of the enterprise (path/login)",
      "example": "",
      "in": "path",
      "name": "enterprise",
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
      "description": "Pull Request status, all, all, open: open, closed: closed, merged: merged",
      "in": "query",
      "name": "state",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "issue global ID",
      "in": "query",
      "name": "issue_number",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "None  \nSort field, creation time: created, update time: updated. Default by creation time",
      "in": "query",
      "name": "sort",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Ascending: asc, Descending: desc",
      "in": "query",
      "name": "direction",
      "required": false,
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
        "type": "integer"
      }
    },
    {
      "description": "The number of items per page, with a maximum of 100. The default is 20.",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "Target branch",
      "in": "query",
      "name": "base",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Pull Request Author",
      "in": "query",
      "name": "author",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Search by title and description with fuzzy query",
      "in": "query",
      "name": "search",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Create merge requests created after the specified time, time format is ISO 8601 for example: 2024-11-20T13:00:21+08:00",
      "in": "query",
      "name": "created_after",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Merge requests created before the specified time, time format is ISO 8601 for example: 2024-11-20T13:00:21+08:00",
      "in": "query",
      "name": "created_before",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Merge requests updated before the specified time, time format is ISO 8601, for example: 2024-11-20T13:00:21+08:00",
      "in": "query",
      "name": "updated_before",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Merge requests updated after the specified time, time format is ISO 8601 for example: 2024-11-20T13:00:21+08:00",
      "in": "query",
      "name": "updated_after",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Filter by the specified label name, multiple ones separated by English commas",
      "in": "query",
      "name": "labels",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/enterprises/{enterprise}/pull_requests",
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
    "name": "Enterprise Pull Request List",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "enterprises",
        ":enterprise",
        "pull_requests"
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
            "content": "Pull Request status, all, all, open: open, closed: closed, merged: merged",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "state",
          "value": ""
        },
        {
          "description": {
            "content": "issue global ID",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "issue_number",
          "value": ""
        },
        {
          "description": {
            "content": "None  \nSort field, creation time: created, update time: updated. Default by creation time",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sort",
          "value": ""
        },
        {
          "description": {
            "content": "Ascending: asc, Descending: desc",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "direction",
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
            "content": "The number of items per page, with a maximum of 100. The default is 20.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "per_page",
          "value": ""
        },
        {
          "description": {
            "content": "Target branch",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "base",
          "value": ""
        },
        {
          "description": {
            "content": "Pull Request Author",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "author",
          "value": ""
        },
        {
          "description": {
            "content": "Search by title and description with fuzzy query",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "search",
          "value": ""
        },
        {
          "description": {
            "content": "Create merge requests created after the specified time, time format is ISO 8601 for example: 2024-11-20T13:00:21+08:00",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "created_after",
          "value": ""
        },
        {
          "description": {
            "content": "Merge requests created before the specified time, time format is ISO 8601 for example: 2024-11-20T13:00:21+08:00",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "created_before",
          "value": ""
        },
        {
          "description": {
            "content": "Merge requests updated before the specified time, time format is ISO 8601, for example: 2024-11-20T13:00:21+08:00",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "updated_before",
          "value": ""
        },
        {
          "description": {
            "content": "Merge requests updated after the specified time, time format is ISO 8601 for example: 2024-11-20T13:00:21+08:00",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "updated_after",
          "value": ""
        },
        {
          "description": {
            "content": "Filter by the specified label name, multiple ones separated by English commas",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "labels",
          "value": ""
        }
      ],
      "variable": [
        {
          "description": {
            "content": "(Required) The path of the enterprise (path/login)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "enterprise",
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
          "example": {
            "assignees": [],
            "assignees_number": 0,
            "base": {
              "ref": null,
              "repo": {
                "name_space": {
                  "path": "repo-dev"
                },
                "path": "test"
              },
              "sha": null
            },
            "can_merge_check": true,
            "head": {
              "ref": "main",
              "repo": {
                "assigner": {
                  "id": "uuid",
                  "login": "Lzm_0916",
                  "name": "Lzm_0916"
                },
                "name_space": {
                  "path": "repo-dev"
                },
                "path": "test"
              },
              "sha": "d874402d259744a00121c2cff0febc8554339aef"
            },
            "html_url": "https://test.gitcode.net/test/test/1",
            "id": 71020,
            "mergeable": null,
            "milestone": {
              "created_at": "2024-04-15T18:33:01+08:00",
              "description": "1",
              "due_on": "2024-04-29",
              "number": 73008,
              "repository_id": 249609,
              "state": "active",
              "title": "the second milestone",
              "updated_at": "2024-04-15T18:33:01+08:00",
              "url": "https://test.gitcode.net/xiaogang_test/test222/milestones/2"
            },
            "number": 1,
            "state": "merged",
            "testers": [],
            "testers_number": 0,
            "url": "https://test.gitcode.net/api/v5/repos/test/test/1"
          },
          "schema": {
            "items": {
              "properties": {
                "assignees": {
                  "items": {
                    "type": "string"
                  },
                  "type": "array"
                },
                "assignees_number": {
                  "type": "integer"
                },
                "base": {
                  "properties": {
                    "ref": {
                      "type": "string"
                    },
                    "repo": {
                      "properties": {
                        "namespace": {
                          "properties": {
                            "path": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "path"
                          ],
                          "type": "object"
                        },
                        "path": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "path",
                        "namespace"
                      ],
                      "type": "object"
                    },
                    "sha": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "ref",
                    "sha",
                    "repo"
                  ],
                  "type": "object"
                },
                "created_at": {
                  "type": "string"
                },
                "head": {
                  "properties": {
                    "ref": {
                      "type": "string"
                    },
                    "repo": {
                      "properties": {
                        "assigner": {
                          "properties": {
                            "id": {
                              "type": "string"
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
                          "type": "object"
                        },
                        "namespace": {
                          "properties": {
                            "path": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "path"
                          ],
                          "type": "object"
                        },
                        "path": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "path",
                        "namespace",
                        "assigner"
                      ],
                      "type": "object"
                    },
                    "sha": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "ref",
                    "sha",
                    "repo"
                  ],
                  "type": "object"
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
                      "created_at": {
                        "type": "string"
                      },
                      "id": {
                        "type": "integer"
                      },
                      "name": {
                        "type": "string"
                      },
                      "updated_at": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "id",
                      "name",
                      "color",
                      "created_at",
                      "updated_at"
                    ],
                    "type": "object"
                  },
                  "type": "array"
                },
                "merged_at": {
                  "type": "string"
                },
                "merged_by": {
                  "description": "Merged Person",
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
                    }
                  },
                  "required": [
                    "id",
                    "login",
                    "name",
                    "avatar_url",
                    "html_url"
                  ],
                  "type": "object"
                },
                "number": {
                  "type": "integer"
                },
                "state": {
                  "type": "string"
                },
                "testers_number": {
                  "type": "integer"
                },
                "title": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                },
                "url": {
                  "type": "string"
                },
                "visibility_reason": {
                  "description": "Visibility, public: Publicly visible, other: Visible to project members only",
                  "type": "string"
                }
              },
              "required": [
                "id",
                "title",
                "url",
                "html_url",
                "number",
                "state",
                "assignees_number",
                "testers_number",
                "assignees",
                "head",
                "base",
                "created_at",
                "updated_at",
                "labels",
                "merged_at"
              ],
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
    "Pull Requests"
  ]
}
```
