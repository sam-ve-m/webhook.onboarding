#!/bin/bash

fission spec init
fission env create --spec --name onboarding-ouroinvest-env --image nexus.sigame.com.br/fission-async:0.1.6 --builder nexus.sigame.com.br/fission-builder-3.8:0.0.1
fission fn create --spec --name onboarding-ouroinvest-fn --env onboarding-ouroinvest-env --src "./func/*" --entrypoint main.onboarding_ouroinvest --executortype newdeploy --maxscale 1
fission route create --spec --name onboarding-ouroinvest-rt --method PUT --url /onboarding-ouroinvest --function onboarding-ouroinvest-fn