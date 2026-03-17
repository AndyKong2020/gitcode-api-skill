# List authorized users' Pull Request list
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-users-merge-requests](https://docs.gitcode.com/en/docs/apis/get-api-v-5-users-merge-requests)
Category: Users
- Method: `GET`
- Path: `/api/v5/user/pulls`
- Operation ID: `get_api_v5_users_merge_requests`
- Tags: `Users`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| access_token | query | true | string | User authorization code |
| state | query | false | string | Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation! Return open, closed, locked, merged, or all merged requests, open: open; closed: closed; locked: locked; merged: merged; all: all. The default is to return all. |
| sort | query | false | string | Merge requests, created at: created; updated at: updated; merged at: merged_at. Sorted by created time by default. |
| direction | query | false | string | Merge requests sorted by the sort field in ascending or descending order, desc: descending; asc: ascending |
| labels | query | false | string | , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,...... |
| created_after | query | false | string | Return merge requests created after the specified time, time format is ISO 8601 for example: 2024-11-20T13:00:21+08:00 |
| created_before | query | false | string | Return the merge requests created before the specified time, the time format is ISO 8601, for example: 2024-11-20T13:00:21+08:00 |
| updated_after | query | false | string | Return the merge requests updated after the specified time, in ISO 8601 format, for example: 2024-11-20T13:00:21+08:00 |
| updated_before | query | false | string | Merge requests updated before the specified time, in ISO 8601 format, for example: 2024-11-20T13:00:21+08:00 |
| scope | query | false | string | Return the merged pull requests within the given range, need_my_approve: pull requests that need my approval; created_by_me: pull requests created by me; assigned_to_me: pull requests assigned to me; need_my_review: pull requests that need my review. By default, return the ones I created. |
| source_branch | query | false | string | Merge request with the given source branch |
| target_branch | query | false | string | Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts! Return the merge request with the given target branch |
| per_page | query | false | string | The number of items per page, with a maximum of 100. The default is 20. |
| page | query | false | string | The current page number |
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
      "added_lines": {
        "description": "New line added",
        "type": "integer"
      },
      "assignees": {
        "description": "Reviewers List",
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
            "email": {
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
            "name_cn": {
              "type": "string"
            },
            "object_id": {
              "type": "string"
            },
            "state": {
              "type": "string"
            },
            "user_id": {
              "type": "string"
            }
          },
          "required": [
            "user_id",
            "object_id",
            "id",
            "login",
            "name",
            "state",
            "avatar_url",
            "email",
            "name_cn",
            "html_url",
            "assignee",
            "code_owner",
            "accept"
          ],
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
            "type": "string"
          },
          "ref": {
            "type": "string"
          },
          "repo": {
            "properties": {
              "assigner": {
                "properties": {
                  "avatar_url": {
                    "type": "string"
                  },
                  "email": {
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
                  "name_cn": {
                    "type": "string"
                  },
                  "state": {
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "login",
                  "name",
                  "state",
                  "avatar_url",
                  "email",
                  "name_cn",
                  "html_url"
                ],
                "type": "object"
              },
              "description": {
                "type": "string"
              },
              "full_name": {
                "type": "string"
              },
              "full_path": {
                "type": "string"
              },
              "html_url": {
                "type": "string"
              },
              "human_name": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "internal": {
                "type": "boolean"
              },
              "name": {
                "type": "string"
              },
              "owner": {
                "properties": {
                  "avatar_url": {
                    "type": "string"
                  },
                  "email": {
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
                  "name_cn": {
                    "type": "string"
                  },
                  "state": {
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "login",
                  "name",
                  "state",
                  "avatar_url",
                  "email",
                  "name_cn",
                  "html_url"
                ],
                "type": "object"
              },
              "path": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "full_path",
              "full_name",
              "human_name",
              "name",
              "path",
              "description",
              "owner",
              "assigner",
              "internal",
              "html_url"
            ],
            "type": "object"
          },
          "user": {
            "properties": {
              "avatar_url": {
                "type": "string"
              },
              "email": {
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
              "name_cn": {
                "type": "string"
              },
              "state": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "login",
              "name",
              "state",
              "avatar_url",
              "email",
              "name_cn",
              "html_url"
            ],
            "type": "object"
          }
        },
        "required": [
          "label",
          "ref",
          "user",
          "repo"
        ],
        "type": "object"
      },
      "body": {
        "description": "description",
        "type": "string"
      },
      "close_related_issue": {
        "description": "Close the associated issue after merging",
        "type": "integer"
      },
      "closed_at": {
        "description": "Close time",
        "type": "string"
      },
      "closed_by": {
        "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts!!! Close personal information",
        "properties": {
          "avatar_url": {
            "type": "string"
          },
          "email": {
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
        "required": [
          "id",
          "name",
          "username",
          "iam_id",
          "nick_name",
          "state",
          "avatar_url",
          "email",
          "name_cn",
          "web_url"
        ],
        "type": "object"
      },
      "created_at": {
        "description": "creation time",
        "type": "string"
      },
      "diff_refs": {
        "description": "Difference Citation",
        "properties": {
          "base_sha": {
            "type": "string"
          },
          "head_sha": {
            "type": "string"
          },
          "start_sha": {
            "type": "string"
          }
        },
        "required": [
          "base_sha",
          "head_sha",
          "start_sha"
        ],
        "type": "object"
      },
      "draft": {
        "description": "Is it a draft status",
        "type": "boolean"
      },
      "head": {
        "description": "commit message",
        "properties": {
          "label": {
            "type": "string"
          },
          "ref": {
            "type": "string"
          },
          "repo": {
            "properties": {
              "assigner": {
                "properties": {
                  "avatar_url": {
                    "type": "string"
                  },
                  "email": {
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
                  "name_cn": {
                    "type": "string"
                  },
                  "state": {
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "login",
                  "name",
                  "state",
                  "avatar_url",
                  "email",
                  "name_cn",
                  "html_url"
                ],
                "type": "object"
              },
              "description": {
                "type": "string"
              },
              "full_name": {
                "type": "string"
              },
              "full_path": {
                "type": "string"
              },
              "html_url": {
                "type": "string"
              },
              "human_name": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "internal": {
                "type": "boolean"
              },
              "name": {
                "type": "string"
              },
              "owner": {
                "properties": {
                  "avatar_url": {
                    "type": "string"
                  },
                  "email": {
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
                  "name_cn": {
                    "type": "string"
                  },
                  "state": {
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "login",
                  "name",
                  "state",
                  "avatar_url",
                  "email",
                  "name_cn",
                  "html_url"
                ],
                "type": "object"
              },
              "path": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "full_path",
              "full_name",
              "human_name",
              "name",
              "path",
              "description",
              "owner",
              "assigner",
              "internal",
              "html_url"
            ],
            "type": "object"
          },
          "user": {
            "properties": {
              "avatar_url": {
                "type": "string"
              },
              "email": {
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
              "name_cn": {
                "type": "string"
              },
              "state": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "login",
              "name",
              "state",
              "avatar_url",
              "email",
              "name_cn",
              "html_url"
            ],
            "type": "object"
          }
        },
        "required": [
          "label",
          "ref",
          "user",
          "repo"
        ],
        "type": "object"
      },
      "html_url": {
        "description": "Page Address",
        "type": "string"
      },
      "id": {
        "type": "integer"
      },
      "iid": {
        "type": "integer"
      },
      "labels": {
        "description": "Label",
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
            },
            "repository_id": {
              "type": "integer"
            },
            "title": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "color",
            "name",
            "title",
            "repository_id"
          ],
          "type": "object"
        },
        "type": "array"
      },
      "locked": {
        "description": "Locked",
        "type": "boolean"
      },
      "merge_request_type": {
        "description": "Pull Request Type",
        "type": "string"
      },
      "mergeable": {
        "description": "Is it possible to merge?",
        "type": "boolean"
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
      "notes": {
        "description": "Comment count",
        "type": "integer"
      },
      "number": {
        "description": "Serial number",
        "type": "integer"
      },
      "project_id": {
        "description": "Project ID",
        "type": "integer"
      },
      "removed_lines": {
        "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts! Delete the number of lines.",
        "type": "integer"
      },
      "source_branch": {
        "description": "Source branch",
        "type": "string"
      },
      "source_git_url": {
        "type": "string"
      },
      "source_project_id": {
        "description": "Source project id",
        "type": "integer"
      },
      "state": {
        "description": "Status, open/closed/merged",
        "type": "string"
      },
      "target_branch": {
        "description": "Target branch",
        "type": "string"
      },
      "testers": {
        "description": "Test Person List",
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
            "email": {
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
            "name_cn": {
              "type": "string"
            },
            "object_id": {
              "type": "string"
            },
            "state": {
              "type": "string"
            },
            "user_id": {
              "type": "string"
            }
          },
          "required": [
            "user_id",
            "object_id",
            "id",
            "login",
            "name",
            "state",
            "avatar_url",
            "email",
            "name_cn",
            "html_url",
            "assignee",
            "accept"
          ],
          "type": "object"
        },
        "type": "array"
      },
      "testers_number": {
        "description": "Number of testers",
        "type": "integer"
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
        "type": "string"
      },
      "user": {
        "description": "Author",
        "properties": {
          "avatar_url": {
            "type": "string"
          },
          "email": {
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
          "name_cn": {
            "type": "string"
          },
          "object_id": {
            "type": "string"
          },
          "state": {
            "type": "string"
          },
          "user_id": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "user_id",
          "object_id",
          "login",
          "name",
          "state",
          "avatar_url",
          "email",
          "name_cn",
          "html_url"
        ],
        "type": "object"
      },
      "visibility_reason": {
        "description": "Visibility, public: Publicly visible, other: Visible to project members only",
        "type": "string"
      },
      "web_url": {
        "type": "string"
      }
    },
    "required": [
      "number",
      "html_url",
      "url",
      "close_related_issue",
      "draft",
      "labels",
      "user",
      "assignees",
      "testers",
      "head",
      "base",
      "id",
      "iid",
      "project_id",
      "title",
      "body",
      "state",
      "assignees_number",
      "testers_number",
      "created_at",
      "updated_at",
      "merged_at",
      "closed_at",
      "target_branch",
      "source_branch",
      "source_project_id",
      "web_url",
      "merge_request_type",
      "added_lines",
      "removed_lines",
      "diff_refs",
      "notes",
      "source_git_url",
      "mergeable",
      "locked",
      "closed_by"
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
  "operationId": "get_api_v5_users_merge_requests",
  "parameters": [
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
      "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation! Return open, closed, locked, merged, or all merged requests, open: open; closed: closed; locked: locked; merged: merged; all: all. The default is to return all.",
      "in": "query",
      "name": "state",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Merge requests, created at: created; updated at: updated; merged at: merged_at. Sorted by created time by default.",
      "in": "query",
      "name": "sort",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Merge requests sorted by the sort field in ascending or descending order, desc: descending; asc: ascending",
      "in": "query",
      "name": "direction",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": ", , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,......",
      "in": "query",
      "name": "labels",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Return merge requests created after the specified time, time format is ISO 8601 for example: 2024-11-20T13:00:21+08:00",
      "in": "query",
      "name": "created_after",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Return the merge requests created before the specified time, the time format is ISO 8601, for example: 2024-11-20T13:00:21+08:00",
      "in": "query",
      "name": "created_before",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Return the merge requests updated after the specified time, in ISO 8601 format, for example: 2024-11-20T13:00:21+08:00",
      "in": "query",
      "name": "updated_after",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Merge requests updated before the specified time, in ISO 8601 format, for example: 2024-11-20T13:00:21+08:00",
      "in": "query",
      "name": "updated_before",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Return the merged pull requests within the given range, need_my_approve: pull requests that need my approval; created_by_me: pull requests created by me; assigned_to_me: pull requests assigned to me; need_my_review: pull requests that need my review. By default, return the ones I created.",
      "in": "query",
      "name": "scope",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Merge request with the given source branch",
      "in": "query",
      "name": "source_branch",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts! Return the merge request with the given target branch",
      "in": "query",
      "name": "target_branch",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "The number of items per page, with a maximum of 100. The default is 20.",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "The current page number",
      "in": "query",
      "name": "page",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/user/pulls",
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
    "name": "List authorized users' Pull Request list",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "user",
        "pulls"
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
            "content": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation! Return open, closed, locked, merged, or all merged requests, open: open; closed: closed; locked: locked; merged: merged; all: all. The default is to return all.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "state",
          "value": ""
        },
        {
          "description": {
            "content": "Merge requests, created at: created; updated at: updated; merged at: merged_at. Sorted by created time by default.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sort",
          "value": ""
        },
        {
          "description": {
            "content": "Merge requests sorted by the sort field in ascending or descending order, desc: descending; asc: ascending",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "direction",
          "value": ""
        },
        {
          "description": {
            "content": ", , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,......",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "labels",
          "value": ""
        },
        {
          "description": {
            "content": "Return merge requests created after the specified time, time format is ISO 8601 for example: 2024-11-20T13:00:21+08:00",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "created_after",
          "value": ""
        },
        {
          "description": {
            "content": "Return the merge requests created before the specified time, the time format is ISO 8601, for example: 2024-11-20T13:00:21+08:00",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "created_before",
          "value": ""
        },
        {
          "description": {
            "content": "Return the merge requests updated after the specified time, in ISO 8601 format, for example: 2024-11-20T13:00:21+08:00",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "updated_after",
          "value": ""
        },
        {
          "description": {
            "content": "Merge requests updated before the specified time, in ISO 8601 format, for example: 2024-11-20T13:00:21+08:00",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "updated_before",
          "value": ""
        },
        {
          "description": {
            "content": "Return the merged pull requests within the given range, need_my_approve: pull requests that need my approval; created_by_me: pull requests created by me; assigned_to_me: pull requests assigned to me; need_my_review: pull requests that need my review. By default, return the ones I created.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "scope",
          "value": ""
        },
        {
          "description": {
            "content": "Merge request with the given source branch",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "source_branch",
          "value": ""
        },
        {
          "description": {
            "content": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts! Return the merge request with the given target branch",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "target_branch",
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
            "content": "The current page number",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "page",
          "value": ""
        }
      ],
      "variable": []
    }
  },
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "schema": {
            "items": {
              "properties": {
                "added_lines": {
                  "description": "New line added",
                  "type": "integer"
                },
                "assignees": {
                  "description": "Reviewers List",
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
                      "email": {
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
                      "name_cn": {
                        "type": "string"
                      },
                      "object_id": {
                        "type": "string"
                      },
                      "state": {
                        "type": "string"
                      },
                      "user_id": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "user_id",
                      "object_id",
                      "id",
                      "login",
                      "name",
                      "state",
                      "avatar_url",
                      "email",
                      "name_cn",
                      "html_url",
                      "assignee",
                      "code_owner",
                      "accept"
                    ],
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
                      "type": "string"
                    },
                    "ref": {
                      "type": "string"
                    },
                    "repo": {
                      "properties": {
                        "assigner": {
                          "properties": {
                            "avatar_url": {
                              "type": "string"
                            },
                            "email": {
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
                            "name_cn": {
                              "type": "string"
                            },
                            "state": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "login",
                            "name",
                            "state",
                            "avatar_url",
                            "email",
                            "name_cn",
                            "html_url"
                          ],
                          "type": "object"
                        },
                        "description": {
                          "type": "string"
                        },
                        "full_name": {
                          "type": "string"
                        },
                        "full_path": {
                          "type": "string"
                        },
                        "html_url": {
                          "type": "string"
                        },
                        "human_name": {
                          "type": "string"
                        },
                        "id": {
                          "type": "integer"
                        },
                        "internal": {
                          "type": "boolean"
                        },
                        "name": {
                          "type": "string"
                        },
                        "owner": {
                          "properties": {
                            "avatar_url": {
                              "type": "string"
                            },
                            "email": {
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
                            "name_cn": {
                              "type": "string"
                            },
                            "state": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "login",
                            "name",
                            "state",
                            "avatar_url",
                            "email",
                            "name_cn",
                            "html_url"
                          ],
                          "type": "object"
                        },
                        "path": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "full_path",
                        "full_name",
                        "human_name",
                        "name",
                        "path",
                        "description",
                        "owner",
                        "assigner",
                        "internal",
                        "html_url"
                      ],
                      "type": "object"
                    },
                    "user": {
                      "properties": {
                        "avatar_url": {
                          "type": "string"
                        },
                        "email": {
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
                        "name_cn": {
                          "type": "string"
                        },
                        "state": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "login",
                        "name",
                        "state",
                        "avatar_url",
                        "email",
                        "name_cn",
                        "html_url"
                      ],
                      "type": "object"
                    }
                  },
                  "required": [
                    "label",
                    "ref",
                    "user",
                    "repo"
                  ],
                  "type": "object"
                },
                "body": {
                  "description": "description",
                  "type": "string"
                },
                "close_related_issue": {
                  "description": "Close the associated issue after merging",
                  "type": "integer"
                },
                "closed_at": {
                  "description": "Close time",
                  "type": "string"
                },
                "closed_by": {
                  "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts!!! Close personal information",
                  "properties": {
                    "avatar_url": {
                      "type": "string"
                    },
                    "email": {
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
                  "required": [
                    "id",
                    "name",
                    "username",
                    "iam_id",
                    "nick_name",
                    "state",
                    "avatar_url",
                    "email",
                    "name_cn",
                    "web_url"
                  ],
                  "type": "object"
                },
                "created_at": {
                  "description": "creation time",
                  "type": "string"
                },
                "diff_refs": {
                  "description": "Difference Citation",
                  "properties": {
                    "base_sha": {
                      "type": "string"
                    },
                    "head_sha": {
                      "type": "string"
                    },
                    "start_sha": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "base_sha",
                    "head_sha",
                    "start_sha"
                  ],
                  "type": "object"
                },
                "draft": {
                  "description": "Is it a draft status",
                  "type": "boolean"
                },
                "head": {
                  "description": "commit message",
                  "properties": {
                    "label": {
                      "type": "string"
                    },
                    "ref": {
                      "type": "string"
                    },
                    "repo": {
                      "properties": {
                        "assigner": {
                          "properties": {
                            "avatar_url": {
                              "type": "string"
                            },
                            "email": {
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
                            "name_cn": {
                              "type": "string"
                            },
                            "state": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "login",
                            "name",
                            "state",
                            "avatar_url",
                            "email",
                            "name_cn",
                            "html_url"
                          ],
                          "type": "object"
                        },
                        "description": {
                          "type": "string"
                        },
                        "full_name": {
                          "type": "string"
                        },
                        "full_path": {
                          "type": "string"
                        },
                        "html_url": {
                          "type": "string"
                        },
                        "human_name": {
                          "type": "string"
                        },
                        "id": {
                          "type": "integer"
                        },
                        "internal": {
                          "type": "boolean"
                        },
                        "name": {
                          "type": "string"
                        },
                        "owner": {
                          "properties": {
                            "avatar_url": {
                              "type": "string"
                            },
                            "email": {
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
                            "name_cn": {
                              "type": "string"
                            },
                            "state": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "login",
                            "name",
                            "state",
                            "avatar_url",
                            "email",
                            "name_cn",
                            "html_url"
                          ],
                          "type": "object"
                        },
                        "path": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "full_path",
                        "full_name",
                        "human_name",
                        "name",
                        "path",
                        "description",
                        "owner",
                        "assigner",
                        "internal",
                        "html_url"
                      ],
                      "type": "object"
                    },
                    "user": {
                      "properties": {
                        "avatar_url": {
                          "type": "string"
                        },
                        "email": {
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
                        "name_cn": {
                          "type": "string"
                        },
                        "state": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "login",
                        "name",
                        "state",
                        "avatar_url",
                        "email",
                        "name_cn",
                        "html_url"
                      ],
                      "type": "object"
                    }
                  },
                  "required": [
                    "label",
                    "ref",
                    "user",
                    "repo"
                  ],
                  "type": "object"
                },
                "html_url": {
                  "description": "Page Address",
                  "type": "string"
                },
                "id": {
                  "type": "integer"
                },
                "iid": {
                  "type": "integer"
                },
                "labels": {
                  "description": "Label",
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
                      },
                      "repository_id": {
                        "type": "integer"
                      },
                      "title": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "id",
                      "color",
                      "name",
                      "title",
                      "repository_id"
                    ],
                    "type": "object"
                  },
                  "type": "array"
                },
                "locked": {
                  "description": "Locked",
                  "type": "boolean"
                },
                "merge_request_type": {
                  "description": "Pull Request Type",
                  "type": "string"
                },
                "mergeable": {
                  "description": "Is it possible to merge?",
                  "type": "boolean"
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
                "notes": {
                  "description": "Comment count",
                  "type": "integer"
                },
                "number": {
                  "description": "Serial number",
                  "type": "integer"
                },
                "project_id": {
                  "description": "Project ID",
                  "type": "integer"
                },
                "removed_lines": {
                  "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts! Delete the number of lines.",
                  "type": "integer"
                },
                "source_branch": {
                  "description": "Source branch",
                  "type": "string"
                },
                "source_git_url": {
                  "type": "string"
                },
                "source_project_id": {
                  "description": "Source project id",
                  "type": "integer"
                },
                "state": {
                  "description": "Status, open/closed/merged",
                  "type": "string"
                },
                "target_branch": {
                  "description": "Target branch",
                  "type": "string"
                },
                "testers": {
                  "description": "Test Person List",
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
                      "email": {
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
                      "name_cn": {
                        "type": "string"
                      },
                      "object_id": {
                        "type": "string"
                      },
                      "state": {
                        "type": "string"
                      },
                      "user_id": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "user_id",
                      "object_id",
                      "id",
                      "login",
                      "name",
                      "state",
                      "avatar_url",
                      "email",
                      "name_cn",
                      "html_url",
                      "assignee",
                      "accept"
                    ],
                    "type": "object"
                  },
                  "type": "array"
                },
                "testers_number": {
                  "description": "Number of testers",
                  "type": "integer"
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
                  "type": "string"
                },
                "user": {
                  "description": "Author",
                  "properties": {
                    "avatar_url": {
                      "type": "string"
                    },
                    "email": {
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
                    "name_cn": {
                      "type": "string"
                    },
                    "object_id": {
                      "type": "string"
                    },
                    "state": {
                      "type": "string"
                    },
                    "user_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "user_id",
                    "object_id",
                    "login",
                    "name",
                    "state",
                    "avatar_url",
                    "email",
                    "name_cn",
                    "html_url"
                  ],
                  "type": "object"
                },
                "visibility_reason": {
                  "description": "Visibility, public: Publicly visible, other: Visible to project members only",
                  "type": "string"
                },
                "web_url": {
                  "type": "string"
                }
              },
              "required": [
                "number",
                "html_url",
                "url",
                "close_related_issue",
                "draft",
                "labels",
                "user",
                "assignees",
                "testers",
                "head",
                "base",
                "id",
                "iid",
                "project_id",
                "title",
                "body",
                "state",
                "assignees_number",
                "testers_number",
                "created_at",
                "updated_at",
                "merged_at",
                "closed_at",
                "target_branch",
                "source_branch",
                "source_project_id",
                "web_url",
                "merge_request_type",
                "added_lines",
                "removed_lines",
                "diff_refs",
                "notes",
                "source_git_url",
                "mergeable",
                "locked",
                "closed_by"
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
  "tags": [
    "Users"
  ]
}
```
