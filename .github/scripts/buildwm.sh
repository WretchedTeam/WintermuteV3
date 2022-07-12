#!/bin/sh

# From: https://github.com/ProjectAliceDev/renpy-build-action

echo "Downloading the specified SDK (8.0.0)..."
wget -q "https://www.renpy.org/dl/8.0.0/renpy-8.0.0-sdk.tar.bz2"
clear

echo "Downloaded SDK version (8.0.0)."
echo "Setting up the specified SDK (8.0.0)..."
tar -xf ./renpy-8.0.0-sdk.tar.bz2
rm ./renpy-8.0.0-sdk.tar.bz2
mv ./renpy-8.0.0-sdk ../renpy

RENPY="../renpy"

RENPYSH="$RENPY/renpy.sh"
RENPYLAUNCHER="$RENPY/launcher"

BUILDINFO_COMMAND="$RENPYSH $1 buildinfo"
DISTRIBUTE_COMMAND="$RENPYSH $RENPYLAUNCHER distribute $1"

echo "Building the project at $1..."

if $BUILDINFO_COMMAND; then
    echo "buildinfo.txt generated."
else
    echo "buildinfo command failed."
    exit 1
fi

if $DISTRIBUTE_COMMAND; then
    title=$(head -1 buildinfo.txt | tail -1)
    version=$(head -2 buildinfo.txt | tail -1)
    dest=$(head -3 buildinfo.txt | tail -1)

    echo "::set-output name=title::$title"
    echo "::set-output name=version::$version"
    echo "::set-output name=dest::$dest"

    echo "Done."
else
    echo "Failed."
fi
