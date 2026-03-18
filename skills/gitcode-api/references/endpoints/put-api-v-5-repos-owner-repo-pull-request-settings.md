# Update Pull Request Settings
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-pull-request-settings](https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-pull-request-settings)
Category: Repositories
- Method: `PUT`
- Path: `/api/v5/repos/{owner}/{repo}/pull_request_settings`
- Operation ID: `put_api_v5_repos_{owner}_{repo}_pull_request_settings`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "add_notes_after_merged": {
      "description": "Allow code review and comments to continue after the merge request is merged.",
      "type": "boolean"
    },
    "approval_approver_ids": {
      "description": "Project reviewer, comma-separated user_ids",
      "type": "string"
    },
    "approval_required_approvers": {
      "description": "The number of approvers required for approval",
      "type": "integer"
    },
    "approval_required_reviewers": {
      "description": "Number of required approvers (minimum review count 【selected number: 1~5, if the reviewer feature is disabled, input 0】)",
      "type": "integer"
    },
    "approval_required_reviewers_enable": {
      "description": "Whether the approval required reviewers feature is enabled",
      "type": "boolean"
    },
    "approval_required_testers": {
      "description": "Test minimum pass count",
      "type": "integer"
    },
    "approval_tester_ids": {
      "description": "Project tester, user_ids separated by commas",
      "type": "string"
    },
    "auto_squash_merge": {
      "description": "Create a new merge request with Squash merging enabled by default.",
      "type": "boolean"
    },
    "can_force_merge": {
      "description": "Allows the administrator to force merge",
      "type": "boolean"
    },
    "can_reopen": {
      "description": "Can a closed merge request be reopened?",
      "type": "boolean"
    },
    "close_issue_when_mr_merged": {
      "description": "When creating a Pull Request, the \"Close associated Issues after merge\" option is selected by default.",
      "type": "boolean"
    },
    "delete_source_branch_when_merged": {
      "description": "Whether to delete the source branch after merging, defaults to deleting the original branch.",
      "type": "boolean"
    },
    "disable_merge_by_self": {
      "description": "Do not merge pull requests created by yourself.",
      "type": "boolean"
    },
    "disable_squash_merge": {
      "description": "Prohibit Squash Merging",
      "type": "boolean"
    },
    "is_allow_lite_merge_request": {
      "description": "Enable lightweight Pull Request",
      "type": "boolean"
    },
    "is_check_cla": {
      "description": "Whether to verify CLA",
      "type": "boolean"
    },
    "lite_merge_request_prefix_title": {
      "description": "Lightweight PR title prefix",
      "type": "string"
    },
    "mark_auto_merged_mr_as_closed": {
      "description": "Whether the automatically merged MR status should be marked as closed",
      "type": "boolean"
    },
    "merge_method": {
      "description": "Merge mode one of three (merge by merge commit: merge; merge by merge commit (recording semi-linear history): rebase_merge; fast-forward merge: ff)",
      "type": "string"
    },
    "merged_commit_author": {
      "description": "Use MR (merge/creation) author to generate the Merge Commit (use merged_by for PR merger, use created_by for PR creator)",
      "type": "string"
    },
    "only_allow_merge_if_all_discussions_are_resolved": {
      "description": "The patch can only be merged after all review comments have been addressed.",
      "type": "boolean"
    },
    "only_allow_merge_if_pipeline_succeeds": {
      "description": "Should the merge be allowed only after the pipeline succeeds?",
      "type": "boolean"
    },
    "squash_merge_with_no_merge_commit": {
      "description": "Squash merge does not produce a Merge node.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```
Example:
```json
""
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
    "merge_method": {
      "type": "string"
    },
    "merge_request_setting": {
      "properties": {
        "add_notes_after_merged": {
          "type": "integer"
        },
        "approval_approvers": {
          "items": {
            "properties": {},
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
            "properties": {},
            "type": "object"
          },
          "type": "array"
        },
        "auto_squash_merge": {
          "type": "integer"
        },
        "can_force_merge": {
          "type": "integer"
        },
        "can_reopen": {
          "type": "integer"
        },
        "close_issue_when_mr_merged": {
          "type": "integer"
        },
        "created_at": {
          "type": "string"
        },
        "delete_source_branch_when_merged": {
          "type": "integer"
        },
        "disable_merge_by_self": {
          "type": "integer"
        },
        "disable_squash_merge": {
          "type": "integer"
        },
        "id": {
          "type": "integer"
        },
        "is_allow_lite_merge_request": {
          "type": "integer"
        },
        "is_check_cla": {
          "type": "integer"
        },
        "mark_auto_merged_mr_as_closed": {
          "type": "integer"
        },
        "merged_commit_author": {
          "type": "string"
        },
        "project_id": {
          "type": "integer"
        },
        "squash_merge_with_no_merge_commit": {
          "type": "integer"
        },
        "updated_at": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "only_allow_merge_if_all_discussions_are_resolved": {
      "type": "integer"
    },
    "only_allow_merge_if_pipeline_succeeds": {
      "type": "integer"
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
  }
}
```
## JSON Request Example
```json
{
  "add_notes_after_merged": true,
  "approval_approver_ids": "string",
  "approval_required_approvers": 0,
  "approval_required_reviewers": 0,
  "approval_required_reviewers_enable": true,
  "approval_required_testers": 0,
  "approval_tester_ids": "string",
  "auto_squash_merge": true,
  "can_force_merge": true,
  "can_reopen": true,
  "close_issue_when_mr_merged": true,
  "delete_source_branch_when_merged": true,
  "disable_merge_by_self": true,
  "disable_squash_merge": true,
  "is_allow_lite_merge_request": true,
  "is_check_cla": true,
  "lite_merge_request_prefix_title": "string",
  "mark_auto_merged_mr_as_closed": true,
  "merge_method": "string",
  "merged_commit_author": "string",
  "only_allow_merge_if_all_discussions_are_resolved": true,
  "only_allow_merge_if_pipeline_succeeds": true,
  "squash_merge_with_no_merge_commit": true
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
  "jsonRequestBodyExample": {
    "add_notes_after_merged": true,
    "approval_approver_ids": "string",
    "approval_required_approvers": 0,
    "approval_required_reviewers": 0,
    "approval_required_reviewers_enable": true,
    "approval_required_testers": 0,
    "approval_tester_ids": "string",
    "auto_squash_merge": true,
    "can_force_merge": true,
    "can_reopen": true,
    "close_issue_when_mr_merged": true,
    "delete_source_branch_when_merged": true,
    "disable_merge_by_self": true,
    "disable_squash_merge": true,
    "is_allow_lite_merge_request": true,
    "is_check_cla": true,
    "lite_merge_request_prefix_title": "string",
    "mark_auto_merged_mr_as_closed": true,
    "merge_method": "string",
    "merged_commit_author": "string",
    "only_allow_merge_if_all_discussions_are_resolved": true,
    "only_allow_merge_if_pipeline_succeeds": true,
    "squash_merge_with_no_merge_commit": true
  },
  "method": "put",
  "operationId": "put_api_v5_repos_{owner}_{repo}_pull_request_settings",
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
      "content": "",
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
    "method": "PUT",
    "name": "Update Pull Request Settings",
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
  "requestBody": {
    "content": {
      "application/json": {
        "example": "",
        "schema": {
          "properties": {
            "add_notes_after_merged": {
              "description": "Allow code review and comments to continue after the merge request is merged.",
              "type": "boolean"
            },
            "approval_approver_ids": {
              "description": "Project reviewer, comma-separated user_ids",
              "type": "string"
            },
            "approval_required_approvers": {
              "description": "The number of approvers required for approval",
              "type": "integer"
            },
            "approval_required_reviewers": {
              "description": "Number of required approvers (minimum review count 【selected number: 1~5, if the reviewer feature is disabled, input 0】)",
              "type": "integer"
            },
            "approval_required_reviewers_enable": {
              "description": "Whether the approval required reviewers feature is enabled",
              "type": "boolean"
            },
            "approval_required_testers": {
              "description": "Test minimum pass count",
              "type": "integer"
            },
            "approval_tester_ids": {
              "description": "Project tester, user_ids separated by commas",
              "type": "string"
            },
            "auto_squash_merge": {
              "description": "Create a new merge request with Squash merging enabled by default.",
              "type": "boolean"
            },
            "can_force_merge": {
              "description": "Allows the administrator to force merge",
              "type": "boolean"
            },
            "can_reopen": {
              "description": "Can a closed merge request be reopened?",
              "type": "boolean"
            },
            "close_issue_when_mr_merged": {
              "description": "When creating a Pull Request, the \"Close associated Issues after merge\" option is selected by default.",
              "type": "boolean"
            },
            "delete_source_branch_when_merged": {
              "description": "Whether to delete the source branch after merging, defaults to deleting the original branch.",
              "type": "boolean"
            },
            "disable_merge_by_self": {
              "description": "Do not merge pull requests created by yourself.",
              "type": "boolean"
            },
            "disable_squash_merge": {
              "description": "Prohibit Squash Merging",
              "type": "boolean"
            },
            "is_allow_lite_merge_request": {
              "description": "Enable lightweight Pull Request",
              "type": "boolean"
            },
            "is_check_cla": {
              "description": "Whether to verify CLA",
              "type": "boolean"
            },
            "lite_merge_request_prefix_title": {
              "description": "Lightweight PR title prefix",
              "type": "string"
            },
            "mark_auto_merged_mr_as_closed": {
              "description": "Whether the automatically merged MR status should be marked as closed",
              "type": "boolean"
            },
            "merge_method": {
              "description": "Merge mode one of three (merge by merge commit: merge; merge by merge commit (recording semi-linear history): rebase_merge; fast-forward merge: ff)",
              "type": "string"
            },
            "merged_commit_author": {
              "description": "Use MR (merge/creation) author to generate the Merge Commit (use merged_by for PR merger, use created_by for PR creator)",
              "type": "string"
            },
            "only_allow_merge_if_all_discussions_are_resolved": {
              "description": "The patch can only be merged after all review comments have been addressed.",
              "type": "boolean"
            },
            "only_allow_merge_if_pipeline_succeeds": {
              "description": "Should the merge be allowed only after the pipeline succeeds?",
              "type": "boolean"
            },
            "squash_merge_with_no_merge_commit": {
              "description": "Squash merge does not produce a Merge node.",
              "type": "boolean"
            }
          },
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
            }
          },
          "schema": {
            "properties": {
              "merge_method": {
                "type": "string"
              },
              "merge_request_setting": {
                "properties": {
                  "add_notes_after_merged": {
                    "type": "integer"
                  },
                  "approval_approvers": {
                    "items": {
                      "properties": {},
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
                      "properties": {},
                      "type": "object"
                    },
                    "type": "array"
                  },
                  "auto_squash_merge": {
                    "type": "integer"
                  },
                  "can_force_merge": {
                    "type": "integer"
                  },
                  "can_reopen": {
                    "type": "integer"
                  },
                  "close_issue_when_mr_merged": {
                    "type": "integer"
                  },
                  "created_at": {
                    "type": "string"
                  },
                  "delete_source_branch_when_merged": {
                    "type": "integer"
                  },
                  "disable_merge_by_self": {
                    "type": "integer"
                  },
                  "disable_squash_merge": {
                    "type": "integer"
                  },
                  "id": {
                    "type": "integer"
                  },
                  "is_allow_lite_merge_request": {
                    "type": "integer"
                  },
                  "is_check_cla": {
                    "type": "integer"
                  },
                  "mark_auto_merged_mr_as_closed": {
                    "type": "integer"
                  },
                  "merged_commit_author": {
                    "type": "string"
                  },
                  "project_id": {
                    "type": "integer"
                  },
                  "squash_merge_with_no_merge_commit": {
                    "type": "integer"
                  },
                  "updated_at": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "only_allow_merge_if_all_discussions_are_resolved": {
                "type": "integer"
              },
              "only_allow_merge_if_pipeline_succeeds": {
                "type": "integer"
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
    "Repositories"
  ]
}
```
