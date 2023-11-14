#!/usr/bin/env bash

files=$(find . -type f | grep -v venv | grep "__pycache__")
dirs=$(find . -type d | grep -v venv | grep "__pycache__")
node_modules_dir=$(find . -type d | grep -v venv | grep "node_modules")

# Clean pycache files and dirs
function clean_pycache(){
  echo ">>> Removing pycache files" ;
  if [ -z "${files}" ]; then
    echo "No files to remove"
  else
    for f in ${files[f]}; do
      echo "Removing pycache file: ${f}" ;
      ( rm "${f}" ; )
    done
  fi

  echo ">>> Removing pycache dirs" ;
  if [ -z "${dirs}" ]; then
    echo "No dirs to remove"
  else
    for d in ${dirs[d]}; do
      echo "Removing pycache dir: ${d}" ;
      ( rmdir "${d}" ; )
    done
  fi
}

# clean node_modules
function clean_node_modules() {
  echo ">>> Removing node_modules dirs" ;
  if [ -z "${node_modules_dir}" ]; then
    echo "No node_modules to remove"
  else
    ( rm -Rf node_modules ; )
  fi
}

function cleanup_complete() {
  echo "Cleanup Complete !!!"
}

function init(){
  clean_pycache ;
  clean_node_modules ;
  cleanup_complete ;

}

init
