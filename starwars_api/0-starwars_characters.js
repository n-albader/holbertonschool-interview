#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, { json: true }, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    return;
  }

  const characters = body.characters;

  const printCharacters = (index) => {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], { json: true }, (err, res, character) => {
      if (!err && res.statusCode === 200) {
        console.log(character.name);
      }

      printCharacters(index + 1);
    });
  };

  printCharacters(0);
});
