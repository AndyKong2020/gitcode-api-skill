# Create Pull Request
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-pulls](https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-pulls)
Category: Pull Requests
- Method: `POST`
- Path: `/api/v5/repos/{owner}/{repo}/pulls`
- Operation ID: `post_api_v5_repos_{owner}_{repo}_pulls`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "assignees": {
      "description": "Optional. Reviewers' usernames, multiple can be specified, separated by half-width commas, e.g., (username1,username2). Note: This option is无效当仓库代码审查设置中已设置【指派审查人员】.",
      "type": "string"
    },
    "base": {
      "description": "Required. The name of the target branch for the Pull Request submission.",
      "type": "string"
    },
    "body": {
      "description": "Optional. Content of the Pull Request",
      "type": "string"
    },
    "close_related_issue": {
      "description": "Optional, whether to close associated Issues after merging, default is set according to the repository configuration",
      "type": "boolean"
    },
    "draft": {
      "description": "Whether to set as draft Default false",
      "type": "boolean"
    },
    "fork_path": {
      "description": "fork project path 【owner/repo】, required for cross-repository PRs.",
      "type": "string"
    },
    "head": {
      "description": "Required. The source branch of the Pull Request submission. Format: branch. If cross-repository PR, pass: username:branch",
      "type": "string"
    },
    "issue": {
      "description": "Optional. The title and body of the Pull Request can be automatically filled based on the specified Issue ID.",
      "type": "string"
    },
    "labels": {
      "description": "A comma-separated list of labels, where the name must be between 2-20 characters long and cannot contain special characters. For example: bug,performance",
      "type": "string"
    },
    "milestone_number": {
      "description": "Optional. Milestone sequence number (id)",
      "type": "integer"
    },
    "prune_source_branch": {
      "description": "Optional. Whether to delete the source branch after merging the PR. Defaults to false (do not delete).",
      "type": "boolean"
    },
    "squash": {
      "description": "When using flat (squash) merging while accepting a Pull Request, defaults to false.",
      "type": "boolean"
    },
    "squash_commit_message": {
      "description": "squash commit messages",
      "type": "string"
    },
    "testers": {
      "description": "Optional. Testers' username, multiple usernames can be provided, separated by half-width commas, e.g., (username1,username2). Note: This option is无效当 repository code review settings have already set 【Assign Testers】.",
      "type": "string"
    },
    "title": {
      "description": "Required. Pull Request title",
      "type": "string"
    }
  },
  "required": [
    "title",
    "head",
    "base"
  ],
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
    "added_lines": {
      "type": "integer"
    },
    "allow_collaboration": {
      "type": "null"
    },
    "allow_maintainer_to_push": {
      "type": "null"
    },
    "approval_merge_request_approvers": {
      "items": {
        "properties": {
          "avatar_url": {
            "type": "string"
          },
          "email": {
            "type": "null"
          },
          "id": {
            "type": "integer"
          },
          "is_codeowner": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "name_cn": {
            "type": "string"
          },
          "nick_name": {
            "type": "null"
          },
          "state": {
            "type": "string"
          },
          "updated_at": {
            "type": "string"
          },
          "username": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "approval_merge_request_reviewers": {
      "items": {
        "properties": {
          "avatar_url": {
            "type": "string"
          },
          "email": {
            "type": "null"
          },
          "id": {
            "type": "integer"
          },
          "is_codeowner": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "name_cn": {
            "type": "string"
          },
          "nick_name": {
            "type": "null"
          },
          "state": {
            "type": "string"
          },
          "updated_at": {
            "type": "string"
          },
          "username": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "approval_merge_request_testers": {
      "items": {
        "properties": {
          "avatar_url": {
            "type": "string"
          },
          "email": {
            "type": "null"
          },
          "id": {
            "type": "integer"
          },
          "is_codeowner": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "name_cn": {
            "type": "string"
          },
          "nick_name": {
            "type": "null"
          },
          "state": {
            "type": "string"
          },
          "updated_at": {
            "type": "string"
          },
          "username": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "assignee": {
      "type": "null"
    },
    "author": {
      "properties": {
        "avatar_path": {
          "type": "null"
        },
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
        "is_member": {
          "type": "null"
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
        "tenant_name": {
          "type": "null"
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
    "auto_merge": {
      "type": "null"
    },
    "can_delete_source_branch": {
      "type": "integer"
    },
    "changes_count": {
      "type": "string"
    },
    "closed_at": {
      "type": "null"
    },
    "closed_by": {
      "type": "null"
    },
    "codequality_status": {
      "type": "string"
    },
    "comments_url": {
      "type": "string"
    },
    "commits_url": {
      "type": "string"
    },
    "created_at": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "description_html": {
      "type": "null"
    },
    "diff_refs": {
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
      "type": "object"
    },
    "diff_url": {
      "type": "string"
    },
    "discussion_locked": {
      "type": "null"
    },
    "diverged_commits_count": {
      "type": "null"
    },
    "downvotes": {
      "type": "integer"
    },
    "e2e_issues": {
      "items": {
        "properties": {
          "auto_c_when_mr_merged": {
            "type": "integer"
          },
          "check_fail_reason": {
            "type": "string"
          },
          "check_result": {
            "type": "integer"
          },
          "commit_id": {
            "type": "null"
          },
          "created_at": {
            "type": "string"
          },
          "id": {
            "type": "integer"
          },
          "issue_link": {
            "type": "string"
          },
          "issue_num": {
            "type": "string"
          },
          "issue_project": {
            "type": "null"
          },
          "issue_project_id": {
            "type": "integer"
          },
          "issue_type": {
            "type": "integer"
          },
          "linked_issue_type": {
            "type": "null"
          },
          "merge_request_id": {
            "type": "integer"
          },
          "mks_id": {
            "type": "null"
          },
          "pbi_id": {
            "type": "null"
          },
          "pbi_name": {
            "type": "null"
          },
          "source": {
            "type": "null"
          },
          "title": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "first_deployed_to_production_at": {
      "type": "null"
    },
    "force_remove_source_branch": {
      "type": "integer"
    },
    "forked_project_name": {
      "type": "null"
    },
    "from_forked_project": {
      "type": "integer"
    },
    "gate_check": {
      "type": "integer"
    },
    "has_pre_merge_ref": {
      "type": "integer"
    },
    "head_pipeline_id": {
      "type": "null"
    },
    "html_url": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "is_source_branch_exist": {
      "type": "integer"
    },
    "issue_url": {
      "type": "string"
    },
    "json_merge_error": {
      "type": "null"
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
          },
          "textColor": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "type": {
            "type": "null"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "latest_build_finished_at": {
      "type": "null"
    },
    "latest_build_started_at": {
      "type": "null"
    },
    "merge_commit_sha": {
      "type": "null"
    },
    "merge_error": {
      "type": "null"
    },
    "merge_request_assignee_list": {
      "items": {
        "properties": {},
        "type": "object"
      },
      "type": "array"
    },
    "merge_request_review_count": {
      "type": "integer"
    },
    "merge_request_reviewer_list": {
      "items": {
        "properties": {},
        "type": "object"
      },
      "type": "array"
    },
    "merge_request_reviewers_count": {
      "type": "integer"
    },
    "merge_request_type": {
      "type": "string"
    },
    "merge_status": {
      "type": "string"
    },
    "merge_when_pipeline_succeeds": {
      "type": "integer"
    },
    "merged_at": {
      "type": "null"
    },
    "merged_by": {
      "type": "null"
    },
    "milestone": {
      "type": "null"
    },
    "notes": {
      "type": "integer"
    },
    "number": {
      "type": "integer"
    },
    "omega_mode": {
      "type": "integer"
    },
    "patch_url": {
      "type": "string"
    },
    "pipeline": {
      "type": "null"
    },
    "pipeline_status": {
      "type": "string"
    },
    "pipeline_status_with_code_quality": {
      "type": "string"
    },
    "rebase_in_progress": {
      "type": "null"
    },
    "removed_lines": {
      "type": "integer"
    },
    "required_reviewers": {
      "items": {
        "properties": {},
        "type": "object"
      },
      "type": "array"
    },
    "review_comment_url": {
      "type": "string"
    },
    "review_comments_url": {
      "type": "string"
    },
    "review_mode": {
      "type": "string"
    },
    "root_mr_locked_detail": {
      "type": "null"
    },
    "sha": {
      "type": "string"
    },
    "should_remove_source_branch": {
      "type": "integer"
    },
    "source_branch": {
      "type": "string"
    },
    "source_git_url": {
      "type": "string"
    },
    "source_project": {
      "properties": {
        "archived": {
          "type": "integer"
        },
        "avatar_url": {
          "type": "null"
        },
        "branch_count": {
          "type": "null"
        },
        "created_at": {
          "type": "string"
        },
        "creator": {
          "properties": {
            "avatar_path": {
              "type": "null"
            },
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
            "is_member": {
              "type": "null"
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
            "tenant_name": {
              "type": "null"
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
        "creator_id": {
          "type": "integer"
        },
        "default_branch": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "develop_mode": {
          "type": "string"
        },
        "empty_repo": {
          "type": "integer"
        },
        "forked_from_project": {
          "type": "null"
        },
        "forks_count": {
          "type": "integer"
        },
        "has_updated_kia": {
          "type": "integer"
        },
        "http_url_to_repo": {
          "type": "string"
        },
        "id": {
          "type": "integer"
        },
        "is_kia": {
          "type": "integer"
        },
        "item_type": {
          "type": "string"
        },
        "last_activity_at": {
          "type": "string"
        },
        "license": {
          "properties": {
            "html_url": {
              "type": "null"
            },
            "key": {
              "type": "string"
            },
            "name": {
              "type": "null"
            },
            "nickname": {
              "type": "null"
            },
            "source_url": {
              "type": "null"
            }
          },
          "type": "object"
        },
        "license_url": {
          "type": "null"
        },
        "main_repository_language": {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "member_count": {
          "type": "null"
        },
        "member_mgnt_mode": {
          "type": "integer"
        },
        "mirror_project_data": {
          "type": "null"
        },
        "name": {
          "type": "string"
        },
        "name_with_namespace": {
          "type": "string"
        },
        "namespace": {
          "properties": {
            "cell": {
              "type": "string"
            },
            "develop_mode": {
              "type": "string"
            },
            "enable_file_control": {
              "type": "null"
            },
            "full_name": {
              "type": "string"
            },
            "full_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "kind": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "owner_id": {
              "type": "null"
            },
            "parent_id": {
              "type": "null"
            },
            "path": {
              "type": "string"
            },
            "region": {
              "type": "null"
            },
            "visibility_level": {
              "type": "integer"
            }
          },
          "type": "object"
        },
        "network_type": {
          "type": "string"
        },
        "open_change_requests_count": {
          "type": "null"
        },
        "open_external_wiki": {
          "type": "integer"
        },
        "open_issues_count": {
          "type": "integer"
        },
        "open_merge_requests_count": {
          "type": "integer"
        },
        "owner": {
          "type": "null"
        },
        "path": {
          "type": "string"
        },
        "path_with_namespace": {
          "type": "string"
        },
        "product_id": {
          "type": "string"
        },
        "product_name": {
          "type": "null"
        },
        "readme_url": {
          "type": "string"
        },
        "release_count": {
          "type": "null"
        },
        "repo_replica_urls": {
          "type": "null"
        },
        "security": {
          "type": "string"
        },
        "ssh_url_to_repo": {
          "type": "string"
        },
        "star_count": {
          "type": "integer"
        },
        "starred": {
          "type": "integer"
        },
        "statistics": {
          "type": "null"
        },
        "tag_count": {
          "type": "null"
        },
        "tag_list": {
          "items": {
            "properties": {},
            "type": "object"
          },
          "type": "array"
        },
        "updated_at": {
          "type": "string"
        },
        "visibility": {
          "type": "string"
        },
        "watch_count": {
          "type": "integer"
        },
        "web_url": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "source_project_id": {
      "type": "integer"
    },
    "squash": {
      "type": "integer"
    },
    "squash_commit_message": {
      "type": "null"
    },
    "state": {
      "type": "string"
    },
    "subscribed": {
      "type": "integer"
    },
    "target_branch": {
      "type": "string"
    },
    "target_project": {
      "properties": {
        "archived": {
          "type": "integer"
        },
        "avatar_url": {
          "type": "null"
        },
        "branch_count": {
          "type": "null"
        },
        "created_at": {
          "type": "string"
        },
        "creator": {
          "properties": {
            "avatar_path": {
              "type": "null"
            },
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
            "is_member": {
              "type": "null"
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
            "tenant_name": {
              "type": "null"
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
        "creator_id": {
          "type": "integer"
        },
        "default_branch": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "develop_mode": {
          "type": "string"
        },
        "empty_repo": {
          "type": "integer"
        },
        "forked_from_project": {
          "type": "null"
        },
        "forks_count": {
          "type": "integer"
        },
        "has_updated_kia": {
          "type": "integer"
        },
        "http_url_to_repo": {
          "type": "string"
        },
        "id": {
          "type": "integer"
        },
        "is_kia": {
          "type": "integer"
        },
        "item_type": {
          "type": "string"
        },
        "last_activity_at": {
          "type": "string"
        },
        "license": {
          "properties": {
            "html_url": {
              "type": "null"
            },
            "key": {
              "type": "string"
            },
            "name": {
              "type": "null"
            },
            "nickname": {
              "type": "null"
            },
            "source_url": {
              "type": "null"
            }
          },
          "type": "object"
        },
        "license_url": {
          "type": "null"
        },
        "main_repository_language": {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "member_count": {
          "type": "null"
        },
        "member_mgnt_mode": {
          "type": "integer"
        },
        "mirror_project_data": {
          "type": "null"
        },
        "name": {
          "type": "string"
        },
        "name_with_namespace": {
          "type": "string"
        },
        "namespace": {
          "properties": {
            "cell": {
              "type": "string"
            },
            "develop_mode": {
              "type": "string"
            },
            "enable_file_control": {
              "type": "null"
            },
            "full_name": {
              "type": "string"
            },
            "full_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "kind": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "owner_id": {
              "type": "null"
            },
            "parent_id": {
              "type": "null"
            },
            "path": {
              "type": "string"
            },
            "region": {
              "type": "null"
            },
            "visibility_level": {
              "type": "integer"
            }
          },
          "type": "object"
        },
        "network_type": {
          "type": "string"
        },
        "open_change_requests_count": {
          "type": "null"
        },
        "open_external_wiki": {
          "type": "integer"
        },
        "open_issues_count": {
          "type": "integer"
        },
        "open_merge_requests_count": {
          "type": "integer"
        },
        "owner": {
          "type": "null"
        },
        "path": {
          "type": "string"
        },
        "path_with_namespace": {
          "type": "string"
        },
        "product_id": {
          "type": "string"
        },
        "product_name": {
          "type": "null"
        },
        "readme_url": {
          "type": "string"
        },
        "release_count": {
          "type": "null"
        },
        "repo_replica_urls": {
          "type": "null"
        },
        "security": {
          "type": "string"
        },
        "ssh_url_to_repo": {
          "type": "string"
        },
        "star_count": {
          "type": "integer"
        },
        "starred": {
          "type": "integer"
        },
        "statistics": {
          "type": "null"
        },
        "tag_count": {
          "type": "null"
        },
        "tag_list": {
          "items": {
            "properties": {},
            "type": "object"
          },
          "type": "array"
        },
        "updated_at": {
          "type": "string"
        },
        "visibility": {
          "type": "string"
        },
        "watch_count": {
          "type": "integer"
        },
        "web_url": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "target_project_id": {
      "type": "integer"
    },
    "time_stats": {
      "properties": {
        "human_time_estimate": {
          "type": "null"
        },
        "human_total_time_spent": {
          "type": "null"
        },
        "time_estimate": {
          "type": "null"
        },
        "total_time_spent": {
          "type": "integer"
        }
      },
      "type": "object"
    },
    "title": {
      "type": "string"
    },
    "title_html": {
      "type": "null"
    },
    "unresolved_discussions_count": {
      "type": "integer"
    },
    "updated_at": {
      "type": "string"
    },
    "upvotes": {
      "type": "integer"
    },
    "url": {
      "type": "string"
    },
    "user": {
      "properties": {
        "can_merge": {
          "type": "integer"
        }
      },
      "type": "object"
    },
    "user_notes_count": {
      "type": "integer"
    },
    "web_url": {
      "type": "string"
    },
    "work_in_progress": {
      "type": "integer"
    }
  },
  "type": "object"
}
```
Example:
```json
{
  "added_lines": 19860,
  "allow_collaboration": null,
  "allow_maintainer_to_push": null,
  "approval_merge_request_approvers": [
    {
      "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ee/dc/7602704ee7dcf13f4383a72d492b1813823afba729ae6e9115877a4a0128d990.jpg?time=1711447395118",
      "email": null,
      "id": 277,
      "is_codeowner": false,
      "name": "renww",
      "name_cn": "renww",
      "nick_name": null,
      "state": "optional",
      "updated_at": "2024-04-14T20:53:23.751+08:00",
      "username": "renww"
    }
  ],
  "approval_merge_request_reviewers": [
    {
      "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/be/fb/7b9e393fbd80ca315dec249f2be6e6a7378f591609b6525798bc6d95abedc992.png?time=1712128581171",
      "email": null,
      "id": 43,
      "is_codeowner": false,
      "name": "green",
      "name_cn": "green",
      "nick_name": null,
      "state": "optional",
      "updated_at": "2024-04-14T20:53:23.021+08:00",
      "username": "green"
    }
  ],
  "approval_merge_request_testers": [
    {
      "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/be/fb/7b9e393fbd80ca315dec249f2be6e6a7378f591609b6525798bc6d95abedc992.png?time=1712128581171",
      "email": null,
      "id": 43,
      "is_codeowner": false,
      "name": "green",
      "name_cn": "green",
      "nick_name": null,
      "state": "optional",
      "updated_at": "2024-04-14T20:53:23.755+08:00",
      "username": "green"
    },
    {
      "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ee/dc/7602704ee7dcf13f4383a72d492b1813823afba729ae6e9115877a4a0128d990.jpg?time=1711447395118",
      "email": null,
      "id": 277,
      "is_codeowner": false,
      "name": "renww",
      "name_cn": "renww",
      "nick_name": null,
      "state": "optional",
      "updated_at": "2024-04-14T20:53:23.755+08:00",
      "username": "renww"
    }
  ],
  "assignee": null,
  "author": {
    "avatar_path": null,
    "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ec/ba/4e7c4661b6154a7dd088d9fe64b4893383a2e318bf362350ce18d44df6ac7e37.png?time=1711533165876",
    "email": "csdntest13@noreply.gitcode.com",
    "iam_id": "d8b3e018b2364546b946886a669d50fc",
    "id": 494,
    "is_member": null,
    "name": "csdntest13",
    "name_cn": "csdntest13",
    "nick_name": "csdntest13_gitcode",
    "state": "active",
    "tenant_name": null,
    "username": "csdntest13",
    "web_url": "https://gitcode.com/csdntest13"
  },
  "auto_merge": null,
  "can_delete_source_branch": true,
  "changes_count": "6",
  "closed_at": null,
  "closed_by": null,
  "codequality_status": "success",
  "comments_url": "https://gitcode.com/api/v5/repos/zzero/demo/pulls/6/comments",
  "commits_url": "https://gitcode.com/api/v5/repos/zzero/demo/pulls/6/commits",
  "created_at": "2024-04-14T20:53:13.185+08:00",
  "description": "update: Update file dev_001.txt  \nupdate: Update file dev_001.txt",
  "description_html": null,
  "diff_refs": {
    "base_sha": "0c02dd57f8945791460a141f155dd2f4bd5dea86",
    "head_sha": "8da7a5c35e71deeb0bf1d9ecae70449c574749f2",
    "start_sha": "fb6495834d1bf7a39dfdb44ad25e6f83c7136310"
  },
  "diff_url": "https://gitcode.com/zzero/demo/pulls/6.diff",
  "discussion_locked": null,
  "diverged_commits_count": null,
  "downvotes": 0,
  "e2e_issues": [
    {
      "auto_c_when_mr_merged": false,
      "check_fail_reason": "",
      "check_result": true,
      "commit_id": null,
      "created_at": "2024-04-14T20:53:23.772+08:00",
      "id": 13588,
      "issue_link": "https://gitcode.com/One/One/issues/100",
      "issue_num": "issue100",
      "issue_project": null,
      "issue_project_id": 243377,
      "issue_type": 7,
      "linked_issue_type": null,
      "merge_request_id": 68253,
      "mks_id": null,
      "pbi_id": null,
      "pbi_name": null,
      "source": null,
      "title": "The boudoir ripenings issue-45"
    }
  ],
  "first_deployed_to_production_at": null,
  "force_remove_source_branch": false,
  "forked_project_name": null,
  "from_forked_project": false,
  "gate_check": true,
  "has_pre_merge_ref": false,
  "head_pipeline_id": null,
  "html_url": "https://gitcode.com/zzero/demo/pulls/6",
  "id": 11264998,
  "is_source_branch_exist": true,
  "issue_url": "https://gitcode.com/api/v5/repos/zzero/demo/pulls/6/issues",
  "json_merge_error": null,
  "labels": [
    {
      "color": "#008672",
      "id": 381445,
      "name": "help wanted",
      "textColor": "#FFFFFF",
      "title": "help wanted",
      "type": null
    },
    {
      "color": "#CFD240",
      "id": 381446,
      "name": "invalid",
      "textColor": "#FFFFFF",
      "title": "invalid",
      "type": null
    },
    {
      "color": "#D876E3",
      "id": 381447,
      "name": "question",
      "textColor": "#333333",
      "title": "question",
      "type": null
    }
  ],
  "latest_build_finished_at": null,
  "latest_build_started_at": null,
  "merge_commit_sha": null,
  "merge_error": null,
  "merge_request_assignee_list": [],
  "merge_request_review_count": 0,
  "merge_request_reviewer_list": [],
  "merge_request_reviewers_count": 0,
  "merge_request_type": "MergeRequest",
  "merge_status": "unchecked",
  "merge_when_pipeline_succeeds": false,
  "merged_at": null,
  "merged_by": null,
  "milestone": null,
  "notes": 0,
  "number": 6,
  "omega_mode": false,
  "patch_url": "https://gitcode.com/zzero/demo/pulls/6.patch",
  "pipeline": null,
  "pipeline_status": "",
  "pipeline_status_with_code_quality": "",
  "rebase_in_progress": null,
  "removed_lines": 1,
  "required_reviewers": [],
  "review_comment_url": "https://gitcode.com/api/v5/repos/zzero/demo/pulls/comments",
  "review_comments_url": "https://gitcode.com/api/v5/repos/zzero/demo/pulls/comments/{/number}",
  "review_mode": "approval",
  "root_mr_locked_detail": null,
  "sha": "8da7a5c35e71deeb0bf1d9ecae70449c574749f2",
  "should_remove_source_branch": false,
  "source_branch": "dev",
  "source_git_url": "ssh://git@gitcode.com:2222/One/One.git",
  "source_project": {
    "archived": false,
    "avatar_url": null,
    "branch_count": null,
    "created_at": "2024-03-19T16:24:01.197+08:00",
    "creator": {
      "avatar_path": null,
      "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ec/ba/4e7c4661b6154a7dd088d9fe64b4893383a2e318bf362350ce18d44df6ac7e37.png?time=1711533165876",
      "email": "csdntest13@noreply.gitcode.com",
      "iam_id": "d8b3e018b2364546b946886a669d50fc",
      "id": 494,
      "is_member": null,
      "name": "csdntest13",
      "name_cn": "csdntest13",
      "nick_name": "csdntest13_gitcode",
      "state": "active",
      "tenant_name": null,
      "username": "csdntest13",
      "web_url": "https://gitcode.com/csdntest13"
    },
    "creator_id": 494,
    "default_branch": "main",
    "description": "csdntest13's first project (public)",
    "develop_mode": "normal",
    "empty_repo": false,
    "forked_from_project": null,
    "forks_count": 0,
    "has_updated_kia": false,
    "http_url_to_repo": "https://gitcode.com/One/One.git",
    "id": 243377,
    "is_kia": false,
    "item_type": "Project",
    "last_activity_at": "2024-04-14T20:43:58.602+08:00",
    "license": {
      "html_url": null,
      "key": "Apache_License_v2.0",
      "name": null,
      "nickname": null,
      "source_url": null
    },
    "license_url": null,
    "main_repository_language": [
      "Text",
      "#cccccc"
    ],
    "member_count": null,
    "member_mgnt_mode": 3,
    "mirror_project_data": null,
    "name": "One",
    "name_with_namespace": "One / One",
    "namespace": {
      "cell": "default",
      "develop_mode": "normal",
      "enable_file_control": null,
      "full_name": "One ",
      "full_path": "One",
      "id": 136909,
      "kind": "group",
      "name": "One",
      "owner_id": null,
      "parent_id": null,
      "path": "One",
      "region": null,
      "visibility_level": 20
    },
    "network_type": "green",
    "open_change_requests_count": null,
    "open_external_wiki": true,
    "open_issues_count": 108,
    "open_merge_requests_count": 32,
    "owner": null,
    "path": "One",
    "path_with_namespace": "One/One",
    "product_id": "28f96caf52004e81ab0bc38d60d11940",
    "product_name": null,
    "readme_url": "https://gitcode.com/One/One/blob/main/README.md",
    "release_count": null,
    "repo_replica_urls": null,
    "security": "internal",
    "ssh_url_to_repo": "ssh://git@gitcode.com:2222/One/One.git",
    "star_count": 1,
    "starred": false,
    "statistics": null,
    "tag_count": null,
    "tag_list": [],
    "updated_at": "2024-03-19T16:42:34.834+08:00",
    "visibility": "public",
    "watch_count": 1,
    "web_url": "https://gitcode.com/One/One"
  },
  "source_project_id": 243377,
  "squash": false,
  "squash_commit_message": null,
  "state": "opened",
  "subscribed": true,
  "target_branch": "test_b5",
  "target_project": {
    "archived": false,
    "avatar_url": null,
    "branch_count": null,
    "created_at": "2024-03-19T16:24:01.197+08:00",
    "creator": {
      "avatar_path": null,
      "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ec/ba/4e7c4661b6154a7dd088d9fe64b4893383a2e318bf362350ce18d44df6ac7e37.png?time=1711533165876",
      "email": "csdntest13@noreply.gitcode.com",
      "iam_id": "d8b3e018b2364546b946886a669d50fc",
      "id": 494,
      "is_member": null,
      "name": "csdntest13",
      "name_cn": "csdntest13",
      "nick_name": "csdntest13_gitcode",
      "state": "active",
      "tenant_name": null,
      "username": "csdntest13",
      "web_url": "https://gitcode.com/csdntest13"
    },
    "creator_id": 494,
    "default_branch": "main",
    "description": "csdntest13's first project (public)",
    "develop_mode": "normal",
    "empty_repo": false,
    "forked_from_project": null,
    "forks_count": 0,
    "has_updated_kia": false,
    "http_url_to_repo": "https://gitcode.com/One/One.git",
    "id": 243377,
    "is_kia": false,
    "item_type": "Project",
    "last_activity_at": "2024-04-14T20:43:58.602+08:00",
    "license": {
      "html_url": null,
      "key": "Apache_License_v2.0",
      "name": null,
      "nickname": null,
      "source_url": null
    },
    "license_url": null,
    "main_repository_language": [
      "Text",
      "#cccccc"
    ],
    "member_count": null,
    "member_mgnt_mode": 3,
    "mirror_project_data": null,
    "name": "One",
    "name_with_namespace": "One / One",
    "namespace": {
      "cell": "default",
      "develop_mode": "normal",
      "enable_file_control": null,
      "full_name": "One ",
      "full_path": "One",
      "id": 136909,
      "kind": "group",
      "name": "One",
      "owner_id": null,
      "parent_id": null,
      "path": "One",
      "region": null,
      "visibility_level": 20
    },
    "network_type": "green",
    "open_change_requests_count": null,
    "open_external_wiki": true,
    "open_issues_count": 108,
    "open_merge_requests_count": 32,
    "owner": null,
    "path": "One",
    "path_with_namespace": "One/One",
    "product_id": "28f96caf52004e81ab0bc38d60d11940",
    "product_name": null,
    "readme_url": "https://gitcode.com/One/One/blob/main/README.md",
    "release_count": null,
    "repo_replica_urls": null,
    "security": "internal",
    "ssh_url_to_repo": "ssh://git@gitcode.com:2222/One/One.git",
    "star_count": 1,
    "starred": false,
    "statistics": null,
    "tag_count": null,
    "tag_list": [],
    "updated_at": "2024-03-19T16:42:34.834+08:00",
    "visibility": "public",
    "watch_count": 1,
    "web_url": "https://gitcode.com/One/One"
  },
  "target_project_id": 243377,
  "time_stats": {
    "human_time_estimate": null,
    "human_total_time_spent": null,
    "time_estimate": null,
    "total_time_spent": 0
  },
  "title": "testing creating PR",
  "title_html": null,
  "unresolved_discussions_count": 0,
  "updated_at": "2024-04-14T20:53:22.634+08:00",
  "upvotes": 0,
  "url": "https://gitcode.com/api/v5/repos/zzero/demo/pulls/6",
  "user": {
    "can_merge": true
  },
  "user_notes_count": 0,
  "web_url": "https://gitcode.com/One/One/merge_requests/53",
  "work_in_progress": false
}
```
## JSON Request Example
```json
{
  "assignees": "string",
  "base": "string",
  "body": "string",
  "close_related_issue": true,
  "draft": true,
  "fork_path": "string",
  "head": "string",
  "issue": "string",
  "labels": "string",
  "milestone_number": 0,
  "prune_source_branch": true,
  "squash": true,
  "squash_commit_message": "string",
  "testers": "string",
  "title": "string"
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
    "assignees": "string",
    "base": "string",
    "body": "string",
    "close_related_issue": true,
    "draft": true,
    "fork_path": "string",
    "head": "string",
    "issue": "string",
    "labels": "string",
    "milestone_number": 0,
    "prune_source_branch": true,
    "squash": true,
    "squash_commit_message": "string",
    "testers": "string",
    "title": "string"
  },
  "method": "post",
  "operationId": "post_api_v5_repos_{owner}_{repo}_pulls",
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
      "description": "User authorization code",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/pulls",
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
    "method": "POST",
    "name": "Create Pull Request",
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
            "assignees": {
              "description": "Optional. Reviewers' usernames, multiple can be specified, separated by half-width commas, e.g., (username1,username2). Note: This option is无效当仓库代码审查设置中已设置【指派审查人员】.",
              "type": "string"
            },
            "base": {
              "description": "Required. The name of the target branch for the Pull Request submission.",
              "type": "string"
            },
            "body": {
              "description": "Optional. Content of the Pull Request",
              "type": "string"
            },
            "close_related_issue": {
              "description": "Optional, whether to close associated Issues after merging, default is set according to the repository configuration",
              "type": "boolean"
            },
            "draft": {
              "description": "Whether to set as draft Default false",
              "type": "boolean"
            },
            "fork_path": {
              "description": "fork project path 【owner/repo】, required for cross-repository PRs.",
              "type": "string"
            },
            "head": {
              "description": "Required. The source branch of the Pull Request submission. Format: branch. If cross-repository PR, pass: username:branch",
              "type": "string"
            },
            "issue": {
              "description": "Optional. The title and body of the Pull Request can be automatically filled based on the specified Issue ID.",
              "type": "string"
            },
            "labels": {
              "description": "A comma-separated list of labels, where the name must be between 2-20 characters long and cannot contain special characters. For example: bug,performance",
              "type": "string"
            },
            "milestone_number": {
              "description": "Optional. Milestone sequence number (id)",
              "type": "integer"
            },
            "prune_source_branch": {
              "description": "Optional. Whether to delete the source branch after merging the PR. Defaults to false (do not delete).",
              "type": "boolean"
            },
            "squash": {
              "description": "When using flat (squash) merging while accepting a Pull Request, defaults to false.",
              "type": "boolean"
            },
            "squash_commit_message": {
              "description": "squash commit messages",
              "type": "string"
            },
            "testers": {
              "description": "Optional. Testers' username, multiple usernames can be provided, separated by half-width commas, e.g., (username1,username2). Note: This option is无效当 repository code review settings have already set 【Assign Testers】.",
              "type": "string"
            },
            "title": {
              "description": "Required. Pull Request title",
              "type": "string"
            }
          },
          "required": [
            "title",
            "head",
            "base"
          ],
          "type": "object"
        }
      }
    }
  },
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "example": {
            "added_lines": 19860,
            "allow_collaboration": null,
            "allow_maintainer_to_push": null,
            "approval_merge_request_approvers": [
              {
                "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ee/dc/7602704ee7dcf13f4383a72d492b1813823afba729ae6e9115877a4a0128d990.jpg?time=1711447395118",
                "email": null,
                "id": 277,
                "is_codeowner": false,
                "name": "renww",
                "name_cn": "renww",
                "nick_name": null,
                "state": "optional",
                "updated_at": "2024-04-14T20:53:23.751+08:00",
                "username": "renww"
              }
            ],
            "approval_merge_request_reviewers": [
              {
                "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/be/fb/7b9e393fbd80ca315dec249f2be6e6a7378f591609b6525798bc6d95abedc992.png?time=1712128581171",
                "email": null,
                "id": 43,
                "is_codeowner": false,
                "name": "green",
                "name_cn": "green",
                "nick_name": null,
                "state": "optional",
                "updated_at": "2024-04-14T20:53:23.021+08:00",
                "username": "green"
              }
            ],
            "approval_merge_request_testers": [
              {
                "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/be/fb/7b9e393fbd80ca315dec249f2be6e6a7378f591609b6525798bc6d95abedc992.png?time=1712128581171",
                "email": null,
                "id": 43,
                "is_codeowner": false,
                "name": "green",
                "name_cn": "green",
                "nick_name": null,
                "state": "optional",
                "updated_at": "2024-04-14T20:53:23.755+08:00",
                "username": "green"
              },
              {
                "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ee/dc/7602704ee7dcf13f4383a72d492b1813823afba729ae6e9115877a4a0128d990.jpg?time=1711447395118",
                "email": null,
                "id": 277,
                "is_codeowner": false,
                "name": "renww",
                "name_cn": "renww",
                "nick_name": null,
                "state": "optional",
                "updated_at": "2024-04-14T20:53:23.755+08:00",
                "username": "renww"
              }
            ],
            "assignee": null,
            "author": {
              "avatar_path": null,
              "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ec/ba/4e7c4661b6154a7dd088d9fe64b4893383a2e318bf362350ce18d44df6ac7e37.png?time=1711533165876",
              "email": "csdntest13@noreply.gitcode.com",
              "iam_id": "d8b3e018b2364546b946886a669d50fc",
              "id": 494,
              "is_member": null,
              "name": "csdntest13",
              "name_cn": "csdntest13",
              "nick_name": "csdntest13_gitcode",
              "state": "active",
              "tenant_name": null,
              "username": "csdntest13",
              "web_url": "https://gitcode.com/csdntest13"
            },
            "auto_merge": null,
            "can_delete_source_branch": true,
            "changes_count": "6",
            "closed_at": null,
            "closed_by": null,
            "codequality_status": "success",
            "comments_url": "https://gitcode.com/api/v5/repos/zzero/demo/pulls/6/comments",
            "commits_url": "https://gitcode.com/api/v5/repos/zzero/demo/pulls/6/commits",
            "created_at": "2024-04-14T20:53:13.185+08:00",
            "description": "update: Update file dev_001.txt  \nupdate: Update file dev_001.txt",
            "description_html": null,
            "diff_refs": {
              "base_sha": "0c02dd57f8945791460a141f155dd2f4bd5dea86",
              "head_sha": "8da7a5c35e71deeb0bf1d9ecae70449c574749f2",
              "start_sha": "fb6495834d1bf7a39dfdb44ad25e6f83c7136310"
            },
            "diff_url": "https://gitcode.com/zzero/demo/pulls/6.diff",
            "discussion_locked": null,
            "diverged_commits_count": null,
            "downvotes": 0,
            "e2e_issues": [
              {
                "auto_c_when_mr_merged": false,
                "check_fail_reason": "",
                "check_result": true,
                "commit_id": null,
                "created_at": "2024-04-14T20:53:23.772+08:00",
                "id": 13588,
                "issue_link": "https://gitcode.com/One/One/issues/100",
                "issue_num": "issue100",
                "issue_project": null,
                "issue_project_id": 243377,
                "issue_type": 7,
                "linked_issue_type": null,
                "merge_request_id": 68253,
                "mks_id": null,
                "pbi_id": null,
                "pbi_name": null,
                "source": null,
                "title": "The boudoir ripenings issue-45"
              }
            ],
            "first_deployed_to_production_at": null,
            "force_remove_source_branch": false,
            "forked_project_name": null,
            "from_forked_project": false,
            "gate_check": true,
            "has_pre_merge_ref": false,
            "head_pipeline_id": null,
            "html_url": "https://gitcode.com/zzero/demo/pulls/6",
            "id": 11264998,
            "is_source_branch_exist": true,
            "issue_url": "https://gitcode.com/api/v5/repos/zzero/demo/pulls/6/issues",
            "json_merge_error": null,
            "labels": [
              {
                "color": "#008672",
                "id": 381445,
                "name": "help wanted",
                "textColor": "#FFFFFF",
                "title": "help wanted",
                "type": null
              },
              {
                "color": "#CFD240",
                "id": 381446,
                "name": "invalid",
                "textColor": "#FFFFFF",
                "title": "invalid",
                "type": null
              },
              {
                "color": "#D876E3",
                "id": 381447,
                "name": "question",
                "textColor": "#333333",
                "title": "question",
                "type": null
              }
            ],
            "latest_build_finished_at": null,
            "latest_build_started_at": null,
            "merge_commit_sha": null,
            "merge_error": null,
            "merge_request_assignee_list": [],
            "merge_request_review_count": 0,
            "merge_request_reviewer_list": [],
            "merge_request_reviewers_count": 0,
            "merge_request_type": "MergeRequest",
            "merge_status": "unchecked",
            "merge_when_pipeline_succeeds": false,
            "merged_at": null,
            "merged_by": null,
            "milestone": null,
            "notes": 0,
            "number": 6,
            "omega_mode": false,
            "patch_url": "https://gitcode.com/zzero/demo/pulls/6.patch",
            "pipeline": null,
            "pipeline_status": "",
            "pipeline_status_with_code_quality": "",
            "rebase_in_progress": null,
            "removed_lines": 1,
            "required_reviewers": [],
            "review_comment_url": "https://gitcode.com/api/v5/repos/zzero/demo/pulls/comments",
            "review_comments_url": "https://gitcode.com/api/v5/repos/zzero/demo/pulls/comments/{/number}",
            "review_mode": "approval",
            "root_mr_locked_detail": null,
            "sha": "8da7a5c35e71deeb0bf1d9ecae70449c574749f2",
            "should_remove_source_branch": false,
            "source_branch": "dev",
            "source_git_url": "ssh://git@gitcode.com:2222/One/One.git",
            "source_project": {
              "archived": false,
              "avatar_url": null,
              "branch_count": null,
              "created_at": "2024-03-19T16:24:01.197+08:00",
              "creator": {
                "avatar_path": null,
                "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ec/ba/4e7c4661b6154a7dd088d9fe64b4893383a2e318bf362350ce18d44df6ac7e37.png?time=1711533165876",
                "email": "csdntest13@noreply.gitcode.com",
                "iam_id": "d8b3e018b2364546b946886a669d50fc",
                "id": 494,
                "is_member": null,
                "name": "csdntest13",
                "name_cn": "csdntest13",
                "nick_name": "csdntest13_gitcode",
                "state": "active",
                "tenant_name": null,
                "username": "csdntest13",
                "web_url": "https://gitcode.com/csdntest13"
              },
              "creator_id": 494,
              "default_branch": "main",
              "description": "csdntest13's first project (public)",
              "develop_mode": "normal",
              "empty_repo": false,
              "forked_from_project": null,
              "forks_count": 0,
              "has_updated_kia": false,
              "http_url_to_repo": "https://gitcode.com/One/One.git",
              "id": 243377,
              "is_kia": false,
              "item_type": "Project",
              "last_activity_at": "2024-04-14T20:43:58.602+08:00",
              "license": {
                "html_url": null,
                "key": "Apache_License_v2.0",
                "name": null,
                "nickname": null,
                "source_url": null
              },
              "license_url": null,
              "main_repository_language": [
                "Text",
                "#cccccc"
              ],
              "member_count": null,
              "member_mgnt_mode": 3,
              "mirror_project_data": null,
              "name": "One",
              "name_with_namespace": "One / One",
              "namespace": {
                "cell": "default",
                "develop_mode": "normal",
                "enable_file_control": null,
                "full_name": "One ",
                "full_path": "One",
                "id": 136909,
                "kind": "group",
                "name": "One",
                "owner_id": null,
                "parent_id": null,
                "path": "One",
                "region": null,
                "visibility_level": 20
              },
              "network_type": "green",
              "open_change_requests_count": null,
              "open_external_wiki": true,
              "open_issues_count": 108,
              "open_merge_requests_count": 32,
              "owner": null,
              "path": "One",
              "path_with_namespace": "One/One",
              "product_id": "28f96caf52004e81ab0bc38d60d11940",
              "product_name": null,
              "readme_url": "https://gitcode.com/One/One/blob/main/README.md",
              "release_count": null,
              "repo_replica_urls": null,
              "security": "internal",
              "ssh_url_to_repo": "ssh://git@gitcode.com:2222/One/One.git",
              "star_count": 1,
              "starred": false,
              "statistics": null,
              "tag_count": null,
              "tag_list": [],
              "updated_at": "2024-03-19T16:42:34.834+08:00",
              "visibility": "public",
              "watch_count": 1,
              "web_url": "https://gitcode.com/One/One"
            },
            "source_project_id": 243377,
            "squash": false,
            "squash_commit_message": null,
            "state": "opened",
            "subscribed": true,
            "target_branch": "test_b5",
            "target_project": {
              "archived": false,
              "avatar_url": null,
              "branch_count": null,
              "created_at": "2024-03-19T16:24:01.197+08:00",
              "creator": {
                "avatar_path": null,
                "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ec/ba/4e7c4661b6154a7dd088d9fe64b4893383a2e318bf362350ce18d44df6ac7e37.png?time=1711533165876",
                "email": "csdntest13@noreply.gitcode.com",
                "iam_id": "d8b3e018b2364546b946886a669d50fc",
                "id": 494,
                "is_member": null,
                "name": "csdntest13",
                "name_cn": "csdntest13",
                "nick_name": "csdntest13_gitcode",
                "state": "active",
                "tenant_name": null,
                "username": "csdntest13",
                "web_url": "https://gitcode.com/csdntest13"
              },
              "creator_id": 494,
              "default_branch": "main",
              "description": "csdntest13's first project (public)",
              "develop_mode": "normal",
              "empty_repo": false,
              "forked_from_project": null,
              "forks_count": 0,
              "has_updated_kia": false,
              "http_url_to_repo": "https://gitcode.com/One/One.git",
              "id": 243377,
              "is_kia": false,
              "item_type": "Project",
              "last_activity_at": "2024-04-14T20:43:58.602+08:00",
              "license": {
                "html_url": null,
                "key": "Apache_License_v2.0",
                "name": null,
                "nickname": null,
                "source_url": null
              },
              "license_url": null,
              "main_repository_language": [
                "Text",
                "#cccccc"
              ],
              "member_count": null,
              "member_mgnt_mode": 3,
              "mirror_project_data": null,
              "name": "One",
              "name_with_namespace": "One / One",
              "namespace": {
                "cell": "default",
                "develop_mode": "normal",
                "enable_file_control": null,
                "full_name": "One ",
                "full_path": "One",
                "id": 136909,
                "kind": "group",
                "name": "One",
                "owner_id": null,
                "parent_id": null,
                "path": "One",
                "region": null,
                "visibility_level": 20
              },
              "network_type": "green",
              "open_change_requests_count": null,
              "open_external_wiki": true,
              "open_issues_count": 108,
              "open_merge_requests_count": 32,
              "owner": null,
              "path": "One",
              "path_with_namespace": "One/One",
              "product_id": "28f96caf52004e81ab0bc38d60d11940",
              "product_name": null,
              "readme_url": "https://gitcode.com/One/One/blob/main/README.md",
              "release_count": null,
              "repo_replica_urls": null,
              "security": "internal",
              "ssh_url_to_repo": "ssh://git@gitcode.com:2222/One/One.git",
              "star_count": 1,
              "starred": false,
              "statistics": null,
              "tag_count": null,
              "tag_list": [],
              "updated_at": "2024-03-19T16:42:34.834+08:00",
              "visibility": "public",
              "watch_count": 1,
              "web_url": "https://gitcode.com/One/One"
            },
            "target_project_id": 243377,
            "time_stats": {
              "human_time_estimate": null,
              "human_total_time_spent": null,
              "time_estimate": null,
              "total_time_spent": 0
            },
            "title": "testing creating PR",
            "title_html": null,
            "unresolved_discussions_count": 0,
            "updated_at": "2024-04-14T20:53:22.634+08:00",
            "upvotes": 0,
            "url": "https://gitcode.com/api/v5/repos/zzero/demo/pulls/6",
            "user": {
              "can_merge": true
            },
            "user_notes_count": 0,
            "web_url": "https://gitcode.com/One/One/merge_requests/53",
            "work_in_progress": false
          },
          "schema": {
            "properties": {
              "added_lines": {
                "type": "integer"
              },
              "allow_collaboration": {
                "type": "null"
              },
              "allow_maintainer_to_push": {
                "type": "null"
              },
              "approval_merge_request_approvers": {
                "items": {
                  "properties": {
                    "avatar_url": {
                      "type": "string"
                    },
                    "email": {
                      "type": "null"
                    },
                    "id": {
                      "type": "integer"
                    },
                    "is_codeowner": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    },
                    "name_cn": {
                      "type": "string"
                    },
                    "nick_name": {
                      "type": "null"
                    },
                    "state": {
                      "type": "string"
                    },
                    "updated_at": {
                      "type": "string"
                    },
                    "username": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "approval_merge_request_reviewers": {
                "items": {
                  "properties": {
                    "avatar_url": {
                      "type": "string"
                    },
                    "email": {
                      "type": "null"
                    },
                    "id": {
                      "type": "integer"
                    },
                    "is_codeowner": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    },
                    "name_cn": {
                      "type": "string"
                    },
                    "nick_name": {
                      "type": "null"
                    },
                    "state": {
                      "type": "string"
                    },
                    "updated_at": {
                      "type": "string"
                    },
                    "username": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "approval_merge_request_testers": {
                "items": {
                  "properties": {
                    "avatar_url": {
                      "type": "string"
                    },
                    "email": {
                      "type": "null"
                    },
                    "id": {
                      "type": "integer"
                    },
                    "is_codeowner": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    },
                    "name_cn": {
                      "type": "string"
                    },
                    "nick_name": {
                      "type": "null"
                    },
                    "state": {
                      "type": "string"
                    },
                    "updated_at": {
                      "type": "string"
                    },
                    "username": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "assignee": {
                "type": "null"
              },
              "author": {
                "properties": {
                  "avatar_path": {
                    "type": "null"
                  },
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
                  "is_member": {
                    "type": "null"
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
                  "tenant_name": {
                    "type": "null"
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
              "auto_merge": {
                "type": "null"
              },
              "can_delete_source_branch": {
                "type": "integer"
              },
              "changes_count": {
                "type": "string"
              },
              "closed_at": {
                "type": "null"
              },
              "closed_by": {
                "type": "null"
              },
              "codequality_status": {
                "type": "string"
              },
              "comments_url": {
                "type": "string"
              },
              "commits_url": {
                "type": "string"
              },
              "created_at": {
                "type": "string"
              },
              "description": {
                "type": "string"
              },
              "description_html": {
                "type": "null"
              },
              "diff_refs": {
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
                "type": "object"
              },
              "diff_url": {
                "type": "string"
              },
              "discussion_locked": {
                "type": "null"
              },
              "diverged_commits_count": {
                "type": "null"
              },
              "downvotes": {
                "type": "integer"
              },
              "e2e_issues": {
                "items": {
                  "properties": {
                    "auto_c_when_mr_merged": {
                      "type": "integer"
                    },
                    "check_fail_reason": {
                      "type": "string"
                    },
                    "check_result": {
                      "type": "integer"
                    },
                    "commit_id": {
                      "type": "null"
                    },
                    "created_at": {
                      "type": "string"
                    },
                    "id": {
                      "type": "integer"
                    },
                    "issue_link": {
                      "type": "string"
                    },
                    "issue_num": {
                      "type": "string"
                    },
                    "issue_project": {
                      "type": "null"
                    },
                    "issue_project_id": {
                      "type": "integer"
                    },
                    "issue_type": {
                      "type": "integer"
                    },
                    "linked_issue_type": {
                      "type": "null"
                    },
                    "merge_request_id": {
                      "type": "integer"
                    },
                    "mks_id": {
                      "type": "null"
                    },
                    "pbi_id": {
                      "type": "null"
                    },
                    "pbi_name": {
                      "type": "null"
                    },
                    "source": {
                      "type": "null"
                    },
                    "title": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "first_deployed_to_production_at": {
                "type": "null"
              },
              "force_remove_source_branch": {
                "type": "integer"
              },
              "forked_project_name": {
                "type": "null"
              },
              "from_forked_project": {
                "type": "integer"
              },
              "gate_check": {
                "type": "integer"
              },
              "has_pre_merge_ref": {
                "type": "integer"
              },
              "head_pipeline_id": {
                "type": "null"
              },
              "html_url": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "is_source_branch_exist": {
                "type": "integer"
              },
              "issue_url": {
                "type": "string"
              },
              "json_merge_error": {
                "type": "null"
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
                    },
                    "textColor": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "type": {
                      "type": "null"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "latest_build_finished_at": {
                "type": "null"
              },
              "latest_build_started_at": {
                "type": "null"
              },
              "merge_commit_sha": {
                "type": "null"
              },
              "merge_error": {
                "type": "null"
              },
              "merge_request_assignee_list": {
                "items": {
                  "properties": {},
                  "type": "object"
                },
                "type": "array"
              },
              "merge_request_review_count": {
                "type": "integer"
              },
              "merge_request_reviewer_list": {
                "items": {
                  "properties": {},
                  "type": "object"
                },
                "type": "array"
              },
              "merge_request_reviewers_count": {
                "type": "integer"
              },
              "merge_request_type": {
                "type": "string"
              },
              "merge_status": {
                "type": "string"
              },
              "merge_when_pipeline_succeeds": {
                "type": "integer"
              },
              "merged_at": {
                "type": "null"
              },
              "merged_by": {
                "type": "null"
              },
              "milestone": {
                "type": "null"
              },
              "notes": {
                "type": "integer"
              },
              "number": {
                "type": "integer"
              },
              "omega_mode": {
                "type": "integer"
              },
              "patch_url": {
                "type": "string"
              },
              "pipeline": {
                "type": "null"
              },
              "pipeline_status": {
                "type": "string"
              },
              "pipeline_status_with_code_quality": {
                "type": "string"
              },
              "rebase_in_progress": {
                "type": "null"
              },
              "removed_lines": {
                "type": "integer"
              },
              "required_reviewers": {
                "items": {
                  "properties": {},
                  "type": "object"
                },
                "type": "array"
              },
              "review_comment_url": {
                "type": "string"
              },
              "review_comments_url": {
                "type": "string"
              },
              "review_mode": {
                "type": "string"
              },
              "root_mr_locked_detail": {
                "type": "null"
              },
              "sha": {
                "type": "string"
              },
              "should_remove_source_branch": {
                "type": "integer"
              },
              "source_branch": {
                "type": "string"
              },
              "source_git_url": {
                "type": "string"
              },
              "source_project": {
                "properties": {
                  "archived": {
                    "type": "integer"
                  },
                  "avatar_url": {
                    "type": "null"
                  },
                  "branch_count": {
                    "type": "null"
                  },
                  "created_at": {
                    "type": "string"
                  },
                  "creator": {
                    "properties": {
                      "avatar_path": {
                        "type": "null"
                      },
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
                      "is_member": {
                        "type": "null"
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
                      "tenant_name": {
                        "type": "null"
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
                  "creator_id": {
                    "type": "integer"
                  },
                  "default_branch": {
                    "type": "string"
                  },
                  "description": {
                    "type": "string"
                  },
                  "develop_mode": {
                    "type": "string"
                  },
                  "empty_repo": {
                    "type": "integer"
                  },
                  "forked_from_project": {
                    "type": "null"
                  },
                  "forks_count": {
                    "type": "integer"
                  },
                  "has_updated_kia": {
                    "type": "integer"
                  },
                  "http_url_to_repo": {
                    "type": "string"
                  },
                  "id": {
                    "type": "integer"
                  },
                  "is_kia": {
                    "type": "integer"
                  },
                  "item_type": {
                    "type": "string"
                  },
                  "last_activity_at": {
                    "type": "string"
                  },
                  "license": {
                    "properties": {
                      "html_url": {
                        "type": "null"
                      },
                      "key": {
                        "type": "string"
                      },
                      "name": {
                        "type": "null"
                      },
                      "nickname": {
                        "type": "null"
                      },
                      "source_url": {
                        "type": "null"
                      }
                    },
                    "type": "object"
                  },
                  "license_url": {
                    "type": "null"
                  },
                  "main_repository_language": {
                    "items": {
                      "type": "string"
                    },
                    "type": "array"
                  },
                  "member_count": {
                    "type": "null"
                  },
                  "member_mgnt_mode": {
                    "type": "integer"
                  },
                  "mirror_project_data": {
                    "type": "null"
                  },
                  "name": {
                    "type": "string"
                  },
                  "name_with_namespace": {
                    "type": "string"
                  },
                  "namespace": {
                    "properties": {
                      "cell": {
                        "type": "string"
                      },
                      "develop_mode": {
                        "type": "string"
                      },
                      "enable_file_control": {
                        "type": "null"
                      },
                      "full_name": {
                        "type": "string"
                      },
                      "full_path": {
                        "type": "string"
                      },
                      "id": {
                        "type": "integer"
                      },
                      "kind": {
                        "type": "string"
                      },
                      "name": {
                        "type": "string"
                      },
                      "owner_id": {
                        "type": "null"
                      },
                      "parent_id": {
                        "type": "null"
                      },
                      "path": {
                        "type": "string"
                      },
                      "region": {
                        "type": "null"
                      },
                      "visibility_level": {
                        "type": "integer"
                      }
                    },
                    "type": "object"
                  },
                  "network_type": {
                    "type": "string"
                  },
                  "open_change_requests_count": {
                    "type": "null"
                  },
                  "open_external_wiki": {
                    "type": "integer"
                  },
                  "open_issues_count": {
                    "type": "integer"
                  },
                  "open_merge_requests_count": {
                    "type": "integer"
                  },
                  "owner": {
                    "type": "null"
                  },
                  "path": {
                    "type": "string"
                  },
                  "path_with_namespace": {
                    "type": "string"
                  },
                  "product_id": {
                    "type": "string"
                  },
                  "product_name": {
                    "type": "null"
                  },
                  "readme_url": {
                    "type": "string"
                  },
                  "release_count": {
                    "type": "null"
                  },
                  "repo_replica_urls": {
                    "type": "null"
                  },
                  "security": {
                    "type": "string"
                  },
                  "ssh_url_to_repo": {
                    "type": "string"
                  },
                  "star_count": {
                    "type": "integer"
                  },
                  "starred": {
                    "type": "integer"
                  },
                  "statistics": {
                    "type": "null"
                  },
                  "tag_count": {
                    "type": "null"
                  },
                  "tag_list": {
                    "items": {
                      "properties": {},
                      "type": "object"
                    },
                    "type": "array"
                  },
                  "updated_at": {
                    "type": "string"
                  },
                  "visibility": {
                    "type": "string"
                  },
                  "watch_count": {
                    "type": "integer"
                  },
                  "web_url": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "source_project_id": {
                "type": "integer"
              },
              "squash": {
                "type": "integer"
              },
              "squash_commit_message": {
                "type": "null"
              },
              "state": {
                "type": "string"
              },
              "subscribed": {
                "type": "integer"
              },
              "target_branch": {
                "type": "string"
              },
              "target_project": {
                "properties": {
                  "archived": {
                    "type": "integer"
                  },
                  "avatar_url": {
                    "type": "null"
                  },
                  "branch_count": {
                    "type": "null"
                  },
                  "created_at": {
                    "type": "string"
                  },
                  "creator": {
                    "properties": {
                      "avatar_path": {
                        "type": "null"
                      },
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
                      "is_member": {
                        "type": "null"
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
                      "tenant_name": {
                        "type": "null"
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
                  "creator_id": {
                    "type": "integer"
                  },
                  "default_branch": {
                    "type": "string"
                  },
                  "description": {
                    "type": "string"
                  },
                  "develop_mode": {
                    "type": "string"
                  },
                  "empty_repo": {
                    "type": "integer"
                  },
                  "forked_from_project": {
                    "type": "null"
                  },
                  "forks_count": {
                    "type": "integer"
                  },
                  "has_updated_kia": {
                    "type": "integer"
                  },
                  "http_url_to_repo": {
                    "type": "string"
                  },
                  "id": {
                    "type": "integer"
                  },
                  "is_kia": {
                    "type": "integer"
                  },
                  "item_type": {
                    "type": "string"
                  },
                  "last_activity_at": {
                    "type": "string"
                  },
                  "license": {
                    "properties": {
                      "html_url": {
                        "type": "null"
                      },
                      "key": {
                        "type": "string"
                      },
                      "name": {
                        "type": "null"
                      },
                      "nickname": {
                        "type": "null"
                      },
                      "source_url": {
                        "type": "null"
                      }
                    },
                    "type": "object"
                  },
                  "license_url": {
                    "type": "null"
                  },
                  "main_repository_language": {
                    "items": {
                      "type": "string"
                    },
                    "type": "array"
                  },
                  "member_count": {
                    "type": "null"
                  },
                  "member_mgnt_mode": {
                    "type": "integer"
                  },
                  "mirror_project_data": {
                    "type": "null"
                  },
                  "name": {
                    "type": "string"
                  },
                  "name_with_namespace": {
                    "type": "string"
                  },
                  "namespace": {
                    "properties": {
                      "cell": {
                        "type": "string"
                      },
                      "develop_mode": {
                        "type": "string"
                      },
                      "enable_file_control": {
                        "type": "null"
                      },
                      "full_name": {
                        "type": "string"
                      },
                      "full_path": {
                        "type": "string"
                      },
                      "id": {
                        "type": "integer"
                      },
                      "kind": {
                        "type": "string"
                      },
                      "name": {
                        "type": "string"
                      },
                      "owner_id": {
                        "type": "null"
                      },
                      "parent_id": {
                        "type": "null"
                      },
                      "path": {
                        "type": "string"
                      },
                      "region": {
                        "type": "null"
                      },
                      "visibility_level": {
                        "type": "integer"
                      }
                    },
                    "type": "object"
                  },
                  "network_type": {
                    "type": "string"
                  },
                  "open_change_requests_count": {
                    "type": "null"
                  },
                  "open_external_wiki": {
                    "type": "integer"
                  },
                  "open_issues_count": {
                    "type": "integer"
                  },
                  "open_merge_requests_count": {
                    "type": "integer"
                  },
                  "owner": {
                    "type": "null"
                  },
                  "path": {
                    "type": "string"
                  },
                  "path_with_namespace": {
                    "type": "string"
                  },
                  "product_id": {
                    "type": "string"
                  },
                  "product_name": {
                    "type": "null"
                  },
                  "readme_url": {
                    "type": "string"
                  },
                  "release_count": {
                    "type": "null"
                  },
                  "repo_replica_urls": {
                    "type": "null"
                  },
                  "security": {
                    "type": "string"
                  },
                  "ssh_url_to_repo": {
                    "type": "string"
                  },
                  "star_count": {
                    "type": "integer"
                  },
                  "starred": {
                    "type": "integer"
                  },
                  "statistics": {
                    "type": "null"
                  },
                  "tag_count": {
                    "type": "null"
                  },
                  "tag_list": {
                    "items": {
                      "properties": {},
                      "type": "object"
                    },
                    "type": "array"
                  },
                  "updated_at": {
                    "type": "string"
                  },
                  "visibility": {
                    "type": "string"
                  },
                  "watch_count": {
                    "type": "integer"
                  },
                  "web_url": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "target_project_id": {
                "type": "integer"
              },
              "time_stats": {
                "properties": {
                  "human_time_estimate": {
                    "type": "null"
                  },
                  "human_total_time_spent": {
                    "type": "null"
                  },
                  "time_estimate": {
                    "type": "null"
                  },
                  "total_time_spent": {
                    "type": "integer"
                  }
                },
                "type": "object"
              },
              "title": {
                "type": "string"
              },
              "title_html": {
                "type": "null"
              },
              "unresolved_discussions_count": {
                "type": "integer"
              },
              "updated_at": {
                "type": "string"
              },
              "upvotes": {
                "type": "integer"
              },
              "url": {
                "type": "string"
              },
              "user": {
                "properties": {
                  "can_merge": {
                    "type": "integer"
                  }
                },
                "type": "object"
              },
              "user_notes_count": {
                "type": "integer"
              },
              "web_url": {
                "type": "string"
              },
              "work_in_progress": {
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
    "Pull Requests"
  ]
}
```
