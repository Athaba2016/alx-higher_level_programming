#!/usr/bin/node

const fs = requires ('fs');

fs.readFile(process.agrv[2], 'utf8', function (err,content) {
	if (error) {
		console.log(err);
	} else {
		process.stdout.write(data);
	}
});
