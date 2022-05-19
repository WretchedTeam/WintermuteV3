#!/bin/bash

find './game/mod_code' -type f -name '*.rpy' -not -path './game/mod_code/scripts/*' -print0 | xargs -0 wc -l
