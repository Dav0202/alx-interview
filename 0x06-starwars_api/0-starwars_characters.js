#!/usr/bin/node
const argv = process.argv;
const FILM_URL = 'https://swapi-api.alx-tools.com/api/films/';
const MOVIE_URL = `${FILM_URL}${argv[2]}/`;

const request = require('request');

request(MOVIE_URL, function (error, response, body) {
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

function GetCharacter(idx, url, characters, limit) {
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
