#!/usr/bin/env bash

source venv/bin/activate ;

function run() {
  ( flask run ; )
}

function init() {
  run
}

init
