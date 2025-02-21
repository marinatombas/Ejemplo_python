#!/usr/bin/env groovy
@Library(["osiris-python-module@release/python39-ada", "osiris-k8s-module"]) _

adanode("python39") {

    try {
        stage("Checkout") {
            checkout scm
        }
        
        stage("Python Module") {
            if (python.isBuildable()) {
                python.module("pipeline")
            }
        }
        
    } finally {
        cleanWs()
    }
}
