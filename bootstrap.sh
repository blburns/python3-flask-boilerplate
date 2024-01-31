#!/usr/bin/env bash

function run() {(
#    source venv/bin/activate ;
    flask run ;
)}

function init() {
  run
}

init
