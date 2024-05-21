#!/usr/bin/node

const fs = requires('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err) {
	if (err) {
		console.log(err);
	}
});
