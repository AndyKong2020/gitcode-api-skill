# Get Pull Request Settings
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pull-request-settings](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pull-request-settings)
Category: Repositories
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/pull_request_settings`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_pull_request_settings`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
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
    "merge_method": {
      "type": "string"
    },
    "merge_request_setting": {
      "properties": {
        "add_notes_after_merged": {
          "type": "boolean"
        },
        "approval_approvers": {
          "items": {
            "properties": {
              "avatar_url": {
                "type": "string"
              },
              "iam_id": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "name": {
                "type": "string"
              },
              "name_cn": {
                "type": "string"
              },
              "nick_name": {
                "type": "string"
              },
              "state": {
                "type": "string"
              },
              "username": {
                "type": "string"
              },
              "web_url": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "type": "array"
        },
        "approval_required_approvers": {
          "type": "integer"
        },
        "approval_required_reviewers": {
          "type": "integer"
        },
        "approval_required_testers": {
          "type": "integer"
        },
        "approval_testers": {
          "items": {
            "properties": {
              "avatar_url": {
                "type": "string"
              },
              "iam_id": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "name": {
                "type": "string"
              },
              "name_cn": {
                "type": "string"
              },
              "nick_name": {
                "type": "string"
              },
              "state": {
                "type": "string"
              },
              "username": {
                "type": "string"
              },
              "web_url": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "type": "array"
        },
        "auto_squash_merge": {
          "type": "boolean"
        },
        "can_force_merge": {
          "type": "boolean"
        },
        "can_reopen": {
          "type": "boolean"
        },
        "close_issue_when_mr_merged": {
          "type": "boolean"
        },
        "codeowner_merge_count": {
          "title": "Code owner review count mode, true: use merge count, code owner counts as reviewer; false: use individual count, code owner does not count as reviewer",
          "type": "boolean"
        },
        "created_at": {
          "type": "string"
        },
        "delete_source_branch_when_merged": {
          "type": "boolean"
        },
        "disable_merge_by_self": {
          "type": "boolean"
        },
        "disable_squash_merge": {
          "type": "boolean"
        },
        "id": {
          "type": "integer"
        },
        "is_allow_lite_merge_request": {
          "type": "boolean"
        },
        "is_check_cla": {
          "type": "boolean"
        },
        "mark_auto_merged_mr_as_closed": {
          "type": "boolean"
        },
        "merged_commit_author": {
          "type": "string"
        },
        "project_id": {
          "type": "integer"
        },
        "squash_merge_with_no_merge_commit": {
          "type": "boolean"
        },
        "updated_at": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "project_id",
        "disable_merge_by_self",
        "created_at",
        "updated_at",
        "can_force_merge",
        "disable_squash_merge",
        "approval_required_reviewers",
        "approval_required_approvers",
        "add_notes_after_merged",
        "merged_commit_author",
        "mark_auto_merged_mr_as_closed",
        "delete_source_branch_when_merged",
        "auto_squash_merge",
        "squash_merge_with_no_merge_commit",
        "close_issue_when_mr_merged",
        "can_reopen",
        "is_check_cla",
        "approval_approvers",
        "approval_testers",
        "approval_required_testers",
        "is_allow_lite_merge_request",
        "codeowner_merge_count"
      ],
      "type": "object"
    },
    "only_allow_merge_if_all_discussions_are_resolved": {
      "type": "boolean"
    },
    "only_allow_merge_if_pipeline_succeeds": {
      "type": "boolean"
    }
  },
  "required": [
    "merge_request_setting",
    "only_allow_merge_if_all_discussions_are_resolved",
    "only_allow_merge_if_pipeline_succeeds",
    "merge_method"
  ],
  "type": "object"
}
```
Example:
```json
{
  "merge_method": "merge",
  "merge_request_setting": {
    "add_notes_after_merged": false,
    "approval_approvers": [],
    "approval_required_approvers": 0,
    "approval_required_reviewers": 0,
    "approval_required_testers": 0,
    "approval_testers": [],
    "auto_squash_merge": false,
    "can_force_merge": false,
    "can_reopen": true,
    "close_issue_when_mr_merged": false,
    "created_at": "2024-03-28T10:04:13.523+08:00",
    "delete_source_branch_when_merged": false,
    "disable_merge_by_self": false,
    "disable_squash_merge": true,
    "id": 1431,
    "is_allow_lite_merge_request": false,
    "is_check_cla": false,
    "mark_auto_merged_mr_as_closed": false,
    "merged_commit_author": "merged_by",
    "project_id": 2745002,
    "squash_merge_with_no_merge_commit": false,
    "updated_at": "2024-11-13T21:30:45.261+08:00"
  },
  "only_allow_merge_if_all_discussions_are_resolved": false,
  "only_allow_merge_if_pipeline_succeeds": false
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_pull_request_settings",
  "parameters": [
    {
      "description": "Repository space address (address path of the enterprise, organization, or individual)",
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
      "description": "User authorization code",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/pull_request_settings",
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
    "name": "Get Pull Request Settings",
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
        "pull_request_settings"
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
        }
      ]
    }
  },
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "example": {
            "merge_method": "merge",
            "merge_request_setting": {
              "add_notes_after_merged": false,
              "approval_approvers": [],
              "approval_required_approvers": 0,
              "approval_required_reviewers": 0,
              "approval_required_testers": 0,
              "approval_testers": [],
              "auto_squash_merge": false,
              "can_force_merge": false,
              "can_reopen": true,
              "close_issue_when_mr_merged": false,
              "created_at": "2024-03-28T10:04:13.523+08:00",
              "delete_source_branch_when_merged": false,
              "disable_merge_by_self": false,
              "disable_squash_merge": true,
              "id": 1431,
              "is_allow_lite_merge_request": false,
              "is_check_cla": false,
              "mark_auto_merged_mr_as_closed": false,
              "merged_commit_author": "merged_by",
              "project_id": 2745002,
              "squash_merge_with_no_merge_commit": false,
              "updated_at": "2024-11-13T21:30:45.261+08:00"
            },
            "only_allow_merge_if_all_discussions_are_resolved": false,
            "only_allow_merge_if_pipeline_succeeds": false
          },
          "schema": {
            "properties": {
              "merge_method": {
                "type": "string"
              },
              "merge_request_setting": {
                "properties": {
                  "add_notes_after_merged": {
                    "type": "boolean"
                  },
                  "approval_approvers": {
                    "items": {
                      "properties": {
                        "avatar_url": {
                          "type": "string"
                        },
                        "iam_id": {
                          "type": "string"
                        },
                        "id": {
                          "type": "integer"
                        },
                        "name": {
                          "type": "string"
                        },
                        "name_cn": {
                          "type": "string"
                        },
                        "nick_name": {
                          "type": "string"
                        },
                        "state": {
                          "type": "string"
                        },
                        "username": {
                          "type": "string"
                        },
                        "web_url": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "type": "array"
                  },
                  "approval_required_approvers": {
                    "type": "integer"
                  },
                  "approval_required_reviewers": {
                    "type": "integer"
                  },
                  "approval_required_testers": {
                    "type": "integer"
                  },
                  "approval_testers": {
                    "items": {
                      "properties": {
                        "avatar_url": {
                          "type": "string"
                        },
                        "iam_id": {
                          "type": "string"
                        },
                        "id": {
                          "type": "integer"
                        },
                        "name": {
                          "type": "string"
                        },
                        "name_cn": {
                          "type": "string"
                        },
                        "nick_name": {
                          "type": "string"
                        },
                        "state": {
                          "type": "string"
                        },
                        "username": {
                          "type": "string"
                        },
                        "web_url": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "type": "array"
                  },
                  "auto_squash_merge": {
                    "type": "boolean"
                  },
                  "can_force_merge": {
                    "type": "boolean"
                  },
                  "can_reopen": {
                    "type": "boolean"
                  },
                  "close_issue_when_mr_merged": {
                    "type": "boolean"
                  },
                  "codeowner_merge_count": {
                    "title": "Code owner review count mode, true: use merge count, code owner counts as reviewer; false: use individual count, code owner does not count as reviewer",
                    "type": "boolean"
                  },
                  "created_at": {
                    "type": "string"
                  },
                  "delete_source_branch_when_merged": {
                    "type": "boolean"
                  },
                  "disable_merge_by_self": {
                    "type": "boolean"
                  },
                  "disable_squash_merge": {
                    "type": "boolean"
                  },
                  "id": {
                    "type": "integer"
                  },
                  "is_allow_lite_merge_request": {
                    "type": "boolean"
                  },
                  "is_check_cla": {
                    "type": "boolean"
                  },
                  "mark_auto_merged_mr_as_closed": {
                    "type": "boolean"
                  },
                  "merged_commit_author": {
                    "type": "string"
                  },
                  "project_id": {
                    "type": "integer"
                  },
                  "squash_merge_with_no_merge_commit": {
                    "type": "boolean"
                  },
                  "updated_at": {
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "project_id",
                  "disable_merge_by_self",
                  "created_at",
                  "updated_at",
                  "can_force_merge",
                  "disable_squash_merge",
                  "approval_required_reviewers",
                  "approval_required_approvers",
                  "add_notes_after_merged",
                  "merged_commit_author",
                  "mark_auto_merged_mr_as_closed",
                  "delete_source_branch_when_merged",
                  "auto_squash_merge",
                  "squash_merge_with_no_merge_commit",
                  "close_issue_when_mr_merged",
                  "can_reopen",
                  "is_check_cla",
                  "approval_approvers",
                  "approval_testers",
                  "approval_required_testers",
                  "is_allow_lite_merge_request",
                  "codeowner_merge_count"
                ],
                "type": "object"
              },
              "only_allow_merge_if_all_discussions_are_resolved": {
                "type": "boolean"
              },
              "only_allow_merge_if_pipeline_succeeds": {
                "type": "boolean"
              }
            },
            "required": [
              "merge_request_setting",
              "only_allow_merge_if_all_discussions_are_resolved",
              "only_allow_merge_if_pipeline_succeeds",
              "merge_method"
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
    "Repositories"
  ]
}
```
