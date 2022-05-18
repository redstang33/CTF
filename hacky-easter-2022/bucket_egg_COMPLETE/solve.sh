#!/usr/bin/env bash

aws s3 cp s3://egg-in-a-bucket/index.html .
aws s3 cp s3://egg-in-a-bucket/bucketbg.jpg .
zbarimg bucketbg.jpg
