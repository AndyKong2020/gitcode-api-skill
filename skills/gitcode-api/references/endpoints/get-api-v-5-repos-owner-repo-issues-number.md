# Get a Specific Issue of a Repository
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-issues-number](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-issues-number)
Category: Issues
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/issues/{number}`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_issues_{number}`
- Tags: `Issues`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| number | path | true | string | Issue Number (case-sensitive, do not add #) |
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
    "body": {
      "type": "string"
    },
    "comments": {
      "type": "integer"
    },
    "created_at": {
      "type": "string"
    },
    "custom_fields": {
      "description": "Custom field information",
      "items": {
        "properties": {
          "field_name": {
            "description": "Custom Field Name",
            "type": "string"
          },
          "field_type": {
            "description": "Field type. text_single: single line text, text_multi: multi-line text, integer: integer, decimal: decimal, date: date, select_single: single select dropdown, select_multi: multi-select dropdown, member_single: single select member, member_multi: multi-select member",
            "type": "string"
          },
          "field_values": {
            "description": "Custom field value",
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "field_visibility": {
            "description": "Visibility. 0: Visible to administrators only, 1: Visible to everyone",
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "finished_at": {
      "type": "string"
    },
    "html_url": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "issue_priority_detail": {
      "description": "Issue Priority",
      "properties": {
        "id": {
          "type": "string"
        },
        "title": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "title"
      ],
      "type": "object"
    },
    "issue_state": {
      "type": "string"
    },
    "issue_state_detail": {
      "properties": {
        "id": {
          "type": "integer"
        },
        "serial": {
          "type": "integer"
        },
        "title": {
          "type": "string"
        }
      },
      "required": [
        "title",
        "serial",
        "id"
      ],
      "type": "object"
    },
    "issue_type": {
      "type": "string"
    },
    "issue_type_detail": {
      "properties": {
        "id": {
          "type": "integer"
        },
        "is_system": {
          "type": "boolean"
        },
        "title": {
          "type": "string"
        }
      },
      "required": [
        "title",
        "id",
        "is_system"
      ],
      "type": "object"
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
    "milestone": {
      "properties": {
        "created_at": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "due_on": {
          "type": "string"
        },
        "number": {
          "type": "integer"
        },
        "repository_id": {
          "type": "integer"
        },
        "state": {
          "type": "string"
        },
        "title": {
          "type": "string"
        },
        "updated_at": {
          "type": "string"
        },
        "url": {
          "type": "string"
        }
      },
      "required": [
        "created_at",
        "description",
        "due_on",
        "number",
        "repository_id",
        "state",
        "title",
        "updated_at",
        "url"
      ],
      "type": "object"
    },
    "number": {
      "type": "string"
    },
    "priority": {
      "type": "integer"
    },
    "repository": {
      "properties": {
        "assigner": {
          "properties": {},
          "type": "object"
        },
        "created_at": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "full_name": {
          "type": "string"
        },
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "paas": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "updated_at": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "full_name",
        "path",
        "name",
        "description",
        "created_at",
        "updated_at",
        "assigner",
        "paas"
      ],
      "type": "object"
    },
    "state": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "updated_at": {
      "type": "string"
    },
    "user": {
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
        "avatar_url",
        "html_url",
        "id",
        "login",
        "name"
      ],
      "type": "object"
    },
    "visibility_reason": {
      "description": "Visibility, public: publicly visible, confidential: confidential, visible to project members, other: visible to project members due to other reasons",
      "type": "string"
    }
  },
  "required": [
    "id",
    "html_url",
    "number",
    "state",
    "title",
    "body",
    "user",
    "repository",
    "created_at",
    "updated_at",
    "finished_at",
    "labels",
    "issue_state",
    "comments",
    "priority",
    "issue_type",
    "milestone"
  ],
  "type": "object"
}
```
Example:
```json
{
  "assignee": null,
  "body": "abcabcabc",
  "created_at": "2024-04-15T21:58:21.188+08:00",
  "finished_at": null,
  "html_url": "https://test.gitcode.net/dengmengmian/test01/issues/3",
  "id": 152212,
  "issue_state": "opened",
  "issue_state_detail": null,
  "issue_type": null,
  "labels": [],
  "number": 3,
  "priority": null,
  "repository": {
    "assignee": null,
    "assignees_number": null,
    "assigner": null,
    "created_at": "2024-04-15T16:27:45.090+08:00",
    "description": "",
    "full_name": "dengmengmian / test01",
    "id": 280713,
    "name": "test01",
    "paas": null,
    "path": "test01",
    "pushed_at": null,
    "testers": null,
    "testers_number": null,
    "updated_at": "2024-04-15T16:27:45.090+08:00"
  },
  "severity": "Major",
  "stage": "New",
  "state": "opened",
  "title": "Inspector Gold Film",
  "updated_at": "2024-04-15T21:58:21.188+08:00",
  "user": {
    "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
    "events_url": null,
    "followers_url": null,
    "following_url": null,
    "gists_url": null,
    "html_url": "https://test.gitcode.net/dengmengmian",
    "id": "661ce4eab470b1430d456154",
    "login": "dengmengmian",
    "member_role": null,
    "name": "MaFan_",
    "organizations_url": null,
    "received_events_url": null,
    "remark": null,
    "repos_url": null,
    "starred_url": null,
    "subscriptions_url": null,
    "type": null,
    "url": null
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_issues_{number}",
  "parameters": [
    {
      "description": "Repository space address (organization or individual's address path)",
      "example": "",
      "in": "path",
      "name": "owner",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Repository path (path)",
      "example": "",
      "in": "path",
      "name": "repo",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Issue Number (case-sensitive, do not add #)",
      "example": "",
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
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/issues/{number}",
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
    "name": "Get a Specific Issue of a Repository",
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
        "issues",
        ":number"
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
            "content": "(Required) Repository space address (organization or individual's address path)",
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
            "content": "(Required) Issue Number (case-sensitive, do not add #)",
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
          "example": {
            "assignee": null,
            "body": "abcabcabc",
            "created_at": "2024-04-15T21:58:21.188+08:00",
            "finished_at": null,
            "html_url": "https://test.gitcode.net/dengmengmian/test01/issues/3",
            "id": 152212,
            "issue_state": "opened",
            "issue_state_detail": null,
            "issue_type": null,
            "labels": [],
            "number": 3,
            "priority": null,
            "repository": {
              "assignee": null,
              "assignees_number": null,
              "assigner": null,
              "created_at": "2024-04-15T16:27:45.090+08:00",
              "description": "",
              "full_name": "dengmengmian / test01",
              "id": 280713,
              "name": "test01",
              "paas": null,
              "path": "test01",
              "pushed_at": null,
              "testers": null,
              "testers_number": null,
              "updated_at": "2024-04-15T16:27:45.090+08:00"
            },
            "severity": "Major",
            "stage": "New",
            "state": "opened",
            "title": "Inspector Gold Film",
            "updated_at": "2024-04-15T21:58:21.188+08:00",
            "user": {
              "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
              "events_url": null,
              "followers_url": null,
              "following_url": null,
              "gists_url": null,
              "html_url": "https://test.gitcode.net/dengmengmian",
              "id": "661ce4eab470b1430d456154",
              "login": "dengmengmian",
              "member_role": null,
              "name": "MaFan_",
              "organizations_url": null,
              "received_events_url": null,
              "remark": null,
              "repos_url": null,
              "starred_url": null,
              "subscriptions_url": null,
              "type": null,
              "url": null
            }
          },
          "schema": {
            "properties": {
              "body": {
                "type": "string"
              },
              "comments": {
                "type": "integer"
              },
              "created_at": {
                "type": "string"
              },
              "custom_fields": {
                "description": "Custom field information",
                "items": {
                  "properties": {
                    "field_name": {
                      "description": "Custom Field Name",
                      "type": "string"
                    },
                    "field_type": {
                      "description": "Field type. text_single: single line text, text_multi: multi-line text, integer: integer, decimal: decimal, date: date, select_single: single select dropdown, select_multi: multi-select dropdown, member_single: single select member, member_multi: multi-select member",
                      "type": "string"
                    },
                    "field_values": {
                      "description": "Custom field value",
                      "items": {
                        "type": "string"
                      },
                      "type": "array"
                    },
                    "field_visibility": {
                      "description": "Visibility. 0: Visible to administrators only, 1: Visible to everyone",
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "finished_at": {
                "type": "string"
              },
              "html_url": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "issue_priority_detail": {
                "description": "Issue Priority",
                "properties": {
                  "id": {
                    "type": "string"
                  },
                  "title": {
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "title"
                ],
                "type": "object"
              },
              "issue_state": {
                "type": "string"
              },
              "issue_state_detail": {
                "properties": {
                  "id": {
                    "type": "integer"
                  },
                  "serial": {
                    "type": "integer"
                  },
                  "title": {
                    "type": "string"
                  }
                },
                "required": [
                  "title",
                  "serial",
                  "id"
                ],
                "type": "object"
              },
              "issue_type": {
                "type": "string"
              },
              "issue_type_detail": {
                "properties": {
                  "id": {
                    "type": "integer"
                  },
                  "is_system": {
                    "type": "boolean"
                  },
                  "title": {
                    "type": "string"
                  }
                },
                "required": [
                  "title",
                  "id",
                  "is_system"
                ],
                "type": "object"
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
              "milestone": {
                "properties": {
                  "created_at": {
                    "type": "string"
                  },
                  "description": {
                    "type": "string"
                  },
                  "due_on": {
                    "type": "string"
                  },
                  "number": {
                    "type": "integer"
                  },
                  "repository_id": {
                    "type": "integer"
                  },
                  "state": {
                    "type": "string"
                  },
                  "title": {
                    "type": "string"
                  },
                  "updated_at": {
                    "type": "string"
                  },
                  "url": {
                    "type": "string"
                  }
                },
                "required": [
                  "created_at",
                  "description",
                  "due_on",
                  "number",
                  "repository_id",
                  "state",
                  "title",
                  "updated_at",
                  "url"
                ],
                "type": "object"
              },
              "number": {
                "type": "string"
              },
              "priority": {
                "type": "integer"
              },
              "repository": {
                "properties": {
                  "assigner": {
                    "properties": {},
                    "type": "object"
                  },
                  "created_at": {
                    "type": "string"
                  },
                  "description": {
                    "type": "string"
                  },
                  "full_name": {
                    "type": "string"
                  },
                  "id": {
                    "type": "integer"
                  },
                  "name": {
                    "type": "string"
                  },
                  "paas": {
                    "type": "string"
                  },
                  "path": {
                    "type": "string"
                  },
                  "updated_at": {
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "full_name",
                  "path",
                  "name",
                  "description",
                  "created_at",
                  "updated_at",
                  "assigner",
                  "paas"
                ],
                "type": "object"
              },
              "state": {
                "type": "string"
              },
              "title": {
                "type": "string"
              },
              "updated_at": {
                "type": "string"
              },
              "user": {
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
                  "avatar_url",
                  "html_url",
                  "id",
                  "login",
                  "name"
                ],
                "type": "object"
              },
              "visibility_reason": {
                "description": "Visibility, public: publicly visible, confidential: confidential, visible to project members, other: visible to project members due to other reasons",
                "type": "string"
              }
            },
            "required": [
              "id",
              "html_url",
              "number",
              "state",
              "title",
              "body",
              "user",
              "repository",
              "created_at",
              "updated_at",
              "finished_at",
              "labels",
              "issue_state",
              "comments",
              "priority",
              "issue_type",
              "milestone"
            ],
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
    "Issues"
  ]
}
```
