# Get Single Pull Request
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-number](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-number)
Category: Pull Requests
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_pulls_{number}`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| number | path | true | integer | The ordinal number of the PR in this repository, i.e., which PR it is. |
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
    "approval_reviewers": {
      "description": "Reviewer Information",
      "items": {
        "properties": {
          "accept": {
            "type": "boolean"
          },
          "assignee": {
            "type": "boolean"
          },
          "avatar_url": {
            "type": "string"
          },
          "code_owner": {
            "type": "boolean"
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
          "html_url",
          "assignee",
          "code_owner",
          "accept"
        ],
        "type": "object"
      },
      "type": "array"
    },
    "assignees": {
      "description": "Auditor Information",
      "items": {
        "properties": {
          "accept": {
            "type": "boolean"
          },
          "assignee": {
            "type": "boolean"
          },
          "avatar_url": {
            "type": "string"
          },
          "code_owner": {
            "type": "boolean"
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
        "type": "object"
      },
      "type": "array"
    },
    "assignees_number": {
      "description": "Number of reviewers",
      "type": "integer"
    },
    "base": {
      "description": "Target branch information",
      "properties": {
        "label": {
          "description": "label",
          "type": "string"
        },
        "ref": {
          "description": "Branch Path",
          "type": "string"
        },
        "repo": {
          "description": "warehouse information",
          "properties": {
            "full_name": {
              "type": "string"
            },
            "html_url": {
              "type": "string"
            },
            "name": {
              "type": "string"
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
            "name",
            "namespace",
            "full_name",
            "html_url"
          ],
          "type": "object"
        },
        "sha": {
          "description": "commit id",
          "type": "string"
        }
      },
      "required": [
        "ref",
        "sha",
        "label",
        "repo"
      ],
      "type": "object"
    },
    "body": {
      "description": "description",
      "type": "string"
    },
    "can_merge_check": {
      "description": "Merge Check",
      "type": "boolean"
    },
    "closed_at": {
      "description": "Close time",
      "type": "string"
    },
    "created_at": {
      "description": "creation time",
      "type": "string"
    },
    "draft": {
      "description": "Is it a draft",
      "type": "boolean"
    },
    "head": {
      "description": "commit message",
      "properties": {
        "label": {
          "description": "label",
          "type": "string"
        },
        "ref": {
          "description": "Branch Path",
          "type": "string"
        },
        "repo": {
          "description": "warehouse information",
          "properties": {
            "full_name": {
              "type": "string"
            },
            "html_url": {
              "type": "string"
            },
            "name": {
              "type": "string"
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
            "name",
            "namespace",
            "full_name",
            "html_url"
          ],
          "type": "object"
        },
        "sha": {
          "description": "commit id",
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
            "id",
            "login",
            "name",
            "avatar_url",
            "html_url"
          ],
          "type": "object"
        }
      },
      "required": [
        "ref",
        "sha",
        "label",
        "repo",
        "user"
      ],
      "type": "object"
    },
    "html_url": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "issue_url": {
      "description": "Associated issue API URL",
      "type": "string"
    },
    "labels": {
      "description": "Tag Information",
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
          "repository_id": {
            "type": "integer"
          },
          "updated_at": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "color",
          "name",
          "repository_id",
          "created_at",
          "updated_at"
        ],
        "type": "object"
      },
      "type": "array"
    },
    "mergeable": {
      "description": "Is it possible to merge?",
      "type": "boolean"
    },
    "mergeable_state": {
      "description": "Access Control Information",
      "properties": {
        "all_depend_merge_request_merged_passed": {
          "description": "All dependent pull requests have been merged and passed.",
          "type": "boolean"
        },
        "approval_approvers_required_passed": {
          "description": "Is the code approval passed?",
          "type": "boolean"
        },
        "approval_approvers_result": {
          "type": "integer"
        },
        "approval_reviewers_required_passed": {
          "description": "Is the code review passed?",
          "type": "boolean"
        },
        "approval_testers_required_passed": {
          "description": "Code test passed",
          "type": "boolean"
        },
        "approval_testers_result": {
          "type": "integer"
        },
        "branch_missing_passed": {
          "description": "Branch missing through",
          "type": "boolean"
        },
        "can_force_merge": {
          "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation!!! You can forcibly merge it.",
          "type": "boolean"
        },
        "check_tasks_num": {
          "description": "Checked Items Total Number",
          "type": "integer"
        },
        "ci_state_passed": {
          "description": "CI Status via",
          "type": "boolean"
        },
        "conflict_passed": {
          "description": "Conflict through",
          "type": "boolean"
        },
        "merge_by_self_passed": {
          "description": "Self-merging through",
          "type": "boolean"
        },
        "merge_request_id": {
          "description": "Merge Request ID",
          "type": "integer"
        },
        "merge_request_switch": {
          "description": "Merge Request Switch",
          "properties": {
            "add_notes_after_merged": {
              "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts besides the translation!! Add comments after merging",
              "type": "boolean"
            },
            "approval_required_reviewers_branch": {
              "description": "Approved Reviewer Branch",
              "type": "string"
            },
            "approval_required_reviewers_count": {
              "description": "Number of reviewers requiring approval",
              "type": "integer"
            },
            "can_force_merge": {
              "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation!!! You can forcibly merge it.",
              "type": "boolean"
            },
            "can_reopen": {
              "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! You can reopen it.",
              "type": "boolean"
            },
            "disable_merge_by_self": {
              "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts! Prohibited from self-merging!",
              "type": "boolean"
            },
            "disable_squash_merge": {
              "description": "Please translate the following content into professional English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation!!! Do not compress or merge!",
              "type": "boolean"
            },
            "mark_auto_merged_mr_as_closed": {
              "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts! Mark automatically merged MRs as closed.",
              "type": "boolean"
            },
            "merge_method": {
              "description": "Merge Method",
              "type": "string"
            },
            "only_allow_merge_if_all_discussions_are_resolved": {
              "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation!!! Only merge after all discussions are resolved.",
              "type": "boolean"
            },
            "only_allow_merge_if_pipeline_succeeds": {
              "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation!!! Only merge after successful pipeline.",
              "type": "boolean"
            },
            "review_mode": {
              "description": "Review mode",
              "type": "string"
            },
            "squash_merge_with_no_merge_commit": {
              "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation!!! No merged submission of compressed merge",
              "type": "boolean"
            }
          },
          "required": [
            "review_mode",
            "merge_method",
            "only_allow_merge_if_all_discussions_are_resolved",
            "disable_merge_by_self",
            "only_allow_merge_if_pipeline_succeeds",
            "disable_squash_merge",
            "squash_merge_with_no_merge_commit",
            "approval_required_reviewers_count",
            "approval_required_reviewers_branch",
            "add_notes_after_merged",
            "mark_auto_merged_mr_as_closed",
            "can_force_merge",
            "can_reopen"
          ],
          "type": "object"
        },
        "merged_by_user_passed": {
          "description": "User merged through",
          "type": "boolean"
        },
        "mr_state_passed": {
          "description": "Merge Request Status Through",
          "type": "boolean"
        },
        "non_ff_passed": {
          "description": "Non-skippable through",
          "type": "boolean"
        },
        "reason": {
          "description": "Reason",
          "properties": {},
          "type": "object"
        },
        "resolve_discussion_passed": {
          "description": "Resolve discussion passed",
          "type": "boolean"
        },
        "state": {
          "description": "Status",
          "type": "boolean"
        },
        "status_without_user_auth": {
          "description": "Status without user authorization",
          "type": "boolean"
        },
        "work_in_progress_passed": {
          "description": "Work progress through",
          "type": "boolean"
        }
      },
      "required": [
        "merge_request_id",
        "state",
        "status_without_user_auth",
        "conflict_passed",
        "branch_missing_passed",
        "non_ff_passed",
        "mr_state_passed",
        "merged_by_user_passed",
        "work_in_progress_passed",
        "resolve_discussion_passed",
        "ci_state_passed",
        "merge_by_self_passed",
        "can_force_merge",
        "approval_reviewers_required_passed",
        "approval_approvers_required_passed",
        "approval_testers_required_passed",
        "merge_request_switch",
        "reason",
        "check_tasks_num",
        "all_depend_merge_request_merged_passed",
        "approval_approvers_result",
        "approval_testers_result"
      ],
      "type": "object"
    },
    "merged_at": {
      "description": "Merge Time",
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
    "milestone": {
      "properties": {
        "created_at": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "number": {
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
        }
      },
      "required": [
        "created_at",
        "description",
        "number",
        "state",
        "title",
        "updated_at"
      ],
      "type": "object"
    },
    "number": {
      "description": "Serial number",
      "type": "integer"
    },
    "prune_branch": {
      "description": "Is the source branch forcibly deleted?",
      "type": "boolean"
    },
    "state": {
      "description": "Status, open/closed/merged",
      "type": "string"
    },
    "testers": {
      "description": "Test Person Information",
      "items": {
        "properties": {
          "accept": {
            "type": "boolean"
          },
          "assignee": {
            "type": "boolean"
          },
          "code_owner": {
            "type": "boolean"
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
        "type": "object"
      },
      "type": "array"
    },
    "title": {
      "description": "Title",
      "type": "string"
    },
    "updated_at": {
      "description": "Update time",
      "type": "string"
    },
    "url": {
      "description": "api url",
      "type": "string"
    },
    "user": {
      "description": "Creator Information",
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
    "visibility_reason": {
      "description": "Visibility, public: Publicly visible, other: Visible to project members only",
      "type": "string"
    }
  },
  "required": [
    "id",
    "html_url",
    "number",
    "state",
    "title",
    "url",
    "issue_url",
    "body",
    "assignees_number",
    "assignees",
    "testers",
    "approval_reviewers",
    "labels",
    "created_at",
    "updated_at",
    "closed_at",
    "merged_at",
    "draft",
    "can_merge_check",
    "prune_branch",
    "mergeable",
    "user",
    "head",
    "base",
    "mergeable_state",
    "milestone",
    "merged_by"
  ],
  "type": "object"
}
```
Example:
```json
{
  "assignees": [
    {
      "accept": true,
      "assigness": true,
      "avatar_url": "http://gitcode.com/sytest/paopao/pull/1.png",
      "code_owner": false,
      "html_url": "http://gitcode.com/sytest/paopao/pull/1",
      "id": 2,
      "login": "test",
      "name": "test_web"
    }
  ],
  "assignees_number": 1,
  "base": {
    "label": "main",
    "ref": "main",
    "repo": {
      "name": "paopao",
      "path": "paopao"
    },
    "sha": "91861a9668041fc1c0ff51d1db66b6297179f5e6"
  },
  "body": "Description",
  "can_merge_check": false,
  "closed__at": "",
  "created_at": "",
  "draft": false,
  "head": {
    "label": "test",
    "ref": "test",
    "repo": {
      "name": "paopao",
      "path": "paopao"
    },
    "sha": "91861a9668041fc1c0ff51d1db66b6297179f5e6"
  },
  "html_url": "http://gitcode.com/sytest/paopao/pull/1",
  "id": 111,
  "issue_url": "https://api.gitcode.com/api/v5/repos/sytest/paopao/pulls/1/issues",
  "labels": [
    {
      "created_at": "",
      "id": 222,
      "name": "label1",
      "repository_id": 1,
      "updated_at": ""
    }
  ],
  "mergeable": true,
  "mergeable_state": {
    "approval_approvers_required_passed": true,
    "approval_reviewers_required_passed": true,
    "approval_testers_required_passed": true,
    "branch_missing_passed": true,
    "can_force_merge": false,
    "check_tasks_num": 0,
    "ci_state_passed": true,
    "conflict_passed": false,
    "merge_by_self_passed": true,
    "merge_request_id": 111,
    "merge_request_switch": {
      "add_notes_after_merged": false,
      "approval_required_reviewers_branch": "*",
      "approval_required_reviewers_count": 0,
      "can_force_merge": false,
      "can_reopen": true,
      "disable_merge_by_self": false,
      "disable_squash_merge": false,
      "mark_auto_merged_mr_as_closed": false,
      "merge_method": "merge",
      "only_allow_merge_if_all_discussions_are_resolved": false,
      "only_allow_merge_if_pipeline_succeeds": false,
      "review_mode": "approval",
      "squash_merge_with_no_merge_commit": false
    },
    "merged_by_user_passed": true,
    "mr_state_passed": true,
    "non_ff_passed": true,
    "reason": {},
    "resolve_discussion_passed": true,
    "state": false,
    "status_without_user_auth": false,
    "work_in_progress_passed": true
  },
  "merged_at": "",
  "number": 1,
  "prune_branch": false,
  "ref_pull_requests": [
    {
      "id": 191973,
      "number": 3,
      "state": "merged",
      "title": "dddd"
    }
  ],
  "state": "open",
  "testers": [
    {
      "accept": true,
      "assigness": true,
      "avatar_url": "http://gitcode.com/sytest/paopao/pull/1.png",
      "code_owner": false,
      "html_url": "http://gitcode.com/sytest/paopao/pull/1",
      "id": 2,
      "login": "test",
      "name": "test_web"
    }
  ],
  "updated_at": "",
  "url": "https://api.gitcode.com/api/v5/repos/sytest/paopao/pulls/1",
  "user": {
    "id": "userId",
    "login": "test"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_pulls_{number}",
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
      "description": "The ordinal number of the PR in this repository, i.e., which PR it is.",
      "example": 0,
      "in": "path",
      "name": "number",
      "required": true,
      "schema": {
        "type": "integer"
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
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}",
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
    "name": "Get Single Pull Request",
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
            "content": "(Required) The ordinal number of the PR in this repository, i.e., which PR it is.",
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
            "assignees": [
              {
                "accept": true,
                "assigness": true,
                "avatar_url": "http://gitcode.com/sytest/paopao/pull/1.png",
                "code_owner": false,
                "html_url": "http://gitcode.com/sytest/paopao/pull/1",
                "id": 2,
                "login": "test",
                "name": "test_web"
              }
            ],
            "assignees_number": 1,
            "base": {
              "label": "main",
              "ref": "main",
              "repo": {
                "name": "paopao",
                "path": "paopao"
              },
              "sha": "91861a9668041fc1c0ff51d1db66b6297179f5e6"
            },
            "body": "Description",
            "can_merge_check": false,
            "closed__at": "",
            "created_at": "",
            "draft": false,
            "head": {
              "label": "test",
              "ref": "test",
              "repo": {
                "name": "paopao",
                "path": "paopao"
              },
              "sha": "91861a9668041fc1c0ff51d1db66b6297179f5e6"
            },
            "html_url": "http://gitcode.com/sytest/paopao/pull/1",
            "id": 111,
            "issue_url": "https://api.gitcode.com/api/v5/repos/sytest/paopao/pulls/1/issues",
            "labels": [
              {
                "created_at": "",
                "id": 222,
                "name": "label1",
                "repository_id": 1,
                "updated_at": ""
              }
            ],
            "mergeable": true,
            "mergeable_state": {
              "approval_approvers_required_passed": true,
              "approval_reviewers_required_passed": true,
              "approval_testers_required_passed": true,
              "branch_missing_passed": true,
              "can_force_merge": false,
              "check_tasks_num": 0,
              "ci_state_passed": true,
              "conflict_passed": false,
              "merge_by_self_passed": true,
              "merge_request_id": 111,
              "merge_request_switch": {
                "add_notes_after_merged": false,
                "approval_required_reviewers_branch": "*",
                "approval_required_reviewers_count": 0,
                "can_force_merge": false,
                "can_reopen": true,
                "disable_merge_by_self": false,
                "disable_squash_merge": false,
                "mark_auto_merged_mr_as_closed": false,
                "merge_method": "merge",
                "only_allow_merge_if_all_discussions_are_resolved": false,
                "only_allow_merge_if_pipeline_succeeds": false,
                "review_mode": "approval",
                "squash_merge_with_no_merge_commit": false
              },
              "merged_by_user_passed": true,
              "mr_state_passed": true,
              "non_ff_passed": true,
              "reason": {},
              "resolve_discussion_passed": true,
              "state": false,
              "status_without_user_auth": false,
              "work_in_progress_passed": true
            },
            "merged_at": "",
            "number": 1,
            "prune_branch": false,
            "ref_pull_requests": [
              {
                "id": 191973,
                "number": 3,
                "state": "merged",
                "title": "dddd"
              }
            ],
            "state": "open",
            "testers": [
              {
                "accept": true,
                "assigness": true,
                "avatar_url": "http://gitcode.com/sytest/paopao/pull/1.png",
                "code_owner": false,
                "html_url": "http://gitcode.com/sytest/paopao/pull/1",
                "id": 2,
                "login": "test",
                "name": "test_web"
              }
            ],
            "updated_at": "",
            "url": "https://api.gitcode.com/api/v5/repos/sytest/paopao/pulls/1",
            "user": {
              "id": "userId",
              "login": "test"
            }
          },
          "schema": {
            "properties": {
              "approval_reviewers": {
                "description": "Reviewer Information",
                "items": {
                  "properties": {
                    "accept": {
                      "type": "boolean"
                    },
                    "assignee": {
                      "type": "boolean"
                    },
                    "avatar_url": {
                      "type": "string"
                    },
                    "code_owner": {
                      "type": "boolean"
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
                    "html_url",
                    "assignee",
                    "code_owner",
                    "accept"
                  ],
                  "type": "object"
                },
                "type": "array"
              },
              "assignees": {
                "description": "Auditor Information",
                "items": {
                  "properties": {
                    "accept": {
                      "type": "boolean"
                    },
                    "assignee": {
                      "type": "boolean"
                    },
                    "avatar_url": {
                      "type": "string"
                    },
                    "code_owner": {
                      "type": "boolean"
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
                  "type": "object"
                },
                "type": "array"
              },
              "assignees_number": {
                "description": "Number of reviewers",
                "type": "integer"
              },
              "base": {
                "description": "Target branch information",
                "properties": {
                  "label": {
                    "description": "label",
                    "type": "string"
                  },
                  "ref": {
                    "description": "Branch Path",
                    "type": "string"
                  },
                  "repo": {
                    "description": "warehouse information",
                    "properties": {
                      "full_name": {
                        "type": "string"
                      },
                      "html_url": {
                        "type": "string"
                      },
                      "name": {
                        "type": "string"
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
                      "name",
                      "namespace",
                      "full_name",
                      "html_url"
                    ],
                    "type": "object"
                  },
                  "sha": {
                    "description": "commit id",
                    "type": "string"
                  }
                },
                "required": [
                  "ref",
                  "sha",
                  "label",
                  "repo"
                ],
                "type": "object"
              },
              "body": {
                "description": "description",
                "type": "string"
              },
              "can_merge_check": {
                "description": "Merge Check",
                "type": "boolean"
              },
              "closed_at": {
                "description": "Close time",
                "type": "string"
              },
              "created_at": {
                "description": "creation time",
                "type": "string"
              },
              "draft": {
                "description": "Is it a draft",
                "type": "boolean"
              },
              "head": {
                "description": "commit message",
                "properties": {
                  "label": {
                    "description": "label",
                    "type": "string"
                  },
                  "ref": {
                    "description": "Branch Path",
                    "type": "string"
                  },
                  "repo": {
                    "description": "warehouse information",
                    "properties": {
                      "full_name": {
                        "type": "string"
                      },
                      "html_url": {
                        "type": "string"
                      },
                      "name": {
                        "type": "string"
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
                      "name",
                      "namespace",
                      "full_name",
                      "html_url"
                    ],
                    "type": "object"
                  },
                  "sha": {
                    "description": "commit id",
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
                      "id",
                      "login",
                      "name",
                      "avatar_url",
                      "html_url"
                    ],
                    "type": "object"
                  }
                },
                "required": [
                  "ref",
                  "sha",
                  "label",
                  "repo",
                  "user"
                ],
                "type": "object"
              },
              "html_url": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "issue_url": {
                "description": "Associated issue API URL",
                "type": "string"
              },
              "labels": {
                "description": "Tag Information",
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
                    "repository_id": {
                      "type": "integer"
                    },
                    "updated_at": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "color",
                    "name",
                    "repository_id",
                    "created_at",
                    "updated_at"
                  ],
                  "type": "object"
                },
                "type": "array"
              },
              "mergeable": {
                "description": "Is it possible to merge?",
                "type": "boolean"
              },
              "mergeable_state": {
                "description": "Access Control Information",
                "properties": {
                  "all_depend_merge_request_merged_passed": {
                    "description": "All dependent pull requests have been merged and passed.",
                    "type": "boolean"
                  },
                  "approval_approvers_required_passed": {
                    "description": "Is the code approval passed?",
                    "type": "boolean"
                  },
                  "approval_approvers_result": {
                    "type": "integer"
                  },
                  "approval_reviewers_required_passed": {
                    "description": "Is the code review passed?",
                    "type": "boolean"
                  },
                  "approval_testers_required_passed": {
                    "description": "Code test passed",
                    "type": "boolean"
                  },
                  "approval_testers_result": {
                    "type": "integer"
                  },
                  "branch_missing_passed": {
                    "description": "Branch missing through",
                    "type": "boolean"
                  },
                  "can_force_merge": {
                    "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation!!! You can forcibly merge it.",
                    "type": "boolean"
                  },
                  "check_tasks_num": {
                    "description": "Checked Items Total Number",
                    "type": "integer"
                  },
                  "ci_state_passed": {
                    "description": "CI Status via",
                    "type": "boolean"
                  },
                  "conflict_passed": {
                    "description": "Conflict through",
                    "type": "boolean"
                  },
                  "merge_by_self_passed": {
                    "description": "Self-merging through",
                    "type": "boolean"
                  },
                  "merge_request_id": {
                    "description": "Merge Request ID",
                    "type": "integer"
                  },
                  "merge_request_switch": {
                    "description": "Merge Request Switch",
                    "properties": {
                      "add_notes_after_merged": {
                        "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts besides the translation!! Add comments after merging",
                        "type": "boolean"
                      },
                      "approval_required_reviewers_branch": {
                        "description": "Approved Reviewer Branch",
                        "type": "string"
                      },
                      "approval_required_reviewers_count": {
                        "description": "Number of reviewers requiring approval",
                        "type": "integer"
                      },
                      "can_force_merge": {
                        "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation!!! You can forcibly merge it.",
                        "type": "boolean"
                      },
                      "can_reopen": {
                        "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! You can reopen it.",
                        "type": "boolean"
                      },
                      "disable_merge_by_self": {
                        "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts! Prohibited from self-merging!",
                        "type": "boolean"
                      },
                      "disable_squash_merge": {
                        "description": "Please translate the following content into professional English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation!!! Do not compress or merge!",
                        "type": "boolean"
                      },
                      "mark_auto_merged_mr_as_closed": {
                        "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts! Mark automatically merged MRs as closed.",
                        "type": "boolean"
                      },
                      "merge_method": {
                        "description": "Merge Method",
                        "type": "string"
                      },
                      "only_allow_merge_if_all_discussions_are_resolved": {
                        "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation!!! Only merge after all discussions are resolved.",
                        "type": "boolean"
                      },
                      "only_allow_merge_if_pipeline_succeeds": {
                        "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation!!! Only merge after successful pipeline.",
                        "type": "boolean"
                      },
                      "review_mode": {
                        "description": "Review mode",
                        "type": "string"
                      },
                      "squash_merge_with_no_merge_commit": {
                        "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation!!! No merged submission of compressed merge",
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "review_mode",
                      "merge_method",
                      "only_allow_merge_if_all_discussions_are_resolved",
                      "disable_merge_by_self",
                      "only_allow_merge_if_pipeline_succeeds",
                      "disable_squash_merge",
                      "squash_merge_with_no_merge_commit",
                      "approval_required_reviewers_count",
                      "approval_required_reviewers_branch",
                      "add_notes_after_merged",
                      "mark_auto_merged_mr_as_closed",
                      "can_force_merge",
                      "can_reopen"
                    ],
                    "type": "object"
                  },
                  "merged_by_user_passed": {
                    "description": "User merged through",
                    "type": "boolean"
                  },
                  "mr_state_passed": {
                    "description": "Merge Request Status Through",
                    "type": "boolean"
                  },
                  "non_ff_passed": {
                    "description": "Non-skippable through",
                    "type": "boolean"
                  },
                  "reason": {
                    "description": "Reason",
                    "properties": {},
                    "type": "object"
                  },
                  "resolve_discussion_passed": {
                    "description": "Resolve discussion passed",
                    "type": "boolean"
                  },
                  "state": {
                    "description": "Status",
                    "type": "boolean"
                  },
                  "status_without_user_auth": {
                    "description": "Status without user authorization",
                    "type": "boolean"
                  },
                  "work_in_progress_passed": {
                    "description": "Work progress through",
                    "type": "boolean"
                  }
                },
                "required": [
                  "merge_request_id",
                  "state",
                  "status_without_user_auth",
                  "conflict_passed",
                  "branch_missing_passed",
                  "non_ff_passed",
                  "mr_state_passed",
                  "merged_by_user_passed",
                  "work_in_progress_passed",
                  "resolve_discussion_passed",
                  "ci_state_passed",
                  "merge_by_self_passed",
                  "can_force_merge",
                  "approval_reviewers_required_passed",
                  "approval_approvers_required_passed",
                  "approval_testers_required_passed",
                  "merge_request_switch",
                  "reason",
                  "check_tasks_num",
                  "all_depend_merge_request_merged_passed",
                  "approval_approvers_result",
                  "approval_testers_result"
                ],
                "type": "object"
              },
              "merged_at": {
                "description": "Merge Time",
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
              "milestone": {
                "properties": {
                  "created_at": {
                    "type": "string"
                  },
                  "description": {
                    "type": "string"
                  },
                  "number": {
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
                  }
                },
                "required": [
                  "created_at",
                  "description",
                  "number",
                  "state",
                  "title",
                  "updated_at"
                ],
                "type": "object"
              },
              "number": {
                "description": "Serial number",
                "type": "integer"
              },
              "prune_branch": {
                "description": "Is the source branch forcibly deleted?",
                "type": "boolean"
              },
              "state": {
                "description": "Status, open/closed/merged",
                "type": "string"
              },
              "testers": {
                "description": "Test Person Information",
                "items": {
                  "properties": {
                    "accept": {
                      "type": "boolean"
                    },
                    "assignee": {
                      "type": "boolean"
                    },
                    "code_owner": {
                      "type": "boolean"
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
                  "type": "object"
                },
                "type": "array"
              },
              "title": {
                "description": "Title",
                "type": "string"
              },
              "updated_at": {
                "description": "Update time",
                "type": "string"
              },
              "url": {
                "description": "api url",
                "type": "string"
              },
              "user": {
                "description": "Creator Information",
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
              "visibility_reason": {
                "description": "Visibility, public: Publicly visible, other: Visible to project members only",
                "type": "string"
              }
            },
            "required": [
              "id",
              "html_url",
              "number",
              "state",
              "title",
              "url",
              "issue_url",
              "body",
              "assignees_number",
              "assignees",
              "testers",
              "approval_reviewers",
              "labels",
              "created_at",
              "updated_at",
              "closed_at",
              "merged_at",
              "draft",
              "can_merge_check",
              "prune_branch",
              "mergeable",
              "user",
              "head",
              "base",
              "mergeable_state",
              "milestone",
              "merged_by"
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
    "Pull Requests"
  ]
}
```
