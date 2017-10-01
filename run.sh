#!/bin/sh
# Build fake files
python faker/fake.py

# Init node app
cd nodelister
yarn
cd ..

# Init python app
pip install virtualenv || true
virtualenv venv
. venv/bin/activate
pip install -r pylister/requirements.txt

# Run node tests
echo "### 1ST NODE TEST ###"
node nodelister/index.js
echo "### 2ND NODE TEST ###"
node nodelister/index.js
echo "### 3RD NODE TEST ###"
node nodelister/index.js
echo "### 4TH NODE TEST ###"
node nodelister/index.js
echo "### 5TH NODE TEST ###"
node nodelister/index.js

# Run python tests
echo "### 1ST PYTHON TEST ###"
python pylister/lister.py
echo "### 2ND PYTHON TEST ###"
python pylister/lister.py
echo "### 3RD PYTHON TEST ###"
python pylister/lister.py
echo "### 4TH PYTHON TEST ###"
python pylister/lister.py
echo "### 5TH PYTHON TEST ###"
python pylister/lister.py

# Clean up
deactivate
rm -rf content
rm -rf lister/node_modules
rm -rf venv
