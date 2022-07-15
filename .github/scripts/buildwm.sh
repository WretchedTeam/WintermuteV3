#!/bin/sh

# From: https://github.com/ProjectAliceDev/renpy-build-action

VERSION="8.0.1"

echo "Downloading the specified SDK ($VERSION)..."
wget -q "https://www.renpy.org/dl/$VERSION/renpy-$VERSION-sdk.tar.bz2"
clear

echo "Downloaded SDK version ($VERSION)."
echo "Setting up the specified SDK ($VERSION)..."
tar -xf ./renpy-$VERSION-sdk.tar.bz2
rm ./renpy-$VERSION-sdk.tar.bz2
mv ./renpy-$VERSION-sdk ../renpy

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
