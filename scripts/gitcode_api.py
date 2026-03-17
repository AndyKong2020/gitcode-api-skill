#!/usr/bin/env python3
import argparse
import json
import os
import re
from pathlib import Path

import requests

BASE_URL = "https://api.gitcode.com"
CATALOG_PATH = Path(__file__).resolve().parent.parent / "references" / "endpoint-catalog.json"


def load_catalog():
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def parse_kv(items):
    values = {}
    for item in items or []:
        if "=" not in item:
            raise SystemExit(f"Expected KEY=VALUE, got: {item}")
        key, value = item.split("=", 1)
        values[key] = value
    return values


def apply_path_params(path, path_params):
    missing = []

    def repl(match):
        key = match.group(1)
        if key not in path_params:
            missing.append(key)
            return match.group(0)
        return path_params[key]

    resolved = re.sub(r"\{([^}]+)\}", repl, path)
    if missing:
        raise SystemExit(f"Missing path params: {', '.join(sorted(set(missing)))}")
    return resolved


def build_auth(query, headers, auth_mode, token):
    if not token or auth_mode == "none":
        return
    if auth_mode == "bearer":
        headers["Authorization"] = f"Bearer {token}"
    elif auth_mode == "private-token":
        headers["PRIVATE-TOKEN"] = token
    elif auth_mode == "query":
        query["access_token"] = token
    else:
        raise SystemExit(f"Unsupported auth mode: {auth_mode}")


def command_search(args):
    catalog = load_catalog()
    needle = args.query.lower()
    results = []
    for item in catalog:
        haystacks = [
            item.get("title", ""),
            item.get("method", ""),
            item.get("path", ""),
            item.get("permalink", ""),
            " ".join(item.get("categories", [])),
            " ".join(item.get("tags", [])),
        ]
        if needle in " | ".join(haystacks).lower():
            results.append(item)
    print(json.dumps(results[: args.limit], ensure_ascii=False, indent=2))


def command_request(args):
    headers = {}
    query = parse_kv(args.query)
    path_params = parse_kv(args.path)
    extra_headers = parse_kv(args.header)
    form_body = parse_kv(args.form)

    token = args.token or os.getenv("GITCODE_TOKEN")
    build_auth(query, headers, args.auth_mode, token)
    headers.update(extra_headers)

    path = apply_path_params(args.endpoint_path, path_params)
    url = args.base_url.rstrip("/") + path

    json_body = None
    if args.json_body and form_body:
        raise SystemExit("Use either --json or --form, not both")
    if args.json_body:
        json_body = json.loads(args.json_body)
        headers.setdefault("Content-Type", "application/json")
    if form_body:
        headers.setdefault("Content-Type", "application/x-www-form-urlencoded")
    headers.setdefault("Accept", "application/json")

    if args.dry_run:
        print(
            json.dumps(
                {
                    "method": args.method.upper(),
                    "url": url,
                    "query": query,
                    "headers": headers,
                    "json": json_body,
                    "form": form_body,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    response = requests.request(
        method=args.method.upper(),
        url=url,
        params=query,
        headers=headers,
        json=json_body,
        data=form_body or None,
        timeout=args.timeout,
    )
    output = {
        "status_code": response.status_code,
        "headers": dict(response.headers),
        "url": response.url,
    }
    content_type = response.headers.get("content-type", "")
    if "application/json" in content_type:
        try:
            output["body"] = response.json()
        except Exception:
            output["body_text"] = response.text
    else:
        output["body_text"] = response.text
    print(json.dumps(output, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description="GitCode API helper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    search = subparsers.add_parser("search", help="Search the endpoint catalog")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=20)
    search.set_defaults(func=command_search)

    request = subparsers.add_parser("request", help="Execute a GitCode API request")
    request.add_argument("method")
    request.add_argument("endpoint_path", help="Path template, e.g. /api/v5/repos/{owner}/issues")
    request.add_argument("--base-url", default=BASE_URL)
    request.add_argument("--auth-mode", choices=["bearer", "private-token", "query", "none"], default="bearer")
    request.add_argument("--token")
    request.add_argument("--path", action="append", default=[], help="Path param KEY=VALUE")
    request.add_argument("--query", action="append", default=[], help="Query param KEY=VALUE")
    request.add_argument("--header", action="append", default=[], help="Header KEY=VALUE")
    request.add_argument("--form", action="append", default=[], help="Form field KEY=VALUE")
    request.add_argument("--json", dest="json_body")
    request.add_argument("--dry-run", action="store_true")
    request.add_argument("--timeout", type=int, default=60)
    request.set_defaults(func=command_request)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
