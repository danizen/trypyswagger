# Testing using pyswagger

## Motivation

We want to build a modern RESTful webapp, with a happy Service-layer
pattern, self-described by swagger.  We wish to test that the server
faithfully implements this layer.

We lack the $$ to purchase licenses for Soap Ng Pro, and the developers
are testing the API anyway.

## Design

- Details about loading the application's endpoint and initializing 
  the client appropriately for security are delegated to pytest fixtures.

- Our tests are concerned only with making requests and receiving replies.

## Issues

- As of now, I only know how to load the application's swagger from a json
  file, but wish to know how to support yaml, loaded from the local 
  filesystem as well.

