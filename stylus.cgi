#!/usr/bin/node

filename = process.env.PATH_TRANSLATED
console.log("Content-type: text/css")
console.log("\r")
if(filename === undefined){
  console.log('file not found')
  return 0
}

var stylus = require('stylus')
var fs = require('fs')

fs.readFile(filename, 'utf8', (err, data) => {
  stylus.render(data, {filename: filename}, (err, css) => {
    if(err){
      console.log(err.message)
    }
    else {
      console.log(css)
    }
  })
})
