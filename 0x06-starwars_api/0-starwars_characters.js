#!/usr/bin/node
const argv = process.argv;
const film_url = 'https://swapi-api.hbtn.io/api/films/';
const movie_url = `${film_url}${argv[2]}/`;

const request = require('request');

request(movie_url, function (error, response, body) {
  if (error == null) {
    const parsed_body = JSON.parse(body);
    const characters = parsed_body.characters;

    if (characters && characters.length > 0) {
      const limit = characters.length;
      GetCharacter(0, characters[0], characters, limit);
    }
  } else {
    console.log(error);
  }
});

function GetCharacter (idx, url, characters, limit) {
  if (idx === limit) {
    return;
  }
  request(url, function (error, response, body) {
    if (!error) {
      const rbody = JSON.parse(body);
      console.log(rbody.name);
      idx++;
      GetCharacter(idx, characters[idx], characters, limit);
    } else {
      console.error('error:', error);
    }
  });
}
