#!/bin/bash
set -euxo pipefail

branch=github-actions
pip install "git+https://github.com/jmlopez-rod/m.git@$branch"

/opt/m_helpers/_init.sh

echo 'close this terminal and open another one then run `pnpm install`'
