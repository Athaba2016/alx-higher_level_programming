#!/usr/bin/node

const request = require('request');

async function get (url, options) {
  return new Promise(function (resolve, reject) {
    request.get(url, options, function (err, res) {
      if (err) {
        reject(err);
      } else {
        resolve(res);
      }
