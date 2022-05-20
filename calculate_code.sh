#!/bin/bash

find './game/mod_code' -type f -name '*.rpy' -print0 | xargs -0 wc -l
