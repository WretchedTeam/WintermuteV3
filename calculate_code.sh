#!/bin/bash

SRC='game/mod_code'
SUBFOLDERS=('app' 'backend' 'definitions' 'screens' 'uikit')

find . -type f -name "*.rpy" -not -path './game/mod_code/scripts/*' -print0 | xargs -0 wc -l