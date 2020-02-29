## The Space, CR+LF Stripper

The Space, CR+LF Stripper, version 1.0.1

### Overview

Currently, I have a project that need to configure [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) process via a [JSON file](https://en.wikipedia.org/wiki/JSON).

I need to write it in python script as the project environment requires [python 2.7.x](https://www.python.org/downloads/release/python-2717/)

This simple tool is named as `"Replace Space or CR or LF with nil"` or `repscrlf` for short.

The `repscrlf` main purpose is to convert an input [JSON file](https://en.wikipedia.org/wiki/JSON) and produce an output string (`string in JSON format`) but can be parse by [AWS CLI](https://aws.amazon.com/cli/) tool.

The sample JSON file is as follows: (*Other fields in there was removed for `brevity`*)

```json
{
    "image": "AWS_CUSTOMER_ID.dkr.ecr.AWS_REGION.amazonaws.com/YOUR_DOCKER_AT_AWS",
    "vcpus": 1,
    "memory": 2048,
    "volumes": [
        {
            "host": {
                "sourcePath": "/scratch"
            },
            "name": "scratch"
        }
    ],
    "mountPoints": [
        {
            "containerPath": "/opt/work",
            "sourceVolume": "scratch"
        }
    ]
}
```

- NOTE:
    1. you need to replace `AWS_CUSTOMER_ID` with your [Amazon console account ID](https://aws.amazon.com/console/),
    2. you need to replace `AWS_REGION` with an Amazon [region ID](https://aws.amazon.com/console/)
    3. you need to replace `YOUR_DOCKER_AT_AWS` with a URI of the actual docker image you publish in [AWS ECR](https://aws.amazon.com/ecr/faqs/)

To convert it to JSON string that is `parsable` by `aws cli`, run it with `repscrlf` as follows:

```bash
./repscrlf.py samples/sample.json
# the resulting string shall be as follows:
```
```json
{"image":"AWS_CUSTOMER_ID.dkr.ecr.AWS_REGION.amazonaws.com/YOUR_DOCKER_AT_AWS","vcpus":1,"memory":2048,"volumes":[{"host":{"sourcePath":"/scratch"},"name":"scratch"}],"mountPoints":[{"containerPath":"/opt/work","sourceVolume":"scratch"}]}
```

## Example how to use repscrlf to register an AWS batch job

Assuming you have an [Amazon Account](https://aws.amazon.com/console/) and you need to login on a terminal as follows:

- Create an `AWS Credential`. Create credentials into `~/.aws` as follows: (*You need to prepare your region ID, secret key, ID*)

- You may need to install [AWS CLI](https://aws.amazon.com/cli/) in your environment.


On Ubuntu 18.03+, you can do the following:

```bash
sudo apt install -y awscli
```

- Create the AWS Credential; Do this only once.

```bash
aws configure
```

- Login into your AWS account

```bash
$(aws ecr get-login --no-include-email)
```

## You can now finally register an AWS batch job as follows:

```bash
containerProperties=$(python repscrlf.py ./samples/sample.json )

$ aws batch register-job-definition \
  --job-definition-name "running-my-awsome-docker-image" \
  --type container \
  --container-properties "$containerProperties" > results-for-sample.json
```

If a successful operation, the content of `results-for-sample.json` as follows:

```json
{
     "jobDefinitionName": "running-my-awsome-docker-image",
     "jobDefinitionArn": "arn:aws:batch:AWS_REGION:AWS_CUSTOMER_ID:job-definition/running-my-awsome-docker-image:1",
     "revision": 1
}
```

## LICENSE

[BSD 3-Clause "New" or "Revised" License](https://github.com/tmalbonph/repscrlf/blob/master/LICENSE)

## Copyright Notices

[AWS](https://aws.amazon.com/terms/?nc1=f_pr) is a trademark of `"Amazon Web Services, Inc. P.O. Box 81226 Seattle, WA 98108-1226 http://aws.amazon.com"`

Other trademarks mention on this [README.md](https://github.com/tmalbonph/repscrlf/blob/master/README.md) is own by there respective owner.

## NOTES

The author of `repscrlf` is not in anyway connected with `Amazon Web Services, Inc.` or its affiliate. `AWS` was only mention here for the purpose of demonstrating how to use `repscrlf` to generate a string that can be use as one of the required parameter upon executing one of the `AWS CLI services`.
