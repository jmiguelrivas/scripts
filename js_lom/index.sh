#!/usr/bin/env bash
set -euo pipefail

# download lom.mjs to a temp file
tmp=$(mktemp --suffix=.mjs)
curl -fsSL "https://raw.githubusercontent.com/jmiguelrivas/scripts-js/master/lom.mjs" -o "$tmp"

# run it with Node
node "$tmp"

# cleanup
rm -f "$tmp"
